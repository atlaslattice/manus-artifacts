import pytest

from reference_impl.execution_gate.execution_request import ExecutionGateError, evaluate_execution_request


def test_without_receipt_fails():
    with pytest.raises(ExecutionGateError):
        evaluate_execution_request({"id": "e1", "gates": {"provenance": "pass", "safety": "pass", "governance": "pass", "human_permission": "pass", "receipt": "fail"}})


def test_without_human_permission_fails():
    with pytest.raises(ExecutionGateError):
        evaluate_execution_request({"id": "e2", "gates": {"provenance": "pass", "safety": "pass", "governance": "pass", "human_permission": "fail", "receipt": "pass"}})


def test_without_safety_fails():
    with pytest.raises(ExecutionGateError):
        evaluate_execution_request({"id": "e3", "gates": {"provenance": "pass", "safety": "fail", "governance": "pass", "human_permission": "pass", "receipt": "pass"}})


def test_pass_creates_audit_event_and_tidelock_route():
    out = evaluate_execution_request({"id": "e4", "repo_related": True, "gates": {"provenance": "pass", "safety": "pass", "governance": "pass", "human_permission": "pass", "receipt": "pass"}})
    assert out["audit_event"]["event_type"] == "execution_request"
    assert "TIDELOCKBrain" in out["route"]


def test_pass_with_gate_suffix_keys_succeeds():
    out = evaluate_execution_request(
        {
            "id": "e5",
            "gates": {
                "provenance_gate": "pass",
                "safety_gate": "pass",
                "governance_gate": "pass",
                "human_permission_gate": "pass",
                "receipt_gate": "pass",
            },
        }
    )
    assert out["status"] == "approved"
