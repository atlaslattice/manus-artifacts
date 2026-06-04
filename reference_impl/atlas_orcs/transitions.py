"""
Atlas / ORCS State Transition Engine.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

Core rule: Authority is a state transition, not a vibe.
"""

import datetime
from typing import Optional, Tuple
from .state import Artifact, TrustState, CanonStatus, DeploymentStatus
from .delta import GovernanceDelta, EventType
from .audit import AuditLog


# Permitted base transitions: (from, to)
PERMITTED_TRANSITIONS = {
    (TrustState.RAW, TrustState.PARSED),
    (TrustState.PARSED, TrustState.CANDIDATE),
    (TrustState.CANDIDATE, TrustState.REVIEWED),
    (TrustState.REVIEWED, TrustState.RATIFIED),     # requires ratification_event
    (TrustState.RATIFIED, TrustState.ACTIVE),        # requires deployment_event
    (TrustState.ACTIVE, TrustState.UNDER_REVIEW),
    (TrustState.UNDER_REVIEW, TrustState.REVIEWED),
    (TrustState.ACTIVE, TrustState.SUPERSEDED),      # requires supersession_event
    # Any state can move to revoked, quarantined, or rejected
    *{(s, TrustState.REVOKED) for s in TrustState},
    *{(s, TrustState.QUARANTINED) for s in TrustState},
    *{(s, TrustState.REJECTED) for s in TrustState},
}


class TransitionError(Exception):
    """Raised when a state transition is not permitted."""
    pass


class RatificationError(TransitionError):
    """Raised when ratification is attempted without required event."""
    pass


class GovernanceError(TransitionError):
    """Raised when deployment status changes without governance event."""
    pass


def apply_transition(
    artifact: Artifact,
    delta: GovernanceDelta,
    audit: AuditLog,
) -> Artifact:
    """
    Apply a governance delta to an artifact, returning the updated artifact.

    Raises TransitionError if the transition is not permitted.
    All transitions are logged to the audit log.
    """
    from_state = artifact.trust_state
    to_state = delta.new_state

    # Check expiry first
    if artifact.is_ratification_expired():
        if artifact.trust_state in (TrustState.RATIFIED, TrustState.ACTIVE):
            artifact.trust_state = TrustState.UNDER_REVIEW
            audit.emit(
                event_type="expiry_check",
                artifact_id=artifact.artifact_id,
                actor="system",
                description=f"Ratification expired; moved to under_review",
                outcome="transition",
            )
            # Reset and re-check from under_review
            from_state = TrustState.UNDER_REVIEW

    # Check permitted transition
    if (from_state, to_state) not in PERMITTED_TRANSITIONS:
        audit.emit(
            event_type="state_transition",
            artifact_id=artifact.artifact_id,
            actor=delta.authority_key,
            description=f"Blocked transition {from_state} → {to_state}",
            outcome="failed",
        )
        raise TransitionError(
            f"Transition {from_state} → {to_state} is not permitted."
        )

    # Ratification requires explicit ratification_event and human permission
    if to_state == TrustState.RATIFIED:
        if delta.event_type != EventType.RATIFICATION:
            raise RatificationError(
                "Artifact cannot move to ratified without a ratification_event."
            )
        if not delta.human_permission:
            raise RatificationError(
                "Ratification requires human permission."
            )
        if not delta.is_valid():
            raise RatificationError(
                "Ratification delta must have non-empty evidence_refs and authority_key."
            )
        # No self-ratification
        if delta.authority_key == artifact.artifact_id:
            raise RatificationError(
                "An artifact cannot self-ratify."
            )
        artifact.ratification_event_id = delta.delta_id
        if delta.expiry_timestamp:
            artifact.ratification_expiry = delta.expiry_timestamp

    # Active requires prior ratification
    if to_state == TrustState.ACTIVE:
        if artifact.trust_state != TrustState.RATIFIED:
            raise TransitionError("Artifact must be ratified before becoming active.")

    # Quarantine preserves lineage
    if to_state == TrustState.QUARANTINED:
        # lineage is preserved; no modification needed
        pass

    # Apply transition
    artifact.trust_state = to_state
    artifact.receipts.append(delta.delta_id or "delta-no-id")

    audit.emit(
        event_type="state_transition",
        artifact_id=artifact.artifact_id,
        actor=delta.authority_key,
        description=f"Transition {from_state} → {to_state}",
        outcome="passed",
    )

    return artifact


def apply_deployment_change(
    artifact: Artifact,
    new_deployment_status: DeploymentStatus,
    governance_delta: GovernanceDelta,
    audit: AuditLog,
) -> Artifact:
    """
    Change deployment status. Requires explicit governance event.
    """
    if artifact.deployment_status == new_deployment_status:
        return artifact

    if governance_delta.event_type not in (
        EventType.GOVERNANCE, EventType.DEPLOYMENT
    ):
        raise GovernanceError(
            "Deployment status cannot change without a governance_event."
        )
    if not governance_delta.is_valid():
        raise GovernanceError("Governance delta must be valid.")

    old_status = artifact.deployment_status
    artifact.deployment_status = new_deployment_status

    audit.emit(
        event_type="state_transition",
        artifact_id=artifact.artifact_id,
        actor=governance_delta.authority_key,
        description=f"Deployment status {old_status} → {new_deployment_status}",
        outcome="passed",
    )

    return artifact


def check_and_expire_ratification(
    artifact: Artifact,
    audit: AuditLog,
    at_time: Optional[datetime.datetime] = None,
) -> Artifact:
    """
    Check if ratification has expired and move artifact to under_review if so.
    """
    if artifact.is_ratification_expired(at_time) and artifact.trust_state in (
        TrustState.RATIFIED, TrustState.ACTIVE
    ):
        artifact.trust_state = TrustState.UNDER_REVIEW
        audit.emit(
            event_type="expiry_check",
            artifact_id=artifact.artifact_id,
            actor="system",
            description="Expired ratification; artifact moved to under_review",
            outcome="transition",
        )
    return artifact
