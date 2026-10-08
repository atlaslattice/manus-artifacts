"""Run 6 — resource and ecology modules, executed one at a time.

SolBrain rule, carried forward verbatim:

    Every resource module needs yield, selectivity, energy, reagents, material
    life, residual fate, market ceiling and ecology before earning value.

This module implements that rule as code. A resource module that cannot answer
all eight questions returns a **transfer function and a zero credit**, never a
point estimate.

Two modules are instantiated: lithium (R01-Li) and deuterium (R01-D). They behave
differently, and the difference is the finding:

* **Lithium** is concentrated by the desalination process itself. It is a
  concentration-and-selectivity problem.
* **Deuterium** is *not* concentrated by the desalination process. The D/H ratio
  is essentially the same in feed, product and brine, because RO does not
  meaningfully fractionate isotopes. Deuterium is an **isotopic separation energy**
  problem, not a concentration problem.

Treating the two lanes as the same kind of lane would be an accounting error.
"""

from __future__ import annotations

from typing import Any

from .common import (
    UNKNOWN,
    UnknownPropagationError,
    guard_fraction,
    is_unknown,
    require_number,
)

# ---------------------------------------------------------------------------
# Sourced constants
# ---------------------------------------------------------------------------

#: Lithium concentration in seawater, mg/L.
#: Reported as ~0.17 ppm by multiple independent sources; a wider band of
#: 0.1-0.2 ppm also appears in the literature. Treated as REPORTED, not MEASURED
#: at Node-001, because no site assay exists.
SEAWATER_LI_MG_L = 0.17
SEAWATER_LI_MG_L_BAND = (0.10, 0.20)

#: Roughly tenfold lithium enrichment reported for nanofiltration-treated
#: desalination brine relative to raw seawater. REFERENCE, not a Node-001 receipt.
NF_BRINE_LI_ENRICHMENT = 10.0

#: Deuterium abundance in natural water, as an atom ratio D/H.
#: ~156 ppm of hydrogen, i.e. roughly 1 hydrogen in 6,400.
D_H_ATOM_RATIO = 1.56e-4

#: Literature disagreement on deuterium abundance, recorded rather than resolved.
#: Reported deuteron concentrations in pure water range 89-156 ppm depending on
#: the natural-abundance value used.
D_ABUNDANCE_BAND_PPM = (89.0, 156.0)

#: Atomic masses used for the mass-fraction conversion.
_M_D = 2.014101778
_M_H = 1.007825032
_M_O = 15.9994
_M_H2O = 2 * _M_H + _M_O

#: The eight questions a resource module must answer before earning value.
RESOURCE_MODULE_REQUIREMENTS: dict[str, str] = {
    "yield": "Measured recovered quantity per unit of brine processed, at this site.",
    "selectivity": "Measured separation factor against the dominant competing ions (Na, Mg, Ca, K, Cl, sulfate).",
    "energy": "Measured net energy per unit of recovered product, including pumping, regeneration and thermal duty.",
    "reagents": "Measured reagent consumption and its own supply chain, cost and residuals.",
    "material_life": "Measured sorbent, membrane or electrode cycle life and replacement interval.",
    "residual_fate": "Where the spent brine, eluate, reagent and exhausted material actually go, with a receipt.",
    "market_ceiling": "Contracted or exchange-published offtake for the actual product grade, not a commodity headline price.",
    "ecology": "Receiving-water and ecological status under INV-19. This one is a veto, not a score.",
}

#: Requirements that are veto-bearing rather than merely blocking.
VETO_REQUIREMENTS = frozenset({"ecology", "residual_fate"})


# ---------------------------------------------------------------------------
# Shared brine arithmetic
# ---------------------------------------------------------------------------
def reject_volume_m3_year(feed_m3_year: float, recovery: float) -> float:
    """Reject-equivalent volume. This is feed minus product, NOT a discharge."""
    feed = require_number(feed_m3_year, "feed_m3_year")
    r = guard_fraction(recovery, "recovery")
    if feed < 0:
        raise ValueError("feed_m3_year must be non-negative")
    return feed * (1.0 - r)


def concentration_factor(recovery: float) -> float:
    """Brine-to-feed concentration factor for a fully rejected species.

    A species rejected to the brine is concentrated by feed/reject = 1/(1-R).
    """
    r = guard_fraction(recovery, "recovery")
    if r == 0:
        raise ValueError("recovery must be greater than zero")
    return 1.0 / (1.0 - r)


def _receipt_register(module_id: str, product: str) -> dict[str, Any]:
    """Every resource module starts fully unreceipted."""
    return {
        "module_id": module_id,
        "product": product,
        "requirements": {
            key: {
                "question": question,
                "status": "UNKNOWN",
                "receipt": UNKNOWN,
                "veto_bearing": key in VETO_REQUIREMENTS,
            }
            for key, question in RESOURCE_MODULE_REQUIREMENTS.items()
        },
        "receipted_count": 0,
        "required_count": len(RESOURCE_MODULE_REQUIREMENTS),
        "value_credit": 0,
        "eligible_for_value": False,
        "blocking_reason": "No receipt exists for any of the eight required questions.",
    }


def module_is_eligible(register: dict[str, Any]) -> bool:
    """A module earns value only when all eight questions are receipted."""
    return register["receipted_count"] == register["required_count"]


# ---------------------------------------------------------------------------
# R01-Li — lithium
# ---------------------------------------------------------------------------
def lithium_transfer_function(
    feed_m3_year: float,
    recovery: float,
    feed_li_mg_l: float = SEAWATER_LI_MG_L,
) -> dict[str, Any]:
    """Lithium inventory passing through the brine, as a transfer function.

    Returns an inventory and a concentration. It does **not** return a recovered
    quantity, because yield is unmeasured at this site.
    """
    feed = require_number(feed_m3_year, "feed_m3_year")
    li = require_number(feed_li_mg_l, "feed_li_mg_l")
    if li < 0:
        raise ValueError("feed_li_mg_l must be non-negative")

    cf = concentration_factor(recovery)
    reject = reject_volume_m3_year(feed, recovery)

    # RO rejects lithium essentially completely, so the rejected mass equals the
    # feed mass. Stated as a product-term subtraction so the assumption is visible
    # rather than implied: rejected = feed * (1 - fraction carried to product).
    fraction_li_to_product = 0.0
    # mg/L * m3 * 1000 L/m3 = mg ; /1e9 = tonnes
    li_in_feed_t_year = feed * 1000.0 * li / 1e9
    li_in_brine_t_year = li_in_feed_t_year * (1.0 - fraction_li_to_product)
    li_in_product_t_year = li_in_feed_t_year * fraction_li_to_product

    register = _receipt_register("R01-Li", "lithium")
    return {
        "module_id": "R01-Li",
        "artifact_id": "DJK-NODE-001-RUN-6-R01-Li-v0.1",
        "status": "EXECUTED_PARAMETRIC_TRANSFER_FUNCTION_NON_CANON",
        "classification": "RESOURCE_INVENTORY_NOT_RECOVERY_YIELD",
        "inputs": {
            "feed_m3_year": feed,
            "recovery": recovery,
            "feed_li_mg_l": li,
            "feed_li_source": "REPORTED seawater concentration ~0.17 ppm; site assay absent",
            "feed_li_band_mg_l": list(SEAWATER_LI_MG_L_BAND),
        },
        "transfer_function": {
            "concentration_factor_brine_to_feed": cf,
            "brine_volume_m3_year": reject,
            "brine_li_mg_l": li * cf,
            "li_in_feed_t_year": li_in_feed_t_year,
            "li_in_brine_t_year": li_in_brine_t_year,
            "li_in_product_t_year": li_in_product_t_year,
            "fraction_li_to_product_assumed": fraction_li_to_product,
            "nf_brine_enrichment_reference": NF_BRINE_LI_ENRICHMENT,
            "brine_li_mg_l_after_nf_reference": li * NF_BRINE_LI_ENRICHMENT,
        },
        "recovery": register,
        "finding": (
            "Lithium is genuinely concentrated by the desalination step, by the "
            "brine concentration factor. The inventory is therefore larger in the "
            "brine than in the feed, and a downstream nanofiltration step is "
            "reported to enrich it roughly tenfold further. This makes lithium a "
            "concentration-and-selectivity problem, which is the favourable case."
        ),
        "not_claimed": [
            "No recovered lithium quantity.",
            "No revenue, because no offtake grade or price is contracted.",
            "No reduction in terrestrial lithium mining. That remains a "
            "POTENTIAL_DISPLACEMENT_HYPOTHESIS until yield, selectivity, energy, "
            "reagents, material life, markets, economics and ecology all close.",
        ],
    }


# ---------------------------------------------------------------------------
# R01-D — deuterium
# ---------------------------------------------------------------------------
def deuterium_mass_fraction_in_water() -> float:
    """Mass fraction of deuterium in natural water, from the atom ratio."""
    # Per mole of water: 2 H sites, D fraction = D/H atom ratio.
    d_mol = 2.0 * D_H_ATOM_RATIO
    mass_d = d_mol * _M_D
    return mass_d / _M_H2O


def deuterium_transfer_function(feed_m3_year: float, recovery: float) -> dict[str, Any]:
    """Deuterium inventory passing through the brine, as a transfer function.

    The critical property: RO does not meaningfully fractionate hydrogen
    isotopes, so the D/H ratio in the brine is approximately the D/H ratio in the
    feed. Unlike lithium, deuterium gains **no** useful concentration from the
    desalination step.
    """
    feed = require_number(feed_m3_year, "feed_m3_year")
    reject = reject_volume_m3_year(feed, recovery)

    d_fraction = deuterium_mass_fraction_in_water()
    # tonnes of water ~ m3 of water at ~1 t/m3
    d_in_feed_t_year = feed * d_fraction
    d_in_brine_t_year = reject * d_fraction

    register = _receipt_register("R01-D", "deuterium")
    return {
        "module_id": "R01-D",
        "artifact_id": "DJK-NODE-001-RUN-6-R01-D-v0.1",
        "status": "EXECUTED_PARAMETRIC_TRANSFER_FUNCTION_NON_CANON",
        "classification": "RESOURCE_INVENTORY_NOT_RECOVERY_YIELD",
        "inputs": {
            "feed_m3_year": feed,
            "recovery": recovery,
            "D_H_atom_ratio": D_H_ATOM_RATIO,
            "D_abundance_band_ppm": list(D_ABUNDANCE_BAND_PPM),
            "D_abundance_source": "REPORTED ~156 ppm of hydrogen in ocean water; literature band 89-156 ppm retained unresolved",
        },
        "transfer_function": {
            "deuterium_mass_fraction_in_water": d_fraction,
            "deuterium_ppm_by_mass_of_water": d_fraction * 1e6,
            "isotopic_enrichment_factor_by_RO": 1.0,
            "d_in_feed_t_year": d_in_feed_t_year,
            "d_in_brine_t_year": d_in_brine_t_year,
            "brine_volume_m3_year": reject,
            "d_in_product_t_year": d_in_feed_t_year - d_in_brine_t_year,
            "note_d_is_not_lost": (
                "Deuterium leaving with the product water is not a loss; it is a "
                "different stream. The point is that no stream is enriched."
            ),
        },
        "recovery": register,
        "finding": (
            "Deuterium is abundant in mass and essentially absent as a "
            "concentration gradient. Every tonne of water at this site carries "
            "roughly the same deuterium fraction as the ocean, and the "
            "desalination step does not change it. The constraint is therefore "
            "isotopic separation energy, not resource availability and not brine "
            "concentration. This lane is architecturally unlike the lithium lane "
            "and must not be modelled as though a brine stream were an ore body."
        ),
        "architecture_consequence": (
            "A deuterium lane should not be sited to exploit brine concentration, "
            "because there is none to exploit. If pursued, it is a heavy-water "
            "separation plant that happens to be co-located with a desalination "
            "plant, and it must be justified on separation energy and heat "
            "integration, not on feed enrichment."
        ),
        "not_claimed": [
            "No heavy-water production rate.",
            "No separation energy figure, because no process route is selected or measured.",
            "No linkage to the deuteron spin ergotropy question, which is a separate "
            "and independent baseline test with its own result: thermal ergotropy is "
            "zero at 1 T / 300 K.",
        ],
    }


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
def run() -> dict[str, Any]:
    """Execute Run 6 with the site's own 2025 volumes from Run 0.2."""
    from . import run0

    operating = run0.operating_2025()
    cases = operating["mass_balance_using_reported_technology_recovery_range"]

    modules = {}
    for label, case in cases.items():
        recovery = float(label)
        feed = case["annual_feed_m3"]
        modules[f"R01-Li@{label}"] = lithium_transfer_function(feed, recovery)
        modules[f"R01-D@{label}"] = deuterium_transfer_function(feed, recovery)

    return {
        "artifact_id": "DJK-NODE-001-RUN-6-RESOURCES-v0.1",
        "status": "EXECUTED_PARAMETRIC_TRANSFER_FUNCTION_NON_CANON",
        "study_classification": "TECHNICAL_FEASIBILITY_PLUS_CONDITIONAL_ECONOMICS",
        "governing_rule": (
            "Every resource module needs yield, selectivity, energy, reagents, "
            "material life, residual fate, market ceiling and ecology before "
            "earning value."
        ),
        "required_questions": RESOURCE_MODULE_REQUIREMENTS,
        "veto_requirements": sorted(VETO_REQUIREMENTS),
        "modules": modules,
        "summary": {
            "modules_instantiated": len(modules),
            "modules_eligible_for_value": 0,
            "total_value_credit": 0,
            "reason": "No module has a receipt for any of the eight required questions.",
        },
        "sequence_rule": (
            "Modules are evaluated one at a time. Stacking survivors is Run 7 and "
            "requires sequence-dependent interference edges, which cannot exist "
            "before individual modules have measured receipts."
        ),
        "unresolved": [
            "Site lithium assay in feed, product and brine.",
            "Site deuterium assay in feed, product and brine, to test the "
            "no-enrichment assumption rather than assert it.",
            "Any sorbent, membrane or electrode performance at this brine chemistry.",
            "Receiving-water and ecological status under INV-19.",
        ],
    }
