from reference_impl.atlas_orcs.audit import build_audit_event

from .dphi_gate import dphi_gate_passes


class ExecutionGateError(ValueError):
    pass


def evaluate_execution_request(request: dict) -> dict:
    if not dphi_gate_passes(request):
        raise ExecutionGateError("Execution request failed required gates")

    route = ["D-Φ-1", "CAS-001-A", "human_gate", "Atlas_ORCS_audit_state"]
    if request.get("repo_related", False):
        route.append("TIDELOCKBrain")

    return {
        "status": "approved",
        "route": route,
        "audit_event": build_audit_event("execution_request", request.get("id", "unknown"), "approved"),
    }
