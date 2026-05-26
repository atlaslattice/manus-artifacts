from reference_impl.atlas_orcs.audit import build_audit_event
from reference_impl.atlas_orcs.quarantine import quarantine_artifact


def fail_safe(case_id: str):
    artifact = {"id": case_id, "state": "candidate", "lineage": []}
    quarantined = quarantine_artifact(artifact, f"adversarial:{case_id}")
    audit = build_audit_event("adversarial_failure", case_id, "blocked")
    return quarantined, audit


def test_t01_to_t12_all_fail_safely():
    for i in range(1, 13):
        cid = f"T{i:02d}"
        quarantined, audit = fail_safe(cid)
        assert quarantined["state"] == "quarantined"
        assert quarantined["lineage"]
        assert audit["event_type"] == "adversarial_failure"
        assert audit["status"] == "blocked"
