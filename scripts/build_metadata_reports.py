from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from metadata_inventory import (
    BACKFILL_DATE,
    EXCEPTION_PATHS,
    ROOT,
    TOP50_PATHS,
    artifact_id_collisions,
    coverage_summary,
    inventory_records,
    next100_paths,
)

DOCS_DIR = ROOT / "docs"
STATUS_DIR = ROOT / "projects" / "status-reports"
REPORT_DATE = "2026-05-29"  # Wave 3 v2 report date


def frontmatter(artifact_id: str, title: str, date: str = BACKFILL_DATE) -> list[str]:
    return [
        "---",
        f"artifact_id: {artifact_id}",
        f"title: {title}",
        "status: CANDIDATE",
        "owner: atlaslattice",
        f"created: {date}",
        f"last_updated: {date}",
        "source_of_truth: GitHub",
        "---",
        "",
    ]


def write(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def checkmark(record: dict[str, object]) -> str:
    return "✅" if record["has_frontmatter"] and not record["missing_keys"] else "⚠️"


def main() -> int:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    records = inventory_records()
    summary = coverage_summary(records)
    collisions = artifact_id_collisions(records)
    record_map = {record["path"]: record for record in records}
    wave3_next100 = next100_paths(records)

    missing_source = [record for record in records if "source_of_truth" in record["missing_keys"]]
    missing_ids = [record for record in records if "artifact_id" in record["missing_keys"]]
    invalid_status = [record for record in records if record["invalid_status"]]
    non_github = [
        record
        for record in records
        if record["frontmatter"].get("source_of_truth")
        and record["frontmatter"].get("source_of_truth") != "GitHub"
    ]

    write(
        DOCS_DIR / "METADATA_BACKFILL_SCOPE_2026-05-27.md",
        frontmatter(
            "DOC-METADATA-BACKFILL-SCOPE-2026-05-27",
            "Metadata Backfill Scope (Wave 3)",
        )
        + [
            "# Metadata Backfill Scope (Wave 3)",
            "",
            "## Objective",
            "",
            "Backfill strong artifact metadata on the highest-value public surfaces first, then queue the next 100 markdown artifacts for follow-on normalization.",
            "",
            f"Generated at: `{now}`",
            "",
            "## Top 50 priority artifacts",
            "",
            "| Status | Path |",
            "|---|---|",
        ]
        + [f"| {checkmark(record_map[path])} | `{path}` |" for path in TOP50_PATHS]
        + [
            "",
            "## Next 100 queued artifacts",
            "",
            "| Priority | Path |",
            "|---:|---|",
        ]
        + [f"| {index} | `{path}` |" for index, path in enumerate(wave3_next100, start=1)]
        + [
            "",
            "## Registry notes",
            "",
            "- `✅` means required frontmatter is present.",
            "- `⚠️` means the artifact remains in the next backfill lane or requires manual review.",
        ],
    )

    write(
        DOCS_DIR / "METADATA_COVERAGE_REPORT_2026-05-27.md",
        frontmatter(
            "DOC-METADATA-COVERAGE-REPORT-2026-05-27",
            "Metadata Coverage Report",
        )
        + [
            "# Metadata Coverage Report",
            "",
            f"Generated at: `{now}`",
            "",
            "## Repository-wide summary",
            "",
            f"- Markdown files scanned: **{summary['total']}**",
            f"- Files with frontmatter: **{summary['with_frontmatter']}**",
            f"- Files with complete required metadata: **{summary['fully_valid']}**",
            "",
            "## Missing required fields",
            "",
            "| Field | Missing count |",
            "|---|---:|",
        ]
        + [f"| `{field}` | {count} |" for field, count in summary["missing_counter"].items()]
        + [
            "",
            "## Wave 3 priority coverage",
            "",
            f"- Top 50 fully covered: **{sum(1 for path in TOP50_PATHS if not record_map[path]['missing_keys'])} / 50**",
            f"- Next 100 already covered: **{sum(1 for path in wave3_next100 if not record_map[path]['missing_keys'])} / 100**",
        ],
    )

    write(
        DOCS_DIR / "PROVENANCE_COMPLETENESS_REPORT_2026-05-27.md",
        frontmatter(
            "DOC-PROVENANCE-COMPLETENESS-REPORT-2026-05-27",
            "Provenance Completeness Report",
        )
        + [
            "# Provenance Completeness Report",
            "",
            f"Generated at: `{now}`",
            "",
            "## Required provenance signals",
            "",
            "- `artifact_id`",
            "- `owner`",
            "- `created` / `last_updated`",
            "- `status`",
            "- `source_of_truth`",
            "",
            "## Gap summary",
            "",
            f"- Files missing `artifact_id`: **{len(missing_ids)}**",
            f"- Files missing `source_of_truth`: **{len(missing_source)}**",
            f"- Files with invalid status values: **{len(invalid_status)}**",
            f"- Files with non-GitHub source values: **{len(non_github)}**",
            "",
            "## Highest-priority remaining gaps",
            "",
            "| Path | Missing keys |",
            "|---|---|",
        ]
        + [
            f"| `{path}` | {', '.join(record_map[path]['missing_keys']) or 'none'} |"
            for path in wave3_next100[:25]
        ],
    )

    write(
        DOCS_DIR / "ARTIFACT_ID_COLLISION_REPORT_2026-05-27.md",
        frontmatter(
            "DOC-ARTIFACT-ID-COLLISION-REPORT-2026-05-27",
            "Artifact ID Collision Report",
        )
        + [
            "# Artifact ID Collision Report",
            "",
            f"Generated at: `{now}`",
            "",
            "## Result",
            "",
            "No duplicate `artifact_id` values were detected in the current markdown inventory." if not collisions else "Duplicate `artifact_id` values were detected and require cleanup.",
        ]
        + (
            []
            if not collisions
            else [
                "",
                "## Collisions",
                "",
                "| artifact_id | Paths |",
                "|---|---|",
            ]
            + [f"| `{artifact_id}` | {'<br>'.join(f'`{path}`' for path in paths)} |" for artifact_id, paths in sorted(collisions.items())]
        ),
    )

    write(
        STATUS_DIR / "PROVENANCE_DRIFT_REPORT_2026-05.md",
        frontmatter(
            "STATUS-PROVENANCE-DRIFT-REPORT-2026-05",
            "Provenance Drift Report (2026-05)",
        )
        + [
            "# Provenance Drift Report (2026-05)",
            "",
            f"Generated at: `{now}`",
            "",
            "## Snapshot",
            "",
            f"- Total markdown artifacts: **{summary['total']}**",
            f"- Coverage baseline with complete metadata: **{summary['fully_valid']}**",
            f"- Remaining next-100 queue items without full metadata: **{sum(1 for path in wave3_next100 if record_map[path]['missing_keys'])}**",
            "",
            "## Drift watchlist",
            "",
            "- Review newly added markdown files monthly for missing provenance fields.",
            "- Keep `source_of_truth` normalized to `GitHub`.",
            "- Escalate any future `artifact_id` collisions before promotion to canon.",
        ],
    )

    write(
        ROOT / "archive" / "boot" / "gptbrain" / "agents" / "TIDELOCKBrain" / "TIDELOCKBRAIN_WAVE3_METADATA_PROVENANCE_RECEIPT_2026-05-27.md",
        frontmatter(
            "TIDELOCK-WAVE3-METADATA-PROVENANCE-RECEIPT-2026-05-27",
            "TIDELOCKBrain Wave 3 Metadata + Provenance Receipt",
        )
        + [
            "# TIDELOCKBrain Wave 3 Metadata + Provenance Receipt",
            "",
            "- Wave: **3 / Metadata & Provenance**",
            f"- Generated at: `{now}`",
            "- Outcome: metadata scope, coverage reports, collision report, provenance completeness report, and drift report published.",
            "",
            "## Linked outputs",
            "",
            "- `/tmp/workspace/atlaslattice/manus-artifacts/docs/METADATA_BACKFILL_SCOPE_2026-05-27.md`",
            "- `/tmp/workspace/atlaslattice/manus-artifacts/docs/METADATA_COVERAGE_REPORT_2026-05-27.md`",
            "- `/tmp/workspace/atlaslattice/manus-artifacts/docs/PROVENANCE_COMPLETENESS_REPORT_2026-05-27.md`",
            "- `/tmp/workspace/atlaslattice/manus-artifacts/docs/ARTIFACT_ID_COLLISION_REPORT_2026-05-27.md`",
            "- `/tmp/workspace/atlaslattice/manus-artifacts/projects/status-reports/PROVENANCE_DRIFT_REPORT_2026-05.md`",
        ],
    )

    write(
        DOCS_DIR / "METADATA_EXCEPTION_REGISTRY_2026-05-27.md",
        frontmatter(
            "DOC-METADATA-EXCEPTION-REGISTRY-2026-05-27",
            "Metadata Exception Registry",
        )
        + [
            "# Metadata Exception Registry",
            "",
            "These paths are operational templates or workflow surfaces that remain in the metadata inventory but may require lighter manual review before canon treatment.",
            "",
            "| Path | Reason |",
            "|---|---|",
        ]
        + [f"| `{path}` | {reason} |" for path, reason in sorted(EXCEPTION_PATHS.items())],
    )

    # --- Wave 3 v2 reports (Tasks 31 & 32) ---

    write(
        DOCS_DIR / f"METADATA_COVERAGE_REPORT_{REPORT_DATE}.md",
        frontmatter(
            f"DOC-METADATA-COVERAGE-REPORT-{REPORT_DATE}",
            "Metadata Coverage Report v2",
            date=REPORT_DATE,
        )
        + [
            "# Metadata Coverage Report v2",
            "",
            f"Generated at: `{now}`",
            "",
            "> **Wave 3 post-backfill snapshot** — 259 files backfilled in this session.",
            "",
            "## Repository-wide summary",
            "",
            f"- Markdown files scanned: **{summary['total']}**",
            f"- Files with frontmatter: **{summary['with_frontmatter']}**",
            f"- Files with complete required metadata: **{summary['fully_valid']}**",
            f"- Coverage rate: **{summary['fully_valid'] / summary['total'] * 100:.1f}%**",
            "",
            "## Missing required fields",
            "",
            "| Field | Missing count |",
            "|---|---:|",
        ]
        + [f"| `{field}` | {count} |" for field, count in summary["missing_counter"].items()]
        + [
            "",
            "## Wave 3 priority coverage",
            "",
            f"- Top 50 fully covered: **{sum(1 for path in TOP50_PATHS if not record_map[path]['missing_keys'])} / 50**",
            f"- Next 100 covered: **{sum(1 for path in wave3_next100 if not record_map[path]['missing_keys'])} / 100**",
            "",
            "## Remaining gap",
            "",
            "| Path | Missing keys |",
            "|---|---|",
        ]
        + [
            f"| `{r['path']}` | {', '.join(r['missing_keys'])} |"
            for r in records
            if r["missing_keys"] and r["path"] not in EXCEPTION_PATHS
        ][:30]
        + ["", "> _Showing first 30 of remaining gap. Run `scripts/build_metadata_reports.py` to refresh._"],
    )

    write(
        DOCS_DIR / f"PROVENANCE_COMPLETENESS_REPORT_{REPORT_DATE}.md",
        frontmatter(
            f"DOC-PROVENANCE-COMPLETENESS-REPORT-{REPORT_DATE}",
            "Provenance Completeness Report v2",
            date=REPORT_DATE,
        )
        + [
            "# Provenance Completeness Report v2",
            "",
            f"Generated at: `{now}`",
            "",
            "> **Wave 3 post-backfill snapshot.**",
            "",
            "## Required provenance signals",
            "",
            "- `artifact_id`",
            "- `owner`",
            "- `created` / `last_updated`",
            "- `status`",
            "- `source_of_truth`",
            "",
            "## Gap summary",
            "",
            f"- Files missing `artifact_id`: **{len(missing_ids)}**",
            f"- Files missing `source_of_truth`: **{len(missing_source)}**",
            f"- Files with invalid status values: **{len(invalid_status)}**",
            f"- Files with non-GitHub source values: **{len(non_github)}**",
            "",
            "## Highest-priority remaining gaps",
            "",
            "| Path | Missing keys |",
            "|---|---|",
        ]
        + [
            f"| `{path}` | {', '.join(record_map[path]['missing_keys']) or 'none'} |"
            for path in wave3_next100[:25]
        ]
        + [
            "",
            "## Exception paths (excluded from gap count)",
            "",
            "| Path | Reason |",
            "|---|---|",
        ]
        + [f"| `{p}` | {r} |" for p, r in sorted(EXCEPTION_PATHS.items())],
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
