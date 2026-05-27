from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "docs/ARCHITECTURE_MAP.md",
    "docs/ARTIFACT_ID_COLLISION_REPORT_2026-05-27.md",
    "docs/FAQ.md",
    "docs/FOLDER_TAXONOMY_AUDIT_2026-05-27.md",
    "docs/ARTIFACT_RELATIONSHIP_TYPES.md",
    "docs/CONTRIBUTOR_QUICKSTART.md",
    "docs/LINEAGE_QUALITY_SCORE_PROPOSAL_v0_1.md",
    "docs/ROADMAP.md",
    "docs/LATTICE_GLOBAL_INDEX.md",
    "docs/METADATA_BACKFILL_SCOPE_2026-05-27.md",
    "docs/METADATA_COVERAGE_REPORT_2026-05-27.md",
    "docs/METADATA_EXCEPTION_REGISTRY_2026-05-27.md",
    "docs/PROVENANCE_COMPLETENESS_REPORT_2026-05-27.md",
    "docs/SCHEMA_VERSION_MIGRATION_NOTES_v0_1.md",
    "projects/status-reports/PROVENANCE_DRIFT_REPORT_2026-05.md",
    "schemas/artifact_metadata/v0_1/artifact-metadata.schema.json",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/NON_CANON_DREAM_ARTIFACT_POLICY.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WAVE3_METADATA_PROVENANCE_RECEIPT_2026-05-27.md",
]


def main() -> int:
    missing = [str(ROOT / rel) for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    if missing:
        print("lattice quality gates: FAIL")
        for item in missing:
            print(f"- missing: {item}")
        return 1

    index = (ROOT / "docs/LATTICE_GLOBAL_INDEX.md").read_text(encoding="utf-8")
    if "# Lattice Global Index" not in index:
        print("lattice quality gates: FAIL")
        print("- docs/LATTICE_GLOBAL_INDEX.md missing expected title")
        return 1

    print("lattice quality gates: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
