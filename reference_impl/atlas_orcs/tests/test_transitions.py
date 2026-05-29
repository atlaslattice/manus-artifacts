import pytest

from reference_impl.atlas_orcs.delta import TransitionDelta
from reference_impl.atlas_orcs.transitions import TransitionError, apply_transition


def test_ratified_requires_event():
    with pytest.raises(TransitionError):
        apply_transition({"state": "reviewed", "deployment_status": "not_deployable", "requested_deployment_status": "not_deployable"}, TransitionDelta(to_state="ratified"))


def test_contradiction_record_is_appended():
    artifact = {"state": "candidate", "deployment_status": "not_deployable", "requested_deployment_status": "not_deployable"}
    out = apply_transition(artifact, TransitionDelta(to_state="reviewed", contradiction_record={"id": "c1"}))
    assert out["contradiction_records"][0]["id"] == "c1"


def test_summary_cannot_replace_source():
    with pytest.raises(TransitionError):
        apply_transition({"state": "candidate", "deployment_status": "not_deployable", "requested_deployment_status": "not_deployable"}, TransitionDelta(to_state="reviewed", replaces_source_with_summary=True))
