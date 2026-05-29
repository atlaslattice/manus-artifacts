#!/usr/bin/env python3
"""
build_lattice_graph.py
======================
Build the Atlas Lattice knowledge graph from:
  1. YAML frontmatter in all repository Markdown files
  2. H-S-N seed JSON files in archive/synthesis/data/

Outputs:
  docs/lattice_graph.json      – JSON-LD graph (nodes + edges)
  docs/lattice_graph_nodes.json – lightweight node list for the visualizer

Usage:
    python scripts/build_lattice_graph.py [--output-dir docs]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HSN_RE = re.compile(r"^H(0[1-9]|1[0-2])-S(0[1-9]|1[0-2])-N(0[1-9]|1[0-2])$")

REVIEW_STATE_ORDER = ["raw", "candidate", "reviewed", "canon-gate", "canon"]

STATUS_COLOR = {
    "CANONICAL": "#22c55e",
    "CANDIDATE": "#f59e0b",
    "DRAFT": "#3b82f6",
    "ARCHIVED": "#6b7280",
    "canon": "#22c55e",
    "canon-gate": "#a855f7",
    "reviewed": "#06b6d4",
    "candidate": "#f59e0b",
    "raw": "#ef4444",
}


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse a minimal subset of YAML (key: value, no nesting needed)."""
    result: dict[str, Any] = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and val:
            result[key] = val
    return result


def load_markdown_nodes(root: Path) -> list[dict[str, Any]]:
    nodes = []
    for md_file in root.rglob("*.md"):
        rel = md_file.relative_to(root).as_posix()
        if rel.startswith(".git/"):
            continue
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        meta = parse_simple_yaml(m.group(1))
        artifact_id = meta.get("artifact_id", "")
        if not artifact_id:
            continue
        node: dict[str, Any] = {
            "id": artifact_id,
            "type": "artifact",
            "title": meta.get("title", md_file.stem),
            "status": meta.get("status", "DRAFT"),
            "owner": meta.get("owner", ""),
            "canon": meta.get("canon", "NO"),
            "review_state": meta.get("review_state", "candidate"),
            "file_path": rel,
            "hsn_coordinate": meta.get("hsn_coordinate", ""),
            "domain": meta.get("domain", ""),
            "created": meta.get("created", ""),
        }
        nodes.append(node)
    return nodes


def load_seed_nodes(root: Path) -> list[dict[str, Any]]:
    seed_dir = root / "archive" / "synthesis" / "data"
    nodes = []
    for json_file in seed_dir.glob("*_hsn_seed.json"):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        # elements, bands, colors, notes — all have artifact_id + hsn_coordinate
        for collection_key in ("elements", "bands", "colors", "notes"):
            for item in data.get(collection_key, []):
                node: dict[str, Any] = {
                    "id": item.get("artifact_id", ""),
                    "type": item.get("type", "seed"),
                    "title": item.get("name", item.get("label", item.get("artifact_id", ""))),
                    "status": "CANDIDATE",
                    "owner": "atlaslattice",
                    "canon": "NO",
                    "review_state": item.get("review_state", "candidate"),
                    "file_path": json_file.relative_to(root).as_posix(),
                    "hsn_coordinate": item.get("hsn_coordinate", ""),
                    "domain": data.get("domain", ""),
                    "created": "2026-05-29",
                    "seed_source": item.get("source", ""),
                }
                if node["id"]:
                    nodes.append(node)
    return nodes


def build_graph(nodes: list[dict[str, Any]]) -> dict[str, Any]:
    """Build JSON-LD graph from node list."""
    node_index = {n["id"]: n for n in nodes}

    # Derive edges: artifacts in the same H-S-N cell are "co-located"
    hsn_buckets: dict[str, list[str]] = {}
    for node in nodes:
        hsn = node.get("hsn_coordinate", "")
        if hsn and HSN_RE.match(hsn):
            hsn_buckets.setdefault(hsn, []).append(node["id"])

    edges = []
    for hsn, ids in hsn_buckets.items():
        for i, src in enumerate(ids):
            for dst in ids[i + 1 :]:
                edges.append({
                    "@type": "CoLocated",
                    "source": src,
                    "target": dst,
                    "hsn_coordinate": hsn,
                })

    # Compute per-house stats
    house_counts: dict[str, int] = {}
    for node in nodes:
        hsn = node.get("hsn_coordinate", "")
        if hsn and len(hsn) >= 3:
            h = hsn[:3]
            house_counts[h] = house_counts.get(h, 0) + 1

    graph: dict[str, Any] = {
        "@context": {
            "@vocab": "https://atlaslattice.org/ontology/v0.1/",
            "hsn_coordinate": "https://atlaslattice.org/ontology/v0.1/hsn_coordinate",
            "review_state": "https://atlaslattice.org/ontology/v0.1/review_state",
            "canon": "https://atlaslattice.org/ontology/v0.1/canon",
        },
        "@type": "LatticeGraph",
        "schema_version": "v0.1",
        "generated": "2026-05-29",
        "stats": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "hsn_cells_occupied": len(hsn_buckets),
            "house_counts": house_counts,
        },
        "@graph": nodes,
        "edges": edges,
    }
    return graph


def build_viz_nodes(nodes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Lightweight node list for the D3/3D visualizer."""
    viz = []
    for node in nodes:
        hsn = node.get("hsn_coordinate", "")
        h = s = n_val = 0
        if hsn and HSN_RE.match(hsn):
            parts = hsn.split("-")
            h = int(parts[0][1:])
            s = int(parts[1][1:])
            n_val = int(parts[2][1:])
        status = node.get("status", "DRAFT")
        color = STATUS_COLOR.get(status, STATUS_COLOR.get(node.get("review_state", ""), "#6b7280"))
        viz.append({
            "id": node["id"],
            "label": node.get("title", node["id"])[:60],
            "type": node.get("type", "artifact"),
            "hsn": hsn,
            "h": h,
            "s": s,
            "n": n_val,
            "status": status,
            "review_state": node.get("review_state", "candidate"),
            "color": color,
            "domain": node.get("domain", ""),
        })
    return viz


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build Atlas Lattice knowledge graph")
    parser.add_argument("--output-dir", default="docs", help="Output directory (relative to repo root)")
    parser.add_argument("--root", default=str(ROOT), help="Repository root")
    args = parser.parse_args(argv)

    root = Path(args.root)
    out_dir = root / args.output_dir

    print("Building graph from Markdown frontmatter…")
    md_nodes = load_markdown_nodes(root)
    print(f"  {len(md_nodes)} Markdown artifacts found")

    print("Loading seed JSON nodes…")
    seed_nodes = load_seed_nodes(root)
    print(f"  {len(seed_nodes)} seed nodes loaded")

    all_nodes = md_nodes + seed_nodes
    print(f"  {len(all_nodes)} total nodes")

    graph = build_graph(all_nodes)
    viz_nodes = build_viz_nodes(all_nodes)

    out_dir.mkdir(parents=True, exist_ok=True)
    graph_path = out_dir / "lattice_graph.json"
    viz_path = out_dir / "lattice_graph_nodes.json"

    graph_path.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")
    viz_path.write_text(json.dumps(viz_nodes, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nGraph written to {graph_path.relative_to(root)}")
    print(f"Viz nodes written to {viz_path.relative_to(root)}")
    print(f"\nStats:")
    for k, v in graph["stats"].items():
        if k != "house_counts":
            print(f"  {k}: {v}")
    print("  house_counts:", graph["stats"]["house_counts"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
