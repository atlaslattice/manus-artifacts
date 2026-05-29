from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone

from reference_impl.atlas_orcs.audit import append_audit_event


def _parse_iso8601(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def has_ratification_event(payload: dict) -> bool:
    event = payload.get("ratification_event")
    return isinstance(event, dict) and bool(event.get("ratification_event_id"))


def is_ratification_expired(artifact: dict, now: datetime | None = None) -> bool:
    expiry = artifact.get("ratification_expires_at")
    if not expiry:
        return False
    now_utc = now or datetime.now(timezone.utc)
    return _parse_iso8601(expiry) <= now_utc


def enforce_ratification_freshness(artifact: dict, now: datetime | None = None) -> dict:
    updated = deepcopy(artifact)
    if updated.get("trust_state") in {"ratified", "active"} and is_ratification_expired(updated, now=now):
        updated["trust_state"] = "under_review"
        updated = append_audit_event(updated, "ratification_expired", {"moved_to": "under_review"})
    return updated
