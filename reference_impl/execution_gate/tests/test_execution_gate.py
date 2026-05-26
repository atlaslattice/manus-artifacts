from reference_impl.execution_gate.execution_request import evaluate_execution_request


def test_execution_request_without_receipt_fails():
    out = evaluate_execution_request({"gates": {"safety_gate": True, "human_permission_gate": True, "governance_gate": True, "provenance_gate": True, "receipt_gate": False}})
    assert out["passed"] is False


def test_execution_request_without_human_permission_fails():
    out = evaluate_execution_request({"gates": {"safety_gate": True, "human_permission_gate": False, "governance_gate": True, "provenance_gate": True, "receipt_gate": True}})
    assert out["passed"] is False


def test_execution_request_without_safety_fails():
    out = evaluate_execution_request({"gates": {"safety_gate": False, "human_permission_gate": True, "governance_gate": True, "provenance_gate": True, "receipt_gate": True}})
    assert out["passed"] is False


def test_pass_creates_audit_event_and_tidelock_route_for_repo_related():
    out = evaluate_execution_request({"repo_related": True, "gates": {"safety_gate": True, "human_permission_gate": True, "governance_gate": True, "provenance_gate": True, "receipt_gate": True}})
    assert out["passed"] is True
    assert out["audit_event"] is not None
    assert "TIDELOCKBrain" in out["route"]
