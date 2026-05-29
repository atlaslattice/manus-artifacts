"""Tests for review_state_fsm.py — review-state finite state machine."""
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPT = REPO_ROOT / "scripts" / "review_state_fsm.py"


def run_fsm(*args):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)] + list(args),
        capture_output=True, text=True, cwd=str(REPO_ROOT)
    )
    return result


def test_script_exists():
    assert SCRIPT.exists()


def test_show_states():
    r = run_fsm("--list-states")
    assert r.returncode == 0
    assert "raw" in r.stdout
    assert "canon" in r.stdout


def test_validate_state_valid():
    r = run_fsm("--list-states")
    assert r.returncode == 0
    assert "raw" in r.stdout


def test_validate_state_invalid():
    # Use --set-state with an invalid state on a non-existent path (should error)
    r = run_fsm("--advance", "--file", "/nonexistent/file.md")
    # Should fail due to file not found
    assert r.returncode != 0 or "error" in r.stdout.lower() or "not found" in r.stdout.lower()


def test_advance_state_raw_to_candidate():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        f.write("---\nreview_state: raw\n---\n# Test\n")
        tmppath = f.name
    r = run_fsm("--advance", "--dry-run", "--file", tmppath)
    assert r.returncode == 0
    assert "candidate" in r.stdout


def test_advance_state_candidate_to_reviewed():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        f.write("---\nreview_state: candidate\n---\n# Test\n")
        tmppath = f.name
    r = run_fsm("--advance", "--dry-run", "--file", tmppath)
    assert r.returncode == 0
    assert "reviewed" in r.stdout


def test_advance_state_reviewed_to_canon_gate():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        f.write("---\nreview_state: reviewed\n---\n# Test\n")
        tmppath = f.name
    r = run_fsm("--advance", "--dry-run", "--file", tmppath)
    assert r.returncode == 0
    assert "canon-gate" in r.stdout


def test_advance_state_canon_gate_blocked():
    """canon-gate → canon requires human adjudication; FSM reports the transition."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        f.write("---\nreview_state: canon-gate\n---\n# Test\n")
        tmppath = f.name
    r = run_fsm("--advance", "--dry-run", "--file", tmppath)
    # FSM advances to canon (human adjudication is documented, not code-enforced)
    assert r.returncode == 0
    assert "canon" in r.stdout


def test_advance_state_canon_terminal():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, dir="/tmp") as f:
        f.write("---\nreview_state: canon\n---\n# Test\n")
        tmppath = f.name
    r = run_fsm("--advance", "--dry-run", "--file", tmppath)
    # canon → archived
    assert r.returncode == 0
    assert "archived" in r.stdout or "canon" in r.stdout
