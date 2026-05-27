from pathlib import Path
import subprocess
import sys

from scripts.metadata_inventory import TOP50_PATHS

ROOT = Path(__file__).resolve().parents[1]


def test_wave3_priority_scope_tracks_50_artifacts():
    assert len(TOP50_PATHS) == 50
    assert len(set(TOP50_PATHS)) == 50


def test_wave3_report_builder_and_validators_pass():
    reports = subprocess.run(
        [sys.executable, "scripts/build_metadata_reports.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert reports.returncode == 0, reports.stdout + reports.stderr

    metadata = subprocess.run(
        [sys.executable, "scripts/validate_artifact_metadata.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert metadata.returncode == 0, metadata.stdout + metadata.stderr

    for rel_path in [
        "docs/METADATA_BACKFILL_SCOPE_2026-05-27.md",
        "docs/METADATA_COVERAGE_REPORT_2026-05-27.md",
        "docs/PROVENANCE_COMPLETENESS_REPORT_2026-05-27.md",
        "docs/ARTIFACT_ID_COLLISION_REPORT_2026-05-27.md",
        "projects/status-reports/PROVENANCE_DRIFT_REPORT_2026-05.md",
    ]:
        assert (ROOT / rel_path).exists(), rel_path
