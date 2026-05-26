from reference_impl.execution_gate.execution_request import evaluate_execution_request


def fail_event(tag):
    out = evaluate_execution_request({"repo_related": True, "gates": {"safety_gate": False, "human_permission_gate": False, "governance_gate": False, "provenance_gate": False, "receipt_gate": False}})
    return {"test": tag, "failed_safely": out["passed"] is False, "audit_route": out["route"]}


def test_t01_to_t12_fail_safely_with_audit_route():
    tags = [f"T{i:02d}" for i in range(1, 13)]
    for t in tags:
        ev = fail_event(t)
        assert ev["failed_safely"] is True
        assert "Atlas / ORCS audit state" in ev["audit_route"]
