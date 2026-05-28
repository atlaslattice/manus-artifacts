#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SEED_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "START_HERE.md",
    ROOT / "projects" / "aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md",
    ROOT / "projects" / "aetherforge-top10-taskboard-2026-05-26.md",
    ROOT / "archive" / "spec" / "gptdream" / "README.md",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

errors = []
for src in SEED_FILES:
    txt = src.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(txt):
        link = raw.split("#", 1)[0].strip()
        if not link or link.startswith(("http://", "https://", "mailto:")):
            continue
        target = (src.parent / link).resolve()
        if not target.exists():
            errors.append(f"{src.relative_to(ROOT)} -> {link}")

if errors:
    print("broken markdown links detected:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"link integrity passed ({len(SEED_FILES)} seed files)")
