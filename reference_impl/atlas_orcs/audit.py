"""
Atlas / ORCS Audit Log.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

Every governance action MUST emit an audit event.
Every failure MUST emit an audit event.
"""

import datetime
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AuditEntry:
    event_type: str
    artifact_id: Optional[str]
    actor: str
    description: str
    outcome: str  # passed | failed | hold | blocked | alert | informational | transition
    timestamp: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    tidelock_involved: bool = False


class AuditLog:
    """Append-only audit log. Every action is recorded."""

    def __init__(self) -> None:
        self._entries: List[AuditEntry] = []

    def emit(
        self,
        event_type: str,
        actor: str,
        description: str,
        outcome: str,
        artifact_id: Optional[str] = None,
        tidelock_involved: bool = False,
    ) -> AuditEntry:
        entry = AuditEntry(
            event_type=event_type,
            artifact_id=artifact_id,
            actor=actor,
            description=description,
            outcome=outcome,
            tidelock_involved=tidelock_involved,
        )
        self._entries.append(entry)
        return entry

    def entries(self) -> List[AuditEntry]:
        return list(self._entries)

    def entries_for(self, artifact_id: str) -> List[AuditEntry]:
        return [e for e in self._entries if e.artifact_id == artifact_id]

    def failures(self) -> List[AuditEntry]:
        return [e for e in self._entries if e.outcome in ("failed", "blocked")]
