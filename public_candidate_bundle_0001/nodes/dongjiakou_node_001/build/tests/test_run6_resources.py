"""Tests for Run 6 — resource modules.

The governing rule under test: a resource module earns value only when all eight
required questions are receipted. Until then it returns a transfer function and
a zero credit, never a point estimate.
"""

from __future__ import annotations

import pytest

from models import run6_resources as r6
from models.common import UNKNOWN, is_unknown


# ---------------------------------------------------------------------------
# The eight-question rule
# ---------------------------------------------------------------------------
def test_eight_requirements_are_declared():
    assert set(r6.RESOURCE_MODULE_REQUIREMENTS) == {
        "yield", "selectivity", "energy", "reagents",
        "material_life", "residual_fate", "market_ceiling", "ecology",
    }


def test_ecology_and_residual_fate_are_veto_bearing():
    """A module that cannot say where its waste goes has not earned a credit."""
    assert "ecology" in r6.VETO_REQUIREMENTS
    assert "residual_fate" in r6.VETO_REQUIREMENTS


def test_fresh_module_is_fully_unreceipted():
    tf = r6.lithium_transfer_function(39_844_444.44, 0.45)
    register = tf["recovery"]
    assert register["receipted_count"] == 0
    assert register["required_count"] == 8
    assert register["eligible_for_value"] is False
    assert register["value_credit"] == 0
    for entry in register["requirements"].values():
        assert entry["status"] == "UNKNOWN"
        assert is_unknown(entry["receipt"])


def test_module_is_eligible_only_when_all_eight_are_receipted():
    register = r6._receipt_register("R01-X", "test")
    assert r6.module_is_eligible(register) is False
    register["receipted_count"] = 7
    assert r6.module_is_eligible(register) is False
    register["receipted_count"] = 8
    assert r6.module_is_eligible(register) is True


def test_run_credits_nothing():
    result = r6.run()
    assert result["summary"]["total_value_credit"] == 0
    assert result["summary"]["modules_eligible_for_value"] == 0
    assert result["summary"]["modules_instantiated"] == 4


# ---------------------------------------------------------------------------
# Brine arithmetic
# ---------------------------------------------------------------------------
def test_concentration_factor():
    assert r6.concentration_factor(0.45) == pytest.approx(1.8181818181818181, rel=1e-12)
    assert r6.concentration_factor(0.50) == pytest.approx(2.0)


def test_concentration_factor_rejects_zero_recovery():
    with pytest.raises(ValueError):
        r6.concentration_factor(0.0)


def test_reject_volume_is_feed_minus_product():
    feed, recovery = 39_844_444.44444444, 0.45
    reject = r6.reject_volume_m3_year(feed, recovery)
    assert reject == pytest.approx(feed * 0.55, rel=1e-12)


def test_reject_volume_rejects_negative_feed():
    with pytest.raises(ValueError):
        r6.reject_volume_m3_year(-1.0, 0.45)


# ---------------------------------------------------------------------------
# R01-Li — lithium IS concentrated by the plant
# ---------------------------------------------------------------------------
def test_lithium_is_concentrated_in_brine():
    tf = r6.lithium_transfer_function(39_844_444.44444444, 0.45)
    assert tf["transfer_function"]["concentration_factor_brine_to_feed"] > 1.0
    assert tf["transfer_function"]["brine_li_mg_l"] == pytest.approx(0.30909090909, rel=1e-8)


def test_lithium_mass_is_conserved_across_the_split():
    tf = r6.lithium_transfer_function(39_844_444.44444444, 0.45)
    f = tf["transfer_function"]
    assert f["li_in_brine_t_year"] + f["li_in_product_t_year"] == pytest.approx(
        f["li_in_feed_t_year"], rel=1e-12
    )


def test_lithium_annual_inventory_is_single_digit_tonnes():
    """The inventory is small. This is the honest scale of the opportunity."""
    tf = r6.lithium_transfer_function(39_844_444.44444444, 0.45)
    assert 6.0 < tf["transfer_function"]["li_in_brine_t_year"] < 7.0


def test_lithium_scales_linearly_with_feed():
    a = r6.lithium_transfer_function(1_000_000.0, 0.45)["transfer_function"]
    b = r6.lithium_transfer_function(2_000_000.0, 0.45)["transfer_function"]
    assert b["li_in_brine_t_year"] == pytest.approx(2 * a["li_in_brine_t_year"])


def test_lithium_does_not_claim_recovery_or_displacement():
    tf = r6.lithium_transfer_function(39_844_444.44444444, 0.45)
    joined = " ".join(tf["not_claimed"])
    assert "No recovered lithium quantity" in joined
    assert "POTENTIAL_DISPLACEMENT_HYPOTHESIS" in joined


def test_lithium_rejects_negative_concentration():
    with pytest.raises(ValueError):
        r6.lithium_transfer_function(1_000_000.0, 0.45, feed_li_mg_l=-0.1)


# ---------------------------------------------------------------------------
# R01-D — deuterium is NOT concentrated by the plant
# ---------------------------------------------------------------------------
def test_deuterium_mass_fraction_is_about_35_ppm():
    ppm = r6.deuterium_mass_fraction_in_water() * 1e6
    assert 34.0 < ppm < 36.0


def test_deuterium_gets_no_enrichment_from_reverse_osmosis():
    """The architectural finding: the plant creates no deuterium gradient."""
    tf = r6.deuterium_transfer_function(39_844_444.44444444, 0.45)
    assert tf["transfer_function"]["isotopic_enrichment_factor_by_RO"] == 1.0


def test_deuterium_is_uniform_across_streams():
    """D/H is the same in feed, brine and product. Only the volume differs."""
    feed, recovery = 39_844_444.44444444, 0.45
    tf = r6.deuterium_transfer_function(feed, recovery)
    f = tf["transfer_function"]
    d_fraction = f["deuterium_mass_fraction_in_water"]
    assert f["d_in_feed_t_year"] == pytest.approx(feed * d_fraction, rel=1e-12)
    assert f["d_in_brine_t_year"] == pytest.approx(
        r6.reject_volume_m3_year(feed, recovery) * d_fraction, rel=1e-12
    )


def test_deuterium_mass_exceeds_lithium_mass_by_orders_of_magnitude():
    """Abundant in mass, absent as a gradient. This contrast is the finding."""
    feed, recovery = 39_844_444.44444444, 0.45
    d = r6.deuterium_transfer_function(feed, recovery)["transfer_function"]["d_in_brine_t_year"]
    li = r6.lithium_transfer_function(feed, recovery)["transfer_function"]["li_in_brine_t_year"]
    assert d / li > 100


def test_deuterium_mass_is_conserved_across_the_split():
    tf = r6.deuterium_transfer_function(39_844_444.44444444, 0.45)
    f = tf["transfer_function"]
    assert f["d_in_brine_t_year"] + f["d_in_product_t_year"] == pytest.approx(
        f["d_in_feed_t_year"], rel=1e-12
    )


def test_deuterium_states_the_architecture_consequence():
    tf = r6.deuterium_transfer_function(39_844_444.44444444, 0.45)
    assert "no brine concentration" in tf["architecture_consequence"].lower() or \
           "there is none to exploit" in tf["architecture_consequence"].lower()


def test_deuterium_keeps_the_literature_band_unresolved():
    tf = r6.deuterium_transfer_function(39_844_444.44444444, 0.45)
    assert tf["inputs"]["D_abundance_band_ppm"] == [89.0, 156.0]


def test_deuterium_does_not_claim_linkage_to_the_ergotropy_question():
    tf = r6.deuterium_transfer_function(39_844_444.44444444, 0.45)
    joined = " ".join(tf["not_claimed"])
    assert "ergotropy" in joined
    assert "separate" in joined


# ---------------------------------------------------------------------------
# Sequencing discipline
# ---------------------------------------------------------------------------
def test_run_declares_the_one_at_a_time_rule():
    result = r6.run()
    assert "one at a time" in result["sequence_rule"]
    assert "Run 7" in result["sequence_rule"]


def test_run_lists_its_unresolved_asks():
    result = r6.run()
    joined = " ".join(result["unresolved"])
    assert "lithium assay" in joined
    assert "deuterium assay" in joined
    assert "INV-19" in joined
