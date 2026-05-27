from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_metadata_schema_exists_and_has_required_fields():
    schema_path = ROOT / "schemas/artifact_metadata/v0_1/artifact-metadata.schema.json"
    text = schema_path.read_text(encoding="utf-8")
    assert "artifact_id" in text
    assert "source_of_truth" in text


def test_wave1_quality_gate_scripts_pass():
    metadata = subprocess.run(
        [sys.executable, "scripts/validate_artifact_metadata.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert metadata.returncode == 0, metadata.stdout + metadata.stderr

    quality = subprocess.run(
        [sys.executable, "scripts/validate_lattice_quality_gates.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert quality.returncode == 0, quality.stdout + quality.stderr
