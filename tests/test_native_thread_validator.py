def validate_native_thread(packet: dict) -> bool:
    for key in ["raw_export_status", "thread_time_range", "access_scope"]:
        if key not in packet:
            return False
    if packet.get("raw_export_status") == "summary_only" and packet.get("full_ingestion", False):
        return False
    if "unavailable_sources" not in packet.get("access_scope", {}):
        return False
    return True


def test_native_thread_rules():
    packet = {
        "raw_export_status": "summary_only",
        "thread_time_range": {"start": "a", "end": "b", "timezone": "UTC"},
        "access_scope": {"visible_sources": [], "unavailable_sources": ["raw"], "assumed_context": ["summary"]},
        "full_ingestion": False,
    }
    assert validate_native_thread(packet)
