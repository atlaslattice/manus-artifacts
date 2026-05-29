#!/usr/bin/env python3
"""
ingest_elements.py — Bridge adapter: Periodic-Table-JSON → Atlas Lattice H01 nodes.

STATUS: CANDIDATE TOOL — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
UPSTREAM: Bowserinator/Periodic-Table-JSON (MIT License)
HSN_COORDINATE: H01-S08-N09

This script reads `data/elements_hsn_seed.json` and prints lattice-compatible
node records for each element.  It also optionally accepts a path to the
upstream PeriodicTableJSON.json for live ingestion.

Usage:
    python forks/periodic-table-json/bridge/ingest_elements.py
    python forks/periodic-table-json/bridge/ingest_elements.py --upstream /path/to/PeriodicTableJSON.json
    python forks/periodic-table-json/bridge/ingest_elements.py --stats
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

BRIDGE_DIR = Path(__file__).resolve().parents[1]
SEED_PATH = BRIDGE_DIR / "data/elements_hsn_seed.json"

PHASE_NODE = {
    "Solid": "N01",
    "Liquid": "N02",
    "Gas": "N03",
    "Plasma": "N04",
    "Unknown": "N08",
}


def load_seed() -> dict:
    return json.loads(SEED_PATH.read_text(encoding="utf-8"))


def ingest_upstream(upstream_path: Path) -> list[dict]:
    """
    Read a Bowserinator/Periodic-Table-JSON file and produce lattice nodes.
    Upstream format has a top-level "elements" array where each element has
    at minimum: name, symbol, number, phase, group, period, category.
    """
    raw = json.loads(upstream_path.read_text(encoding="utf-8"))
    elements = raw.get("elements", raw if isinstance(raw, list) else [])
    nodes = []
    for elem in elements:
        z = elem.get("number", 0)
        symbol = elem.get("symbol", "?")
        phase = elem.get("phase", "Unknown")
        node_code = PHASE_NODE.get(phase, "N08")
        coord = f"H01-S06-{node_code}"
        nodes.append(
            {
                "artifact_id": f"ATLAS-ELEM-{symbol.upper()}-{z:03d}",
                "node_type": "element",
                "name": elem.get("name", "?"),
                "symbol": symbol,
                "atomic_number": z,
                "standard_phase": phase,
                "group": elem.get("group"),
                "period": elem.get("period"),
                "category": elem.get("category", "?"),
                "atomic_mass": elem.get("atomic_mass"),
                "electron_config": elem.get("electron_configuration"),
                "electronegativity": elem.get("electronegativity_pauling"),
                "hsn_coordinate": coord,
                "house": "H01",
                "sphere": "S06",
                "node": node_code,
                "canon_status": "not_canon",
                "deployment_status": "not_deployable",
                "trust_state": "candidate_unverified",
                "source": "upstream: Bowserinator/Periodic-Table-JSON (MIT)",
                "lattice_notes": (
                    f"Live-ingested from upstream. "
                    f"Phase={phase} → HSN {coord}. "
                    "Periodic Table 2.0 candidate seed node."
                ),
            }
        )
    return nodes


def print_stats(elements: list[dict]) -> None:
    print(f"\n{'='*64}")
    print("  PERIODIC TABLE — H01 LATTICE SEED STATS")
    print(f"{'='*64}")
    print(f"  Total elements  : {len(elements)}")
    phase_counts = Counter(e["standard_phase"] for e in elements)
    coord_counts = Counter(e["hsn_coordinate"] for e in elements)
    print()
    print("  Phase → HSN coordinate:")
    for phase, node in PHASE_NODE.items():
        coord = f"H01-S06-{node}"
        cnt = coord_counts.get(coord, 0)
        print(f"    {phase:<10}  {coord}  →  {cnt} elements")
    print()
    cat_counts = Counter(e.get("category", "?") for e in elements)
    print("  Category distribution:")
    for cat, cnt in cat_counts.most_common():
        print(f"    {cat:<30}  {cnt}")
    print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--upstream", help="Path to upstream PeriodicTableJSON.json for live ingestion")
    parser.add_argument("--stats", action="store_true", help="Print seed statistics and exit")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args(argv)

    if args.upstream:
        upstream_path = Path(args.upstream)
        if not upstream_path.exists():
            print(f"ERROR: upstream file not found at {upstream_path}")
            return 1
        elements = ingest_upstream(upstream_path)
        print(f"Ingested {len(elements)} elements from {upstream_path}")
    else:
        seed = load_seed()
        elements = seed.get("elements", [])
        if not elements:
            print("ERROR: no elements found in seed file")
            return 1

    if args.stats:
        print_stats(elements)
        return 0

    if args.output:
        out = {
            "schema_id": "elements_hsn_seed.v1.0",
            "status": "CANDIDATE BRIDGE DATA — NOT CANON",
            "element_count": len(elements),
            "elements": elements,
        }
        Path(args.output).write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
        print(f"Written {len(elements)} elements to {args.output}")
    else:
        # Default: print first 10 as sample
        print(f"\nSample of H01 element nodes ({len(elements)} total):\n")
        for elem in elements[:10]:
            print(f"  {elem['hsn_coordinate']}  Z={elem['atomic_number']:3d}  {elem['symbol']:3s}  {elem['name']:<15}  phase={elem['standard_phase']}")
        if len(elements) > 10:
            print(f"  … and {len(elements) - 10} more. Use --stats for full breakdown.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
