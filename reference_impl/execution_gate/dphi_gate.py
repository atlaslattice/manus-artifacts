def dphi_gate(receipt_gate: bool, safety_gate: bool, human_permission_gate: bool) -> bool:
    return all([receipt_gate, safety_gate, human_permission_gate])
