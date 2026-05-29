def strongest_safe_claim(packet: dict) -> str:
    status = packet.get("raw_export_status")
    base = packet.get("strongest_safe_claim", "candidate claim only")
    if status in {"summary_only", "unavailable", "partial_raw"}:
        return f"{base} (caveat: raw source absent or incomplete)"
    return base
