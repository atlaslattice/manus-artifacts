from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/LATTICE_GLOBAL_INDEX.md"
BACKFILL_DATE = "2026-05-27"

EXCLUDED_PREFIXES = {
    ".git/",
}

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(?P<title>.+?)\s*$")

STATUS_EMOJI = {
    "CANONICAL": "🟢",
    "CANDIDATE": "🟡",
    "DRAFT": "🔵",
    "ARCHIVED": "⬛",
}


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return not any(rel.startswith(prefix) for prefix in EXCLUDED_PREFIXES)


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}
    frontmatter: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()
    return frontmatter


def extract_heading_title(text: str) -> str:
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            return m.group("title").strip()
    return ""


def artifact_record(path: Path) -> dict[str, str]:
    rel = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        text = ""
    fm = parse_frontmatter(text)
    title = fm.get("title") or extract_heading_title(text) or path.stem.replace("-", " ").replace("_", " ")
    return {
        "path": rel,
        "title": title,
        "artifact_id": fm.get("artifact_id", "—"),
        "status": fm.get("status", "—"),
        "owner": fm.get("owner", "—"),
        "created": fm.get("created", "—"),
    }


def build_index() -> str:
    markdown_files = sorted(
        p for p in ROOT.rglob("*.md") if p.is_file() and should_include(p)
    )

    records = [artifact_record(p) for p in markdown_files]

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for rec in records:
        top = rec["path"].split("/")[0] if "/" in rec["path"] else "(root)"
        grouped[top].append(rec)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    total = len(records)

    lines = [
        "---",
        "artifact_id: DOC-LATTICE-GLOBAL-INDEX-2026-05-27",
        "title: Lattice Global Index",
        "status: CANDIDATE",
        "owner: atlaslattice",
        f"created: {BACKFILL_DATE}",
        f"last_updated: {BACKFILL_DATE}",
        "source_of_truth: GitHub",
        "---",
        "",
        "# Lattice Global Index",
        "",
        f"Generated at: `{now}`  ",
        f"Total artifacts indexed: **{total}**",
        "",
        "> Full deep index of every markdown artifact in this repository.",
        "> Status legend: 🟢 CANONICAL · 🟡 CANDIDATE · 🔵 DRAFT · ⬛ ARCHIVED · — unset",
        "",
        "## Domain Summary",
        "",
        "| Domain | Artifacts | With Frontmatter |",
        "|---|---:|---:|",
    ]

    for domain in sorted(grouped):
        recs = grouped[domain]
        with_fm = sum(1 for r in recs if r["artifact_id"] != "—")
        lines.append(f"| `{domain}` | {len(recs)} | {with_fm} |")

    lines.extend([
        "",
        "---",
        "",
        "## Full Artifact Register",
        "",
        "> Every file enumerated. Sorted by domain then path.",
        "",
    ])

    for domain in sorted(grouped):
        recs = sorted(grouped[domain], key=lambda r: r["path"])
        lines.append(f"### {domain}")
        lines.append("")
        lines.append("| Path | Title | Status | Artifact ID |")
        lines.append("|---|---|---|---|")
        for r in recs:
            emoji = STATUS_EMOJI.get(r["status"], "")
            status_cell = f"{emoji} {r['status']}" if emoji else r["status"]
            # Escape pipes in title
            title = r["title"].replace("|", "\\|")
            artifact_id = r["artifact_id"].replace("|", "\\|")
            lines.append(f"| `{r['path']}` | {title} | {status_cell} | `{artifact_id}` |")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    OUTPUT.write_text(build_index(), encoding="utf-8")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
