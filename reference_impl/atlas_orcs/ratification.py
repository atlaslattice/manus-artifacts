"""
Atlas/ORCS Ratification Module
NOT CANON — NOT DEPLOYABLE — reference implementation only

Handles the ratification lifecycle. Ratification is the ONLY path to canon status.
No self-ratification. No implicit ratification. Always explicit.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import List, Optional, TYPE_CHECKING
from state import TrustState, CanonStatus
from delta import RatificationEvent, AuditEvent
from audit import AuditLog, create_audit_event

if TYPE_CHECKING:
    from transitions import Artifact


class SelfRatificationError(ValueError):
    """Raised when an artifact attempts to self-ratify."""
    pass


class InvalidRatificationStateError(ValueError):
    """Raised when ratification is attempted from invalid state."""
    pass


def ratify_artifact(
    artifact: "Artifact",
    ratifier_id: str,
    ratification_scope: List[str],
    council_members: List[str],
    expiry_days: int,
    adjudicated_by: Optional[str],
    actor_id: str,
    audit_log: AuditLog,
) -> tuple["Artifact", RatificationEvent]:
    """
    Ratify an artifact.

    CRITICAL RULES:
    1. Artifact must be in REVIEWED state
    2. ratifier_id MUST differ from artifact.author_id (no self-ratification)
    3. Ratification creates an explicit event record
    4. For full canon, adjudicated_by must be @atlaslattice

    Returns (updated_artifact, ratification_event)
    """
    now = datetime.now(timezone.utc)

    # Rule 1: Must be reviewed
    if artifact.trust_state != TrustState.REVIEWED:
        raise InvalidRatificationStateError(
            f"Artifact must be in REVIEWED state for ratification. "
            f"Current state: {artifact.trust_state}"
        )

    # Rule 2: No self-ratification
    if ratifier_id == artifact.author_id:
        raise SelfRatificationError(
            f"Self-ratification prohibited: ratifier_id '{ratifier_id}' "
            f"equals artifact author_id '{artifact.author_id}'"
        )

    # Create ratification event
    expiry = (now + timedelta(days=expiry_days)).isoformat()
    event_id = f"ratify-{artifact.artifact_id}-{now.isoformat()}"

    event = RatificationEvent(
        event_id=event_id,
        artifact_id=artifact.artifact_id,
        actor_id=actor_id,
        occurred_at=now.isoformat(),
        ratifier_id=ratifier_id,
        ratification_scope=ratification_scope,
        council_quorum=len(council_members) or 1,
        council_members=council_members,
        adjudicated_by=adjudicated_by,
        expiry=expiry,
    )

    # Validate
    event.validate(artifact.author_id)

    # Apply state change
    artifact.trust_state = TrustState.RATIFIED
    artifact.ratification_event_id = event_id
    artifact.ratification_expiry = expiry
    artifact.governance_events.append(event_id)

    # Set canon status — candidate until website publication
    # Full canon requires adjudication + website publication
    if adjudicated_by:
        artifact.canon_status = CanonStatus.CANDIDATE  # Still candidate until website
    else:
        artifact.canon_status = CanonStatus.CANDIDATE

    # Audit
    audit_event = create_audit_event(
        event_subtype="ratification",
        artifact_id=artifact.artifact_id,
        actor_id=actor_id,
        details=(
            f"Artifact ratified by {ratifier_id}. "
            f"Council quorum: {len(council_members)}. "
            f"Expiry: {expiry}. "
            f"Adjudicated: {adjudicated_by or 'no'}. "
            f"Scope: {ratification_scope}"
        ),
    )
    audit_log.append(audit_event)

    return artifact, event


def check_and_expire_ratifications(
    artifacts: List["Artifact"],
    audit_log: AuditLog,
    current_time: Optional[str] = None,
) -> List["Artifact"]:
    """
    Batch check all artifacts for expired ratifications.
    Expired ratifications move artifacts to UNDER_REVIEW.
    """
    from transitions import check_ratification_expiry

    now = current_time or datetime.now(timezone.utc).isoformat()
    updated = []

    for artifact in artifacts:
        artifact = check_ratification_expiry(artifact, now, audit_log)
        updated.append(artifact)

    return updated


def is_canon(artifact: "Artifact") -> bool:
    """
    Check if an artifact is fully canon.
    Requires ALL of:
    - ratified_canon status (set only after website publication + adjudication)
    - ratification_event_id present (cannot be self-assigned)
    - trust_state == active or ratified
    GitHub presence alone is NEVER sufficient.
    Direct assignment of canon_status without ratification_event_id is NOT canon.
    """
    if artifact.canon_status != CanonStatus.RATIFIED_CANON:
        return False
    if not artifact.ratification_event_id:
        return False
    if artifact.trust_state not in (TrustState.RATIFIED, TrustState.ACTIVE):
        return False
    return True
