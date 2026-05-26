from .audit import make_audit_event
from .state import Artifact, TrustState


def quarantine_artifact(artifact: Artifact, reason: str):
    artifact.lineage.append(artifact.trust_state.value)
    artifact.trust_state = TrustState.QUARANTINED
    return make_audit_event("quarantine", artifact.artifact_id, reason=reason, lineage=list(artifact.lineage))
