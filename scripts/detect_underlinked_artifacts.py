#!/usr/bin/env python3
"""
AX-13: Under-linked and missing-link artifact detector.

Reads the lattice global index and produces a human-readable report of:
- Under-linked artifacts (0 outbound links)
- Isolated artifacts (0 outbound AND 0 inbound links)
- Artifacts with unresolved links
- Top-priority backlink candidates ranked by inbound demand

Usage:
    python scripts/detect_underlinked_artifacts.py
    python scripts/detect_underlinked_artifacts.py --repo-root . --index archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json
    python scripts/detect_underlinked_artifacts.py --top 20 --fail-on-threshold 0.30
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


EXCLUDE_DIRS = {
    "quarantine",
    ".git",
    ".pytest_cache",
    "__pycache__",
}

DEFAULT_INDEX_PATH = "archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json"
DEFAULT_REPO_ROOT = "."


def load_index(repo_root: Path, index_path: str) -> dict:
    full = repo_root / index_path
    return json.loads(full.read_text(encoding="utf-8"))


def is_excluded(path: str) -> bool:
    parts = Path(path).parts
    return any(part in EXCLUDE_DIRS for part in parts)


def analyze_links(index: dict) -> dict:
    artifacts = index.get("artifacts", [])
    markdown = [a for a in artifacts if a["path"].endswith(".md") and not is_excluded(a["path"])]

    inbound_counts: Counter[str] = Counter()
    for art in markdown:
        for target in art.get("outbound_repo_links", []):
            if target.endswith(".md"):
                inbound_counts[target] += 1

    underlinked: list[dict] = []
    isolated: list[dict] = []
    with_unresolved: list[dict] = []

    for art in markdown:
        outbound = art.get("outbound_repo_links", [])
        inbound = art.get("inbound_repo_links", [])
        unresolved = art.get("unresolved_repo_links", [])
        if not outbound:
            underlinked.append(art)
            if not inbound:
                isolated.append(art)
        if unresolved:
            with_unresolved.append(art)

    # Group under-linked by top-level directory
    by_dir: dict[str, list[str]] = {}
    for art in underlinked:
        parts = Path(art["path"]).parts
        bucket = parts[0] if len(parts) > 1 else "(root)"
        by_dir.setdefault(bucket, []).append(art["path"])

    # Backlink candidates: isolated artifacts that are referenced most by connected nodes
    # Rank by: inbound link count (higher = already somewhat known, just missing outbound)
    candidate_scores: list[tuple[str, int]] = []
    for art in underlinked:
        score = inbound_counts.get(art["path"], 0)
        candidate_scores.append((art["path"], score))
    candidate_scores.sort(key=lambda x: (-x[1], x[0]))

    return {
        "total_markdown": len(markdown),
        "underlinked": underlinked,
        "isolated": isolated,
        "with_unresolved": with_unresolved,
        "by_dir": by_dir,
        "candidate_scores": candidate_scores,
        "inbound_counts": dict(inbound_counts),
    }


def print_report(analysis: dict, top: int) -> None:
    total = analysis["total_markdown"]
    underlinked = analysis["underlinked"]
    isolated = analysis["isolated"]
    with_unresolved = analysis["with_unresolved"]
    by_dir = analysis["by_dir"]
    candidate_scores = analysis["candidate_scores"]

    pct_under = 100 * len(underlinked) / total if total else 0
    pct_isolated = 100 * len(isolated) / total if total else 0

    print("=" * 70)
    print("LATTICE UNDER-LINKED ARTIFACT REPORT  (AX-13)")
    print("=" * 70)
    print(f"Total markdown artifacts:  {total}")
    print(f"Under-linked (0 outbound): {len(underlinked)}  ({pct_under:.1f}%)")
    print(f"Isolated (0 in + 0 out):   {len(isolated)}  ({pct_isolated:.1f}%)")
    print(f"With unresolved links:     {len(with_unresolved)}")
    print()

    print("--- Under-linked by directory ---")
    for d, paths in sorted(by_dir.items(), key=lambda x: -len(x[1])):
        print(f"  {d:40s}  {len(paths):4d} artifacts")
    print()

    if with_unresolved:
        print("--- Artifacts with unresolved links (top 10) ---")
        for art in with_unresolved[:10]:
            print(f"  {art['path']}")
            for link in art.get("unresolved_repo_links", [])[:3]:
                print(f"      ↳ broken: {link}")
        print()

    print(f"--- Top {top} backlink candidates (by inbound demand) ---")
    for path, score in candidate_scores[:top]:
        label = f"inbound={score}" if score > 0 else "isolated"
        print(f"  [{label:12s}]  {path}")
    print()
    print("=" * 70)


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect under-linked artifacts in the lattice KG.")
    parser.add_argument("--repo-root", default=DEFAULT_REPO_ROOT)
    parser.add_argument("--index", default=DEFAULT_INDEX_PATH)
    parser.add_argument("--top", type=int, default=20, help="Number of top candidates to list")
    parser.add_argument(
        "--fail-on-threshold",
        type=float,
        default=None,
        metavar="RATIO",
        help="Exit 1 if under-linked ratio exceeds this threshold (0–1). Default: no threshold.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    index = load_index(repo_root, args.index)
    analysis = analyze_links(index)
    print_report(analysis, args.top)

    if args.fail_on_threshold is not None:
        total = analysis["total_markdown"]
        underlinked = len(analysis["underlinked"])
        ratio = underlinked / total if total else 0
        if ratio > args.fail_on_threshold:
            print(
                f"THRESHOLD EXCEEDED: {underlinked}/{total} = {ratio:.2%} "
                f"> {args.fail_on_threshold:.2%}"
            )
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
