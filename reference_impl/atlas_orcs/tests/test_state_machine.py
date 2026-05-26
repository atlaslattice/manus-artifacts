from datetime import datetime, timedelta
import pytest

from reference_impl.atlas_orcs.state import Artifact
from reference_impl.atlas_orcs.delta import GovernanceDelta
from reference_impl.atlas_orcs.transitions import transition, change_deployment_status, add_contradiction, apply_ratification_expiry
from reference_impl.atlas_orcs.quarantine import quarantine


def test_ratified_requires_event():
    a = Artifact("a1", state="reviewed")
    with pytest.raises(ValueError):
        transition(a, "ratified", GovernanceDelta(ratification_event=False))


def test_deployment_requires_governance_event():
    a = Artifact("a1")
    with pytest.raises(ValueError):
        change_deployment_status(a, "deployable", GovernanceDelta(governance_event=False))


def test_quarantine_preserves_lineage():
    a = Artifact("a1", state="candidate")
    q = quarantine(a)
    assert q.state == "quarantined"
    assert "candidate" in q.lineage


def test_contradiction_appends_record_not_overwrite():
    a = Artifact("a1")
    add_contradiction(a, {"id": 1})
    add_contradiction(a, {"id": 2})
    assert len(a.contradiction_records) == 2


def test_expired_ratification_moves_under_review():
    a = Artifact("a1", state="ratified")
    a.ratification_expires_at = datetime.utcnow() - timedelta(seconds=1)
    out = apply_ratification_expiry(a, datetime.utcnow())
    assert out.state == "under_review"
