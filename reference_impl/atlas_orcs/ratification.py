"""
Atlas / ORCS Ratification Engine.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

No artifact can self-ratify.
Ratification requires explicit ratification_event, human permission, and evidence.
"""

from .state import Artifact, TrustState
from .delta import GovernanceDelta, EventType
from .audit import AuditLog
from .transitions import apply_transition, RatificationError


def ratify(
    artifact: Artifact,
    delta: GovernanceDelta,
    audit: AuditLog,
) -> Artifact:
    """
    Attempt to ratify an artifact.

    Raises RatificationError if:
    - event_type is not ratification_event
    - human_permission is False
    - evidence_refs is empty
    - authority_key matches artifact_id (self-ratification)
    - artifact is not in 'reviewed' state
    """
    if artifact.trust_state != TrustState.REVIEWED:
        raise RatificationError(
            f"Artifact must be in 'reviewed' state to ratify. "
            f"Current state: {artifact.trust_state}"
        )

    if delta.authority_key == artifact.artifact_id:
        audit.emit(
            event_type="ratification_attempt",
            artifact_id=artifact.artifact_id,
            actor=delta.authority_key,
            description="Self-ratification attempt blocked",
            outcome="blocked",
        )
        raise RatificationError("An artifact cannot self-ratify.")

    return apply_transition(artifact, delta, audit)


def is_ratified(artifact: Artifact) -> bool:
    """Return True if artifact is in ratified or active state."""
    return artifact.trust_state in (TrustState.RATIFIED, TrustState.ACTIVE)


def has_ratification_event(artifact: Artifact) -> bool:
    """Return True if artifact has a recorded ratification event."""
    return artifact.ratification_event_id is not None
