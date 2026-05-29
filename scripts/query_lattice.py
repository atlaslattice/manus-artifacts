#!/usr/bin/env python3
"""
query_lattice.py — Address-first knowledge graph query for the Atlas Lattice.

Usage:
  python scripts/query_lattice.py H04-S09-N02
  python scripts/query_lattice.py --house H04
  python scripts/query_lattice.py --sphere S09
  python scripts/query_lattice.py --node N02
  python scripts/query_lattice.py --stats
  python scripts/query_lattice.py --list-houses
  python scripts/query_lattice.py --list-all-coords

STATUS: CANDIDATE TOOL — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none

Returns all artifacts at the given H-S-N coordinate, their edges, and
their review state.  This is the moment the repo becomes actually navigable.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json"
ONTOLOGY_PATH = ROOT / "archive/knowledge_graph/lattice_kg/v0_5/HSN_AXIS_DEFINITIONS_v1.0.yaml"

HSN_RE = re.compile(r"^H(0[1-9]|1[0-2])-S(0[1-9]|1[0-2])-N(0[1-9]|1[0-2])$")


def _load_index() -> dict:
    if not INDEX_PATH.exists():
        sys.exit(f"ERROR: Index not found at {INDEX_PATH}\nRun: python scripts/build_lattice_global_index.py --repo-root .")
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def _parse_yaml_labels(text: str) -> dict[str, dict]:
    """Minimal YAML parser to extract H/S/N labels from the ontology file.
    Returns {code: {"label": ..., "definition": ...}} for each axis entry.
    """
    labels: dict[str, dict] = {}
    current_code: str | None = None
    current_label: str | None = None
    current_def_lines: list[str] = []
    in_definition = False

    for line in text.splitlines():
        # Match axis entry like "  H01:" or "  S01:" or "  N01:"
        code_match = re.match(r"^\s{2}(H\d{2}|S\d{2}|N\d{2}):\s*$", line)
        if code_match:
            if current_code:
                labels[current_code] = {
                    "label": current_label or current_code,
                    "definition": " ".join(current_def_lines).strip(),
                }
            current_code = code_match.group(1)
            current_label = None
            current_def_lines = []
            in_definition = False
            continue

        if current_code:
            label_match = re.match(r'^\s{4}label:\s+"?([^"]+)"?\s*$', line)
            if label_match:
                current_label = label_match.group(1).strip()
                continue

            def_start = re.match(r"^\s{4}definition:\s*>-\s*$", line)
            if def_start:
                in_definition = True
                continue

            if in_definition:
                # continuation lines are indented ≥ 6 spaces
                stripped = line.lstrip()
                if line.startswith("      ") or line.startswith("\t"):
                    current_def_lines.append(stripped)
                elif stripped and not line.startswith("    ") and not line.startswith("  "):
                    in_definition = False
                elif line.startswith("    ") and not line.startswith("      "):
                    # new field under same axis
                    in_definition = False

    if current_code:
        labels[current_code] = {
            "label": current_label or current_code,
            "definition": " ".join(current_def_lines).strip(),
        }
    return labels


def _ontology_labels() -> dict[str, dict]:
    if not ONTOLOGY_PATH.exists():
        return {}
    return _parse_yaml_labels(ONTOLOGY_PATH.read_text(encoding="utf-8"))


def _format_artifact(art: dict, verbose: bool = False) -> str:
    coord = art.get("hsn_coordinate", "unknown")
    path = art["path"]
    trust = art.get("trust_state", "?")
    canon = art.get("canon_status", "?")
    out_links = art.get("outbound_repo_links", [])
    in_links = art.get("inbound_repo_links", [])
    lines = [
        f"  {coord}  {path}",
        f"    trust={trust}  canon={canon}  out_edges={len(out_links)}  in_edges={len(in_links)}",
    ]
    if verbose:
        if out_links:
            lines.append("    → " + ", ".join(out_links[:5]) + ("…" if len(out_links) > 5 else ""))
        if in_links:
            lines.append("    ← " + ", ".join(in_links[:5]) + ("…" if len(in_links) > 5 else ""))
    return "\n".join(lines)


def cmd_query(args: argparse.Namespace) -> int:
    """Query by full coordinate or axis filter."""
    index = _load_index()
    artifacts = index.get("artifacts", [])
    labels = _ontology_labels()

    coord = getattr(args, "coordinate", None)
    house = getattr(args, "house", None)
    sphere = getattr(args, "sphere", None)
    node = getattr(args, "node", None)

    # Validate coordinate format
    if coord:
        if not HSN_RE.match(coord):
            sys.exit(f"ERROR: Invalid coordinate '{coord}'. Expected format: H##-S##-N## (e.g. H04-S09-N02)")
        h, s, n = coord.split("-")
        house, sphere, node = h, s, n

    # Filter
    results = []
    for art in artifacts:
        art_coord = art.get("hsn_coordinate", "")
        if not art_coord:
            continue
        parts = art_coord.split("-")
        if len(parts) != 3:
            continue
        ah, as_, an = parts
        if house and ah != house:
            continue
        if sphere and as_ != sphere:
            continue
        if node and an != node:
            continue
        results.append(art)

    # Build display
    if coord:
        h_info = labels.get(house, {})
        s_info = labels.get(sphere, {})
        n_info = labels.get(node, {})
        print(f"\n{'='*72}")
        print(f"  LATTICE QUERY: {coord}")
        print(f"  H={house} {h_info.get('label','?')}  |  S={sphere} {s_info.get('label','?')}  |  N={node} {n_info.get('label','?')}")
        print(f"  {len(results)} artifact(s) found")
        print(f"{'='*72}")
        if h_info.get("definition"):
            print(f"\n  House: {h_info['definition'][:120]}…")
    else:
        filters = []
        if house:
            filters.append(f"H={house} {labels.get(house,{}).get('label','')}")
        if sphere:
            filters.append(f"S={sphere} {labels.get(sphere,{}).get('label','')}")
        if node:
            filters.append(f"N={node} {labels.get(node,{}).get('label','')}")
        print(f"\n{'='*72}")
        print(f"  LATTICE QUERY: {' | '.join(filters) or 'all'}")
        print(f"  {len(results)} artifact(s) found")
        print(f"{'='*72}")

    if not results:
        print("\n  No artifacts found at this coordinate.")
        print("  (Run `python scripts/build_lattice_global_index.py --repo-root .` to refresh the index.)")
        return 0

    print()
    for art in results[:50]:
        print(_format_artifact(art, verbose=getattr(args, "verbose", False)))
        print()
    if len(results) > 50:
        print(f"  … and {len(results) - 50} more. Use --verbose or a narrower filter.")

    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    """Print coverage statistics."""
    index = _load_index()
    artifacts = index.get("artifacts", [])
    coverage = index.get("hsn_coverage", {})
    labels = _ontology_labels()

    from collections import Counter
    house_counts: Counter = Counter()
    sphere_counts: Counter = Counter()
    coord_counts: Counter = Counter()
    orphan_count = 0

    for art in artifacts:
        coord = art.get("hsn_coordinate", "")
        if coord and HSN_RE.match(coord):
            h, s, _n = coord.split("-")
            house_counts[h] += 1
            sphere_counts[s] += 1
            coord_counts[coord] += 1
        else:
            orphan_count += 1

        out = art.get("outbound_repo_links", [])
        in_ = art.get("inbound_repo_links", [])
        if not out and not in_:
            orphan_count += 1 if not coord else 0  # already counted above if no coord

    # Recompute orphan count (zero edges artifacts)
    orphans = [a for a in artifacts if not a.get("outbound_repo_links") and not a.get("inbound_repo_links")]

    print(f"\n{'='*72}")
    print("  STATE OF THE LATTICE — HSN COVERAGE STATS")
    print(f"{'='*72}")
    print(f"  Total artifacts : {coverage.get('total_artifacts', len(artifacts))}")
    print(f"  HSN assigned    : {coverage.get('hsn_assigned_total', '?')} ({coverage.get('coverage_pct', '?')}%)")
    print(f"  Non-default HSN : {coverage.get('hsn_non_default_assigned', '?')}")
    print(f"  Zero-edge nodes : {len(orphans)}")
    print()

    print("  House distribution (top 12):")
    for code, count in house_counts.most_common(12):
        label = labels.get(code, {}).get("label", "?")
        bar = "█" * min(count // 10, 40)
        print(f"    {code}  {label:<28} {count:>5}  {bar}")

    print()
    print("  Sphere distribution:")
    for code in [f"S{i:02d}" for i in range(1, 13)]:
        count = sphere_counts.get(code, 0)
        label = labels.get(code, {}).get("label", "?")
        bar = "█" * min(count // 10, 40)
        print(f"    {code}  {label:<28} {count:>5}  {bar}")

    print()
    print(f"  Most populated coordinates (top 10):")
    for coord, count in coord_counts.most_common(10):
        h, s, n = coord.split("-")
        h_label = labels.get(h, {}).get("label", "?")
        s_label = labels.get(s, {}).get("label", "?")
        print(f"    {coord}  {h_label} / {s_label}  →  {count} artifacts")

    print()
    link_health = index.get("link_health", {})
    print("  Link health:")
    print(f"    Markdown total         : {link_health.get('markdown_artifacts_total','?')}")
    print(f"    Root-reachable         : {link_health.get('root_reachable_markdown_artifacts','?')}")
    print(f"    Isolated (zero edges)  : {link_health.get('isolated_markdown_artifacts','?')}")
    print(f"    Unresolved links       : {link_health.get('unresolved_repo_links','?')}")
    print()

    return 0


def cmd_list_houses(args: argparse.Namespace) -> int:
    labels = _ontology_labels()
    print(f"\n{'='*72}")
    print("  LATTICE HOUSES (H01–H12)")
    print(f"{'='*72}\n")
    for i in range(1, 13):
        code = f"H{i:02d}"
        info = labels.get(code, {})
        print(f"  {code}  {info.get('label', '?')}")
        defn = info.get("definition", "")
        if defn:
            print(f"       {defn[:100]}…" if len(defn) > 100 else f"       {defn}")
        print()
    return 0


def cmd_list_all_coords(args: argparse.Namespace) -> int:
    """Print all distinct H-S-N coordinates present in the index."""
    index = _load_index()
    artifacts = index.get("artifacts", [])
    labels = _ontology_labels()

    from collections import Counter
    counts: Counter = Counter()
    for art in artifacts:
        coord = art.get("hsn_coordinate", "")
        if coord and HSN_RE.match(coord):
            counts[coord] += 1

    print(f"\n{'='*72}")
    print(f"  POPULATED H-S-N COORDINATES ({len(counts)} distinct cells of 1728)")
    print(f"{'='*72}\n")
    for coord in sorted(counts.keys()):
        h, s, n = coord.split("-")
        h_label = labels.get(h, {}).get("label", "")
        s_label = labels.get(s, {}).get("label", "")
        n_label = labels.get(n, {}).get("label", "")
        cnt = counts[coord]
        print(f"  {coord}  [{h_label} / {s_label} / {n_label}]  →  {cnt}")

    print(f"\n  Unpopulated cells: {1728 - len(counts)} of 1728")
    return 0


def main(argv: list[str] | None = None) -> int:
    global INDEX_PATH  # noqa: PLW0603
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Default positional: query by full coordinate
    parser.add_argument(
        "coordinate",
        nargs="?",
        help="Full H-S-N coordinate to query (e.g. H04-S09-N02)",
    )
    parser.add_argument("--house", help="Filter by House code (e.g. H04)")
    parser.add_argument("--sphere", help="Filter by Sphere code (e.g. S09)")
    parser.add_argument("--node", help="Filter by Node code (e.g. N02)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show edge detail")
    parser.add_argument("--stats", action="store_true", help="Print coverage statistics")
    parser.add_argument("--list-houses", action="store_true", help="List all Houses with definitions")
    parser.add_argument("--list-all-coords", action="store_true", help="List all populated coordinates")
    parser.add_argument(
        "--index",
        default=str(INDEX_PATH),
        help="Path to lattice_global_index.v0.1.json",
    )

    args = parser.parse_args(argv)

    # Override index path if provided
    INDEX_PATH = Path(args.index)

    if args.stats:
        return cmd_stats(args)
    if args.list_houses:
        return cmd_list_houses(args)
    if getattr(args, "list_all_coords", False):
        return cmd_list_all_coords(args)
    if args.coordinate or args.house or args.sphere or args.node:
        return cmd_query(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
