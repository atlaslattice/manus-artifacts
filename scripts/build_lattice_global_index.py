#!/usr/bin/env python3
"""Build the unified Lattice global knowledge-graph index.

Crawls every markdown file in the repository, extracts YAML frontmatter,
and writes two JSONL files to the KG v0.6 output directory:
  - lattice_global_index.jsonl  — one record per artifact node
  - lattice_cross_links.jsonl   — one record per directed cross-link edge

This is the single ingestion + indexing pipeline that lands every artifact
in the same graph substrate (the "12D octopus hypercube, not a bunch of legos").
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterator


# ---------------------------------------------------------------------------
# Dimension prefix mapping (D01–D12 short labels → task ranges)
# Supports both dot-separated lowercase (governance.x.v1) and
# dash-separated uppercase (GOVERNANCE-X-001) artifact ID styles.
# ---------------------------------------------------------------------------
DIMENSION_PREFIX_MAP: dict[str, str] = {
    # lowercase dot-style
    "governance": "D01",
    "legal": "D02",
    "repo_arch": "D03",
    "docs": "D04",
    "kg_layer": "D05",
    "cicd": "D06",
    "security": "D07",
    "testing": "D08",
    "accessibility": "D09",
    "devex": "D10",
    "community": "D11",
    "operations": "D12",
    # common alternative spellings (lowercase)
    "kg": "D05",
    "spec": "D05",
    "project": "D11",
    "archive": "D03",
    # uppercase dash-style (actual repo artifact IDs)
    "governance-": "D01",   # matched via startswith below
    "sec-": "D07",
    "cicd-": "D06",
    "a11y-": "D09",
    "dx-": "D10",
    "comm-": "D11",
    "kg-": "D05",
    "doc-": "D04",
    "launch-": "D12",
    "test-": "D08",
    "legal-": "D02",
    "privacy-": "D02",
    "trust-": "D02",
}

# Prefix patterns that require startswith checks (uppercase dash style)
_STARTSWITH_PREFIXES: list[tuple[str, str]] = [
    ("GOVERNANCE", "D01"),
    ("SEC-", "D07"),
    ("SECURITY-", "D07"),
    ("CICD-", "D06"),
    ("A11Y-", "D09"),
    ("ACCESSIBILITY-", "D09"),
    ("DX-", "D10"),
    ("DEVEX-", "D10"),
    ("COMM-", "D11"),
    ("COMMUNITY-", "D11"),
    ("KG-", "D05"),
    ("DOC-", "D04"),
    ("DOCS-", "D04"),
    ("LAUNCH-", "D12"),
    ("OPS-", "D12"),
    ("OPERATIONS-", "D12"),
    ("TEST-", "D08"),
    ("TESTING-", "D08"),
    ("RELIABILITY-", "D08"),
    ("LEGAL-", "D02"),
    ("PRIVACY-", "D02"),
    ("TRUST-", "D02"),
    ("ARCH-", "D03"),
    ("REPO-", "D03"),
]

DIMENSION_LABELS: dict[str, str] = {
    "D01": "Governance & Canon",
    "D02": "Legal, Privacy & Trust",
    "D03": "Repository Architecture",
    "D04": "Documentation Excellence",
    "D05": "Knowledge Graph Layer",
    "D06": "CI/CD & Automation",
    "D07": "Security & Supply Chain",
    "D08": "Testing & Reliability",
    "D09": "Accessibility & Global Reach",
    "D10": "Developer Experience",
    "D11": "Community & Ecosystem",
    "D12": "Launch & World-Class Operations",
}

OUTPUT_DIR = Path("archive/knowledge_graph/lattice_kg/v0_6")
INDEX_FILE = OUTPUT_DIR / "lattice_global_index.jsonl"
CROSSLINKS_FILE = OUTPUT_DIR / "lattice_cross_links.jsonl"

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".github"}


# ---------------------------------------------------------------------------
# Frontmatter parser
# ---------------------------------------------------------------------------
_FM_PATTERN = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Return a flat key→value dict from YAML-like frontmatter, or empty dict."""
    m = _FM_PATTERN.match(text)
    if not m:
        return {}
    block = m.group(1)
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        k = key.strip()
        v = value.strip()
        if k and v:
            # strip inline yaml list brackets / quotes if present
            if v.startswith("[") and v.endswith("]"):
                v = v[1:-1]
            data[k] = v.strip("\"'")
    return data


def extract_cross_links_from_text(text: str, repo_root: Path, file_path: Path) -> list[str]:
    """Return list of artifact_ids referenced as relative markdown links in the file."""
    # Match [text](relative/path/to/file.md) — any relative (non-http) link
    rel_link_re = re.compile(r"\[.*?\]\(([^)]+\.md)\)")
    ids: list[str] = []
    for m in rel_link_re.finditer(text):
        href = m.group(1)
        # Skip absolute URLs and fragment-only links
        if href.startswith("http") or href.startswith("#"):
            continue
        # Resolve relative to the file's directory
        target_path = (file_path.parent / href).resolve()
        if not target_path.exists():
            continue
        try:
            target_text = target_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        fm = parse_frontmatter(target_text)
        aid = fm.get("artifact_id")
        if aid and aid not in ("<stable id>", "<string>", "null", "ALF-YYYY-NNNNN",
                               "ALF-[DOMAIN]-[YEAR]-[SEQUENCE]"):
            ids.append(aid)
    return ids


def infer_dimension_from_path(path_str: str) -> str | None:
    """Infer dimension from path heuristics when artifact_id prefix is unknown."""
    p = path_str.lower()
    # D02 legal/privacy/trust
    if any(kw in p for kw in ("pii", "redaction", "privacy", "legal", "compliance",
                               "vulnerability_disclosure", "risk_register", "retention",
                               "export_control", "license_audit", "quarterly_legal",
                               "trademark", "attribution_inventory", "sensitive_content")):
        return "D02"
    # D01 governance/canon
    if any(kw in p for kw in ("canon", "ratification", "governance", "provenance",
                               "lifecycle_state", "naming_convention", "deprecation",
                               "change_classif", "review_sla", "council_review",
                               "section_ownership")):
        return "D01"
    # D04 documentation
    if any(kw in p for kw in ("glossary", "editorial_style", "changelog", "release_notes",
                               "newcomer_faq", "executive_summar", "start_here",
                               "archive_index", "top_artifact")):
        return "D04"
    return None


def infer_dimension(artifact_id: str, path_str: str = "") -> str:
    """Infer dimension D01–D12 from artifact_id prefix, defaulting to D03."""
    if not artifact_id:
        if path_str:
            return infer_dimension_from_path(path_str) or "D03"
        return "D03"
    upper = artifact_id.upper()
    for prefix, dim in _STARTSWITH_PREFIXES:
        if upper.startswith(prefix):
            return dim
    first_part = artifact_id.split(".")[0].lower().split("-")[0]
    result = DIMENSION_PREFIX_MAP.get(first_part, None)
    if result:
        return result
    if path_str:
        return infer_dimension_from_path(path_str) or "D03"
    return "D03"


# ---------------------------------------------------------------------------
# Crawler
# ---------------------------------------------------------------------------
def iter_markdown_files(root: Path) -> Iterator[Path]:
    for path in root.rglob("*.md"):
        if any(skip in path.parts for skip in SKIP_DIRS):
            continue
        yield path


def build_index(root: Path) -> tuple[list[dict], list[dict]]:
    nodes: list[dict] = []
    edges: list[dict] = []
    seen_ids: dict[str, str] = {}  # artifact_id → first file path

    for md_path in sorted(iter_markdown_files(root)):
        rel = str(md_path.relative_to(root))
        try:
            text = md_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        fm = parse_frontmatter(text)
        artifact_id = fm.get("artifact_id") or fm.get("artifact") or ""
        if not artifact_id:
            # Generate a path-based fallback id so every file gets a node
            artifact_id = "path." + rel.replace("/", ".").replace(" ", "_").rstrip(".md")

        dimension_id = fm.get("dimension_id") or infer_dimension(artifact_id, rel)

        node: dict = {
            "artifact_id": artifact_id,
            "path": rel,
            "dimension_id": dimension_id,
            "dimension_label": DIMENSION_LABELS.get(dimension_id, dimension_id),
            "canon_status": fm.get("canon_status", "not_canon"),
            "status": fm.get("status", "candidate"),
            "lifecycle_state": fm.get("lifecycle_state", ""),
            "trust_state": fm.get("trust_state", "WORK"),
            "title": fm.get("title", md_path.stem.replace("_", " ").replace("-", " ")),
            "owner": fm.get("owner", ""),
            "last_updated": fm.get("last_updated", ""),
        }
        nodes.append(node)

        # Duplicate-ID detection (emit warning, keep first)
        if artifact_id in seen_ids:
            node["_duplicate_warning"] = f"also at {seen_ids[artifact_id]}"
        else:
            seen_ids[artifact_id] = rel

        # Cross-link edges from markdown link targets that have artifact_ids
        linked_ids = extract_cross_links_from_text(text, root, md_path)
        for target_id in linked_ids:
            if target_id != artifact_id:
                edges.append(
                    {
                        "edge_id": f"link.{artifact_id}.{target_id}",
                        "edge_type": "links_to",
                        "from_artifact_id": artifact_id,
                        "to_artifact_id": target_id,
                        "from_dimension": dimension_id,
                        "source_file": rel,
                    }
                )

    return nodes, edges


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Query surface (--query mode)
# ---------------------------------------------------------------------------
def query_mode(root: Path, query: str) -> None:
    index_path = root / INDEX_FILE
    if not index_path.exists():
        print("Index not built yet. Run without --query first.", file=sys.stderr)
        raise SystemExit(1)

    q = query.lower()
    results: list[dict] = []
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        searchable = " ".join(str(v).lower() for v in rec.values())
        if q in searchable:
            results.append(rec)

    if not results:
        print(f"No results for: {query}")
        return

    for rec in results:
        print(f"[{rec['dimension_id']}] {rec['artifact_id']}")
        print(f"  path:   {rec['path']}")
        print(f"  status: {rec.get('canon_status', '?')}")
        print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the Lattice unified global knowledge-graph index."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root directory (default: repo root).",
    )
    parser.add_argument(
        "--query",
        metavar="TERM",
        help="Query the index instead of rebuilding it.",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a dimension coverage summary after building.",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()

    if args.query:
        query_mode(root, args.query)
        return 0

    nodes, edges = build_index(root)

    write_jsonl(root / INDEX_FILE, nodes)
    write_jsonl(root / CROSSLINKS_FILE, edges)

    # Dimension coverage summary
    dim_counts: dict[str, int] = {}
    for node in nodes:
        d = node["dimension_id"]
        dim_counts[d] = dim_counts.get(d, 0) + 1

    print(
        f"Lattice global index built: {len(nodes)} nodes, {len(edges)} cross-link edges."
    )
    if args.report:
        print("\nDimension coverage:")
        for dim in sorted(DIMENSION_LABELS):
            label = DIMENSION_LABELS[dim]
            count = dim_counts.get(dim, 0)
            bar = "█" * min(count, 40)
            print(f"  {dim} {label:<35} {count:4d}  {bar}")

    missing_dims = [d for d in DIMENSION_LABELS if dim_counts.get(d, 0) == 0]
    if missing_dims:
        print(f"\nWARNING: dimensions with no nodes: {missing_dims}", file=sys.stderr)

    duplicates = [n for n in nodes if "_duplicate_warning" in n]
    if duplicates:
        print(
            f"\nWARNING: {len(duplicates)} duplicate artifact_id(s) detected.",
            file=sys.stderr,
        )
        for d in duplicates[:10]:
            print(f"  {d['artifact_id']} ({d['path']}) — {d['_duplicate_warning']}",
                  file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
