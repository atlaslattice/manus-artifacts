#!/usr/bin/env python3
"""
build_lattice_global_index.py

Scans the ENTIRE repository and emits docs/LATTICE_GLOBAL_INDEX.md —
a machine-readable table of every markdown artifact with detected
metadata fields, domain classification, and source_system tagging.

Coverage: all .md files in the repo (full-repo scan, not just 6 subdirs).
This is the pre-synthesis comprehensive index required before merging
fragmented GitHub repos, Notion, and Drive sources.

The index is regenerated on every CI push to main so it stays current.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "docs" / "LATTICE_GLOBAL_INDEX.md"

# Directories to skip entirely
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

STATUS_RE = re.compile(r"STATUS:\s*(.+)", re.IGNORECASE)
HEADING_RE = re.compile(r"^#\s+(.+)", re.MULTILINE)
SOURCE_RE = re.compile(r"source_system:\s*(.+)", re.IGNORECASE)

# Domain mapping: top-level (or two-level) directory → human label
DOMAIN_MAP: dict[str, str] = {
    "archive/boot": "boot-infrastructure",
    "archive/spec": "spec-vault",
    "archive/architecture": "architecture",
    "archive/assessments": "assessments",
    "archive/build": "build-ops",
    "archive/chatlogs": "chatlogs",
    "archive/culture": "culture",
    "archive/deployments": "deployments",
    "archive/forks": "forks",
    "archive/governance": "governance",
    "archive/integrations": "integrations",
    "archive/ops": "ops",
    "archive/play": "play",
    "archive/provenance": "provenance",
    "archive/simulation": "simulation",
    "archive/stress-tests": "stress-tests",
    "archive/synthesis": "synthesis",
    "archives": "janus-archives",
    "aluminum-os": "aluminum-os",
    "aluminum-os-core": "aluminum-os-core",
    "bazinga": "bazinga",
    "codebases/aluminum-os": "codebase-aluminum-os",
    "codebases/atlas-lattice": "codebase-atlas-lattice",
    "codebases/atlas-vault": "codebase-atlas-vault",
    "codebases/colab-notebooks": "codebase-colab",
    "codebases/data-pipeline": "codebase-data-pipeline",
    "codebases/email-processing": "codebase-email",
    "codebases/free-bank": "codebase-free-bank",
    "codebases/other": "codebase-other",
    "codebases/project-symbiote": "codebase-symbiote",
    "codebases/saas-killer": "codebase-saas-killer",
    "codebases/sheldonbrain": "codebase-sheldonbrain",
    "codebases/snrs": "codebase-snrs",
    "codebases/sovereign-oracle": "codebase-sovereign-oracle",
    "codebases/uws": "codebase-uws",
    "council": "council",
    "council-reviews": "council-reviews",
    "docs": "docs",
    "health": "health",
    "manus-vault": "manus-vault",
    "projects": "projects",
    "reference_impl": "reference-impl",
    "research": "research",
    "schemas": "schemas",
    "sheldonbrain": "sheldonbrain",
    "about": "about",
    ".github": "github-meta",
    "tests": "tests",
    "fixtures": "fixtures",
}

# Source system inference: when a file came from an external origin
SOURCE_SYSTEM_HINTS: dict[str, str] = {
    "codebases/sheldonbrain": "github:sheldonbrain",
    "codebases/snrs": "github:snrs",
    "codebases/uws": "github:uws",
    "codebases/aluminum-os": "github:aluminum-os",
    "codebases/atlas-lattice": "github:atlas-lattice",
    "codebases/free-bank": "github:free-bank",
    "codebases/other": "notion-export",
    "manus-vault": "manus-agent",
    "archive/chatlogs": "chatlog-export",
    "research/intelligence-sweeps": "research-sweep",
}


def domain_for(path: Path) -> str:
    """Return the domain label for a given file path."""
    rel = path.relative_to(REPO_ROOT)
    parts = rel.parts
    # Try two-level match first
    if len(parts) >= 2:
        two = f"{parts[0]}/{parts[1]}"
        if two in DOMAIN_MAP:
            return DOMAIN_MAP[two]
    # Try one-level match
    if parts[0] in DOMAIN_MAP:
        return DOMAIN_MAP[parts[0]]
    # Root-level file
    if len(parts) == 1:
        return "root"
    # Fallback to first path component
    return parts[0]


def source_system_for(path: Path, declared: str | None) -> str:
    """Infer source_system if not declared in the file."""
    if declared:
        return declared
    rel = str(path.relative_to(REPO_ROOT))
    for prefix, system in SOURCE_SYSTEM_HINTS.items():
        if rel.startswith(prefix):
            return system
    return "github:manus-artifacts"


def extract_meta(f: Path) -> dict:
    text = f.read_text(encoding="utf-8", errors="replace")
    header = "\n".join(text.splitlines()[:60])

    status_m = STATUS_RE.search(header)
    heading_m = HEADING_RE.search(text)
    source_m = SOURCE_RE.search(header)

    declared_source = source_m.group(1).strip() if source_m else None

    return {
        "path": str(f.relative_to(REPO_ROOT)),
        "title": heading_m.group(1).strip() if heading_m else f.stem,
        "status": status_m.group(1).strip() if status_m else "unknown",
        "domain": domain_for(f),
        "source_system": source_system_for(f, declared_source),
        "size_lines": len(text.splitlines()),
    }


def collect_files() -> list[Path]:
    """Collect every .md file in the repo, skipping system directories."""
    files = [
        p
        for p in REPO_ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    ]
    return sorted(files)


def group_by_domain(rows: list[dict]) -> dict[str, list[dict]]:
    """Group rows by domain, preserving insertion order."""
    groups: dict[str, list[dict]] = {}
    for row in rows:
        groups.setdefault(row["domain"], []).append(row)
    return groups


def build_index() -> str:
    files = collect_files()
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    rows = [extract_meta(f) for f in files]
    groups = group_by_domain(rows)

    source_counts: dict[str, int] = {}
    for row in rows:
        source_counts[row["source_system"]] = source_counts.get(row["source_system"], 0) + 1

    lines = [
        "# Lattice Global Index",
        "",
        "```",
        "STATUS: CANDIDATE — auto-generated, not canon",
        f"GENERATED: {now}",
        f"TOTAL_ARTIFACTS: {len(rows)}",
        f"DOMAINS: {len(groups)}",
        "SCOPE: full-repository (all .md files)",
        "```",
        "",
        "This file is **auto-generated** by `scripts/build_lattice_global_index.py`.",
        "Do not edit manually — it is regenerated on every CI push to main.",
        "",
        "## Source System Breakdown",
        "",
        "| Source System | Count |",
        "|---|---|",
    ]
    for system, count in sorted(source_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| `{system}` | {count} |")

    lines += [
        "",
        "---",
        "",
        "## Artifact Table (by Domain)",
        "",
    ]

    global_i = 1
    for domain, domain_rows in sorted(groups.items()):
        lines.append(f"### {domain} ({len(domain_rows)} artifacts)")
        lines.append("")
        lines.append("| # | Path | Title | Status | Source | Lines |")
        lines.append("|---|------|-------|--------|--------|-------|")
        for row in domain_rows:
            title = row["title"].replace("|", "\\|")[:80]
            status = row["status"].replace("|", "\\|")[:40]
            source = row["source_system"].replace("|", "\\|")
            lines.append(
                f"| {global_i} | `{row['path']}` | {title} | {status} | {source} | {row['size_lines']} |"
            )
            global_i += 1
        lines.append("")

    lines += [
        "---",
        "",
        f"*Auto-generated at {now}.*",
        f"*Total artifacts indexed: {len(rows)} across {len(groups)} domains.*",
        "*To add a new source system, update `SOURCE_SYSTEM_HINTS` in `scripts/build_lattice_global_index.py`.*",
    ]

    return "\n".join(lines) + "\n"


def main() -> int:
    index_content = build_index()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(index_content, encoding="utf-8")
    print(f"Lattice global index written to {OUTPUT_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
