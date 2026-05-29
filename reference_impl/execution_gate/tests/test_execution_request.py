from reference_impl.execution_gate.execution_request import process_execution_request


def test_execution_request_without_receipt_fails():
    ok, data = process_execution_request({"request_id": "r1"})
    assert ok is False
    assert data["reason"] == "missing_receipt"


def test_execution_request_without_human_permission_fails():
    ok, data = process_execution_request({"request_id": "r1", "receipt_present": True, "human_permission": False, "safety_pass": True})
    assert ok is False
    assert data["reason"] == "missing_human_permission"


def test_execution_request_without_safety_pass_fails():
    ok, data = process_execution_request({"request_id": "r1", "receipt_present": True, "human_permission": True, "safety_pass": False})
    assert ok is False
    assert data["reason"] == "safety_gate_failed"


def test_pass_creates_audit_event_and_tidelock_route_for_repo_related():
    ok, data = process_execution_request(
        {
            "request_id": "r1",
            "artifact_id": "a1",
            "receipt_present": True,
            "human_permission": True,
            "safety_pass": True,
            "repo_related": True,
        }
    )
    assert ok is True
    assert data["audit_event"].event_type == "execution_request_passed"
    assert "TIDELOCK" in data["route"]
