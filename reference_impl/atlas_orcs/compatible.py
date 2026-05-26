from enum import Enum


class Verdict(str, Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    HOLD = "HOLD"


def compatible_edge(edge: dict) -> Verdict:
    return Verdict(edge.get("verdict", "FALSE"))


def _increase_without_governance(edge: dict, key: str) -> bool:
    return edge.get(f"{key}_increase", False) and not edge.get("governance_delta", False)


def launder_path(path: list[dict]) -> bool:
    keys = ["authority", "canon", "deployment", "proof", "public_claim"]
    for edge in path:
        if any(_increase_without_governance(edge, key) for key in keys):
            return True
    return False


def compatible_path(path: list[dict]) -> Verdict:
    if any(compatible_edge(edge) == Verdict.FALSE for edge in path):
        return Verdict.FALSE
    if any(compatible_edge(edge) == Verdict.HOLD for edge in path):
        return Verdict.HOLD
    if launder_path(path):
        return Verdict.FALSE
    return Verdict.TRUE
