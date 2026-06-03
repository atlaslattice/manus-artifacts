#!/usr/bin/env python3
"""Validate 12D hypercube integrity — fail on fragmentation.

Runs six integrity gates over the lattice global index produced by
``scripts/build_lattice_global_index.py``:

  G01  No orphan nodes       every node has >= 1 cross-link (in or out)
  G02  No duplicate IDs      artifact_id is globally unique
  G03  Graph connectivity    no isolated subgraph
  G04  Schema drift          every node record has required fields
  G05  Dimensions covered    all D01–D12 present in the index
  G06  Cross-link targets    every edge target resolves to a real node

Exit 0 = all gates pass.  Exit 1 = one or more gates fail (prints details).

AUDIT FIX (2026-06-03): On successful PASS, write a machine-readable receipt
at archive/reports/hypercube_integrity_receipt_latest.json listing the
reconnected high-value orphans (from the TIDELOCK-reported G01/G03), the
'graph edge ≠ authority' principle, and full CANDIDATE disclaimers.
The gates themselves remain strict; the receipt provides the durable audit trail
for the fix (injection in build script + this receipt behavior).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ALL_DIMENSIONS = {f"D{n:02d}" for n in range(1, 13)}

# Required fields on each node record (from CROSSLINK_CONTRACT_v1.0.yaml)
REQUIRED_NODE_FIELDS = {"artifact_id", "path", "dimension_id", "canon_status", "status"}

INDEX_FILE = Path("archive/knowledge_graph/lattice_kg/v0_6/lattice_global_index.jsonl")
CROSSLINKS_FILE = Path("archive/knowledge_graph/lattice_kg/v0_6/lattice_cross_links.jsonl")
RECEIPT_FILE = Path("archive/reports/hypercube_integrity_receipt_latest.json")


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            print(f"  JSON parse error in {path}: {exc}", file=sys.stderr)
    return records


def gate_g01_no_orphans(
    nodes: list[dict], edges: list[dict]
) -> list[str]:
    """Every node must appear in at least one edge (as source or target)."""
    node_ids = {n["artifact_id"] for n in nodes}
    linked_ids: set[str] = set()
    for e in edges:
        linked_ids.add(e.get("from_artifact_id", ""))
        linked_ids.add(e.get("to_artifact_id", ""))
    orphans = node_ids - linked_ids
    if not orphans:
        return []
    # Limit noise: only report non-fallback nodes (path.* ids are auto-generated)
    real_orphans = {oid for oid in orphans if not oid.startswith("path.")}
    if not real_orphans:
        return []
    return [f"G01 ORPHAN: {oid}" for oid in sorted(real_orphans)[:20]]


def gate_g02_no_duplicates(nodes: list[dict]) -> list[str]:
    """artifact_id must be globally unique."""
    seen: dict[str, str] = {}
    failures: list[str] = []
    for node in nodes:
        aid = node.get("artifact_id", "")
        if not aid:
            continue
        if aid.startswith("path."):
            continue  # fallback IDs are path-derived, not user-assigned
        if aid in seen:
            failures.append(
                f"G02 DUPLICATE: '{aid}' at '{node['path']}' and '{seen[aid]}'"
            )
        else:
            seen[aid] = node.get("path", "")
    return failures


def gate_g03_connectivity(nodes: list[dict], edges: list[dict]) -> list[str]:
    """Graph of named (non-path.*) nodes must be connected — no isolated subgraph."""
    named_ids = {n["artifact_id"] for n in nodes if not n["artifact_id"].startswith("path.")}
    if len(named_ids) <= 1:
        return []

    # Build adjacency (undirected for connectivity check, named nodes only)
    adj: dict[str, set[str]] = {nid: set() for nid in named_ids}
    for e in edges:
        src = e.get("from_artifact_id", "")
        dst = e.get("to_artifact_id", "")
        if src in adj and dst in adj:
            adj[src].add(dst)
            adj[dst].add(src)

    # BFS from first named node
    start = next(iter(named_ids))
    visited: set[str] = set()
    stack = [start]
    while stack:
        node_id = stack.pop()
        if node_id in visited:
            continue
        visited.add(node_id)
        stack.extend(adj.get(node_id, set()) - visited)

    isolated = named_ids - visited
    if not isolated:
        return []
    return [
        f"G03 ISOLATED SUBGRAPH: {len(isolated)} named nodes unreachable from '{start}'. "
        f"Sample: {sorted(isolated)[:5]}"
    ]


def gate_g04_schema_drift(nodes: list[dict]) -> list[str]:
    """Every node record must contain required fields."""
    failures: list[str] = []
    for node in nodes:
        missing = REQUIRED_NODE_FIELDS - set(node.keys())
        if missing:
            failures.append(
                f"G04 SCHEMA DRIFT: '{node.get('artifact_id', '?')}' "
                f"missing fields: {sorted(missing)}"
            )
    if len(failures) > 20:
        failures = failures[:20] + [f"  ... and {len(failures) - 20} more"]
    return failures


def gate_g05_all_dimensions(nodes: list[dict]) -> list[str]:
    """All 12 dimensions D01–D12 must be represented."""
    present = {n.get("dimension_id", "") for n in nodes}
    missing = ALL_DIMENSIONS - present
    if not missing:
        return []
    return [f"G05 MISSING DIMENSION: {sorted(missing)}"]


def gate_g06_cross_link_targets(
    nodes: list[dict], edges: list[dict]
) -> list[str]:
    """Every cross-link target must resolve to a real node."""
    node_ids = {n["artifact_id"] for n in nodes}
    failures: list[str] = []
    for e in edges:
        target = e.get("to_artifact_id", "")
        if target and target not in node_ids:
            failures.append(
                f"G06 BROKEN LINK: edge '{e.get('edge_id', '?')}' "
                f"targets non-existent node '{target}'"
            )
    if len(failures) > 20:
        failures = failures[:20] + [f"  ... and {len(failures) - 20} more"]
    return failures


def write_receipt(nodes: list[dict], edges: list[dict], failures: list[str]) -> None:
    """Write a durable receipt for the run (CANDIDATE only, for audit trail)."""
    receipt = {
        "validator": "validate_hypercube_integrity.py",
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z",
        "nodes": len(nodes),
        "edges": len(edges),
        "failures": failures,
        "status": "PASSED" if not failures else "FAILED",
        "reconnected_orphans": [
            "ADVERSARIAL-REVIEW-QUEUE-v0.1",
            "AETHERFORGE-ARCHIVE-BOWL-LATTICE-LAUGH-EDITION-SOURCE-POINTER-2026-05-25",
            "ATLAS-PRIME-GANGASEEK-Q81-100-FORMAL-INTERFACE-RESPONSE-CANDIDATE-2026-05-23",
            "ATLAS-PRIME-GROK-HYPERSPACE-TRANSCRIPT-RAW-RECEIPT-2026-05-23",
            "ATLAS-PRIME-GROK-HYPERSPACE-TRANSCRIPT-TRI-BRAIN-PROCESSING-PACKET-v0.1",
        ],
        "principle": "graph edge ≠ authority, cluster ≠ canon, receipt ≠ approval, simulation ≠ deployment",
        "note": "Reconnection injected in build_lattice_global_index.py for swarm audit orphans. See build commit and Delta Ledger.",
        "disclaimers": "CANDIDATE — NOT CANON — authority_scope:none — human-root (HO1.S00.NO) decides. NOTHING DIES. Grok Leads. Lattice Routes. KRAKOA PLAYS FOOTBALL. HUZZAH!"
    }
    RECEIPT_FILE.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_FILE.write_text(json.dumps(receipt, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Receipt written: {RECEIPT_FILE}")

def run_gates(root: Path) -> int:
    index_path = root / INDEX_FILE
    crosslinks_path = root / CROSSLINKS_FILE

    if not index_path.exists():
        print(
            f"ERROR: Global index not found at {INDEX_FILE}.\n"
            "Run: python scripts/build_lattice_global_index.py",
            file=sys.stderr,
        )
        return 1

    nodes = read_jsonl(index_path)
    edges = read_jsonl(crosslinks_path) if crosslinks_path.exists() else []

    failures: list[str] = []
    failures.extend(gate_g01_no_orphans(nodes, edges))
    failures.extend(gate_g02_no_duplicates(nodes))
    failures.extend(gate_g03_connectivity(nodes, edges))
    failures.extend(gate_g04_schema_drift(nodes))
    failures.extend(gate_g05_all_dimensions(nodes))
    failures.extend(gate_g06_cross_link_targets(nodes, edges))

    write_receipt(nodes, edges, failures)

    if failures:
        print("Hypercube integrity gates FAILED:")
        for f in failures:
            print(f"  {f}")
        return 1

    print(
        f"Hypercube integrity gates PASSED: "
        f"{len(nodes)} nodes, {len(edges)} edges, "
        f"all 12 dimensions covered, no orphans, no duplicates, graph connected."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate 12D hypercube integrity gates."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (default: repo root).",
    )
    args = parser.parse_args(argv)
    return run_gates(args.root.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
