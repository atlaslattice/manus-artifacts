"""
Tests for Atlas/ORCS State Machine
NOT CANON — NOT DEPLOYABLE — reference implementation only
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from datetime import datetime, timezone, timedelta

from state import TrustState, CanonStatus, DeploymentStatus, CompatibleResult
from delta import (
    RatificationEvent, PromoteEvent, QuarantineEvent,
    ContradictEvent, AuditEvent, ExpireEvent,
)
from transitions import Artifact, apply_transition, apply_contradiction, check_ratification_expiry, TransitionForbidden, TransitionHeld
from audit import AuditLog, create_audit_event
from quarantine import quarantine_artifact, QuarantineStore
from ratification import ratify_artifact, SelfRatificationError, InvalidRatificationStateError, is_canon


def make_artifact(
    artifact_id="art-001",
    author_id="LucernaBrain",
    trust_state=TrustState.RAW,
    canon_status=CanonStatus.NOT_CANON,
) -> Artifact:
    return Artifact(
        artifact_id=artifact_id,
        author_id=author_id,
        trust_state=trust_state,
        canon_status=canon_status,
    )


def make_audit_log() -> AuditLog:
    return AuditLog()


# ── State Transition Tests ─────────────────────────────────────────────────────

class TestPermittedTransitions:
    def test_raw_to_parsed(self):
        artifact = make_artifact(trust_state=TrustState.RAW)
        log = make_audit_log()
        event = AuditEvent(
            event_id="e1", event_type="ORCS-PARSE",
            artifact_id="art-001", actor_id="system",
            occurred_at="2026-05-26T18:00:00Z",
        )
        result = apply_transition(artifact, TrustState.PARSED, event, log)
        assert result.trust_state == TrustState.PARSED

    def test_parsed_to_candidate(self):
        artifact = make_artifact(trust_state=TrustState.PARSED)
        log = make_audit_log()
        event = AuditEvent(
            event_id="e2", event_type="ORCS-REVIEW",
            artifact_id="art-001", actor_id="system",
            occurred_at="2026-05-26T18:00:00Z",
        )
        result = apply_transition(artifact, TrustState.CANDIDATE, event, log)
        assert result.trust_state == TrustState.CANDIDATE

    def test_cannot_skip_to_ratified(self):
        """Artifact cannot jump from raw to ratified."""
        artifact = make_artifact(trust_state=TrustState.RAW)
        log = make_audit_log()
        event = RatificationEvent(
            event_id="e3", artifact_id="art-001",
            actor_id="ratifier", occurred_at="2026-05-26T18:00:00Z",
            ratifier_id="ratifier", expiry="2027-01-01T00:00:00Z",
        )
        with pytest.raises(TransitionForbidden):
            apply_transition(artifact, TrustState.RATIFIED, event, log)


class TestRatification:
    def test_ratification_requires_reviewed_state(self):
        """Artifact must be REVIEWED before ratification."""
        artifact = make_artifact(trust_state=TrustState.CANDIDATE)
        log = make_audit_log()
        with pytest.raises(InvalidRatificationStateError):
            ratify_artifact(
                artifact=artifact,
                ratifier_id="AtlasBrain",
                ratification_scope=["content"],
                council_members=["AtlasBrain"],
                expiry_days=365,
                adjudicated_by=None,
                actor_id="AtlasBrain",
                audit_log=log,
            )

    def test_no_self_ratification(self):
        """An artifact cannot self-ratify."""
        artifact = make_artifact(
            author_id="LucernaBrain",
            trust_state=TrustState.REVIEWED,
        )
        log = make_audit_log()
        with pytest.raises(SelfRatificationError):
            ratify_artifact(
                artifact=artifact,
                ratifier_id="LucernaBrain",  # Same as author!
                ratification_scope=["content"],
                council_members=["LucernaBrain"],
                expiry_days=365,
                adjudicated_by=None,
                actor_id="LucernaBrain",
                audit_log=log,
            )

    def test_valid_ratification(self):
        """Valid ratification from a different ratifier."""
        artifact = make_artifact(
            author_id="LucernaBrain",
            trust_state=TrustState.REVIEWED,
        )
        log = make_audit_log()
        updated, event = ratify_artifact(
            artifact=artifact,
            ratifier_id="AtlasBrain",  # Different from author
            ratification_scope=["content"],
            council_members=["AtlasBrain", "HashlightBrain"],
            expiry_days=365,
            adjudicated_by=None,
            actor_id="AtlasBrain",
            audit_log=log,
        )
        assert updated.trust_state == TrustState.RATIFIED
        assert updated.ratification_event_id == event.event_id

    def test_ratified_artifact_is_not_canon_without_website(self):
        """Ratified != canon. Canon requires website publication."""
        artifact = make_artifact(
            author_id="LucernaBrain",
            trust_state=TrustState.REVIEWED,
        )
        log = make_audit_log()
        updated, _ = ratify_artifact(
            artifact=artifact,
            ratifier_id="AtlasBrain",
            ratification_scope=["content"],
            council_members=["AtlasBrain"],
            expiry_days=365,
            adjudicated_by="atlaslattice",
            actor_id="AtlasBrain",
            audit_log=log,
        )
        # Even with adjudication, not canon until website publication
        assert not is_canon(updated)
        assert updated.canon_status != CanonStatus.RATIFIED_CANON


class TestExpiredRatification:
    def test_expired_ratification_moves_to_under_review(self):
        """When ratification expires, artifact moves to under_review."""
        artifact = make_artifact(trust_state=TrustState.ACTIVE)
        past = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        artifact.ratification_expiry = past
        artifact.ratification_event_id = "ratify-001"

        log = make_audit_log()
        now = datetime.now(timezone.utc).isoformat()
        updated = check_ratification_expiry(artifact, now, log)

        assert updated.trust_state == TrustState.UNDER_REVIEW
        assert updated.ratification_event_id is None


class TestContradiction:
    def test_contradiction_preserves_both_artifacts(self):
        """Contradiction creates a record; neither artifact is overwritten."""
        art_a = make_artifact(artifact_id="art-a", trust_state=TrustState.ACTIVE)
        art_b = make_artifact(artifact_id="art-b", trust_state=TrustState.ACTIVE)
        log = make_audit_log()

        event = ContradictEvent(
            event_id="contra-001",
            artifact_id="art-a",
            actor_id="AtlasBrain",
            occurred_at="2026-05-26T18:00:00Z",
            artifact_id_b="art-b",
            contradiction_type="factual",
            contradiction_record_id="contra-record-001",
        )

        record = apply_contradiction(art_a, art_b, event, log)

        # Both artifacts preserved
        assert art_a.artifact_id == "art-a"
        assert art_b.artifact_id == "art-b"
        # Contradiction record created
        assert record.record_id == "contra-record-001"
        assert record.artifact_id_a == "art-a"
        assert record.artifact_id_b == "art-b"
        assert record.status == "open"


class TestQuarantine:
    def test_quarantine_preserves_lineage(self):
        """Quarantine preserves lineage — it is not deletion."""
        artifact = make_artifact(trust_state=TrustState.CANDIDATE)
        artifact.lineage = {"parent": "art-parent"}
        log = make_audit_log()
        store = QuarantineStore()

        updated, record = quarantine_artifact(
            artifact=artifact,
            reason="adversarial pattern detected",
            trigger_rule_id="QR-001",
            actor_id="AtlasBrain",
            audit_log=log,
            quarantine_store=store,
        )

        assert updated.trust_state == TrustState.QUARANTINED
        assert record.lineage_preserved is True
        assert record.original_state_snapshot is not None
        assert "parent" in record.original_state_snapshot.get("lineage", {})

    def test_quarantine_creates_audit_event(self):
        artifact = make_artifact(trust_state=TrustState.CANDIDATE)
        log = make_audit_log()
        store = QuarantineStore()

        quarantine_artifact(
            artifact=artifact,
            reason="test quarantine",
            trigger_rule_id="QR-TEST",
            actor_id="AtlasBrain",
            audit_log=log,
            quarantine_store=store,
        )

        events = log.get_events()
        assert any(e.event_subtype == "quarantine_applied" for e in events)


class TestSummaryVsSource:
    def test_summary_does_not_equal_source(self):
        """Summary artifact cannot inherit source's canon status."""
        source = make_artifact(artifact_id="source-001")
        source.canon_status = CanonStatus.CANDIDATE
        source.trust_state = TrustState.RATIFIED

        # Summary artifact
        summary = make_artifact(artifact_id="summary-001")
        summary.lineage = {"summary_of": "source-001"}

        # Summary is NOT canon just because source is ratified
        assert not is_canon(summary)
        assert summary.canon_status == CanonStatus.NOT_CANON


class TestAuditLog:
    def test_audit_events_immutable(self):
        """Audit log returns copies; modifications don't affect original."""
        log = make_audit_log()
        event = create_audit_event(
            event_subtype="test",
            artifact_id="art-001",
            actor_id="system",
            details="test event",
        )
        log.append(event)

        events_copy = log.get_events()
        events_copy.clear()  # Try to clear the copy

        # Original should still have the event
        assert len(log) == 1
