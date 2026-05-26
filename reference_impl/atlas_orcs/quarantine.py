"""
Atlas / ORCS Quarantine Engine.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

Quarantine preserves lineage. It never destroys source artifacts.
"""

from dataclasses import dataclass, field
from typing import Optional
from .state import Artifact, TrustState
from .audit import AuditLog


@dataclass
class QuarantineRecord:
    """Records that an artifact was quarantined, preserving full lineage."""
    quarantine_id: str
    artifact_id: str
    reason: str
    trigger_event_type: str
    lineage_preserved: bool = True
    source_preserved: bool = True


def quarantine_artifact(
    artifact: Artifact,
    reason: str,
    trigger_event_type: str,
    audit: AuditLog,
    quarantine_id: Optional[str] = None,
) -> tuple:
    """
    Quarantine an artifact.

    Returns (updated_artifact, quarantine_record).
    Lineage is ALWAYS preserved.
    Source is ALWAYS preserved.
    An audit event is ALWAYS emitted.
    """
    previous_state = artifact.trust_state

    # Preserve lineage — quarantine records the history, does not erase it
    artifact.trust_state = TrustState.QUARANTINED
    # lineage is unchanged — quarantine does not modify lineage

    record = QuarantineRecord(
        quarantine_id=quarantine_id or f"quarantine-{artifact.artifact_id}",
        artifact_id=artifact.artifact_id,
        reason=reason,
        trigger_event_type=trigger_event_type,
        lineage_preserved=True,
        source_preserved=True,
    )

    audit.emit(
        event_type="quarantine_triggered",
        artifact_id=artifact.artifact_id,
        actor="quarantine_engine",
        description=f"Quarantined from {previous_state}: {reason}",
        outcome="alert",
    )

    return artifact, record
