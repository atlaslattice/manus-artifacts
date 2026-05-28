from __future__ import annotations

from copy import deepcopy
from datetime import datetime

from reference_impl.atlas_orcs.audit import append_audit_event, record_contradiction
from reference_impl.atlas_orcs.quarantine import quarantine_artifact
from reference_impl.atlas_orcs.ratification import enforce_ratification_freshness
from reference_impl.atlas_orcs.state import normalize_artifact
from reference_impl.atlas_orcs.transitions import validate_transition


def apply_delta(artifact: dict, delta: dict, now: datetime | None = None) -> tuple[dict, list[str]]:
    before = normalize_artifact(artifact)
    after = normalize_artifact(deepcopy(before))

    if "contradiction_claim" in delta:
        after = record_contradiction(
            after,
            conflicting_claim=delta["contradiction_claim"],
            reason=delta.get("contradiction_reason", "unspecified"),
            contradiction_event_id=delta.get("contradiction_event_id"),
        )

    for key, value in delta.items():
        if key in {"contradiction_claim", "contradiction_reason", "contradiction_event_id", "quarantine_reason"}:
            continue
        if key == "trust_state" and value == "quarantined":
            continue
        after[key] = value

    if delta.get("trust_state") == "quarantined":
        after = quarantine_artifact(after, reason=delta.get("quarantine_reason", "unspecified"))

    errors = validate_transition(before, after, delta)
    if errors:
        return before, errors

    after = enforce_ratification_freshness(after, now=now)

    if before.get("trust_state") != after.get("trust_state"):
        after = append_audit_event(
            after,
            "state_transition",
            {"from": before.get("trust_state"), "to": after.get("trust_state")},
        )

    return after, []
