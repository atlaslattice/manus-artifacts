#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "generated" / "QUALITY_DASHBOARD_DATA.json"
TOP50 = ROOT / "projects" / "aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md"
ROADMAP = ROOT / "docs" / "ROADMAP.md"
QUESTBOARD = ROOT / "projects" / "AETHERFORGE_PUBLIC_QUESTBOARD_v0.1.md"

TASK_RE = re.compile(r"^\s*(\d+)\.\s+\[( |x)\]\s+(.+?)\s*$")
KPI_BULLET_RE = re.compile(r"^- (.+)$", re.MULTILINE)


def count_markdown(path: Path) -> int:
    return len(list(path.glob("*.md")))


ring_totals = {"ring_iii": {"done": 0, "total": 0}, "ring_iv": {"done": 0, "total": 0}, "ring_v": {"done": 0, "total": 0}}

for raw_line in TOP50.read_text(encoding="utf-8").splitlines():
    line = raw_line.rstrip()
    match = TASK_RE.match(line)
    if not match:
        continue
    number = int(match.group(1))
    done = match.group(2) == "x"
    if 21 <= number <= 30:
        bucket = "ring_iii"
    elif 31 <= number <= 40:
        bucket = "ring_iv"
    elif 41 <= number <= 50:
        bucket = "ring_v"
    else:
        continue
    ring_totals[bucket]["total"] += 1
    if done:
        ring_totals[bucket]["done"] += 1

roadmap_text = ROADMAP.read_text(encoding="utf-8")
measurement_anchor_lines = []
if "## Measurement anchors" in roadmap_text:
    anchor_block = roadmap_text.split("## Measurement anchors", 1)[1]
    if "## " in anchor_block:
        anchor_block = anchor_block.split("## ", 1)[0]
    measurement_anchor_lines = [m.group(1).strip() for m in KPI_BULLET_RE.finditer(anchor_block)]

quest_text = QUESTBOARD.read_text(encoding="utf-8")
open_quests = len(re.findall(r"^\d+\.\s+\[ \]\s+", quest_text, flags=re.MULTILINE))

payload = {
    "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "repository_health": {
        "docs_markdown_files": count_markdown(ROOT / "docs"),
        "governance_markdown_files": count_markdown(ROOT / "governance"),
        "project_markdown_files": count_markdown(ROOT / "projects"),
    },
    "top50_execution": ring_totals,
    "roadmap_kpis": {
        "count": len(measurement_anchor_lines),
        "anchors": measurement_anchor_lines,
    },
    "public_questboard": {
        "open_quests": open_quests,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
