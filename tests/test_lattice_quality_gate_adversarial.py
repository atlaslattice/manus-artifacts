"""Adversarial checks for lattice quality-gate failure modes."""

from __future__ import annotations

from scripts.validate_lattice_quality_gates import (
    validate_candidate_governance_state,
    validate_cross_reference_contract,
)


def test_adversarial_detects_governance_state_drift() -> None:
    artifacts = [
        {
            "path": "archive/example.md",
            "canon_status": "ratified",
            "deployment_status": "deployable",
            "trust_state": "trusted",
        }
    ]
    errors = validate_candidate_governance_state(artifacts)
    assert any("canon_status drift" in error for error in errors)
    assert any("deployment_status drift" in error for error in errors)
    assert any("trust_state drift" in error for error in errors)


def test_adversarial_detects_cross_reference_contract_breakage() -> None:
    payload = {
        "link_health": {
            "markdown_artifacts_total": 1,
            "underlinked_markdown_artifacts": 0,
            "unresolved_repo_links": 0,
        },
        "artifacts": [
            {
                "path": "projects/aetherforge-top10-taskboard-2026-05-28.md",
                "outbound_repo_links": "not-a-list",
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            }
        ],
    }
    errors = validate_cross_reference_contract(payload)
    assert any("must be a list" in error for error in errors)
