"""Adversarial checks for lattice quality-gate failure modes."""

from __future__ import annotations

from scripts.validate_lattice_quality_gates import (
    validate_candidate_governance_state,
    validate_cross_reference_contract,
    validate_required_surface_connectivity,
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
            "isolated_markdown_artifacts": 0,
            "connected_markdown_components": 1,
            "root_reachable_markdown_artifacts": 1,
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


def test_adversarial_detects_connectivity_metric_mismatch() -> None:
    payload = {
        "link_health": {
            "markdown_artifacts_total": 2,
            "underlinked_markdown_artifacts": 0,
            "unresolved_repo_links": 0,
            "isolated_markdown_artifacts": 0,
            "connected_markdown_components": 1,
            "root_reachable_markdown_artifacts": 2,
        },
        "artifacts": [
            {
                "path": "README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "projects/aetherforge-top10-taskboard-2026-05-28.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
        ],
    }
    errors = validate_cross_reference_contract(payload)
    assert any("connected_markdown_components mismatch" in error for error in errors)
    assert any("root_reachable_markdown_artifacts mismatch" in error for error in errors)


def test_adversarial_detects_required_surface_root_reachability_failure() -> None:
    payload = {
        "artifacts": [
            {
                "path": "README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "docs/README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "archive/README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "archive/aetherforge/README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "archive/aetherforge/gptdreampp-openai/README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "archive/knowledge_graph/lattice_kg/v0_5/README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "projects/README.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "projects/aetherforge-world-class-authoritative-roadmap-v0.1.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "projects/aetherforge-144-task-campaign-2026-05-27.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "projects/aetherforge-top10-taskboard-2026-05-28.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "projects/aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
            {
                "path": "archive/spec/gptdream/GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md",
                "outbound_repo_links": [],
                "unresolved_repo_links": [],
                "inbound_repo_links": [],
            },
        ]
    }
    errors = validate_required_surface_connectivity(payload)
    assert any("not root-reachable" in error for error in errors)
    assert any("split across" in error for error in errors)
