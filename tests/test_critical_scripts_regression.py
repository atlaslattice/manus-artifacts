import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

CRITICAL_COMMANDS = [
    ["python", "scripts/validate_artifact_metadata.py"],
    ["python", "scripts/check_markdown_links.py"],
    ["python", "scripts/detect_orphaned_artifacts.py"],
    ["python", "scripts/validate_canon_state_transitions.py"],
    ["python", "scripts/validate_governance_required_sections.py"],
    ["python", "scripts/check_external_link_policy.py"],
    ["python", "scripts/validate_sensitive_claim_provenance.py"],
    ["python", "scripts/build_quality_dashboard_data.py"],
]


def test_critical_scripts_regression_suite():
    for command in CRITICAL_COMMANDS:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        assert result.returncode == 0, (
            f"command failed: {' '.join(command)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
