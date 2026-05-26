from enum import Enum

class Decision(str, Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    HOLD = "HOLD"


def compatible_edge(edge: dict) -> Decision:
    if edge.get("local_valid") is False:
        return Decision.FALSE
    if edge.get("hold") is True:
        return Decision.HOLD
    return Decision.TRUE


def launder(path: list[dict]) -> bool:
    for edge in path:
        for key in ("authority", "canon", "deployment", "proof", "public_claim"):
            before = edge.get("before", {}).get(key)
            after = edge.get("after", {}).get(key)
            if before != after and edge.get("governance_delta_permitted") is not True:
                return True
    return False


def compatible_path(path: list[dict]) -> Decision:
    for edge in path:
        d = compatible_edge(edge)
        if d == Decision.FALSE:
            return Decision.FALSE
        if d == Decision.HOLD:
            return Decision.HOLD
    if launder(path):
        return Decision.FALSE
    return Decision.TRUE
