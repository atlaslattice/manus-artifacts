from __future__ import annotations

from copy import deepcopy

TRUST_STATES = {
    "raw",
    "parsed",
    "candidate",
    "reviewed",
    "ratified",
    "active",
    "under_review",
    "superseded",
    "revoked",
    "quarantined",
    "rejected",
}


def is_valid_state(state: str | None) -> bool:
    return isinstance(state, str) and state in TRUST_STATES


def normalize_artifact(artifact: dict | None) -> dict:
    base = deepcopy(artifact or {})
    base.setdefault("trust_state", "raw")
    base.setdefault("deployment_status", "not_deployable")
    base.setdefault("lineage", [])
    base.setdefault("contradiction_records", [])
    base.setdefault("audit_log", [])
    return base
