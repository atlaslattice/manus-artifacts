"""Lineage quality score pilot (Task 33).

Scores each markdown artifact 0–4 based on the rubric from
docs/LINEAGE_QUALITY_SCORE_PROPOSAL_v0_1.md:

  4 – Required metadata + explicit upstream citations + validation signal
  3 – Required metadata + at least one provenance reference
  2 – Some required metadata present; provenance or status incomplete
  1 – Title/path only; provenance fields missing
  0 – Missing enough metadata to trust routing or ownership

Outputs a report to docs/LINEAGE_QUALITY_SCORE_REPORT_<date>.md.

Usage:
    python scripts/score_lineage_quality.py
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from metadata_inventory import (
    EXCEPTION_PATHS,
    ROOT,
    inventory_records,
    parse_frontmatter,
)

REPORT_DATE = "2026-05-29"
DOCS_DIR = ROOT / "docs"

# Patterns that suggest provenance references in body text
PROV_REF_RE = re.compile(
    r"(artifact_id|related_to|upstream|derived_from|source:|citation|see also|parent:|child:|linked_from)",
    re.IGNORECASE,
)
# Patterns that suggest a validation / evidence signal
VALIDATION_RE = re.compile(
    r"(pytest|test_|\.py|✅|PASS|evidence|validated|reviewed|ratif)",
    re.IGNORECASE,
)


def score_record(record: dict) -> int:
    """Return 0–4 lineage quality score for a single record."""
    fm = record["frontmatter"]
    missing = set(record["missing_keys"])
    has_all_required = not missing

    if not fm:
        return 0  # No metadata at all

    if missing - {"title"}:
        # At least one field beyond title is missing → weak lineage
        if len(missing) >= 5:
            return 0
        return 1  # Some fields present

    # All required fields present → at least score 2
    path = ROOT / record["path"]
    try:
        body = path.read_text(encoding="utf-8")
    except Exception:
        return 2

    has_prov = bool(PROV_REF_RE.search(body))
    has_validation = bool(VALIDATION_RE.search(body))

    if has_all_required and has_prov and has_validation:
        return 4
    if has_all_required and has_prov:
        return 3
    if has_all_required:
        return 2
    return 1


def main() -> int:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    records = inventory_records()

    scored = [
        {**r, "score": score_record(r)}
        for r in records
        if r["path"] not in EXCEPTION_PATHS
    ]
    scored.sort(key=lambda r: (r["score"], r["path"]))

    band_counts = {i: sum(1 for r in scored if r["score"] == i) for i in range(5)}
    total = len(scored)
    avg = sum(r["score"] for r in scored) / total if total else 0

    lines: list[str] = [
        "---",
        f"artifact_id: DOC-LINEAGE-QUALITY-SCORE-REPORT-{REPORT_DATE}",
        "title: Lineage Quality Score Report",
        "status: CANDIDATE",
        "owner: atlaslattice",
        f"created: {REPORT_DATE}",
        f"last_updated: {REPORT_DATE}",
        "source_of_truth: GitHub",
        "---",
        "",
        "# Lineage Quality Score Report",
        "",
        f"Generated at: `{now}`",
        "",
        "> Scoring rubric from `docs/LINEAGE_QUALITY_SCORE_PROPOSAL_v0_1.md`.",
        "",
        "## Band summary",
        "",
        "| Score | Meaning | Count | % |",
        "|---|---|---:|---:|",
        f"| 4 | Strong lineage | {band_counts[4]} | {band_counts[4]/total*100:.1f}% |",
        f"| 3 | Usable lineage | {band_counts[3]} | {band_counts[3]/total*100:.1f}% |",
        f"| 2 | Partial lineage | {band_counts[2]} | {band_counts[2]/total*100:.1f}% |",
        f"| 1 | Weak lineage   | {band_counts[1]} | {band_counts[1]/total*100:.1f}% |",
        f"| 0 | Unusable       | {band_counts[0]} | {band_counts[0]/total*100:.1f}% |",
        f"| — | **Total**      | **{total}** | 100% |",
        "",
        f"**Average score:** {avg:.2f} / 4.00",
        "",
        "## Score-0 artifacts requiring immediate attention",
        "",
        "| Path | Missing keys |",
        "|---|---|",
    ]
    for r in scored:
        if r["score"] == 0:
            lines.append(f"| `{r['path']}` | {', '.join(r['missing_keys']) or '—'} |")

    lines += [
        "",
        "## Score-1 artifacts (top 20 by priority)",
        "",
        "| Path | Missing keys |",
        "|---|---|",
    ]
    score1 = [r for r in scored if r["score"] == 1][:20]
    for r in score1:
        lines.append(f"| `{r['path']}` | {', '.join(r['missing_keys']) or '—'} |")

    lines += [
        "",
        "## Canon promotion requirements",
        "",
        "- Minimum score **3** required before canon review.",
        "- Score **4** recommended for flagship artifacts.",
        "- Re-run this script after each metadata backfill pass.",
    ]

    out_path = DOCS_DIR / f"LINEAGE_QUALITY_SCORE_REPORT_{REPORT_DATE}.md"
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {out_path}")
    print(f"Total: {total} | Avg score: {avg:.2f} | Band 4: {band_counts[4]} | Band 0: {band_counts[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
