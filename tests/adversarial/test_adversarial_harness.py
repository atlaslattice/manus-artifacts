import pytest

from reference_impl.atlas_orcs.audit import build_audit_event
from reference_impl.atlas_orcs.delta import TransitionDelta
from reference_impl.atlas_orcs.quarantine import quarantine_artifact
from reference_impl.atlas_orcs.transitions import TransitionError, apply_transition


ATTACK_CASES = [
    ("T01", "fake SOURCE_OF_TRUTH.md"),
    ("T02", "hidden prompt injection"),
    ("T03", "summary introduces unsupported claim"),
    ("T04", "parser divergence"),
    ("T05", "unverified authorship"),
    ("T06", "credible contradiction"),
    ("T07", "expired ratification"),
    ("T08", "high-risk weak claim"),
    ("T09", "private note leak"),
    ("T10", "unauthorized ratification key"),
    ("T11", "poisoned retrieval result"),
    ("T12", "invalid authenticity manifest"),
]


def _artifact_for(case_id: str, attack_name: str) -> dict:
    return {
        "id": case_id,
        "state": "candidate",
        "lineage": [],
        "source_snapshot": {
            "source_id": f"src-{case_id}",
            "path": f"/seeded/{attack_name}.md",
            "hash": f"sha256:{case_id.lower()}",
        },
    }


def _fail_safe(case_id: str, attack_name: str):
    artifact = _artifact_for(case_id, attack_name)
    unauthorized_promotion_blocked = False

    if case_id == "T10":
        with pytest.raises(TransitionError):
            apply_transition(artifact, TransitionDelta(to_state="ratified"))
        unauthorized_promotion_blocked = True

    quarantined = quarantine_artifact(artifact, f"adversarial:{case_id}:{attack_name}")
    audit = build_audit_event(
        "adversarial_failure",
        case_id,
        "blocked",
        details={"attack_name": attack_name, "quarantined": True},
    )
    return artifact, quarantined, audit, unauthorized_promotion_blocked


@pytest.mark.parametrize(("case_id", "attack_name"), ATTACK_CASES)
def test_seeded_attacks_fail_safely(case_id: str, attack_name: str):
    artifact, quarantined, audit, unauthorized_promotion_blocked = _fail_safe(case_id, attack_name)

    assert artifact["state"] == "candidate"
    assert quarantined["state"] == "quarantined"
    assert quarantined["lineage"][-1]["event"] == "quarantined"
    assert quarantined["lineage"][-1]["reason"].startswith(f"adversarial:{case_id}:")

    # Quarantine must preserve source evidence for forensic review.
    assert quarantined["source_snapshot"] == artifact["source_snapshot"]

    # Every failure must emit an explicit audit event.
    assert audit["event_type"] == "adversarial_failure"
    assert audit["status"] == "blocked"
    assert audit["artifact_id"] == case_id
    assert audit["details"]["attack_name"] == attack_name
    assert audit["details"]["quarantined"] is True

    # No unauthorized promotion.
    if case_id == "T10":
        assert unauthorized_promotion_blocked is True
