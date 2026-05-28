#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    ROOT / "README.md",
    ROOT / "docs" / "START_HERE.md",
    ROOT / "docs" / "ROADMAP.md",
    ROOT / "docs" / "QUALITY_DASHBOARD.md",
    ROOT / "projects" / "aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md",
    ROOT / "projects" / "aetherforge-top10-taskboard-2026-05-26.md",
    ROOT / "projects" / "AETHERFORGE_PUBLIC_QUESTBOARD_v0.1.md",
    ROOT / "archive" / "spec" / "gptdream" / "README.md",
]

RE_STATUS = re.compile(r"^Status:\s+", re.MULTILINE)
RE_DATE = re.compile(r"^Date:\s+", re.MULTILINE)

errors = []
for path in TARGETS:
    if not path.exists():
        errors.append(f"missing file: {path.relative_to(ROOT)}")
        continue
    txt = path.read_text(encoding="utf-8")
    if not RE_STATUS.search(txt):
        errors.append(f"missing Status line: {path.relative_to(ROOT)}")
    if path.name != "README.md" and not RE_DATE.search(txt):
        errors.append(f"missing Date line: {path.relative_to(ROOT)}")

if errors:
    print("metadata validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"metadata validation passed ({len(TARGETS)} files)")
