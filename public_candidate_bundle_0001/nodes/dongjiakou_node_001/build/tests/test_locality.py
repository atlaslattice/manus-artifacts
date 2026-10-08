"""Tests for the Dongjiakou Locality Stream Register v0.2.

The register encodes rules that must not soften:
  1. No module receives benefit before measurement.
  2. A stream may be counted once, by one owner; allocation is separate.
  3. A stream must not claim a sink it has not got.
  4. NODE_PASS = AND(all vetoes pass). An unresolved veto is not a pass.
  5. Simulator validation is not locality clearance.
"""

from __future__ import annotations

import json
import pathlib

import pytest

from models import locality as loc
from models import run3_compute as r3

BUILD = pathlib.Path(__file__).resolve().parents[1]
REGISTER = BUILD / "lattice" / "CHINA_DESAL_NODE_REGISTER.json"


# ---------------------------------------------------------------------------
# Structure
# ---------------------------------------------------------------------------
def test_subnodes_are_declared():
    for required in ("W01", "C01", "P01", "E01", "E02", "R01", "BIO01", "M01",
                     "MAT01", "CHEM01", "AGR01", "CARB01", "ECO01", "GOV01", "EXT01"):
        assert required in loc.SUBNODES


def test_eighteen_stream_fields_are_declared():
    assert len(loc.STREAM_FIELDS) == 18
    for f in ("edge_state", "candidate_allocation_owner", "realized_credit",
              "primary_credit_owner", "residual_fate", "time_profile"):
        assert f in loc.STREAM_FIELDS


def test_twelve_flywheel_layers_are_declared():
    assert sorted(loc.FLYWHEEL_LAYER_SUBNODES) == list(range(1, 13))
    assert sorted(loc.FLYWHEEL_LAYER_NAMES) == list(range(1, 13))


def test_every_stream_has_the_complete_schema():
    result = loc.run()
    assert result["counts"]["streams_with_incomplete_schema"] == 0
    for s in result["physical_streamgraph"] + result["opportunity_graph"]:
        for f in loc.STREAM_FIELDS:
            assert f in s, f"{s['stream_id']} missing {f}"


def test_stream_ids_are_unique():
    ids = [s["stream_id"] for s in loc.known_streams()]
    assert len(ids) == len(set(ids))


def test_every_stream_uses_a_declared_evidence_class_and_edge_state():
    for s in loc.known_streams():
        assert s["evidence_class"] in loc.EVIDENCE_CLASSES, s["stream_id"]
        assert s["edge_state"] in loc.EDGE_STATES, s["stream_id"]


def test_every_stream_endpoint_is_a_declared_subnode():
    for s in loc.known_streams():
        assert s["source_subnode"] in loc.SUBNODES, s["stream_id"]
        assert s["sink_subnode"] in loc.SUBNODES, s["stream_id"]


def test_undeclared_edge_state_is_rejected():
    with pytest.raises(ValueError):
        loc._s("X", "W01", "P01", "test", "1", "REPORTED", "NOT_A_REAL_STATE")


# ---------------------------------------------------------------------------
# PATCH 1 — no credit before measurement
# ---------------------------------------------------------------------------
def test_no_stream_realizes_credit():
    """The v0.1 bug. The modeled PV stream carried credit; it must not."""
    result = loc.run()
    assert result["counts"]["streams_realizing_credit"] == 0


def test_only_measured_physical_can_realize_credit():
    assert loc.CREDIT_REALIZING_EDGE_STATES == frozenset({"MEASURED_PHYSICAL"})
    assert "REPORTED_PHYSICAL" not in loc.CREDIT_REALIZING_EDGE_STATES
    assert "MODELED" not in loc.CREDIT_REALIZING_EDGE_STATES


def test_modeled_pv_stream_carries_no_credit():
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    pv = by_id["S-S01-C01-01"]
    assert pv["evidence_class"] == "MODELED"
    assert pv["edge_state"] == "CANDIDATE_COUPLING"
    assert pv["realized_credit"] is False
    assert pv["primary_credit_owner"] == "NONE"


def test_credit_ownership_is_singular_never_shared():
    """Shared credit ownership is where double counting sneaks back in."""
    for s in loc.known_streams():
        owner = s["primary_credit_owner"]
        assert owner in ("NONE", "UNKNOWN") or "/" not in owner, s["stream_id"]
        assert "SHARED" not in owner, s["stream_id"]


def test_allocation_owner_is_not_a_credit_owner():
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    pv = by_id["S-S01-C01-01"]
    assert pv["candidate_allocation_owner"] == "E01/S01"
    assert pv["realized_credit"] is False


def test_allocation_conservation_holds_and_can_fail():
    ok = loc.allocation_conservation(
        "S-X", 2.70619355, {"W01": 1.0, "C01": 1.5},
        measured_basis="GWh/year", allocation_basis="GWh/year")
    assert ok["conserved"] is True
    assert ok["total_allocated"] == pytest.approx(2.5)
    bad = loc.allocation_conservation(
        "S-X", 2.70619355, {"W01": 2.0, "C01": 2.0},
        measured_basis="GWh/year", allocation_basis="GWh/year")
    assert bad["conserved"] is False


def test_negative_allocation_is_rejected():
    """The v0.2 loophole: {-100, +102} summed to 2.0 and passed."""
    r = loc.allocation_conservation(
        "S-X", 2.7, {"W01": -100, "C01": 102},
        measured_basis="GWh/year", allocation_basis="GWh/year")
    assert r["conserved"] is False
    assert any("negative allocation" in e for e in r["errors"])


def test_negative_measured_quantity_is_rejected():
    r = loc.allocation_conservation(
        "S-X", -1.0, {"W01": 0.0},
        measured_basis="GWh/year", allocation_basis="GWh/year")
    assert r["conserved"] is False


def test_basis_mismatch_is_rejected():
    """2.7 GWh/year and 2.7 MWh/hour must never share a conservation check."""
    r = loc.allocation_conservation(
        "S-X", 2.7, {"W01": 1.0},
        measured_basis="GWh/year", allocation_basis="MWh/hour")
    assert r["conserved"] is False
    assert any("basis mismatch" in e for e in r["errors"])


def test_unstated_basis_is_rejected():
    r = loc.allocation_conservation("S-X", 2.7, {"W01": 1.0})
    assert r["conserved"] is False
    assert any("basis is not stated" in e for e in r["errors"])


def test_zero_allocation_is_conserved():
    r = loc.allocation_conservation(
        "S-X", 2.7, {}, measured_basis="GWh/year", allocation_basis="GWh/year")
    assert r["conserved"] is True


# ---------------------------------------------------------------------------
# PATCH 2 — physical vs opportunity, and no unearned sinks
# ---------------------------------------------------------------------------
def test_streams_split_into_two_graphs():
    result = loc.run()
    assert result["counts"]["physical_streams"] + result["counts"]["opportunity_streams"] \
        == result["counts"]["streams_total"]
    for s in result["physical_streamgraph"]:
        assert s["edge_state"] in loc.PHYSICAL_EDGE_STATES
    for s in result["opportunity_graph"]:
        assert s["edge_state"] in loc.OPPORTUNITY_EDGE_STATES


def test_product_water_sink_is_now_resolved_to_the_industrial_cluster():
    """v0.1 wrongly drew this water to the port. Round 1 resolved the sink entirely.

    The stream was REPLACED rather than supplemented: it is the same water and
    may be counted once.
    """
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    s = by_id["S-W01-IND-01"]
    assert s["sink_subnode"] == "IND01"
    assert s["edge_state"] == "REPORTED_PHYSICAL"
    assert s["realized_credit"] is False
    assert "S-W01-EXT-01" not in by_id


def test_port_is_not_among_the_contracted_water_offtakers():
    """Evidence AGAINST a previously registered candidacy."""
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    port = by_id["S-W01-P01-C1"]
    assert port["edge_state"] == "CANDIDATE_COUPLING"
    assert "NOT among them" in port["quantity"]
    assert port["realized_credit"] is False


def test_brine_does_not_claim_resource_recovery_as_its_sink():
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    assert by_id["S-W01-EXT-02"]["sink_subnode"] == "EXT01"
    candidate = by_id["S-W01-R01-C1"]
    assert candidate["edge_state"] == "CANDIDATE_COUPLING"
    assert candidate["realized_credit"] is False


def test_reference_only_edges_are_flagged():
    """68 C heat is Xinfa Liaocheng, a different site. Not this locality."""
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    ref = by_id["S-CHEM01-AGR01-01"]
    assert ref["edge_state"] == "REFERENCE_ONLY"
    assert "Xinfa" in ref["quantity"]
    assert ref["realized_credit"] is False


def test_lng_cascade_edges_are_separate_and_uncounted():
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    gen = by_id["S-E02-GRID-01"]
    cool = by_id["S-E02-IND-01"]
    assert gen["edge_state"] == "UNDER_CONSTRUCTION"
    assert cool["edge_state"] == "UNDER_CONSTRUCTION"
    assert gen["realized_credit"] is False
    assert cool["realized_credit"] is False
    assert gen["stream_id"] != cool["stream_id"]


def test_brine_stream_is_veto_bearing():
    by_id = {s["stream_id"]: s for s in loc.known_streams()}
    assert "INV-19" in by_id["S-W01-EXT-02"]["vetoes"]


def test_physical_graph_is_small_relative_to_opportunity():
    result = loc.run()
    assert result["counts"]["physical_streams"] < result["counts"]["opportunity_streams"]


# ---------------------------------------------------------------------------
# PATCH 3 — clearance separation
# ---------------------------------------------------------------------------
def test_simulator_validation_and_locality_clearance_are_separate():
    cl = loc.clearance_status()
    assert cl["SIMULATOR_VALIDATION"]["answer"] == "PASS"
    assert cl["LOCALITY_CLEARANCE"]["answer"] == "NOT_ESTABLISHED"
    assert cl["SIMULATOR_VALIDATION"]["question"] != cl["LOCALITY_CLEARANCE"]["question"]


def test_clearance_warning_forbids_conflating_the_two():
    warning = loc.clearance_status()["warning"]
    assert "refused to clear" in warning
    assert "Never present the gate count" in warning


def test_unresolved_and_fail_are_semantically_distinct():
    reg = {k: {"state": "UNRESOLVED", "definition": "", "why": ""} for k in loc.VETO_DEFINITIONS}
    result = loc.node_pass(reg)
    assert result["unresolved"] == sorted(loc.VETO_DEFINITIONS)
    assert result["failed"] == []
    assert result["node_pass"] is False


def test_unresolved_veto_is_not_a_pass():
    result = loc.node_pass()
    assert result["node_pass"] is False
    assert result["verdict"] == "NODE_PASS_NOT_ESTABLISHED"
    assert len(result["unresolved"]) == 5


def test_node_pass_requires_every_veto_to_pass():
    reg = {k: {"state": "PASS", "definition": "", "why": ""} for k in loc.VETO_DEFINITIONS}
    assert loc.node_pass(reg)["node_pass"] is True
    reg["INV-19"]["state"] = "FAIL"
    assert loc.node_pass(reg)["node_pass"] is False


# ---------------------------------------------------------------------------
# PATCH 4 — geography and count semantics
# ---------------------------------------------------------------------------
def test_register_retains_167_as_a_project_discovery_count():
    d = json.loads(REGISTER.read_text(encoding="utf-8"))
    assert d["national_desal_project_discovery_count"] == 167
    assert d["target_locality_node_count"] == "UNKNOWN"
    assert "target_node_count" not in d


def test_register_has_no_nested_peer_localities():
    """One peer locality node may not geographically contain another."""
    d = json.loads(REGISTER.read_text(encoding="utf-8"))
    localities = [n for n in d["nodes"] if n.get("node_class") == "LOCALITY_NODE"]
    parents = d.get("regional_parents", [])
    assert all(n["node_class"] == "REGIONAL_PARENT" for n in parents)
    locality_ids = {n["candidate_node_id"] for n in localities}
    for parent in parents:
        for child in parent.get("child_localities", []):
            assert child in locality_ids
            assert child not in {p["candidate_node_id"] for p in parents}


def test_qingdao_is_a_regional_parent_not_a_peer():
    d = json.loads(REGISTER.read_text(encoding="utf-8"))
    parent = d["regional_parents"][0]
    assert parent["node_class"] == "REGIONAL_PARENT"
    assert "DJK-LATTICE-NODE-001" in parent["child_localities"]
    assert "reporting-only" in parent["aggregation_rule"]
    assert "DJK-LATTICE-NODE-002" not in {n["candidate_node_id"] for n in d["nodes"]}


def test_register_declares_the_ontology_rule():
    d = json.loads(REGISTER.read_text(encoding="utf-8"))
    onto = d["ontology"]
    assert "non-overlapping" in onto["peer_unit"]
    assert "node 120" in onto["why"]


# ---------------------------------------------------------------------------
# Scale, flywheel, governance
# ---------------------------------------------------------------------------
def test_e02_total_is_named_an_impact_not_a_stream():
    scale = loc.scale_comparison()
    assert "projected_grid_electricity_impact_gwh" in scale
    assert "e02_total_gwh" not in scale
    assert "separate edges" in scale["e02_note"]


def test_lng_impact_is_about_86_percent_of_w01_process_energy():
    scale = loc.scale_comparison()
    assert scale["projected_grid_electricity_impact_gwh"] == pytest.approx(34.0)
    assert scale["e02_impact_share_of_w01_process_energy"] == pytest.approx(0.8619, abs=5e-4)


def test_40mw_scenario_matches_the_arithmetic():
    s = r3.locality_scenario_40mw()
    assert s["it_energy_gwh_year_at_L1"] == pytest.approx(350.4)
    assert s["facility_energy_gwh_year_at_pue_1_25"] == pytest.approx(438.0)
    assert s["comparisons"]["multiple_of_w01_process_energy"] == pytest.approx(11.1, abs=0.1)


def test_40mw_is_not_a_commissioning_tier():
    assert r3.locality_scenario_40mw()["status"] == "SCENARIO_ONLY_NOT_A_COMMISSIONING_TIER"
    assert 40_000.0 not in r3.TIERS_KW


def test_flywheel_is_derived_from_the_register():
    layers = loc.derive_flywheel()
    assert len(layers) == 12
    for lay in layers.values():
        assert lay["status"] in (
            "PHYSICAL_FLOW_PRESENT", "OPPORTUNITY_ONLY", "NO_REGISTERED_STREAM",
            "CONTROLLED_BY_VETO_AND_PERMIT_STATE",
            "AWAITING_PRIMARY_ECOLOGICAL_EVIDENCE",
            "NO_METERED_STREAM",
        )
        assert lay["layer_basis"] in loc.LAYER_BASES
        assert lay["realized_credit"] == 0


def test_jobs_layer_reports_no_metered_stream():
    """Honest: the jobs/community layer has no metered stream."""
    assert loc.derive_flywheel()[10]["status"] == "NO_METERED_STREAM"
    assert loc.derive_flywheel()[10]["layer_basis"] == "SOCIAL_METRIC_DERIVED"


def test_governance_is_control_derived_not_a_missing_stream():
    """Absence of a physical stream is not absence of a working layer."""
    gov = loc.derive_flywheel()[12]
    assert gov["layer_basis"] == "CONTROL_DERIVED"
    assert gov["status"] == "CONTROLLED_BY_VETO_AND_PERMIT_STATE"
    assert gov["status"] != "NO_REGISTERED_STREAM"


def test_ecology_is_evidence_derived():
    eco = loc.derive_flywheel()[7]
    assert eco["layer_basis"] == "EVIDENCE_DERIVED"
    assert eco["status"] == "AWAITING_PRIMARY_ECOLOGICAL_EVIDENCE"


def test_every_layer_declares_a_basis():
    assert sorted(loc.LAYER_BASIS) == list(range(1, 13))
    assert all(b in loc.LAYER_BASES for b in loc.LAYER_BASIS.values())


def test_water_layer_has_a_physical_flow():
    assert loc.derive_flywheel()[3]["status"] == "PHYSICAL_FLOW_PRESENT"


def test_register_declares_the_pareto_rule():
    assert "Pareto front" in loc.run()["pareto_rule"]


def test_register_preserves_runs_0_to_3():
    assert "do not become obsolete" in loc.run()["what_this_changes"]


def test_register_lists_next_receipts():
    joined = " ".join(loc.run()["next_receipts"])
    assert "circular-economy implementation plan" in joined
    assert "green-direct" in joined
# ---------------------------------------------------------------------------
# PATCH 5 — the credit gate must not trust edge_state alone
# ---------------------------------------------------------------------------
def test_reported_evidence_cannot_realize_credit_even_if_tagged_measured_physical():
    """The v0.2 loophole. Trusting edge_state alone defeated the whole rule."""
    s = loc._s("X", "W01", "P01", "test", "1",
               evidence="REPORTED", edge_state="MEASURED_PHYSICAL",
               credit_owner="W01")
    assert s["realized_credit"] is False


def test_measured_evidence_with_measured_physical_and_owner_does_realize_credit():
    s = loc._s("X", "W01", "P01", "test", "1",
               evidence="MEASURED", edge_state="MEASURED_PHYSICAL",
               credit_owner="W01")
    assert s["realized_credit"] is True


def test_measured_physical_without_a_valid_owner_cannot_realize_credit():
    for owner in ("NONE", "UNKNOWN"):
        s = loc._s("X", "W01", "P01", "test", "1",
                   evidence="MEASURED", edge_state="MEASURED_PHYSICAL",
                   credit_owner=owner)
        assert s["realized_credit"] is False, owner


def test_credit_requires_all_three_conditions():
    assert loc._realizes_credit("MEASURED_PHYSICAL", "MEASURED", "W01") is True
    assert loc._realizes_credit("MEASURED_PHYSICAL", "MEASURED", "NONE") is False
    assert loc._realizes_credit("MEASURED_PHYSICAL", "REPORTED", "W01") is False
    assert loc._realizes_credit("REPORTED_PHYSICAL", "MEASURED", "W01") is False


def test_every_measured_evidence_stream_is_also_measured_physical():
    """Cross-check: measured evidence implies a measured physical flow."""
    for s in loc.known_streams():
        if s["evidence_class"] == "MEASURED":
            assert s["edge_state"] == "MEASURED_PHYSICAL", s["stream_id"]


def test_stream_inconsistencies_detects_a_planted_defect():
    bad = loc._s("BAD", "W01", "P01", "test", "1",
                 evidence="REPORTED", edge_state="MEASURED_PHYSICAL",
                 credit_owner="W01")
    found = loc.stream_inconsistencies([bad])
    assert len(found) == 1
    assert found[0]["stream_id"] == "BAD"
    assert "without measured evidence" in found[0]["problem"]


def test_real_register_has_no_inconsistencies():
    result = loc.run()
    assert result["counts"]["streams_with_inconsistent_evidence"] == 0
    assert result["stream_inconsistencies"] == []


def test_register_reports_zero_realized_credit():
    assert loc.run()["counts"]["streams_realizing_credit"] == 0


def test_layer_bases_are_exported():
    assert loc.run()["layer_bases"] == list(loc.LAYER_BASES)
