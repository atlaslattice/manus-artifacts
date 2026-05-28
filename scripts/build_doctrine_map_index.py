#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = DOCS / "DOCTRINE_MAP_INDEX.md"

EXCLUDE = {
    "DOCTRINE_MAP_INDEX.md",
}

files = sorted(
    [p for p in DOCS.glob("*.md") if p.name not in EXCLUDE],
    key=lambda p: p.name.lower(),
)

ts = datetime.now(timezone.utc).strftime("%Y-%m-%d")

lines = [
    "# Doctrine Map Index",
    "Status: Candidate",
    f"Date: {ts}",
    "",
    "This file is auto-generated from markdown doctrine surfaces in `/docs`.",
    "",
    "## Index",
    "",
]

for p in files:
    title = p.stem.replace("_", " ").replace("-", " ")
    lines.append(f"- [{title}]({p.name})")

lines.extend(
    [
        "",
        "## Generation",
        "",
        "- Script: `scripts/build_doctrine_map_index.py`",
        "- Command: `python scripts/build_doctrine_map_index.py`",
    ]
)

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"wrote {OUT}")
