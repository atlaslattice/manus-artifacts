def evaluate_dphi_gate(receipt_present: bool, human_permission: bool, safety_pass: bool) -> tuple[bool, str]:
    if not receipt_present:
        return False, "missing_receipt"
    if not human_permission:
        return False, "missing_human_permission"
    if not safety_pass:
        return False, "safety_gate_failed"
    return True, "pass"
