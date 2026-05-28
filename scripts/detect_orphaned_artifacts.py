#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

CRITICAL = [
    ROOT / "docs" / "LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md",
    ROOT / "docs" / "ARTIFACT_RELATIONSHIP_TYPES.md",
    ROOT / "docs" / "CROSS_DOMAIN_LINK_POLICY.md",
    ROOT / "docs" / "PUBLIC_ARCHIVE_MAP.md",
    ROOT / "docs" / "WEEKLY_DELTA_DIGEST_TEMPLATE.md",
    ROOT / "projects" / "AETHERFORGE_PUBLIC_QUESTBOARD_v0.1.md",
    ROOT / "archive" / "spec" / "gptdream" / "README.md",
]

SOURCE_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "START_HERE.md",
    ROOT / "projects" / "aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md",
    ROOT / "projects" / "aetherforge-top10-taskboard-2026-05-26.md",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
linked = set()
for src in SOURCE_FILES:
    txt = src.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(txt):
        link = raw.split("#", 1)[0].strip()
        if not link or link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"):
            continue
        linked.add((src.parent / link).resolve())

orphans = [p for p in CRITICAL if p.resolve() not in linked]
if orphans:
    print("critical orphaned artifacts found:")
    for o in orphans:
        print(f"- {o.relative_to(ROOT)}")
    sys.exit(1)

print(f"orphan detection passed ({len(CRITICAL)} critical artifacts reachable)")
