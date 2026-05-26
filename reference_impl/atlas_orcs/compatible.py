from enum import Enum
from typing import Iterable


class CompatibleDecision(str, Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    HOLD = "HOLD"


AUTH_INCREASE_FIELDS = {"authority_scope", "canon_status", "deployment_status", "proof_status", "public_claim_status"}


def compatible_edge(edge: dict) -> CompatibleDecision:
    if edge.get("hold"):
        return CompatibleDecision.HOLD
    if edge.get("allowed") is False:
        return CompatibleDecision.FALSE
    return CompatibleDecision.TRUE


def launder(path: Iterable[dict]) -> bool:
    for edge in path:
        increased = set(edge.get("increased", []))
        if increased & AUTH_INCREASE_FIELDS and not edge.get("governance_delta_permitted", False):
            return True
    return False


def compatible_path(path: Iterable[dict]) -> CompatibleDecision:
    decisions = [compatible_edge(e) for e in path]
    if CompatibleDecision.FALSE in decisions:
        return CompatibleDecision.FALSE
    if CompatibleDecision.HOLD in decisions:
        return CompatibleDecision.HOLD
    if launder(path):
        return CompatibleDecision.FALSE
    return CompatibleDecision.TRUE
