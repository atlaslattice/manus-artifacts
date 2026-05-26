from __future__ import annotations

from typing import Any


REQUIRED_FIELDS = {
    "raw_export_status",
    "thread_time_range",
    "access_scope",
    "epistemic_label",
    "authority_scope",
    "gates",
}

REQUIRED_GATE_FIELDS = {
    "provenance_gate",
    "safety_gate",
    "governance_gate",
    "data_residency_gate",
}

EXECUTION_PASS_GATES = {
    "provenance_gate",
    "safety_gate",
    "governance_gate",
    "human_permission_gate",
    "receipt_gate",
}


def _as_gate_value(gates: dict[str, Any], key: str) -> Any:
    if key in gates:
        return gates.get(key)
    legacy = key.replace("_gate", "")
    return gates.get(legacy)


def validate_oai_packet(packet: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    for field in sorted(REQUIRED_FIELDS):
        if field not in packet:
            errors.append(f"missing required field: {field}")

    gates = packet.get("gates", {})
    if not isinstance(gates, dict):
        errors.append("gates must be an object")
        gates = {}

    for gate in sorted(REQUIRED_GATE_FIELDS):
        if gate not in gates:
            errors.append(f"missing required gate field: gates.{gate}")

    if packet.get("raw_export_status") == "summary_only" and packet.get("public_use_status") == "source_complete":
        errors.append("summary_only packets cannot have public_use_status=source_complete")

    access_scope = packet.get("access_scope", {})
    if not isinstance(access_scope, dict):
        errors.append("access_scope must be an object")
    else:
        for field in ("unavailable_sources", "assumed_context"):
            if field not in access_scope:
                errors.append(f"access_scope must explicitly include: {field}")

    if packet.get("packet_kind") == "execution_request":
        for gate in sorted(EXECUTION_PASS_GATES):
            if _as_gate_value(gates, gate) != "pass":
                errors.append(f"execution_request requires pass gate: {gate}")

    return len(errors) == 0, errors
