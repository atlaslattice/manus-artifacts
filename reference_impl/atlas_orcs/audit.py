from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AuditEvent:
    event_type: str
    artifact_id: str
    details: Dict[str, Any]


def make_audit_event(event_type: str, artifact_id: str, **details: Any) -> AuditEvent:
    return AuditEvent(event_type=event_type, artifact_id=artifact_id, details=details)
