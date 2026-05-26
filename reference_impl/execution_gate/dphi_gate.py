def dphi_gate_passes(request: dict) -> bool:
    gates = request.get("gates", {})
    required = ["provenance_gate", "safety_gate", "governance_gate", "human_permission_gate", "receipt_gate"]

    def gate_value(name: str):
        if name in gates:
            return gates.get(name)
        return gates.get(name.replace("_gate", ""))

    return all(gate_value(g) == "pass" for g in required)
