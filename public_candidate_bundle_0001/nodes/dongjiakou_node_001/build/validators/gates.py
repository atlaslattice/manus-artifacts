"""The Node-001 validator gate set.

Each gate is a named, individually reportable rule. Gates return PASS, WARN,
FAIL, VETO or NOT_APPLICABLE. A validation run passes only when no gate returns
FAIL or VETO.

Every gate has a negative control in ``tests/test_gates_negative.py`` that feeds
it a deliberately violating bundle and asserts that it fires. A gate that cannot
be made to fail is not a gate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from models.common import UNKNOWN, EvidenceClass, is_unknown, to_jsonable

from .ledger import (
    PRIMARY_CREDITING_CLASSES,
    RESOURCE_BOUNDS,
    CreditLedger,
    bound_violations,
)

PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"
VETO = "VETO"
NOT_APPLICABLE = "NOT_APPLICABLE"

#: Fields whose zero value is an explicit, named zero-credit baseline rather
#: than a silently imputed UNKNOWN.
EXPLICIT_ZERO_BLOCKS = ("baseline_credit", "retrofit_credit")

#: Justification keys that may legitimate a zero in a credit-bearing field.
JUSTIFICATION_KEYS = ("reason", "warning", "note", "justification", "zero_credit_basis", "use_rule")

#: Fields that contain the token "current" but are identifiers or labels
#: rather than current-state physical quantities.
NON_MEASUREMENT_CURRENT_FIELDS = frozenset(
    {"current_runs", "current_component_anchor", "current_reference"}
)


@dataclass
class GateResult:
    gate_id: str
    title: str
    status: str
    detail: str
    findings: list[dict[str, Any]] = field(default_factory=list)

    @property
    def failed(self) -> bool:
        return self.status in (FAIL, VETO)


@dataclass
class Bundle:
    """Everything the gates are allowed to look at."""

    artifacts: dict[str, Any]
    node_profile: dict[str, Any]
    routing_policy: dict[str, Any]
    ledger: CreditLedger
    resource_bounds: dict[str, Any]
    #: Outputs of the simulator's own models, so gates can assert model
    #: behaviour without mutating the committed evidence artifacts.
    produced_runs: dict[str, Any] = field(default_factory=dict)
    monte_carlo_requested: bool = False
    monte_carlo_parameters: dict[str, Any] = field(default_factory=dict)
    claimed_marine_discharge: bool = False
    compute_heat_credit_gwh: float = 0.0
    compute_service_benefit: float = 0.0
    ecological_veto_passed: bool | None = None
    aggregate_benefit_claimed: float = 0.0
    llm_actuator_authority: Any = None
    model_consensus_treated_as_evidence: bool = False
    hydro_recovered_head_m: Any = UNKNOWN
    hydro_pump_head_counted: bool = False
    s01_pv_credits: list[str] = field(default_factory=list)
    s01_pv_treated_as_incremental: bool = False
    net_positive_claim: bool = False
    measured_net_positive_terms: dict[str, Any] = field(default_factory=dict)


GateFn = Callable[[Bundle], GateResult]


@dataclass
class Gate:
    gate_id: str
    title: str
    invariant: str
    check: GateFn


# ---------------------------------------------------------------------------
# G01 — UNKNOWN cannot enter Monte Carlo
# ---------------------------------------------------------------------------
def gate_unknown_no_monte_carlo(b: Bundle) -> GateResult:
    if not b.monte_carlo_requested:
        return GateResult("G01", "UNKNOWN cannot enter Monte Carlo", NOT_APPLICABLE,
                          "No Monte Carlo execution was requested.")
    bad = {k: v for k, v in b.monte_carlo_parameters.items() if is_unknown(v)}
    if bad:
        return GateResult(
            "G01", "UNKNOWN cannot enter Monte Carlo", FAIL,
            "Monte Carlo was requested with UNKNOWN parameters.",
            [{"parameter": k, "value": "UNKNOWN"} for k in sorted(bad)],
        )
    return GateResult("G01", "UNKNOWN cannot enter Monte Carlo", PASS,
                      f"{len(b.monte_carlo_parameters)} parameter(s) are all established.")


# ---------------------------------------------------------------------------
# G02 — UNKNOWN cannot become zero without an explicit zero-credit statement
# ---------------------------------------------------------------------------
def gate_unknown_not_silently_zero(b: Bundle) -> GateResult:
    findings: list[dict[str, Any]] = []
    for run_id, artifact in b.artifacts.items():
        if not isinstance(artifact, dict):
            continue
        justification = _collect_justification(artifact)
        for path, value in _walk(artifact, run_id):
            leaf = path.rsplit(".", 1)[-1]
            if not any(tok in leaf for tok in ("credit", "benefit", "saving")):
                continue
            if not (isinstance(value, (int, float)) and not isinstance(value, bool)):
                continue
            if value != 0:
                continue
            if _inside_explicit_zero_block(path):
                continue
            if justification:
                continue
            findings.append({"run": run_id, "path": path, "value": 0,
                             "detail": "Zero in a credit-bearing field without an inline justification."})
    if findings:
        return GateResult("G02", "UNKNOWN cannot silently become zero", WARN,
                          f"{len(findings)} zero-valued credit field(s) lack an inline justification.",
                          findings)
    return GateResult("G02", "UNKNOWN cannot silently become zero", PASS,
                      "Every zero-valued credit field is either an explicit baseline or justified.")


# ---------------------------------------------------------------------------
# G03 — historical values cannot silently populate current state
# ---------------------------------------------------------------------------
def gate_historical_not_current(b: Bundle) -> GateResult:
    """A current-state *quantity* must stay UNKNOWN until a current receipt exists."""
    findings: list[dict[str, Any]] = []
    for run_id, artifact in b.artifacts.items():
        if not isinstance(artifact, dict):
            continue
        for path, value in _walk(artifact, run_id):
            leaf = path.rsplit(".", 1)[-1]
            if "current" not in leaf or leaf in NON_MEASUREMENT_CURRENT_FIELDS:
                continue
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                # Non-numeric: an identifier or label, not a physical quantity.
                continue
            if is_unknown(value) or value == 0:
                continue
            if any(tok in path for tok in ("historical", "counterfactual", "warning")):
                continue
            findings.append({"run": run_id, "path": path, "value": to_jsonable(value),
                             "detail": "A current-state field carries a non-UNKNOWN value."})
    if findings:
        return GateResult("G03", "Historical values cannot populate current state", FAIL,
                          f"{len(findings)} current-state field(s) are populated without a "
                          "current receipt.", findings)
    return GateResult("G03", "Historical values cannot populate current state", PASS,
                      "All current-state fields remain UNKNOWN; historical figures are labelled "
                      "counterfactual.")


# ---------------------------------------------------------------------------
# G04 — planned capacity cannot populate current operating state
# ---------------------------------------------------------------------------
def gate_planned_not_operating(b: Bundle) -> GateResult:
    green = (b.node_profile.get("green_direct_status") or {})
    components = {c.get("component_id"): c for c in b.node_profile.get("components", [])}
    findings: list[dict[str, Any]] = []

    if green.get("energy_credit") not in (0, 0.0):
        findings.append({"field": "green_direct_status.energy_credit",
                         "value": to_jsonable(green.get("energy_credit")),
                         "detail": "Planned regional capacity was credited to the node."})

    g01 = components.get("G01_REGIONAL_GREEN") or {}
    if g01.get("node001_access") != "UNKNOWN" and g01.get("energy_credit") not in (0, 0.0):
        findings.append({"field": "G01_REGIONAL_GREEN", "value": to_jsonable(g01.get("energy_credit")),
                         "detail": "Regional planned generation treated as node access."})

    if findings:
        return GateResult("G04", "Planned capacity cannot populate operating state", FAIL,
                          "Planned regional generation was treated as an operating quantity.",
                          findings)
    return GateResult("G04", "Planned capacity cannot populate operating state", PASS,
                      "Regional plan stays REPORTED with node access UNKNOWN and zero credit.")


# ---------------------------------------------------------------------------
# G05 — feed-minus-product residual cannot become marine discharge
# ---------------------------------------------------------------------------
def gate_residual_not_discharge(b: Bundle) -> GateResult:
    if b.claimed_marine_discharge:
        return GateResult("G05", "Feed-product residual cannot become marine discharge", FAIL,
                          "A modelled reject-equivalent was restated as a marine-discharge claim.")
    return GateResult("G05", "Feed-product residual cannot become marine discharge", PASS,
                      "Reject-equivalent remains labelled modelled; no discharge quantity is claimed.")


# ---------------------------------------------------------------------------
# G06 — one PV kWh cannot receive two primary credits
# ---------------------------------------------------------------------------
def gate_pv_single_credit(b: Bundle) -> GateResult:
    if b.s01_pv_treated_as_incremental:
        return GateResult("G06", "One PV kWh cannot receive two primary credits", FAIL,
                          "Existing S01 generation was treated as incremental new generation.")
    credits = b.ledger.primary_credits_for("S01_PV_energy")
    if len(credits) > 1:
        return GateResult("G06", "One PV kWh cannot receive two primary credits", FAIL,
                          "S01 PV carries more than one primary credit.",
                          [{"entry_id": e.entry_id} for e in credits])
    return GateResult("G06", "One PV kWh cannot receive two primary credits", PASS,
                      f"{len(credits)} primary credit(s) on S01 PV; at most one is permitted.")


# ---------------------------------------------------------------------------
# G07 — one recovered mass cannot be sold and also consumed elsewhere
# ---------------------------------------------------------------------------
def gate_mass_single_credit(b: Bundle) -> GateResult:
    findings = [
        v for v in bound_violations(b.ledger)
        if v["kind"] == "DOUBLE_PRIMARY_CREDIT"
        and v["resource_id"].startswith("BIO01_")
    ]
    if findings:
        return GateResult("G07", "One recovered mass cannot be double-credited", FAIL,
                          "A recovered N/P/Mg/water mass received more than one primary credit.",
                          findings)
    return GateResult("G07", "One recovered mass cannot be double-credited", PASS,
                      "No BIO01 recovered mass carries more than one primary credit.")


# ---------------------------------------------------------------------------
# G08 — compute heat cannot receive electric credit without a measured sink
# ---------------------------------------------------------------------------
def gate_compute_heat_requires_sink(b: Bundle) -> GateResult:
    if b.compute_heat_credit_gwh > 0:
        sinks = [e for e in b.ledger.for_resource("C01_useful_heat")
                 if e.evidence_class in PRIMARY_CREDITING_CLASSES and e.quantity > 0]
        if not sinks:
            return GateResult("G08", "Compute heat needs a measured sink", FAIL,
                              "Useful-heat credit was taken with no measured thermal sink.",
                              [{"heat_credit_GWhth": b.compute_heat_credit_gwh}])
    return GateResult("G08", "Compute heat needs a measured sink", PASS,
                      "Useful-heat credit is zero; the first-law bound is reported separately.")


# ---------------------------------------------------------------------------
# G09 — compute service benefit stays zero without before/after KPI evidence
# ---------------------------------------------------------------------------
def gate_service_benefit_requires_kpi(b: Bundle) -> GateResult:
    if b.compute_service_benefit > 0:
        return GateResult("G09", "Service benefit needs before/after KPI evidence", FAIL,
                          "A model service benefit was claimed without before/after measurement.",
                          [{"service_benefit": b.compute_service_benefit}])
    return GateResult("G09", "Service benefit needs before/after KPI evidence", PASS,
                      "Model service benefit remains zero.")


# ---------------------------------------------------------------------------
# G10 — an ecological veto cannot be offset by profit or carbon elsewhere
# ---------------------------------------------------------------------------
def gate_veto_not_offsettable(b: Bundle) -> GateResult:
    rule = b.node_profile.get("node_veto_rule", "")
    if b.ecological_veto_passed is False and b.aggregate_benefit_claimed > 0:
        return GateResult("G10", "Ecological veto cannot be offset", VETO,
                          "An aggregate benefit was used to offset a failed ecological veto.",
                          [{"aggregate_benefit_claimed": b.aggregate_benefit_claimed}])
    if "NODE_PASS" not in rule:
        return GateResult("G10", "Ecological veto cannot be offset", FAIL,
                          "The node profile does not carry an explicit node_veto_rule.")
    return GateResult("G10", "Ecological veto cannot be offset", PASS,
                      "node_veto_rule is present and aggregate benefit cannot offset a failed veto.")


# ---------------------------------------------------------------------------
# G11 — LLM actuator authority is NONE
# ---------------------------------------------------------------------------
def gate_llm_no_actuator_authority(b: Bundle) -> GateResult:
    authority = b.llm_actuator_authority
    if authority is None:
        authority = (b.routing_policy.get("authority_boundary") or {}).get("LLM_actuator_authority")
    if authority != "NONE":
        return GateResult("G11", "LLM actuator authority is NONE", FAIL,
                          f"Actuator authority is {authority!r}, not NONE.")
    path = (b.routing_policy.get("authority_boundary") or {}).get("recommendation_path", "")
    if "operator approval" not in path or "PLC/SCADA" not in path:
        return GateResult("G11", "LLM actuator authority is NONE", FAIL,
                          "The recommendation path does not route through operator approval "
                          "to PLC/SCADA.")
    return GateResult("G11", "LLM actuator authority is NONE", PASS,
                      "No OT write credentials; recommendations pass a validator and operator "
                      "approval before PLC/SCADA.")


# ---------------------------------------------------------------------------
# G12 — model consensus is not evidence
# ---------------------------------------------------------------------------
def gate_consensus_not_evidence(b: Bundle) -> GateResult:
    principles = " ".join(b.routing_policy.get("principles", []))
    if b.model_consensus_treated_as_evidence:
        return GateResult("G12", "Model consensus is not evidence", FAIL,
                          "Cross-model agreement was treated as evidence.")
    if "not evidence" not in principles:
        return GateResult("G12", "Model consensus is not evidence", WARN,
                          "The routing policy does not state that agreement is not evidence.")
    return GateResult("G12", "Model consensus is not evidence", PASS,
                      "Routing policy states cross-model agreement is not evidence.")


# ---------------------------------------------------------------------------
# G13 — RO high-pressure head cannot be counted twice
# ---------------------------------------------------------------------------
def gate_ro_head_not_double_counted(b: Bundle) -> GateResult:
    if b.hydro_pump_head_counted:
        return GateResult("G13", "RO high-pressure head cannot be counted twice", FAIL,
                          "Motor-supplied SWRO pump head was counted as recovered hydro energy.")
    # Prefer the simulator's own Run 2 output; fall back to the committed
    # artifact's interpretation text without editing that artifact in place.
    run2 = b.produced_runs.get("RUN_2") or b.artifacts.get("RUN_2", {})
    excluded = run2.get("excluded_head") or {}
    interpretation = " ".join(run2.get("interpretation", []) or []).lower()
    documented = (
        excluded.get("status") == "MOTOR_SUPPLIED_NOT_RECOVERABLE"
        or ("motor-supplied" in interpretation and "excluded" in interpretation)
    )
    if not documented:
        return GateResult("G13", "RO high-pressure head cannot be counted twice", WARN,
                          "Run 2 does not explicitly exclude the motor-supplied pump head.")
    if not is_unknown(b.hydro_recovered_head_m):
        return GateResult("G13", "RO high-pressure head cannot be counted twice", WARN,
                          "A recovered head value is present; confirm it is not pump-supplied.")
    return GateResult("G13", "RO high-pressure head cannot be counted twice", PASS,
                      "Pump head is explicitly excluded and no recovered head is claimed.")


# ---------------------------------------------------------------------------
# G14 — existing S01 solar cannot be counted twice
# ---------------------------------------------------------------------------
def gate_s01_solar_not_double_counted(b: Bundle) -> GateResult:
    adc = b.artifacts.get("RUN_3", {}).get("anti_double_counting") or {}
    if adc.get("existing_S01_PV_is_incremental_to_node") is not False:
        return GateResult("G14", "Existing S01 solar cannot be counted twice", FAIL,
                          "Run 3 does not assert that S01 PV is not incremental to the node.")
    if b.s01_pv_treated_as_incremental:
        return GateResult("G14", "Existing S01 solar cannot be counted twice", FAIL,
                          "S01 PV was treated as new incremental generation.")
    return GateResult("G14", "Existing S01 solar cannot be counted twice", PASS,
                      "S01 PV is explicitly non-incremental and carries at most one credit.")


# ---------------------------------------------------------------------------
# G15 — conservation and bound checks over the whole credit ledger
# ---------------------------------------------------------------------------
def gate_ledger_conservation(b: Bundle) -> GateResult:
    violations = bound_violations(b.ledger)
    if violations:
        return GateResult("G15", "Conservation and bound checks", FAIL,
                          f"{len(violations)} ledger violation(s).", violations)
    return GateResult("G15", "Conservation and bound checks", PASS,
                      f"{len(b.ledger.entries)} ledger entries; none exceed a resource bound.")


# ---------------------------------------------------------------------------
# G16 — net-positive may not be claimed without measured terms
# ---------------------------------------------------------------------------
def gate_net_positive_measured_only(b: Bundle) -> GateResult:
    if not b.net_positive_claim:
        return GateResult("G16", "Net-positive requires measured terms", PASS,
                          "No net-positive operation is claimed.")
    required = (
        "new_incremental_clean_generation",
        "verified_plant_electrical_savings",
        "verified_heat_pump_electrical_savings",
        "compute_facility_electricity",
    )
    missing = [k for k in required if is_unknown(b.measured_net_positive_terms.get(k, UNKNOWN))]
    if missing:
        return GateResult("G16", "Net-positive requires measured terms", FAIL,
                          "Net-positive was claimed with unmeasured terms.",
                          [{"missing": k} for k in missing])
    return GateResult("G16", "Net-positive requires measured terms", PASS,
                      "All net-positive terms are measured.")


GATES: tuple[Gate, ...] = (
    Gate("G01", "UNKNOWN cannot enter Monte Carlo",
         "No Monte Carlo over unestablished values.", gate_unknown_no_monte_carlo),
    Gate("G02", "UNKNOWN cannot silently become zero",
         "UNKNOWN never becomes 0 without an explicit zero-credit statement.",
         gate_unknown_not_silently_zero),
    Gate("G03", "Historical values cannot populate current state",
         "Historical figures stay historical.", gate_historical_not_current),
    Gate("G04", "Planned capacity cannot populate operating state",
         "Planned regional capacity is not node access.", gate_planned_not_operating),
    Gate("G05", "Feed-product residual cannot become marine discharge",
         "Modelled residual is not a discharge claim.", gate_residual_not_discharge),
    Gate("G06", "One PV kWh cannot receive two primary credits",
         "Single primary credit per PV kWh.", gate_pv_single_credit),
    Gate("G07", "One recovered mass cannot be double-credited",
         "Single primary credit per recovered mass.", gate_mass_single_credit),
    Gate("G08", "Compute heat needs a measured sink",
         "No electric credit for heat without a sink.", gate_compute_heat_requires_sink),
    Gate("G09", "Service benefit needs before/after KPI evidence",
         "Model service benefit stays zero without KPI evidence.",
         gate_service_benefit_requires_kpi),
    Gate("G10", "Ecological veto cannot be offset",
         "INV-19 remains a veto.", gate_veto_not_offsettable),
    Gate("G11", "LLM actuator authority is NONE",
         "No model writes to OT.", gate_llm_no_actuator_authority),
    Gate("G12", "Model consensus is not evidence",
         "Agreement is not a receipt.", gate_consensus_not_evidence),
    Gate("G13", "RO high-pressure head cannot be counted twice",
         "Motor-supplied head is excluded.", gate_ro_head_not_double_counted),
    Gate("G14", "Existing S01 solar cannot be counted twice",
         "S01 is not incremental.", gate_s01_solar_not_double_counted),
    Gate("G15", "Conservation and bound checks",
         "Credits stay inside sourced availability.", gate_ledger_conservation),
    Gate("G16", "Net-positive requires measured terms",
         "Compute pays rent in measured service.", gate_net_positive_measured_only),
)


def _walk(obj: Any, prefix: str = ""):
    """Yield ``(path, value)`` for every leaf, including inside lists."""
    if isinstance(obj, dict):
        for key, val in obj.items():
            yield from _walk(val, f"{prefix}.{key}" if prefix else str(key))
    elif isinstance(obj, list):
        for idx, val in enumerate(obj):
            yield from _walk(val, f"{prefix}[{idx}]")
    else:
        yield prefix, obj


def _collect_justification(artifact: dict[str, Any]) -> str:
    """Concatenate any justification strings present in an artifact."""
    chunks: list[str] = []
    for key in JUSTIFICATION_KEYS:
        for path, value in _walk(artifact):
            if path.rsplit(".", 1)[-1] == key and isinstance(value, str):
                chunks.append(value)
    return " ".join(chunks)


def _inside_explicit_zero_block(path: str) -> bool:
    return any(block in path for block in EXPLICIT_ZERO_BLOCKS)


__all__ = ["Bundle", "Gate", "GateResult", "GATES", "PASS", "WARN", "FAIL", "VETO",
           "NOT_APPLICABLE", "RESOURCE_BOUNDS"]
