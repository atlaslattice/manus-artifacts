def dphi_gate_passes(request: dict) -> bool:
    gates = request.get("gates", {})
    required = ["provenance", "safety", "governance", "human_permission", "receipt"]
    return all(gates.get(g) == "pass" for g in required)
