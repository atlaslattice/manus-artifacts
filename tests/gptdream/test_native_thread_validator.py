from reference_impl.native_thread.validator import validate_native_thread_packet


def test_native_thread_required_fields_and_caveat_rule():
    pkt = {
        "seat_name": "TIDELOCKBrain",
        "model_surface": "task-thread",
        "source_thread_label": "example",
        "thread_time_range": {"start": "2026-05-26T00:00:00Z", "end": "2026-05-26T01:00:00Z", "timezone": "UTC"},
        "raw_export_status": "summary_only",
        "access_scope": {"visible_sources": ["summary"], "unavailable_sources": ["raw"], "assumed_context": ["partial"]},
        "strongest_safe_claim": "Caveat: partial evidence only.",
        "next_action": "request raw export",
    }
    assert validate_native_thread_packet(pkt) == []


def test_summary_only_cannot_claim_full_ingestion():
    pkt = {
        "raw_export_status": "summary_only",
        "thread_time_range": {"start": "a", "end": "b", "timezone": "UTC"},
        "access_scope": {"visible_sources": [], "unavailable_sources": [], "assumed_context": []},
        "strongest_safe_claim": "Caveat: limited",
        "ingestion_completeness": "full",
    }
    errors = validate_native_thread_packet(pkt)
    assert "summary_only_cannot_claim_full_ingestion" in errors
