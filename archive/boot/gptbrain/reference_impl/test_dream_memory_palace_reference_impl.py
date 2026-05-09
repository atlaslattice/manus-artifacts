"""
Tests for dream_memory_palace_reference_impl.py

Status: TEST SCAFFOLD — NOT CANON
Purpose: protect the first GPTBrain / S1 reference implementation invariants.

Run from this directory:
    python -m pytest test_dream_memory_palace_reference_impl.py
"""

from __future__ import annotations

import json
import pytest

from dream_memory_palace_reference_impl import (
    AccessClass,
    ClaimConfidence,
    ConsentLevel,
    DreamMemoryPalace,
    MemoryObject,
    MemoryType,
    PermissionPolicy,
    Provenance,
    EpistemicCategory,
    EpistemicStatus,
    RecallMode,
    RecallQuery,
    make_claim,
)


def test_remember_and_recall_project_claim() -> None:
    palace = DreamMemoryPalace()
    claim = palace.remember(
        make_claim(
            "Memory is not truth",
            "Stored memory must track epistemic status and provenance.",
            "GPTBrain",
            ClaimConfidence.C3_MULTIPLE_ARTIFACTS_CONVERGE,
        )
    )

    results = palace.recall(
        RecallQuery(
            text="GPTBrain provenance",
            mode=RecallMode.PROJECT_CONTEXT,
            projects=["GPTBrain"],
            max_results=5,
        )
    )

    assert results
    assert any(result.memory.memory_id == claim.memory_id for result in results)
    assert palace.audit_log[-1].event_type.value == "memory_read"


def test_contradiction_links_both_claims_and_creates_unresolved_object() -> None:
    palace = DreamMemoryPalace()
    claim_a = palace.remember(make_claim("Claim A", "Raw provenance matters.", "GPTBrain"))
    claim_b = palace.remember(make_claim("Claim B", "Summaries alone are enough.", "GPTBrain"))

    contradiction = palace.create_contradiction(
        claim_a.memory_id,
        claim_b.memory_id,
        "Raw provenance requirement conflicts with summary-only memory.",
        severity="high",
    )

    assert contradiction.type == MemoryType.CONTRADICTION
    assert contradiction.payload["status"] == "unresolved"
    assert contradiction.payload["human_review_required"] is True
    assert contradiction.memory_id in claim_a.links.contradicted_by
    assert contradiction.memory_id in claim_b.links.contradicted_by
    assert claim_a.epistemic_status.contested is True
    assert claim_b.epistemic_status.contested is True


def test_challenge_flags_c0_unsourced_unratified_claim() -> None:
    palace = DreamMemoryPalace()
    claim = palace.remember(
        make_claim(
            "Unsupported claim",
            "This should not be claimed externally.",
            "GPTBrain",
            ClaimConfidence.C0_UNSUPPORTED,
        )
    )

    report = palace.challenge(claim.memory_id)
    findings = "\n".join(report["red_team_findings"])

    assert "C0" in findings
    assert "No user-visible citation" in findings
    assert "do not treat as ratified canon" in findings
    assert report["recommended_next_step"] == "Keep as variant/candidate until human-root review."


def test_canon_promotion_requires_human_root_approval() -> None:
    palace = DreamMemoryPalace()
    claim = palace.remember(make_claim("Candidate", "Candidate canon text.", "GPTBrain"))

    with pytest.raises(PermissionError):
        palace.promote_to_ratified_canon(claim.memory_id)

    assert palace.audit_log[-1].event_type.value == "canon_promotion_blocked"

    promoted = palace.promote_to_ratified_canon(claim.memory_id, human_root_approved=True)
    assert promoted.canon_status.value == "ratified_canon"


def test_sealed_sensitive_memory_is_not_readable() -> None:
    palace = DreamMemoryPalace()
    sealed = MemoryObject(
        title="Sealed note",
        type=MemoryType.NOTE,
        summary="This should not be returned by recall.",
        epistemic_status=EpistemicStatus(category=EpistemicCategory.USER_CLAIM),
        provenance=Provenance(source_type="test", actor="tester"),
        permissions=PermissionPolicy(
            access_class=AccessClass.SEALED_SENSITIVE,
            consent_levels=[ConsentLevel.DURABLE_MEMORY, ConsentLevel.SENSITIVE_MEMORY],
        ),
        payload={"project": "GPTBrain"},
    )
    palace.remember(sealed)

    results = palace.recall(RecallQuery(text="sealed", projects=["GPTBrain"]))

    assert all(result.memory.memory_id != sealed.memory_id for result in results)
    assert any(event.event_type.value == "consent_denied" for event in palace.audit_log)


def test_save_json_writes_memories_and_audit_log(tmp_path) -> None:
    palace = DreamMemoryPalace()
    palace.remember(make_claim("Serializable", "This should serialize.", "GPTBrain"))
    out = tmp_path / "palace.json"

    palace.save_json(out)
    data = json.loads(out.read_text(encoding="utf-8"))

    assert "memories" in data
    assert "audit_log" in data
    assert data["memories"][0]["title"] == "Serializable"
