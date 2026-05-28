#!/usr/bin/env python3
"""export_children_swarm_lattice.py — Wave 4, Task 41.

Exports a derived-lattice JSON for the Children Swarm based on the current
global index and any agent-specific contribution markers found in the repo.

Usage:
    python scripts/export_children_swarm_lattice.py [--agent-id <id>] [--out <path>]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODE_INDEX = ROOT / "docs" / "LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md"
GLOBAL_INDEX = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"
OUTPUT_DIR = ROOT / "docs" / "generated" / "swarm_exports"

ROW_RE = re.compile(
    r"^\|\s*(N-[^|]+?)\s*\|\s*([^|]+?)\s*\|\s*\[(.*?)\]\((.*?)\)\s*\|\s*(.*?)\s*\|$"
)

AGENT_NODE_TYPES = {"Agent", "Program"}


def get_git_head_sha() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def parse_global_index() -> dict[str, dict]:
    if not GLOBAL_INDEX.exists():
        return {}
    data = json.loads(GLOBAL_INDEX.read_text(encoding="utf-8"))
    return {n["id"]: n for n in data.get("nodes", [])}


def filter_swarm_nodes(
    all_nodes: dict[str, dict],
) -> list[dict]:
    """Return nodes relevant to the Children Swarm (Agent + connected programs)."""
    swarm_roots = {
        node_id
        for node_id, node in all_nodes.items()
        if node.get("type") in AGENT_NODE_TYPES
    }
    # Expand one hop: include any node linked from a swarm root
    reachable = set(swarm_roots)
    for node_id in swarm_roots:
        reachable.update(all_nodes[node_id].get("links", []))

    result = []
    for node_id in sorted(reachable):
        if node_id in all_nodes:
            result.append(all_nodes[node_id])
    return result


def build_edges(nodes: list[dict]) -> list[dict]:
    node_ids = {n["id"] for n in nodes}
    edges = []
    for node in nodes:
        for target in node.get("links", []):
            if target in node_ids:
                edges.append({"from": node["id"], "to": target, "rel": "links-to"})
    return edges


def validate_derived_lattice(nodes: list[dict], all_node_ids: set[str]) -> list[str]:
    errors = []
    seen_ids: set[str] = set()
    for node in nodes:
        nid = node["id"]
        if nid in seen_ids:
            errors.append(f"duplicate node id: {nid}")
        seen_ids.add(nid)
        for link in node.get("links", []):
            if link not in seen_ids and link not in all_node_ids:
                errors.append(f"unknown link target {link!r} in node {nid}")
    orphans = [n["id"] for n in nodes if not n.get("links")]
    for o in orphans:
        errors.append(f"orphan node (no links): {o}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export Children Swarm derived lattice")
    parser.add_argument(
        "--agent-id",
        default=f"copilot-{datetime.now(timezone.utc).strftime('%Y%m%d')}",
        help="Agent identifier for this export session",
    )
    parser.add_argument(
        "--agent-type",
        default="copilot",
        choices=["copilot", "tidelock", "gptbrain", "custom"],
        help="Agent type",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output file path (default: docs/generated/swarm_exports/<agent-id>.json)",
    )
    parser.add_argument(
        "--wake-artifact",
        default=None,
        help="Optional path to TIDELOCKBrain wake artifact",
    )
    parser.add_argument(
        "--pr-url",
        default=None,
        help="Optional GitHub PR URL",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate only, do not write output",
    )
    args = parser.parse_args(argv)

    if not GLOBAL_INDEX.exists():
        print(f"global index not found: {GLOBAL_INDEX}; run build_lattice_global_index.py first")
        return 1

    all_nodes = parse_global_index()
    if not all_nodes:
        print("no nodes found in global index")
        return 1

    swarm_nodes = filter_swarm_nodes(all_nodes)
    if not swarm_nodes:
        print("no swarm nodes found")
        return 1

    edges = build_edges(swarm_nodes)
    all_node_ids = set(all_nodes.keys())
    errors = validate_derived_lattice(swarm_nodes, all_node_ids)

    if errors:
        print("derived-lattice validation errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    sha = get_git_head_sha()
    payload = {
        "status": "Candidate",
        "agent_id": args.agent_id,
        "agent_type": args.agent_type,
        "session_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "parent_lattice": "LATTICE_GLOBAL_INDEX",
        "metrics": {
            "node_count": len(swarm_nodes),
            "edge_count": len(edges),
        },
        "nodes": swarm_nodes,
        "edges": edges,
        "provenance": {
            "commit_sha": sha,
            "pr_url": args.pr_url,
            "wake_artifact": args.wake_artifact,
        },
    }

    if args.validate_only:
        print(
            f"derived-lattice valid: {len(swarm_nodes)} nodes, {len(edges)} edges"
        )
        return 0

    out_path = Path(args.out) if args.out else OUTPUT_DIR / f"{args.agent_id}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    try:
        display = out_path.relative_to(ROOT)
    except ValueError:
        display = out_path
    print(
        f"wrote derived lattice: {display} "
        f"({len(swarm_nodes)} nodes, {len(edges)} edges)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
