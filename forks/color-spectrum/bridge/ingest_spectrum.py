#!/usr/bin/env python3
"""
ingest_spectrum.py — Bridge adapter: color/frequency spectrum → Atlas Lattice H04 nodes.

STATUS: CANDIDATE TOOL — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
HSN_COORDINATE: H04-S08-N09

Seeds the Rainbow Yin-Yang layer of the lattice with spectral band nodes and
chromatic harmonic nodes.  Riemann S is the candidate operator for spectral
structure across H02-H03-H04.

Usage:
    python forks/color-spectrum/bridge/ingest_spectrum.py
    python forks/color-spectrum/bridge/ingest_spectrum.py --stats
    python forks/color-spectrum/bridge/ingest_spectrum.py --filter-type band
    python forks/color-spectrum/bridge/ingest_spectrum.py --filter-node N06
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

BRIDGE_DIR = Path(__file__).resolve().parents[1]
SEED_PATH = BRIDGE_DIR / "data/spectrum_hsn_seed.json"


def load_seed() -> dict:
    return json.loads(SEED_PATH.read_text(encoding="utf-8"))


def print_stats(nodes: list[dict]) -> None:
    print(f"\n{'='*64}")
    print("  COLOR/FREQUENCY SPECTRUM — H04 LATTICE SEED STATS")
    print(f"{'='*64}")
    print(f"  Total nodes     : {len(nodes)}")
    type_counts = Counter(n["node_type"] for n in nodes)
    coord_counts = Counter(n["hsn_coordinate"] for n in nodes)
    polarity_counts = Counter(n.get("yin_yang_polarity", "n/a") for n in nodes)
    print()
    print("  Node types:")
    for t, c in type_counts.most_common():
        print(f"    {t:<20}  {c}")
    print()
    print("  Coordinate distribution:")
    for coord in sorted(coord_counts.keys()):
        cnt = coord_counts[coord]
        n_code = coord.split("-")[2]
        bar = "█" * cnt
        print(f"    {coord}  {bar} ({cnt})")
    print()
    print("  Yin-Yang polarity:")
    for p, c in polarity_counts.most_common():
        print(f"    {p:<10}  {c}")

    # Riemann S weights
    band_nodes = [n for n in nodes if n.get("node_type") == "spectral_band"]
    if band_nodes:
        print()
        print("  Riemann S weights (spectral bands, ordered by frequency):")
        for n in band_nodes:
            w = n.get("riemann_s_weight", "?")
            freq = n.get("frequency_range_THz", "?")
            color = n.get("hex_color_center", "")
            print(f"    {n['name']:<15}  S={w:<5}  {freq}  {color}")
    print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stats", action="store_true", help="Print stats and exit")
    parser.add_argument("--filter-type", help="Filter by node_type (band|note)")
    parser.add_argument("--filter-node", help="Filter by Node code (e.g. N06)")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args(argv)

    seed = load_seed()
    nodes = seed.get("nodes", [])

    if args.filter_type:
        keyword = args.filter_type
        nodes = [n for n in nodes if keyword in n.get("node_type", "")]
    if args.filter_node:
        nodes = [n for n in nodes if n.get("hsn_coordinate", "").endswith(f"-{args.filter_node}")]

    if args.stats:
        print_stats(seed.get("nodes", []))
        return 0

    if args.output:
        out = {
            "schema_id": "spectrum_hsn_seed.v1.0",
            "status": "CANDIDATE BRIDGE DATA — NOT CANON",
            "node_count": len(nodes),
            "nodes": nodes,
        }
        Path(args.output).write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
        print(f"Written {len(nodes)} nodes to {args.output}")
    else:
        print(f"\nH04 Spectrum nodes ({len(nodes)} total):\n")
        for node in nodes:
            coord = node["hsn_coordinate"]
            name = node["name"]
            ntype = node["node_type"]
            freq = node.get("frequency_range_THz") or f"{node.get('frequency_hz','?')} Hz"
            color = node.get("hex_color_center") or node.get("hex_color_harmonic", "")
            print(f"  {coord}  {name:<20}  [{ntype}]  {freq}  {color}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
