from reference_impl.atlas_orcs.quarantine import quarantine_artifact
from reference_impl.atlas_orcs.state import Artifact, TrustState


def test_quarantine_preserves_lineage():
    artifact = Artifact("a1", trust_state=TrustState.REVIEWED)
    event = quarantine_artifact(artifact, "safety-check-failed")
    assert artifact.trust_state == TrustState.QUARANTINED
    assert "reviewed" in artifact.lineage
    assert event.event_type == "quarantine"
