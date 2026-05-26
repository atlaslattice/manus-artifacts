from __future__ import annotations

from copy import deepcopy
from uuid import uuid4


def append_audit_event(artifact: dict, event_type: str, details: dict | None = None) -> dict:
    updated = deepcopy(artifact)
    updated.setdefault("audit_log", []).append({
        "event_type": event_type,
        "details": details or {},
    })
    return updated


def record_contradiction(
    artifact: dict,
    conflicting_claim: dict,
    reason: str,
    contradiction_event_id: str | None = None,
) -> dict:
    updated = deepcopy(artifact)
    updated.setdefault("contradiction_records", []).append(
        {
            "contradiction_id": contradiction_event_id or str(uuid4()),
            "reason": reason,
            "existing_claim": updated.get("claim"),
            "conflicting_claim": conflicting_claim,
        }
    )
    return append_audit_event(updated, "contradiction_recorded", {"reason": reason})
