from .audit import make_audit_event
from .delta import TransitionDelta
from .state import Artifact, TrustState


class TransitionError(ValueError):
    pass


def apply_delta(artifact: Artifact, delta: TransitionDelta):
    if delta.target_state == TrustState.RATIFIED and not delta.ratification_event_id:
        raise TransitionError("ratification_event required for ratified transition")

    if delta.new_deployment_status is not None and delta.governance_event_id is None:
        raise TransitionError("governance_event required for deployment status change")

    if delta.contradiction_note:
        artifact.contradiction_records.append({"note": delta.contradiction_note, "state": artifact.trust_state.value})

    artifact.trust_state = delta.target_state

    if delta.new_canon_status is not None:
        artifact.canon_status = delta.new_canon_status

    if delta.new_deployment_status is not None:
        artifact.deployment_status = delta.new_deployment_status

    return make_audit_event(
        "transition",
        artifact.artifact_id,
        target_state=delta.target_state.value,
        ratification_event_id=delta.ratification_event_id,
        governance_event_id=delta.governance_event_id,
    )
