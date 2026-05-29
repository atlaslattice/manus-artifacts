"""Tests for ingest_artifact.py — artifact ingest and frontmatter pipeline."""
import subprocess
import sys
import tempfile
import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPT = REPO_ROOT / "scripts" / "ingest_artifact.py"


def run_ingest(*args):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)] + list(args),
        capture_output=True, text=True, cwd=str(REPO_ROOT)
    )
    return result


def test_script_exists():
    assert SCRIPT.exists()


def test_dry_run_single_file():
    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:
        tmppath = Path(tmpdir) / "test_artifact.md"
        tmppath.write_text("# Test Artifact\n\nThis is a test.\n")
        r = run_ingest("--dry-run", "--root", tmpdir, str(tmppath))
        assert r.returncode == 0, f"dry-run failed: {r.stderr}"


def test_dry_run_directory():
    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:
        Path(tmpdir, "doc1.md").write_text("# Doc 1\n\nContent.\n")
        Path(tmpdir, "doc2.md").write_text("# Doc 2\n\nContent.\n")
        r = run_ingest("--dry-run", "--root", tmpdir, tmpdir)
        assert r.returncode == 0, f"dir dry-run failed: {r.stderr}"


def test_dry_run_doesnt_write():
    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:
        tmppath = Path(tmpdir) / "no_frontmatter.md"
        original = "# Original\n\nNo frontmatter.\n"
        tmppath.write_text(original)
        run_ingest("--dry-run", "--root", tmpdir, str(tmppath))
        content = tmppath.read_text()
        assert content == original, "dry-run should not modify the file"


def test_preview_shows_hsn():
    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:
        tmppath = Path(tmpdir) / "my_document.md"
        tmppath.write_text("# My Document\n\nContent here.\n")
        r = run_ingest("--dry-run", "--root", tmpdir, str(tmppath))
        # Should mention H-S-N or artifact_id in the preview
        assert "H" in r.stdout and ("S" in r.stdout or "hsn" in r.stdout.lower()), \
            f"Expected HSN in dry-run output, got: {r.stdout[:200]}"
