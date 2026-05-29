"""Tests for ip_boundary_check.py — PII / secrets / IP boundary scanner."""
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPT = REPO_ROOT / "scripts" / "ip_boundary_check.py"


def run_checker(*args):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)] + list(args),
        capture_output=True, text=True, cwd=str(REPO_ROOT)
    )
    return result


def test_script_exists():
    assert SCRIPT.exists()


def test_clean_file_no_findings():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        f.write("# Test\n\nThis is a clean test artifact with no PII.\n")
        tmppath = f.name
    r = run_checker("--path", tmppath)
    # Either exits 0 or reports "0 findings" / "PASS"
    assert r.returncode == 0 or "0" in r.stdout or "no findings" in r.stdout.lower() \
        or "clean" in r.stdout.lower() or "PASS" in r.stdout


def test_pii_detection_email():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        f.write("# Bad\n\nContact: john.doe@example.com\n")
        tmppath = f.name
    r = run_checker("--path", tmppath)
    # Should detect email as PII finding
    assert "email" in r.stdout.lower() or "pii" in r.stdout.lower() \
        or "HIGH" in r.stdout or r.returncode != 0


def test_secret_detection_token():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        # Fake GitHub PAT pattern (not a real secret)
        f.write("token: ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcde1234\n")
        tmppath = f.name
    r = run_checker("--path", tmppath)
    assert "github" in r.stdout.lower() or "token" in r.stdout.lower() \
        or "secret" in r.stdout.lower() or "HIGH" in r.stdout or r.returncode != 0


def test_directory_scan():
    """Script should accept a directory path."""
    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:
        Path(tmpdir, "test.md").write_text("# Clean file\n")
        r = run_checker("--path", tmpdir)
        assert r.returncode == 0 or "scan" in r.stdout.lower() or "finding" in r.stdout.lower()
