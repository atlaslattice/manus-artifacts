"""
Atlas/ORCS Audit Module
NOT CANON — NOT DEPLOYABLE — reference implementation only

Provides audit event creation and logging for the Atlas/ORCS system.
Every significant action MUST generate an audit event.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional
from delta import AuditEvent, GovernanceEvent


class AuditLog:
    """
    In-memory audit log for Atlas/ORCS events.
    Audit events are IMMUTABLE once created — no edits, no deletes.
    """

    def __init__(self):
        self._events: List[AuditEvent] = []

    def append(self, event: AuditEvent) -> None:
        """Append an audit event. Events are immutable once logged."""
        self._events.append(event)

    def get_events(self) -> List[AuditEvent]:
        """Return a copy of all events (cannot modify original)."""
        return list(self._events)

    def get_events_for_artifact(self, artifact_id: str) -> List[AuditEvent]:
        """Return all events for a specific artifact."""
        return [e for e in self._events if e.artifact_id == artifact_id]

    def __len__(self):
        return len(self._events)


def create_audit_event(
    event_subtype: str,
    artifact_id: str,
    actor_id: str,
    details: str,
    event_id: Optional[str] = None,
    compatible_result: Optional[str] = None,
    gate_states: Optional[dict] = None,
    from_state: Optional[str] = None,
    to_state: Optional[str] = None,
) -> AuditEvent:
    """Create a new audit event with current timestamp."""
    now = datetime.now(timezone.utc).isoformat()
    eid = event_id or f"audit-{artifact_id}-{now}"

    return AuditEvent(
        event_id=eid,
        event_type="ORCS-AUDIT",
        artifact_id=artifact_id,
        actor_id=actor_id,
        occurred_at=now,
        event_subtype=event_subtype,
        details=details,
        compatible_result=compatible_result,
        gate_states=gate_states,
        notes=f"from_state={from_state}, to_state={to_state}" if from_state else None,
    )


def log_execution_request(
    audit_log: AuditLog,
    artifact_id: str,
    actor_id: str,
    gate_states: dict,
    approved: bool,
    details: str,
) -> AuditEvent:
    """
    Log an execution request audit event.
    Every execution request MUST be logged, whether approved or rejected.
    """
    event = create_audit_event(
        event_subtype="execution_request" if approved else "execution_rejected",
        artifact_id=artifact_id,
        actor_id=actor_id,
        details=details,
        gate_states=gate_states,
    )
    audit_log.append(event)
    return event


def log_laundering_detection(
    audit_log: AuditLog,
    artifact_id: str,
    actor_id: str,
    laundering_type: str,
    details: str,
) -> AuditEvent:
    """
    Log a laundering detection. Always generates an audit event.
    """
    event = create_audit_event(
        event_subtype="laundering_detected",
        artifact_id=artifact_id,
        actor_id=actor_id,
        details=f"Laundering detected ({laundering_type}): {details}",
        compatible_result="FALSE",
    )
    audit_log.append(event)
    return event


def log_rehydration(
    audit_log: AuditLog,
    agent_id: str,
    raw_export_status: str,
    access_scope: dict,
    strongest_safe_claim: str,
) -> AuditEvent:
    """Log an agent rehydration event."""
    event = create_audit_event(
        event_subtype="rehydration",
        artifact_id="habitat",
        actor_id=agent_id,
        details=(
            f"Agent {agent_id} rehydrated. "
            f"raw_export_status={raw_export_status}. "
            f"strongest_safe_claim={strongest_safe_claim}"
        ),
    )
    audit_log.append(event)
    return event
