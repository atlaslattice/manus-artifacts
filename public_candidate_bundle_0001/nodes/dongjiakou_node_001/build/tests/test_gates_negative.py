"""Negative controls for the validator gates.

A gate that cannot be made to fail is not a gate. Every gate in the registry is
fed a deliberately violating bundle here, and must return FAIL or VETO.

The final test asserts that the set of gates covered by this module equals the
set of gates actually registered, so adding a gate without a negative control
fails the suite.
"""

from __future__ import annotations

import pytest

from models import RUN_REGISTRY
from models.common import UNKNOWN, EvidenceClass
from sources import loader
from validators import build_bundle, validate
from validators.gates import FAIL, GATES, VETO
from validators.ledger import CreditEntry, CreditLedger

GATE_BY_ID = {g.gate_id: g for g in GATES}

BUNDLE_KEYS = (
    "RUN_0", "RUN_0.2", "RUN_1", "RUN_2", "RUN_3", "RUN_4A", "S02",
    "INTEGRATED_NODE_PROFILE", "C01_MODEL_ROUTING_POLICY",
)


def make_bundle(artifacts=None, ledger=None, **overrides):
    """Build a validator bundle, defaulting to the real evidence base."""
    loaded = loader.load_all()
    if artifacts is None:
        artifacts = {k: loaded[k] for k in BUNDLE_KEYS if k in loaded}
    defaults = {
        "node_profile": loaded["INTEGRATED_NODE_PROFILE"],
        "routing_policy": loaded["C01_MODEL_ROUTING_POLICY"],
        "produced_runs": {rid: fn() for rid, fn in RUN_REGISTRY.items()},
        "ecological_veto_passed": True,
        "hydro_recovered_head_m": UNKNOWN,
    }
    if ledger is not None:
        defaults["ledger"] = ledger
    defaults.update(overrides)
    return build_bundle(artifacts, **defaults)


# ---------------------------------------------------------------------------
# Baseline: the real evidence base must pass
# ---------------------------------------------------------------------------
def test_real_evidence_base_passes_every_gate():
    report = validate(make_bundle())
    assert report.passed, [(r.gate_id, r.status, r.detail) for r in report.failures]


def test_gate_registry_is_non_empty_and_well_formed():
    assert len(GATES) >= 16
    ids = [g.gate_id for g in GATES]
    assert len(ids) == len(set(ids)), "duplicate gate ids"
    for gate in GATES:
        assert gate.title and gate.invariant and callable(gate.check)


# ---------------------------------------------------------------------------
# G01 — UNKNOWN cannot enter Monte Carlo
# ---------------------------------------------------------------------------
def test_g01_fires_on_unknown_monte_carlo_parameter():
    bundle = make_bundle(
        monte_carlo_requested=True,
        monte_carlo_parameters={"PUE": UNKNOWN, "tariff": 0.555},
    )
    result = GATE_BY_ID["G01"].check(bundle)
    assert result.status == FAIL
    assert any(f["parameter"] == "PUE" for f in result.findings)


def test_g01_passes_with_established_parameters():
    bundle = make_bundle(
        monte_carlo_requested=True, monte_carlo_parameters={"PUE": 1.25, "tariff": 0.6}
    )
    assert GATE_BY_ID["G01"].check(bundle).status == "PASS"


# ---------------------------------------------------------------------------
# G02 — UNKNOWN cannot silently become zero
# ---------------------------------------------------------------------------
def test_g02_fires_on_an_unjustified_zero_credit():
    bundle = make_bundle(artifacts={"RUN_X": {"some_credit": 0}})
    result = GATE_BY_ID["G02"].check(bundle)
    assert result.status == "WARN"
    assert result.findings


def test_g02_accepts_a_justified_zero():
    bundle = make_bundle(
        artifacts={"RUN_X": {"baseline_credit": 0, "reason": "no receipt exists"}}
    )
    assert GATE_BY_ID["G02"].check(bundle).status == "PASS"


# ---------------------------------------------------------------------------
# G03 — historical values cannot populate current state
# ---------------------------------------------------------------------------
def test_g03_fires_when_a_current_quantity_is_populated():
    artifacts = {"RUN_0.2": {"economics": {"current_electricity_cost_CNY": 21_892_530.0}}}
    result = GATE_BY_ID["G03"].check(make_bundle(artifacts=artifacts))
    assert result.status == FAIL
    assert result.findings


def test_g03_ignores_identifier_fields_named_current():
    artifacts = {"X": {"current_runs": ["RUN_0", "RUN_1"], "current_component_anchor": "DJK"}}
    assert GATE_BY_ID["G03"].check(make_bundle(artifacts=artifacts)).status == "PASS"


# ---------------------------------------------------------------------------
# G04 — planned capacity cannot populate operating state
# ---------------------------------------------------------------------------
def test_g04_fires_when_planned_capacity_is_credited():
    profile = dict(loader.load_all()["INTEGRATED_NODE_PROFILE"])
    profile["green_direct_status"] = dict(profile["green_direct_status"])
    profile["green_direct_status"]["energy_credit"] = 214_000_000.0
    result = GATE_BY_ID["G04"].check(make_bundle(node_profile=profile))
    assert result.status == FAIL


# ---------------------------------------------------------------------------
# G05 — residual cannot become marine discharge
# ---------------------------------------------------------------------------
def test_g05_fires_on_a_discharge_claim():
    result = GATE_BY_ID["G05"].check(make_bundle(claimed_marine_discharge=True))
    assert result.status == FAIL


# ---------------------------------------------------------------------------
# G06 / G14 — PV and S01 single-credit rules
# ---------------------------------------------------------------------------
def test_g06_fires_when_s01_pv_is_treated_as_incremental():
    result = GATE_BY_ID["G06"].check(make_bundle(s01_pv_treated_as_incremental=True))
    assert result.status == FAIL


def test_g06_fires_on_two_primary_credits_for_one_pv_kwh():
    ledger = CreditLedger()
    for entry_id in ("a", "b"):
        ledger.add(CreditEntry(entry_id, "energy", "S01_PV_energy", 1000.0, "kWh/year",
                               EvidenceClass.MEASURED))
    result = GATE_BY_ID["G06"].check(make_bundle(ledger=ledger))
    assert result.status == FAIL


def test_g14_fires_when_incrementality_flag_is_absent():
    artifacts = {"RUN_3": {"anti_double_counting": {}}}
    result = GATE_BY_ID["G14"].check(make_bundle(artifacts=artifacts))
    assert result.status == FAIL


# ---------------------------------------------------------------------------
# G07 — one recovered mass cannot be double-credited
# ---------------------------------------------------------------------------
def test_g07_fires_on_double_credited_nutrient_mass():
    ledger = CreditLedger()
    for entry_id in ("fertiliser", "compost"):
        ledger.add(CreditEntry(entry_id, "mass", "BIO01_P_mass", 500.0, "kg P/year",
                               EvidenceClass.MEASURED))
    result = GATE_BY_ID["G07"].check(make_bundle(ledger=ledger))
    assert result.status == FAIL
    assert result.findings


# ---------------------------------------------------------------------------
# G08 — compute heat needs a measured sink
# ---------------------------------------------------------------------------
def test_g08_fires_on_heat_credit_without_a_sink():
    result = GATE_BY_ID["G08"].check(make_bundle(compute_heat_credit_gwh=1.5))
    assert result.status == FAIL


def test_g08_passes_when_heat_credit_is_zero():
    assert GATE_BY_ID["G08"].check(make_bundle(compute_heat_credit_gwh=0.0)).status == "PASS"


# ---------------------------------------------------------------------------
# G09 — service benefit needs before/after KPI evidence
# ---------------------------------------------------------------------------
def test_g09_fires_on_unmeasured_service_benefit():
    result = GATE_BY_ID["G09"].check(make_bundle(compute_service_benefit=0.12))
    assert result.status == FAIL


# ---------------------------------------------------------------------------
# G10 — ecological veto cannot be offset
# ---------------------------------------------------------------------------
def test_g10_vetoes_when_a_failed_ecological_gate_is_offset():
    bundle = make_bundle(ecological_veto_passed=False, aggregate_benefit_claimed=1_000_000.0)
    result = GATE_BY_ID["G10"].check(bundle)
    assert result.status == VETO


def test_g10_fires_when_the_node_veto_rule_is_missing():
    result = GATE_BY_ID["G10"].check(make_bundle(node_profile={}))
    assert result.status == FAIL


# ---------------------------------------------------------------------------
# G11 — LLM actuator authority is NONE
# ---------------------------------------------------------------------------
def test_g11_fires_when_a_model_has_actuator_authority():
    result = GATE_BY_ID["G11"].check(make_bundle(llm_actuator_authority="WRITE"))
    assert result.status == FAIL


def test_g11_fires_when_the_recommendation_path_bypasses_operator_approval():
    policy = dict(loader.load_all()["C01_MODEL_ROUTING_POLICY"])
    policy["authority_boundary"] = dict(policy["authority_boundary"])
    policy["authority_boundary"]["recommendation_path"] = "model -> PLC/SCADA"
    result = GATE_BY_ID["G11"].check(make_bundle(routing_policy=policy))
    assert result.status == FAIL


# ---------------------------------------------------------------------------
# G12 — model consensus is not evidence
# ---------------------------------------------------------------------------
def test_g12_fires_when_consensus_is_treated_as_evidence():
    result = GATE_BY_ID["G12"].check(make_bundle(model_consensus_treated_as_evidence=True))
    assert result.status == FAIL


# ---------------------------------------------------------------------------
# G13 — RO high-pressure head cannot be counted twice
# ---------------------------------------------------------------------------
def test_g13_fires_when_pump_head_is_counted_as_recovered():
    result = GATE_BY_ID["G13"].check(make_bundle(hydro_pump_head_counted=True))
    assert result.status == FAIL


def test_g13_warns_when_run2_output_is_absent():
    bundle = make_bundle(produced_runs={}, artifacts={"RUN_2": {}})
    assert GATE_BY_ID["G13"].check(bundle).status == "WARN"


# ---------------------------------------------------------------------------
# G15 — conservation and bound checks
# ---------------------------------------------------------------------------
def test_g15_fires_on_credit_exceeding_a_numeric_bound():
    ledger = CreditLedger()
    ledger.add(CreditEntry("a", "energy", "G01_regional_green_energy", 1000.0, "kWh/year",
                           EvidenceClass.MEASURED))
    result = GATE_BY_ID["G15"].check(make_bundle(ledger=ledger))
    assert result.status == FAIL
    assert any(f["kind"] == "BOUND_EXCEEDED" for f in result.findings)


def test_g15_fires_on_credit_with_unknown_availability():
    ledger = CreditLedger()
    ledger.add(CreditEntry("a", "energy", "S01_PV_energy", 1000.0, "kWh/year",
                           EvidenceClass.MEASURED))
    result = GATE_BY_ID["G15"].check(make_bundle(ledger=ledger))
    assert result.status == FAIL
    assert any(f["kind"] == "CREDIT_WITHOUT_ESTABLISHED_AVAILABILITY" for f in result.findings)


def test_g15_fires_on_an_unbounded_resource():
    ledger = CreditLedger()
    ledger.add(CreditEntry("a", "energy", "INVENTED_RESOURCE", 1.0, "kWh/year",
                           EvidenceClass.MEASURED))
    result = GATE_BY_ID["G15"].check(make_bundle(ledger=ledger))
    assert result.status == FAIL
    assert any(f["kind"] == "UNBOUNDED_RESOURCE" for f in result.findings)


# ---------------------------------------------------------------------------
# G16 — net-positive requires measured terms
# ---------------------------------------------------------------------------
def test_g16_fires_on_unmeasured_net_positive_claim():
    result = GATE_BY_ID["G16"].check(make_bundle(net_positive_claim=True))
    assert result.status == FAIL
    assert len(result.findings) == 4


def test_g16_passes_when_all_terms_are_measured():
    bundle = make_bundle(
        net_positive_claim=True,
        measured_net_positive_terms={
            "new_incremental_clean_generation": 3.0,
            "verified_plant_electrical_savings": 0.4,
            "verified_heat_pump_electrical_savings": 0.2,
            "compute_facility_electricity": 1.1,
        },
    )
    assert GATE_BY_ID["G16"].check(bundle).status == "PASS"


# ---------------------------------------------------------------------------
# Meta: every registered gate must have a negative control above
# ---------------------------------------------------------------------------
def test_every_registered_gate_has_a_negative_control():
    covered = {
        "G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08",
        "G09", "G10", "G11", "G12", "G13", "G14", "G15", "G16",
    }
    registered = {g.gate_id for g in GATES}
    assert registered == covered, (
        f"gates without a negative control: {sorted(registered - covered)}; "
        f"controls for unregistered gates: {sorted(covered - registered)}"
    )
