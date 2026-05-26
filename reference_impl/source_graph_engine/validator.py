from __future__ import annotations

NODE_TYPES = {"raw_source", "parsed_fact", "claim", "evidence", "review", "action"}
EDGE_TYPES = {"derived_from", "supports", "contradicts", "supersedes", "quarantines"}


def _node_index(graph: dict) -> dict[str, dict]:
    return {n["id"]: n for n in graph.get("nodes", []) if "id" in n}


def validate_graph(graph: dict) -> tuple[bool, list[str]]:
    errors: list[str] = []
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    if not isinstance(nodes, list) or not isinstance(edges, list):
        return False, ["graph must contain list fields: nodes, edges"]

    node_by_id = _node_index(graph)

    for node in nodes:
        node_id = node.get("id")
        node_type = node.get("type")
        if not node_id:
            errors.append("node missing id")
            continue
        if node_type not in NODE_TYPES:
            errors.append(f"node {node_id} has invalid type: {node_type}")

    for edge in edges:
        src = edge.get("src")
        dst = edge.get("dst")
        edge_type = edge.get("type")
        if edge_type not in EDGE_TYPES:
            errors.append(f"edge {src}->{dst} has invalid type: {edge_type}")
        if src not in node_by_id:
            errors.append(f"edge src missing node: {src}")
        if dst not in node_by_id:
            errors.append(f"edge dst missing node: {dst}")

    errors.extend(validate_no_claim_without_source_edge(graph))

    return len(errors) == 0, errors


def validate_no_claim_without_source_edge(graph: dict) -> list[str]:
    """Reject claims without an incoming `derived_from` source edge."""
    errors: list[str] = []
    node_by_id = _node_index(graph)
    edges = graph.get("edges", [])

    claims = [n for n in graph.get("nodes", []) if n.get("type") == "claim"]
    for claim in claims:
        claim_id = claim["id"]
        incoming = [
            e
            for e in edges
            if e.get("src") == claim_id
            and e.get("type") == "derived_from"
            and node_by_id.get(e.get("dst"), {}).get("type") in {"parsed_fact", "raw_source"}
        ]
        if not incoming:
            errors.append(f"claim {claim_id} has no derived_from edge to parsed_fact/raw_source")

    return errors
