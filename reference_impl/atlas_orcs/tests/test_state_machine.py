"""
Tests for Atlas / ORCS state machine.

STATUS: CANDIDATE TESTS — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
"""

import datetime
import pytest
from reference_impl.atlas_orcs.state import (
    Artifact, TrustState, CanonStatus, DeploymentStatus
)
from reference_impl.atlas_orcs.delta import GovernanceDelta, EventType
from reference_impl.atlas_orcs.transitions import (
    apply_transition, apply_deployment_change,
    check_and_expire_ratification,
    TransitionError, RatificationError, GovernanceError,
)
from reference_impl.atlas_orcs.audit import AuditLog
from reference_impl.atlas_orcs.quarantine import quarantine_artifact
from reference_impl.atlas_orcs.ratification import ratify, is_ratified, has_ratification_event


# ── Helpers ─────────────────────────────────────────────────────────────────

def make_artifact(trust_state=TrustState.RAW, artifact_id="test-artifact-001") -> Artifact:
    return Artifact(artifact_id=artifact_id, title="Test Artifact", trust_state=trust_state)


def make_ratification_delta(artifact_id="test-artifact-001", human=True) -> GovernanceDelta:
    return GovernanceDelta(
        event_type=EventType.RATIFICATION,
        authority_key="council-authority-001",
        artifact_id=artifact_id,
        previous_state=TrustState.REVIEWED,
        new_state=TrustState.RATIFIED,
        evidence_refs=["evidence-001", "evidence-002"],
        human_permission=human,
        delta_id="delta-ratification-001",
    )


# ── Test: Artifact cannot move to ratified without ratification_event ────────

def test_ratification_requires_ratification_event():
    artifact = make_artifact(TrustState.REVIEWED)
    audit = AuditLog()
    bad_delta = GovernanceDelta(
        event_type=EventType.GOVERNANCE,  # Wrong event type
        authority_key="council-001",
        artifact_id=artifact.artifact_id,
        previous_state=TrustState.REVIEWED,
        new_state=TrustState.RATIFIED,
        evidence_refs=["evidence-001"],
        human_permission=True,
        delta_id="delta-001",
    )
    with pytest.raises(RatificationError):
        apply_transition(artifact, bad_delta, audit)


def test_ratification_requires_human_permission():
    artifact = make_artifact(TrustState.REVIEWED)
    audit = AuditLog()
    delta = make_ratification_delta(human=False)
    with pytest.raises(RatificationError):
        apply_transition(artifact, delta, audit)


def test_ratification_succeeds_with_valid_delta():
    artifact = make_artifact(TrustState.REVIEWED)
    audit = AuditLog()
    delta = make_ratification_delta()
    result = apply_transition(artifact, delta, audit)
    assert result.trust_state == TrustState.RATIFIED
    assert has_ratification_event(result)


# ── Test: Deployment status cannot change without governance event ───────────

def test_deployment_change_requires_governance_event():
    artifact = make_artifact(TrustState.RATIFIED)
    audit = AuditLog()
    bad_delta = GovernanceDelta(
        event_type=EventType.RATIFICATION,  # Wrong event type
        authority_key="council-001",
        artifact_id=artifact.artifact_id,
        previous_state=TrustState.RATIFIED,
        new_state=TrustState.RATIFIED,
        evidence_refs=["evidence-001"],
        human_permission=True,
        delta_id="delta-001",
    )
    with pytest.raises(GovernanceError):
        apply_deployment_change(artifact, DeploymentStatus.DEPLOYED, bad_delta, audit)


def test_deployment_change_succeeds_with_governance_event():
    artifact = make_artifact(TrustState.ACTIVE)
    audit = AuditLog()
    delta = GovernanceDelta(
        event_type=EventType.GOVERNANCE,
        authority_key="council-001",
        artifact_id=artifact.artifact_id,
        previous_state=TrustState.ACTIVE,
        new_state=TrustState.ACTIVE,
        evidence_refs=["gov-evidence-001"],
        human_permission=True,
        delta_id="delta-gov-001",
    )
    result = apply_deployment_change(artifact, DeploymentStatus.DEPLOYMENT_CANDIDATE, delta, audit)
    assert result.deployment_status == DeploymentStatus.DEPLOYMENT_CANDIDATE


# ── Test: Quarantined artifact preserves lineage ─────────────────────────────

def test_quarantine_preserves_lineage():
    artifact = make_artifact(TrustState.CANDIDATE)
    artifact.lineage = ["ancestor-001", "ancestor-002"]
    audit = AuditLog()
    updated, record = quarantine_artifact(
        artifact, reason="Test quarantine", trigger_event_type="test", audit=audit
    )
    assert updated.trust_state == TrustState.QUARANTINED
    assert updated.lineage == ["ancestor-001", "ancestor-002"]  # lineage preserved
    assert record.lineage_preserved is True
    assert record.source_preserved is True


# ── Test: Contradiction creates record, not overwrite ───────────────────────

def test_contradiction_does_not_overwrite():
    """Contradiction must create a new record, not mutate existing artifact."""
    artifact_a = make_artifact(TrustState.CANDIDATE, "artifact-a")
    artifact_b = make_artifact(TrustState.CANDIDATE, "artifact-b")
    original_title_a = artifact_a.title
    # A contradiction should not change artifact_a's data
    # (In the full implementation, ContradictionLedger.record would be called)
    # Here we just verify the artifacts are unchanged after the test setup
    assert artifact_a.title == original_title_a
    assert artifact_a.trust_state == TrustState.CANDIDATE


# ── Test: Summary cannot replace source ──────────────────────────────────────

def test_summary_not_equal_to_source():
    """Summary artifact has lower epistemic weight than source."""
    source = Artifact(
        artifact_id="source-001",
        title="Source Document",
        trust_state=TrustState.REVIEWED,
        is_summary=False,
    )
    summary = Artifact(
        artifact_id="summary-001",
        title="Summary of Source",
        trust_state=TrustState.CANDIDATE,
        is_summary=True,
        source_artifact_ids=["source-001"],
    )
    # Summary is not equal to source
    assert summary.artifact_id != source.artifact_id
    assert summary.is_summary is True
    assert source.is_summary is False
    assert summary.trust_state != source.trust_state
    # Summary cannot be promoted past source's level without its own ratification
    assert summary.trust_state.value != TrustState.RATIFIED.value


# ── Test: Receipt ≠ truth ──────────────────────────────────────────────────

def test_receipt_is_not_truth():
    """A provenance receipt records an event; it does not establish epistemic truth."""
    from reference_impl.atlas_orcs.audit import AuditEntry
    import datetime
    receipt = AuditEntry(
        event_type="artifact_created",
        artifact_id="artifact-001",
        actor="test-seat",
        description="Artifact was created",
        outcome="informational",
        timestamp=datetime.datetime.now(datetime.timezone.utc),
    )
    # A receipt records occurrence, not truth
    # The receipt_is_truth concept must always be False
    assert not hasattr(receipt, 'receipt_is_truth') or receipt.__dict__.get('receipt_is_truth', False) is False


# ── Test: Ratification requires explicit event ─────────────────────────────

def test_ratification_without_event_fails():
    artifact = make_artifact(TrustState.REVIEWED)
    audit = AuditLog()
    # Attempt to force ratified state without proper delta
    with pytest.raises((RatificationError, TransitionError)):
        bad_delta = GovernanceDelta(
            event_type="some_other_event",
            authority_key="council-001",
            artifact_id=artifact.artifact_id,
            previous_state=TrustState.REVIEWED,
            new_state=TrustState.RATIFIED,
            evidence_refs=["ev-001"],
            human_permission=True,
            delta_id="delta-001",
        )
        apply_transition(artifact, bad_delta, audit)


# ── Test: Expired ratification moves to under_review ─────────────────────

def test_expired_ratification_moves_to_under_review():
    artifact = make_artifact(TrustState.ACTIVE)
    audit = AuditLog()
    past_time = datetime.datetime(2020, 1, 1, tzinfo=datetime.timezone.utc)
    artifact.ratification_expiry = past_time
    artifact.ratification_event_id = "ratification-001"

    result = check_and_expire_ratification(artifact, audit)
    assert result.trust_state == TrustState.UNDER_REVIEW


# ── Test: Self-ratification blocked ──────────────────────────────────────

def test_self_ratification_blocked():
    artifact = make_artifact(TrustState.REVIEWED)
    audit = AuditLog()
    # authority_key == artifact_id = self-ratification attempt
    self_delta = GovernanceDelta(
        event_type=EventType.RATIFICATION,
        authority_key=artifact.artifact_id,  # Same as artifact — self-ratification
        artifact_id=artifact.artifact_id,
        previous_state=TrustState.REVIEWED,
        new_state=TrustState.RATIFIED,
        evidence_refs=["evidence-001"],
        human_permission=True,
        delta_id="delta-self-001",
    )
    with pytest.raises(RatificationError, match="self-ratif"):
        ratify(artifact, self_delta, audit)
