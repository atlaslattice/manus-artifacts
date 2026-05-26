"""compatible() anti-laundering predicate.

STATUS: CANDIDATE BUILD PLAN — NOT CANON — NON-DEPLOYABLE
"""

from __future__ import annotations

from typing import Any, Iterable, Literal

Decision = Literal["TRUE", "FALSE", "HOLD"]

_ORDERINGS = {
    "authority": {"NONE": 0, "QUERY_ONLY": 1, "FORMALIZATION_ONLY": 2, "GOVERNED": 3},
    "canon": {"NOT_CANON": 0, "CANDIDATE": 1, "RATIFIED_CANON": 2},
    "deployment": {"NON_DEPLOYABLE": 0, "CANDIDATE_ONLY": 1, "DEPLOYABLE": 2},
    "proof": {"NONE": 0, "RECEIPT_ONLY": 1, "PROOF": 2},
    "public_claim": {"PRIVATE": 0, "PUBLIC_VISIBLE": 1, "AUTHORITATIVE_CLAIM": 2},
}


def _level(kind: str, value: str) -> int:
    return _ORDERINGS[kind].get(value, -1)


def _increase(kind: str, old: dict[str, Any], new: dict[str, Any]) -> bool:
    return _level(kind, str(new.get(kind, ""))) > _level(kind, str(old.get(kind, "")))


def _has_delta(delta: dict[str, Any], key: str) -> bool:
    return bool(delta.get(key))


def compatible(edge: dict[str, Any]) -> Decision:
    """Return TRUE, FALSE, or HOLD for one transition edge."""
    if not edge.get("local_valid", True):
        return "FALSE"
    if edge.get("hold", False):
        return "HOLD"

    old = dict(edge.get("from", {}))
    new = dict(edge.get("to", {}))
    delta = dict(edge.get("governance_delta", {}))

    if _increase("canon", old, new) and not _has_delta(delta, "ratification_event_id"):
        return "FALSE"
    if _increase("authority", old, new) and not _has_delta(delta, "authority_grant_id"):
        return "FALSE"
    if _increase("deployment", old, new) and not _has_delta(delta, "deployment_approval_id"):
        return "FALSE"
    if _increase("proof", old, new) and not _has_delta(delta, "proof_attestation_id"):
        return "FALSE"
    if _increase("public_claim", old, new) and not _has_delta(delta, "public_claim_approval_id"):
        return "FALSE"

    # Receipt-only path cannot become proof unless explicitly attested.
    if old.get("proof") == "RECEIPT_ONLY" and new.get("proof") == "PROOF":
        if not _has_delta(delta, "proof_attestation_id"):
            return "FALSE"

    # Public visibility cannot become authority unless explicitly granted.
    if old.get("public_claim") == "PUBLIC_VISIBLE" and _increase("authority", old, new):
        if not _has_delta(delta, "authority_grant_id"):
            return "FALSE"

    return "TRUE"


def launder(path: Iterable[dict[str, Any]]) -> bool:
    """Return True if the path composes into unauthorized status escalation."""
    for edge in path:
        if compatible(edge) != "TRUE":
            return True
    return False


def compatible_path(path: Iterable[dict[str, Any]]) -> bool:
    """Path rule: all edges TRUE and NOT launder(path)."""
    edges = list(path)
    return all(compatible(edge) == "TRUE" for edge in edges) and not launder(edges)
