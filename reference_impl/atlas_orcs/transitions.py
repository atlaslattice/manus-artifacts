"""
Atlas/ORCS Transitions Engine
NOT CANON — NOT DEPLOYABLE — reference implementation only

Implements the delta function Δ(a, σ, e) = (a', σ') for Atlas/ORCS state transitions.
All transitions are checked against compatible_Γ before application.
See: archive/spec/gptdream/appendices/APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, List
from state import (
    TrustState, CanonStatus, DeploymentStatus,
    PERMITTED_TRANSITIONS, GOVERNANCE_REQUIRED_TRANSITIONS,
    CompatibleResult,
)
from delta import (
    GovernanceEvent, RatificationEvent, PromoteEvent,
    SupersedeEvent, RevokeEvent, QuarantineEvent,
    ContradictEvent, ExpireEvent, AuditEvent,
)
from compatible import compatible


class TransitionForbidden(Exception):
    """Raised when a transition is prohibited by compatible_Γ."""
    pass


class TransitionHeld(Exception):
    """Raised when a transition is HELD pending a governance event."""
    pass


@dataclass
class Artifact:
    """
    In-memory representation of an Atlas/ORCS artifact.
    Tracks state, lineage, and governance events.
    """

    artifact_id: str
    author_id: str
    trust_state: TrustState = TrustState.RAW
    canon_status: CanonStatus = CanonStatus.NOT_CANON
    deployment_status: DeploymentStatus = DeploymentStatus.NOT_DEPLOYABLE
    ratification_event_id: Optional[str] = None
    ratification_expiry: Optional[str] = None  # ISO 8601
    governance_events: List[str] = field(default_factory=list)
    lineage: dict = field(default_factory=dict)
    contradiction_records: List[str] = field(default_factory=list)


@dataclass
class ContradictionRecord:
    """
    Created when ORCS-CONTRADICT fires. Never overwrites artifacts.
    """
    record_id: str
    artifact_id_a: str
    artifact_id_b: str
    contradiction_type: str
    detected_by: str
    detected_at: str
    status: str = "open"


def apply_transition(
    artifact: Artifact,
    target_state: TrustState,
    event: GovernanceEvent,
    audit_log: List[AuditEvent],
) -> Artifact:
    """
    Apply a state transition to an artifact after checking compatible_Γ.

    Returns the updated artifact.
    Raises TransitionForbidden if FALSE.
    Raises TransitionHeld if HOLD.
    """
    edge = (artifact.trust_state, target_state)

    # Check compatible_Γ
    result = compatible(
        from_state=artifact.trust_state,
        to_state=target_state,
        event=event,
        artifact=artifact,
    )

    audit_log.append(AuditEvent(
        event_id=f"audit-{event.event_id}",
        event_type="ORCS-AUDIT",
        artifact_id=artifact.artifact_id,
        actor_id=event.actor_id,
        occurred_at=event.occurred_at,
        event_subtype="compatible_check",
        compatible_result=result.value,
        details=f"compatible_Γ({artifact.trust_state} → {target_state}) = {result}",
    ))

    if result == CompatibleResult.FALSE:
        raise TransitionForbidden(
            f"Transition {artifact.trust_state} → {target_state} is FORBIDDEN. "
            f"compatible_Γ returned FALSE. Event: {event.event_type}"
        )
    elif result == CompatibleResult.HOLD:
        raise TransitionHeld(
            f"Transition {artifact.trust_state} → {target_state} is HELD. "
            f"A required governance event is missing. Event: {event.event_type}"
        )

    # Apply specific event logic
    from_state = artifact.trust_state

    if isinstance(event, RatificationEvent):
        event.validate(artifact.author_id)
        artifact.ratification_event_id = event.event_id
        artifact.ratification_expiry = event.expiry
        artifact.canon_status = CanonStatus.CANDIDATE  # candidate until website publication

    elif isinstance(event, PromoteEvent):
        if artifact.trust_state != TrustState.RATIFIED:
            raise TransitionForbidden("Can only promote from ratified state")

    elif isinstance(event, QuarantineEvent):
        # Quarantine preserves lineage
        event.lineage_preserved = True  # Always enforce

    elif isinstance(event, SupersedeEvent):
        artifact.lineage["superseded_by"] = event.superseded_by

    elif isinstance(event, ExpireEvent):
        # Expired ratification → under_review
        artifact.ratification_event_id = None
        artifact.ratification_expiry = None

    # Apply the transition
    artifact.trust_state = target_state
    artifact.governance_events.append(event.event_id)

    # Log the state transition
    audit_log.append(AuditEvent(
        event_id=f"transition-{event.event_id}",
        event_type="ORCS-AUDIT",
        artifact_id=artifact.artifact_id,
        actor_id=event.actor_id,
        occurred_at=event.occurred_at,
        event_subtype="state_transition",
        details=f"State: {from_state} → {target_state} via {event.event_type}",
    ))

    return artifact


def apply_contradiction(
    artifact_a: Artifact,
    artifact_b: Artifact,
    event: ContradictEvent,
    audit_log: List[AuditEvent],
) -> ContradictionRecord:
    """
    Create a contradiction record. NEVER overwrites artifacts.
    Both artifacts are preserved; contradiction is logged.
    """
    record = ContradictionRecord(
        record_id=event.contradiction_record_id or f"contra-{event.event_id}",
        artifact_id_a=artifact_a.artifact_id,
        artifact_id_b=artifact_b.artifact_id,
        contradiction_type=event.contradiction_type,
        detected_by=event.actor_id,
        detected_at=event.occurred_at,
        status="open",
    )

    artifact_a.contradiction_records.append(record.record_id)
    artifact_b.contradiction_records.append(record.record_id)

    audit_log.append(AuditEvent(
        event_id=f"contra-audit-{event.event_id}",
        event_type="ORCS-AUDIT",
        artifact_id=artifact_a.artifact_id,
        actor_id=event.actor_id,
        occurred_at=event.occurred_at,
        event_subtype="contradiction_detected",
        details=f"Contradiction between {artifact_a.artifact_id} and {artifact_b.artifact_id}: {event.contradiction_type}",
    ))

    return record


def check_ratification_expiry(
    artifact: Artifact,
    current_time: str,
    audit_log: List[AuditEvent],
) -> Artifact:
    """
    Check if an artifact's ratification has expired.
    If expired, move to under_review and log an expiry event.
    """
    if artifact.trust_state not in (TrustState.RATIFIED, TrustState.ACTIVE):
        return artifact

    if not artifact.ratification_expiry:
        return artifact

    expiry = datetime.fromisoformat(artifact.ratification_expiry.replace("Z", "+00:00"))
    now = datetime.fromisoformat(current_time.replace("Z", "+00:00"))

    if now > expiry:
        expire_event = ExpireEvent(
            event_id=f"expire-{artifact.artifact_id}-{current_time}",
            artifact_id=artifact.artifact_id,
            actor_id="system",
            occurred_at=current_time,
            expired_ratification_id=artifact.ratification_event_id or "",
        )
        artifact = apply_transition(
            artifact=artifact,
            target_state=TrustState.UNDER_REVIEW,
            event=expire_event,
            audit_log=audit_log,
        )

    return artifact
