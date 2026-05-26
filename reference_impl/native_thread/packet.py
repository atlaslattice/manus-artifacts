def strongest_safe_claim(packet: dict) -> str:
    raw_status = packet.get("raw_export_status")
    claim = packet.get("strongest_safe_claim", "")
    if raw_status in {"summary_only", "unavailable"}:
        return f"{claim} (caveated: raw absent)"
    return claim
