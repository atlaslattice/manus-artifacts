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

_DELTA_KEYS = {
    "authority": "authority_grant_id",
    "canon": "ratification_event_id",
    "deployment": "deployment_approval_id",
    "proof": "proof_attestation_id",
    "public_claim": "public_claim_approval_id",
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

    for kind, delta_key in _DELTA_KEYS.items():
        if _increase(kind, old, new) and not _has_delta(delta, delta_key):
            return "FALSE"

    return "TRUE"


def launder(path: Iterable[dict[str, Any]]) -> bool:
    """Return True when a path causes unauthorized status escalation."""
    edges = list(path)
    if not edges:
        return False

    start = dict(edges[0].get("from", {}))
    end = dict(edges[-1].get("to", {}))

    seen_deltas: set[str] = set()
    for edge in edges:
        delta = dict(edge.get("governance_delta", {}))
        for key in _DELTA_KEYS.values():
            if _has_delta(delta, key):
                seen_deltas.add(key)

    for kind, delta_key in _DELTA_KEYS.items():
        if _increase(kind, start, end) and delta_key not in seen_deltas:
            return True

    return False


def compatible_path(path: Iterable[dict[str, Any]]) -> bool:
    """Path rule: all edges TRUE and NOT launder(path)."""
    edges = list(path)
    if any(compatible(edge) != "TRUE" for edge in edges):
        return False
    return not launder(edges)
