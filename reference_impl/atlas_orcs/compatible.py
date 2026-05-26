from enum import Enum

class Decision(str, Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    HOLD = "HOLD"


# Ordinal rank tables for each governed status dimension.
# A value absent from the table is treated as rank 0 (lowest).
# Laundering is detected when rank(after) > rank(before) without
# an explicit permitted governance delta.
_RANKS: dict[str, dict[str | None, int]] = {
    "authority": {None: 0, "none": 1, "unofficial": 2, "official": 3},
    "canon": {None: 0, "not_canon": 1, "candidate": 2, "ratified": 3},
    "deployment": {None: 0, "not_deployable": 1, "candidate": 2, "deployable": 3},
    "proof": {None: 0, "none": 1, "receipt": 2, "proof": 3},
    "public_claim": {None: 0, "none": 1, "visible": 2, "authority": 3},
}


def _rank(dimension: str, value: str | None) -> int:
    return _RANKS[dimension].get(value, 0)


def compatible_edge(edge: dict) -> Decision:
    if edge.get("local_valid") is False:
        return Decision.FALSE
    if edge.get("hold") is True:
        return Decision.HOLD
    return Decision.TRUE


def launder(path: list[dict]) -> bool:
    """Return True if any edge in path increases a governed status dimension
    without an explicit permitted governance delta."""
    for edge in path:
        if edge.get("governance_delta_permitted") is True:
            continue
        before = edge.get("before", {})
        after = edge.get("after", {})
        for dim in _RANKS:
            if _rank(dim, after.get(dim)) > _rank(dim, before.get(dim)):
                return True
    return False


def compatible_path(path: list[dict]) -> Decision:
    """Evaluate a path of edges.

    Returns FALSE if any edge is locally invalid or if the path launders.
    Returns HOLD if any edge is on hold (and none are FALSE).
    Returns TRUE only when all edges are TRUE and no laundering occurs.
    """
    result = Decision.TRUE
    for edge in path:
        d = compatible_edge(edge)
        if d == Decision.FALSE:
            # FALSE is terminal — no need to inspect further edges.
            return Decision.FALSE
        if d == Decision.HOLD:
            result = Decision.HOLD
    if launder(path):
        return Decision.FALSE
    return result
