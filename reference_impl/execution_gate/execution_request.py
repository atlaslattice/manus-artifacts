from .dphi_gate import dphi_gate
from .cas001a_anchor import cas001a_anchor


def evaluate_execution_request(request: dict) -> dict:
    gates = request.get("gates", {})
    passed = dphi_gate(
        gates.get("receipt_gate", False),
        gates.get("safety_gate", False),
        gates.get("human_permission_gate", False),
    ) and cas001a_anchor(
        gates.get("governance_gate", False),
        gates.get("provenance_gate", False),
    )

    route = ["D-Φ-1 / CAS-001-A / human gate", "Atlas / ORCS audit state"]
    if request.get("repo_related"):
        route.append("TIDELOCKBrain")

    if not passed:
        return {"passed": False, "route": route, "audit_event": None}

    return {
        "passed": True,
        "route": route,
        "audit_event": {
            "schema_version": "0.1",
            "event_type": "atlas-audit-event",
            "lane": "TIDELOCK" if request.get("repo_related") else "STANDARD",
        },
    }
