from __future__ import annotations

from reference_impl.atlas_orcs.ratification import has_ratification_event
from reference_impl.atlas_orcs.state import is_valid_state


ALLOWED_TRANSITIONS: dict[str, set[str]] = {
    "raw": {"parsed", "candidate", "rejected", "quarantined"},
    "parsed": {"candidate", "rejected", "quarantined"},
    "candidate": {"reviewed", "rejected", "quarantined", "superseded"},
    "reviewed": {"ratified", "rejected", "quarantined", "under_review"},
    "ratified": {"active", "under_review", "superseded", "revoked", "quarantined"},
    "active": {"under_review", "superseded", "revoked", "quarantined"},
    "under_review": {"reviewed", "ratified", "revoked", "quarantined"},
    "superseded": {"under_review", "quarantined"},
    "revoked": {"under_review", "quarantined"},
    "quarantined": {"under_review", "rejected"},
    "rejected": set(),
}


def validate_transition(before: dict, after: dict, delta: dict) -> list[str]:
    errors: list[str] = []

    previous_state = before.get("trust_state")
    next_state = after.get("trust_state")

    if not is_valid_state(previous_state):
        errors.append("invalid:previous_trust_state")
    if not is_valid_state(next_state):
        errors.append("invalid:trust_state")

    if not errors and previous_state != next_state:
        if next_state not in ALLOWED_TRANSITIONS.get(previous_state, set()):
            errors.append("invalid:state_transition")

    if next_state == "ratified" and not has_ratification_event(after):
        errors.append("ratified_requires_ratification_event")

    if before.get("deployment_status") != after.get("deployment_status"):
        gov = delta.get("governance_event") or after.get("governance_event")
        if not (isinstance(gov, dict) and gov.get("governance_event_id")):
            errors.append("deployment_change_requires_governance_event")

    if before.get("source_status") == "source" and after.get("source_basis") == "summary_only":
        errors.append("summary_cannot_replace_source")

    return errors
