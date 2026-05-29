import pytest

from reference_impl.atlas_orcs.delta import TransitionDelta
from reference_impl.atlas_orcs.state import Artifact, TrustState
from reference_impl.atlas_orcs.transitions import TransitionError, apply_delta
from reference_impl.atlas_orcs.ratification import enforce_ratification_expiry


def test_ratified_requires_ratification_event():
    artifact = Artifact("a1", trust_state=TrustState.REVIEWED)
    with pytest.raises(TransitionError):
        apply_delta(artifact, TransitionDelta(target_state=TrustState.RATIFIED))


def test_deployment_change_requires_governance_event():
    artifact = Artifact("a1", trust_state=TrustState.CANDIDATE)
    with pytest.raises(TransitionError):
        apply_delta(artifact, TransitionDelta(target_state=TrustState.REVIEWED, new_deployment_status="deployable"))


def test_contradiction_creates_record_not_overwrite():
    artifact = Artifact("a1", trust_state=TrustState.CANDIDATE)
    apply_delta(artifact, TransitionDelta(target_state=TrustState.REVIEWED, contradiction_note="new contradiction"))
    assert len(artifact.contradiction_records) == 1


def test_expired_ratification_moves_under_review():
    artifact = Artifact("a1", trust_state=TrustState.RATIFIED, ratification_expires_at="2026-01-01T00:00:00Z")
    changed = enforce_ratification_expiry(artifact, "2026-05-26T00:00:00Z")
    assert changed is True
    assert artifact.trust_state == TrustState.UNDER_REVIEW
