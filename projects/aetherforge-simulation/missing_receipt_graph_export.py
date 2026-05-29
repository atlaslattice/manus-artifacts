"""Export Lucerna missing receipt / hash gap register as graph nodes and edges."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

REGISTER_PATH = Path(__file__).with_name("lucerna_missing_receipt_hash_gap_register_v0_1.json")
PROJECT_ID = "project:aetherforge-sheldonbrain-kg-gap-register"
REGISTER_ID = "artifact:lucerna-missing-receipt-hash-gap-register-v0.1"
BOUNDARY_ID = "boundary:gap-register-non-canon"


def load_register(path: Path = REGISTER_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def key(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


def node(node_id: str, label: str, node_type: str, **properties: Any) -> dict[str, Any]:
    return {"id": node_id, "label": label, "type": node_type, "properties": properties}


def edge(source: str, relation: str, target: str, **properties: Any) -> dict[str, Any]:
    return {"source": source, "relation": relation, "target": target, "properties": properties}


def validate_register(register: dict[str, Any]) -> dict[str, Any]:
    missing = register["missing_receipt_nodes"]
    blockers = register["human_root_blockers"]
    mr_ids = [item["id"] for item in missing]
    blocker_ids = [item["id"] for item in blockers]
    boundary = register["boundary"]
    report = {
        "missing_receipt_count": len(missing),
        "human_root_blocker_count": len(blockers),
        "unique_missing_receipt_ids": len(set(mr_ids)),
        "unique_blocker_ids": len(set(blocker_ids)),
        "canon_false": boundary.get("canon") is False,
        "deployment_false": boundary.get("deployment") is False,
        "authority_none": boundary.get("authority") == "none",
        "has_source_url": bool(register.get("source_url")),
    }
    report["ok"] = (
        report["missing_receipt_count"] == 7
        and report["human_root_blocker_count"] == 4
        and report["unique_missing_receipt_ids"] == 7
        and report["unique_blocker_ids"] == 4
        and report["canon_false"]
        and report["deployment_false"]
        and report["authority_none"]
        and report["has_source_url"]
    )
    return report


def surface_node_id(surface: str) -> str:
    return f"surface:{key(surface)}"


def build_graph(register_path: Path = REGISTER_PATH) -> dict[str, Any]:
    register = load_register(register_path)
    validation = validate_register(register)
    nodes: list[dict[str, Any]] = [
        node(PROJECT_ID, "Aetherforge / Sheldonbrain KG gap register", "Project"),
        node(REGISTER_ID, register["artifact_id"], "GapRegister", source_url=register["source_url"], status=register["status"]),
        node(BOUNDARY_ID, "Candidate gap register boundary", "Boundary", **register["boundary"]),
    ]
    edges: list[dict[str, Any]] = [
        edge(PROJECT_ID, "contains", REGISTER_ID),
        edge(BOUNDARY_ID, "constrains", PROJECT_ID),
        edge(BOUNDARY_ID, "constrains", REGISTER_ID),
    ]

    surfaces = sorted({item["surface"] for item in register["missing_receipt_nodes"] + register["human_root_blockers"]})
    for surface in surfaces:
        sid = surface_node_id(surface)
        nodes.append(node(sid, surface, "SourceSurface"))
        edges.append(edge(REGISTER_ID, "mentions_surface", sid))

    for gap in register["missing_receipt_nodes"]:
        gid = f"missing-receipt:{gap['id']}"
        sid = surface_node_id(gap["surface"])
        nodes.append(node(gid, gap["title"], "MissingReceipt", **gap))
        edges.extend([
            edge(REGISTER_ID, "contains", gid),
            edge(gid, "belongs_to_surface", sid),
            edge(BOUNDARY_ID, "constrains", gid),
        ])
        for blocked in gap.get("blocks", []):
            bid = f"blocked-object:{key(blocked)}"
            if not any(existing["id"] == bid for existing in nodes):
                nodes.append(node(bid, blocked, "BlockedObject"))
            edges.append(edge(bid, "blocked_by", gid))

    for blocker in register["human_root_blockers"]:
        bid = f"human-root-blocker:{blocker['id']}"
        sid = surface_node_id(blocker["surface"])
        nodes.append(node(bid, blocker["title"], "HumanRootBlocker", **blocker))
        edges.extend([
            edge(REGISTER_ID, "contains", bid),
            edge(bid, "belongs_to_surface", sid),
            edge(BOUNDARY_ID, "constrains", bid),
        ])

    graph = {
        "schema_version": "lucerna.gap_register_graph.v0_1",
        "project": PROJECT_ID,
        "source_register": register_path.name,
        "validation": validation,
        "summary": {
            "nodes": len(nodes),
            "edges": len(edges),
            "missing_receipts": validation["missing_receipt_count"],
            "human_root_blockers": validation["human_root_blocker_count"],
        },
        "nodes": sorted(nodes, key=lambda item: item["id"]),
        "edges": sorted(edges, key=lambda item: (item["source"], item["relation"], item["target"])),
    }
    return graph


def render_text(graph: dict[str, Any]) -> str:
    summary = graph["summary"]
    return "\n".join([
        "Lucerna missing receipt graph",
        f"nodes: {summary['nodes']}",
        f"edges: {summary['edges']}",
        f"missing_receipts: {summary['missing_receipts']}",
        f"human_root_blockers: {summary['human_root_blockers']}",
        f"validation_ok: {graph['validation']['ok']}",
    ])


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export Lucerna missing receipt register graph.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--register-path", default=str(REGISTER_PATH), help="Path to gap register JSON.")
    args = parser.parse_args(list(argv) if argv is not None else None)
    graph = build_graph(Path(args.register_path))
    print(json.dumps(graph, indent=2, sort_keys=True) if args.json else render_text(graph))
    return 0 if graph["validation"]["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
