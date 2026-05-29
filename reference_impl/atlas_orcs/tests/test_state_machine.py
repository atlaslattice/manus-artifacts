from datetime import datetime, timezone

from reference_impl.atlas_orcs.delta import apply_delta


def test_cannot_move_to_ratified_without_ratification_event():
    artifact = {"artifact_id": "a1", "trust_state": "reviewed"}
    updated, errors = apply_delta(artifact, {"trust_state": "ratified"})
    assert errors == ["ratified_requires_ratification_event"]
    assert updated["trust_state"] == "reviewed"


def test_deployment_change_requires_governance_event():
    artifact = {"artifact_id": "a1", "trust_state": "reviewed", "deployment_status": "candidate"}
    updated, errors = apply_delta(artifact, {"deployment_status": "active"})
    assert "deployment_change_requires_governance_event" in errors
    assert updated["deployment_status"] == "candidate"


def test_quarantine_preserves_lineage():
    artifact = {"artifact_id": "a1", "trust_state": "candidate", "lineage": ["root-1"]}
    updated, errors = apply_delta(artifact, {"trust_state": "quarantined", "quarantine_reason": "bad provenance"})
    assert errors == []
    assert updated["trust_state"] == "quarantined"
    assert updated["lineage"] == ["root-1", "a1"]


def test_contradiction_creates_record_not_overwrite():
    artifact = {"artifact_id": "a1", "trust_state": "reviewed", "claim": {"value": "source-backed"}}
    updated, errors = apply_delta(
        artifact,
        {
            "contradiction_claim": {"value": "incompatible-summary"},
            "contradiction_reason": "source mismatch",
        },
    )
    assert errors == []
    assert updated["claim"] == {"value": "source-backed"}
    assert len(updated["contradiction_records"]) == 1
    assert updated["contradiction_records"][0]["conflicting_claim"] == {"value": "incompatible-summary"}


def test_summary_cannot_replace_source():
    artifact = {
        "artifact_id": "a1",
        "trust_state": "reviewed",
        "source_status": "source",
        "source_basis": "full_source",
    }
    updated, errors = apply_delta(artifact, {"source_basis": "summary_only"})
    assert "summary_cannot_replace_source" in errors
    assert updated["source_basis"] == "full_source"


def test_expired_ratification_moves_to_under_review():
    artifact = {
        "artifact_id": "a1",
        "trust_state": "ratified",
        "ratification_event": {"ratification_event_id": "rat-1"},
        "ratification_expires_at": "2026-01-01T00:00:00Z",
    }
    updated, errors = apply_delta(
        artifact,
        {"trust_state": "ratified"},
        now=datetime(2026, 5, 26, tzinfo=timezone.utc),
    )
    assert errors == []
    assert updated["trust_state"] == "under_review"
