from datetime import datetime
from .state import Artifact, VALID_STATES
from .delta import GovernanceDelta


def transition(artifact: Artifact, target_state: str, delta: GovernanceDelta) -> Artifact:
    if target_state not in VALID_STATES:
        raise ValueError("invalid target state")
    if target_state == "ratified" and not delta.ratification_event:
        raise ValueError("ratification_event required")
    artifact.state = target_state
    return artifact


def change_deployment_status(artifact: Artifact, deployment_status: str, delta: GovernanceDelta) -> Artifact:
    if not delta.governance_event:
        raise ValueError("governance_event required")
    artifact.deployment_status = deployment_status
    return artifact


def add_contradiction(artifact: Artifact, record: dict) -> Artifact:
    artifact.contradiction_records.append(record)
    return artifact


def apply_ratification_expiry(artifact: Artifact, now: datetime) -> Artifact:
    if artifact.ratification_expires_at and now >= artifact.ratification_expires_at and artifact.state in {"ratified", "active"}:
        artifact.state = "under_review"
    return artifact
