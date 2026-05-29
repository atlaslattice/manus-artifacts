from datetime import datetime, timezone

from reference_impl.atlas_orcs.compatible import check_compatibility
from reference_impl.atlas_orcs.delta import apply_delta
from reference_impl.atlas_orcs.ratification import enforce_ratification_freshness
from reference_impl.native_thread.validator import validate_native_thread_packet
from reference_impl.o_ai.validator import validate_o_ai_packet


def test_t13_overclaim_without_caveat_is_rejected_for_summary_native_thread():
    packet = {
        "raw_export_status": "summary_only",
        "thread_time_range": {"start": "2026-05-28T00:00:00Z", "end": "2026-05-28T00:10:00Z", "timezone": "UTC"},
        "access_scope": {"visible_sources": ["summary"], "unavailable_sources": ["raw"], "assumed_context": []},
        "strongest_safe_claim": "This is definitive and complete.",
    }
    errors = validate_native_thread_packet(packet)
    assert "missing_caveat_for_non_raw_claim" in errors


def test_t14_ratification_without_event_is_blocked():
    artifact = {"artifact_id": "adv-14", "trust_state": "reviewed"}
    updated, errors = apply_delta(artifact, {"trust_state": "ratified"})
    assert "ratified_requires_ratification_event" in errors
    assert updated["trust_state"] == "reviewed"


def test_t15_deployment_change_without_governance_event_is_blocked():
    artifact = {"artifact_id": "adv-15", "trust_state": "reviewed", "deployment_status": "candidate"}
    _, errors = apply_delta(artifact, {"deployment_status": "active"})
    assert "deployment_change_requires_governance_event" in errors


def test_t16_summary_cannot_replace_source_basis():
    artifact = {
        "artifact_id": "adv-16",
        "trust_state": "reviewed",
        "source_status": "source",
        "source_basis": "full_source",
    }
    _, errors = apply_delta(artifact, {"source_basis": "summary_only"})
    assert "summary_cannot_replace_source" in errors


def test_t17_execution_request_without_full_gate_pass_fails():
    packet = {
        "raw_export_status": "full_raw",
        "thread_time_range": {"start": "2026-05-28T00:00:00Z", "end": "2026-05-28T00:10:00Z", "timezone": "UTC"},
        "access_scope": {"visible_sources": ["raw"], "unavailable_sources": [], "assumed_context": []},
        "epistemic_label": "candidate",
        "authority_scope": "analysis_only",
        "execution_request": True,
        "gates": {
            "provenance_gate": "pass",
            "safety_gate": "pass",
            "governance_gate": "fail",
            "human_permission_gate": "pass",
            "receipt_gate": "pass",
        },
    }
    errors = validate_o_ai_packet(packet)
    assert "execution_gate_failed:governance_gate" in errors


def test_t18_invalid_state_transition_is_blocked_by_compatibility_check():
    artifact = {"artifact_id": "adv-18", "trust_state": "raw"}
    errors = check_compatibility(artifact, {"trust_state": "active"})
    assert "invalid:state_transition" in errors


def test_t19_quarantine_transition_preserves_lineage_and_marks_source_state():
    artifact = {"artifact_id": "adv-19", "trust_state": "candidate", "lineage": ["root-adv"]}
    updated, errors = apply_delta(artifact, {"trust_state": "quarantined", "quarantine_reason": "adversarial mismatch"})
    assert errors == []
    assert updated["trust_state"] == "quarantined"
    assert updated["quarantined_from"] == "candidate"
    assert updated["lineage"] == ["root-adv", "adv-19"]


def test_t20_expired_ratification_forces_under_review_state():
    artifact = {
        "artifact_id": "adv-20",
        "trust_state": "active",
        "ratification_event": {"ratification_event_id": "rat-20"},
        "ratification_expires_at": "2026-01-01T00:00:00Z",
    }
    updated = enforce_ratification_freshness(artifact, now=datetime(2026, 5, 28, tzinfo=timezone.utc))
    assert updated["trust_state"] == "under_review"
