from __future__ import annotations


def _node_index(graph: dict) -> dict[str, dict]:
    return {n["id"]: n for n in graph.get("nodes", []) if "id" in n}


def where_claim_came_from(graph: dict, claim_id: str) -> list[str]:
    """Return chain from claim to source via derived_from edges."""
    node_by_id = _node_index(graph)
    edges = graph.get("edges", [])

    lineage = [claim_id]
    current = claim_id
    visited = {claim_id}
    while True:
        step = next((e for e in edges if e.get("src") == current and e.get("type") == "derived_from"), None)
        if not step:
            break
        nxt = step.get("dst")
        if not nxt or nxt in visited:
            break
        lineage.append(nxt)
        visited.add(nxt)
        current = nxt
        if node_by_id.get(nxt, {}).get("type") == "raw_source":
            break

    return lineage


def evidence_supporting_claim(graph: dict, claim_id: str) -> list[str]:
    edges = graph.get("edges", [])
    return [e["src"] for e in edges if e.get("type") == "supports" and e.get("dst") == claim_id]


def summary_only_nodes(graph: dict) -> list[str]:
    out = []
    for n in graph.get("nodes", []):
        if n.get("raw_export_status") in {"summary_only", "partial_raw", "unavailable"}:
            out.append(n["id"])
        elif n.get("public_use_status") == "source_incomplete":
            out.append(n["id"])
    return sorted(set(out))


def blocked_from_public_use(graph: dict) -> list[str]:
    out = []
    for n in graph.get("nodes", []):
        if n.get("public_use_status") in {"blocked", "source_incomplete"}:
            out.append(n["id"])
        if n.get("blocked_reason"):
            out.append(n["id"])
    return sorted(set(out))
