from __future__ import annotations


def validate_o_ai_packet(packet: dict) -> list[str]:
    errors: list[str] = []
    for field in ("raw_export_status", "thread_time_range", "access_scope", "epistemic_label", "authority_scope", "gates"):
        if field not in packet:
            errors.append(f"missing:{field}")

    if "access_scope" in packet:
        for field in ("visible_sources", "unavailable_sources", "assumed_context"):
            if field not in packet["access_scope"]:
                errors.append(f"missing:access_scope.{field}")

    if packet.get("raw_export_status") == "summary_only" and packet.get("public_use_status") == "source_complete":
        errors.append("summary_only_cannot_be_source_complete")

    if packet.get("execution_request") is True:
        gates = packet.get("gates", {})
        required_pass = (
            "provenance_gate",
            "safety_gate",
            "governance_gate",
            "human_permission_gate",
            "receipt_gate",
        )
        for g in required_pass:
            if gates.get(g) != "pass":
                errors.append(f"execution_gate_failed:{g}")

    return errors
