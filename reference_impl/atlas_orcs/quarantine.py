"""
Atlas/ORCS Quarantine Module
NOT CANON — NOT DEPLOYABLE — reference implementation only

Handles quarantine operations. Quarantine PRESERVES lineage.
Quarantine is not deletion. Source is always kept.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional, TYPE_CHECKING
from state import TrustState
from delta import QuarantineEvent, AuditEvent
from audit import AuditLog, create_audit_event

if TYPE_CHECKING:
    from transitions import Artifact


@dataclass
class QuarantineRecord:
    """Records a quarantine action. Lineage always preserved."""
    record_id: str
    artifact_id: str
    quarantine_reason: str
    trigger_rule_id: str
    quarantined_by: str
    quarantined_at: str
    lineage_preserved: bool = True  # Always True
    original_state_snapshot: Optional[dict] = None
    resolution_event_id: Optional[str] = None
    resolved_at: Optional[str] = None


class QuarantineStore:
    """In-memory store for quarantine records."""

    def __init__(self):
        self._records: dict[str, QuarantineRecord] = {}

    def add(self, record: QuarantineRecord) -> None:
        self._records[record.record_id] = record

    def get(self, record_id: str) -> Optional[QuarantineRecord]:
        return self._records.get(record_id)

    def get_for_artifact(self, artifact_id: str) -> List[QuarantineRecord]:
        return [r for r in self._records.values() if r.artifact_id == artifact_id]


def quarantine_artifact(
    artifact: "Artifact",
    reason: str,
    trigger_rule_id: str,
    actor_id: str,
    audit_log: AuditLog,
    quarantine_store: QuarantineStore,
) -> tuple["Artifact", QuarantineRecord]:
    """
    Quarantine an artifact.
    - Lineage ALWAYS preserved
    - Original state snapshot saved
    - Audit event created
    - Returns (updated_artifact, quarantine_record)
    """
    now = datetime.now(timezone.utc).isoformat()

    # Save state snapshot before quarantine
    state_snapshot = {
        "trust_state": artifact.trust_state,
        "canon_status": artifact.canon_status,
        "deployment_status": artifact.deployment_status,
        "governance_events": list(artifact.governance_events),
        "lineage": dict(artifact.lineage),
    }

    # Create quarantine record
    record = QuarantineRecord(
        record_id=f"quarantine-{artifact.artifact_id}-{now}",
        artifact_id=artifact.artifact_id,
        quarantine_reason=reason,
        trigger_rule_id=trigger_rule_id,
        quarantined_by=actor_id,
        quarantined_at=now,
        lineage_preserved=True,  # Always True
        original_state_snapshot=state_snapshot,
    )
    quarantine_store.add(record)

    # Apply quarantine event
    event = QuarantineEvent(
        event_id=record.record_id,
        artifact_id=artifact.artifact_id,
        actor_id=actor_id,
        occurred_at=now,
        quarantine_reason=reason,
        trigger_rule_id=trigger_rule_id,
        lineage_preserved=True,
    )

    # Move to quarantined state directly (quarantine bypasses compatible_Γ for safety)
    artifact.trust_state = TrustState.QUARANTINED
    artifact.governance_events.append(event.event_id)

    # Preserve lineage explicitly
    if "quarantine_history" not in artifact.lineage:
        artifact.lineage["quarantine_history"] = []
    artifact.lineage["quarantine_history"].append({
        "record_id": record.record_id,
        "reason": reason,
        "at": now,
    })

    # Audit
    audit_event = create_audit_event(
        event_subtype="quarantine_applied",
        artifact_id=artifact.artifact_id,
        actor_id=actor_id,
        details=f"Artifact quarantined: {reason}. Rule: {trigger_rule_id}. Lineage preserved.",
    )
    audit_log.append(audit_event)

    return artifact, record


def release_from_quarantine(
    artifact: "Artifact",
    record: QuarantineRecord,
    resolution_event_id: str,
    actor_id: str,
    audit_log: AuditLog,
    quarantine_store: QuarantineStore,
) -> "Artifact":
    """
    Release an artifact from quarantine after review.
    Returns the artifact in CANDIDATE state (reset, not restored to pre-quarantine state).
    """
    now = datetime.now(timezone.utc).isoformat()

    if artifact.trust_state != TrustState.QUARANTINED:
        raise ValueError(f"Artifact {artifact.artifact_id} is not quarantined")

    # Update quarantine record
    record.resolution_event_id = resolution_event_id
    record.resolved_at = now

    # Return to candidate state (re-enter governance pipeline)
    artifact.trust_state = TrustState.CANDIDATE
    artifact.governance_events.append(resolution_event_id)

    audit_event = create_audit_event(
        event_subtype="quarantine_released",
        artifact_id=artifact.artifact_id,
        actor_id=actor_id,
        details=f"Artifact released from quarantine. Resolution: {resolution_event_id}",
    )
    audit_log.append(audit_event)

    return artifact
