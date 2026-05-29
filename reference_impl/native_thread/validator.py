from __future__ import annotations


def validate_native_thread_packet(packet: dict) -> list[str]:
    errors: list[str] = []
    for field in ("raw_export_status", "thread_time_range", "access_scope", "strongest_safe_claim"):
        if field not in packet:
            errors.append(f"missing:{field}")

    if "access_scope" in packet:
        for field in ("visible_sources", "unavailable_sources", "assumed_context"):
            if field not in packet["access_scope"]:
                errors.append(f"missing:access_scope.{field}")

    if packet.get("raw_export_status") == "summary_only" and packet.get("ingestion_completeness") == "full":
        errors.append("summary_only_cannot_claim_full_ingestion")

    if packet.get("raw_export_status") != "full_raw":
        claim = packet.get("strongest_safe_claim", "")
        if "caveat" not in claim.lower():
            errors.append("missing_caveat_for_non_raw_claim")

    return errors
