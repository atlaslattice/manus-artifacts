from datetime import datetime, timezone

from .delta import TransitionDelta
from .ratification import requires_explicit_ratification


class TransitionError(ValueError):
    pass


def apply_transition(artifact: dict, delta: TransitionDelta, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)

    if delta.replaces_source_with_summary:
        raise TransitionError("Summary cannot replace source")

    if not requires_explicit_ratification(delta.to_state, delta.ratification_event_id):
        raise TransitionError("ratification_event required for ratified state")

    if artifact.get("deployment_status") != artifact.get("requested_deployment_status"):
        if not delta.governance_event_id:
            raise TransitionError("deployment status changes require governance event")

    updated = dict(artifact)
    updated["state"] = delta.to_state

    if delta.contradiction_record:
        updated.setdefault("contradiction_records", []).append(delta.contradiction_record)

    expiry = updated.get("ratification_expires_at")
    if expiry:
        expires_at = datetime.fromisoformat(expiry.replace("Z", "+00:00"))
        if expires_at < now and updated.get("state") == "ratified":
            updated["state"] = "under_review"

    return updated
