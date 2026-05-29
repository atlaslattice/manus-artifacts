#!/usr/bin/env python3
"""
query_lattice.py
================
CLI query interface for the Atlas Lattice knowledge graph.

Loads docs/lattice_graph.json (built by scripts/build_lattice_graph.py)
and lets you filter + inspect nodes from the command line.

Usage examples:
    python scripts/query_lattice.py --house 1
    python scripts/query_lattice.py --house 2 --sphere 3
    python scripts/query_lattice.py --house 1 --sphere 4 --node 2
    python scripts/query_lattice.py --artifact-id ELEMENT-FE-026
    python scripts/query_lattice.py --status CANDIDATE
    python scripts/query_lattice.py --type element
    python scripts/query_lattice.py --domain H01-Elements
    python scripts/query_lattice.py --review-state reviewed
    python scripts/query_lattice.py --stats
    python scripts/query_lattice.py --list-houses
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GRAPH = ROOT / "docs" / "lattice_graph.json"

HOUSE_LABELS = {
    1: "Elements & Isotopes",
    2: "Frequency & Resonance",
    3: "Color & Harmonic Spectrum",
    4: "Acoustic Resonance",
    5: "States of Matter",
    6: "Spin & Quantum States",
    7: "Neuromorphic Principles",
    8: "Human Knowledge Domains",
    9: "Archive Artifacts",
    10: "IP Lineage",
    11: "Review & Governance States",
    12: "Synthesis & Meta",
}


def load_graph(path: Path) -> dict:
    if not path.exists():
        print(f"ERROR: Graph file not found: {path}", file=sys.stderr)
        print("Run: python scripts/build_lattice_graph.py", file=sys.stderr)
        sys.exit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def hsn_match(node: dict, h: int | None, s: int | None, n: int | None) -> bool:
    hsn = node.get("hsn_coordinate") or node.get("hsn", "")
    if not hsn:
        return False
    parts = hsn.split("-")
    if len(parts) != 3:
        return False
    try:
        nh, ns, nn = int(parts[0][1:]), int(parts[1][1:]), int(parts[2][1:])
    except (ValueError, IndexError):
        return False
    if h is not None and nh != h:
        return False
    if s is not None and ns != s:
        return False
    if n is not None and nn != n:
        return False
    return True


def filter_nodes(nodes: list[dict], args: argparse.Namespace) -> list[dict]:
    results = nodes
    if args.house is not None or args.sphere is not None or args.node is not None:
        results = [nd for nd in results if hsn_match(nd, args.house, args.sphere, args.node)]
    if args.artifact_id:
        results = [nd for nd in results if nd.get("id", "") == args.artifact_id]
    if args.status:
        results = [nd for nd in results if nd.get("status", "").upper() == args.status.upper()]
    if args.type:
        results = [nd for nd in results if nd.get("type", "") == args.type]
    if args.domain:
        results = [nd for nd in results if args.domain.lower() in nd.get("domain", "").lower()]
    if args.review_state:
        results = [nd for nd in results if nd.get("review_state", "") == args.review_state]
    return results


def print_node(node: dict, verbose: bool = False) -> None:
    hsn = node.get("hsn_coordinate") or node.get("hsn", "(no coord)")
    status = node.get("status", "")
    review = node.get("review_state", "")
    title = node.get("title", node.get("id", ""))
    print(f"  [{hsn}] {node.get('id','')}  —  {title}")
    if verbose:
        print(f"    type:         {node.get('type','')}")
        print(f"    status:       {status}")
        print(f"    review_state: {review}")
        print(f"    owner:        {node.get('owner','')}")
        print(f"    canon:        {node.get('canon','')}")
        print(f"    domain:       {node.get('domain','')}")
        if node.get("file_path"):
            print(f"    file:         {node['file_path']}")
        if node.get("seed_source"):
            print(f"    source:       {node['seed_source']}")
        print()


def cmd_stats(graph: dict) -> None:
    stats = graph.get("stats", {})
    print("\n=== Atlas Lattice Graph Stats ===")
    print(f"  Total nodes:        {stats.get('node_count', '?')}")
    print(f"  Total edges:        {stats.get('edge_count', '?')}")
    print(f"  H-S-N cells used:   {stats.get('hsn_cells_occupied', '?')} / 1728")
    print(f"  Generated:          {graph.get('generated', '?')}")
    hc = stats.get("house_counts", {})
    if hc:
        print("\n  Per-House node counts:")
        for h_key in sorted(hc.keys()):
            h_num = int(h_key[1:]) if h_key.startswith("H") else 0
            label = HOUSE_LABELS.get(h_num, "")
            print(f"    {h_key}  {hc[h_key]:>5}  {label}")
    print()


def cmd_list_houses() -> None:
    print("\n=== Atlas Lattice — 12 Houses (H-S-N Axes) ===")
    for h, label in HOUSE_LABELS.items():
        print(f"  H{h:02d}  {label}")
    print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Query the Atlas Lattice knowledge graph",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--graph", default=str(DEFAULT_GRAPH), help="Path to lattice_graph.json")
    parser.add_argument("--house", "-H", type=int, metavar="N", help="Filter by House (1-12)")
    parser.add_argument("--sphere", "-S", type=int, metavar="N", help="Filter by Sphere (1-12)")
    parser.add_argument("--node", "-N", type=int, metavar="N", help="Filter by Node (1-12)")
    parser.add_argument("--artifact-id", metavar="ID", help="Filter by exact artifact_id")
    parser.add_argument("--status", metavar="STATUS", help="Filter by status (CANDIDATE, CANONICAL, etc.)")
    parser.add_argument("--type", metavar="TYPE", help="Filter by node type (element, artifact, etc.)")
    parser.add_argument("--domain", metavar="DOMAIN", help="Filter by domain string (partial match)")
    parser.add_argument("--review-state", metavar="STATE", help="Filter by review_state")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show full node details")
    parser.add_argument("--stats", action="store_true", help="Show graph statistics")
    parser.add_argument("--list-houses", action="store_true", help="List the 12 Houses")
    parser.add_argument("--limit", type=int, default=200, help="Max results to show (default 200)")
    args = parser.parse_args(argv)

    if args.list_houses:
        cmd_list_houses()
        return 0

    graph = load_graph(Path(args.graph))

    if args.stats:
        cmd_stats(graph)
        return 0

    nodes = graph.get("@graph", [])
    results = filter_nodes(nodes, args)

    if not results:
        print("No nodes match the given filters.")
        return 0

    # Build header
    filters = []
    if args.house is not None:
        filters.append(f"H{args.house:02d}")
    if args.sphere is not None:
        filters.append(f"S{args.sphere:02d}")
    if args.node is not None:
        filters.append(f"N{args.node:02d}")
    if args.artifact_id:
        filters.append(f"id={args.artifact_id}")
    if args.status:
        filters.append(f"status={args.status}")
    if args.type:
        filters.append(f"type={args.type}")
    if args.domain:
        filters.append(f"domain~{args.domain}")
    if args.review_state:
        filters.append(f"review_state={args.review_state}")

    label = " / ".join(filters) if filters else "all"
    shown = results[: args.limit]
    print(f"\n=== Query: {label} — {len(results)} result(s) ===\n")
    for node in shown:
        print_node(node, verbose=args.verbose)
    if len(results) > args.limit:
        print(f"\n  … {len(results) - args.limit} more (use --limit to see more)")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
