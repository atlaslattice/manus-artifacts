from reference_impl.atlas_orcs.audit import make_audit_event

from .cas001a_anchor import anchor_request
from .dphi_gate import evaluate_dphi_gate


def process_execution_request(payload: dict) -> tuple[bool, dict]:
    gate_ok, reason = evaluate_dphi_gate(
        receipt_present=payload.get("receipt_present", False),
        human_permission=payload.get("human_permission", False),
        safety_pass=payload.get("safety_pass", False),
    )
    if not gate_ok:
        return False, {"reason": reason}

    anchor = anchor_request(payload.get("request_id", "unknown"))
    audit = make_audit_event("execution_request_passed", payload.get("artifact_id", "unknown"), anchor=anchor)

    route = ["D-Φ-1", "CAS-001-A", "human_gate", "atlas_orcs_audit_state"]
    if payload.get("repo_related") or payload.get("merge_order") or payload.get("code_execution"):
        route.append("TIDELOCK")

    return True, {"audit_event": audit, "route": route, "lane": "tidelock" if "TIDELOCK" in route else "standard"}
