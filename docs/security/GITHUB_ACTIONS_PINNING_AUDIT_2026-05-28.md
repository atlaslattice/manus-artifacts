---
artifact_id: DOC-GITHUB-ACTIONS-PINNING-AUDIT-2026-05-28
title: GitHub Actions Pinning Audit
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# GitHub Actions Pinning Audit

## Summary

This audit reviews whether GitHub Actions workflows are pinned to immutable SHAs or mutable version tags.

## Findings

| Workflow | Third-party actions used | Pinning state | Notes |
|---|---|---|---|
| `docs-link-checks.yml` | `actions/checkout@v4` | Tag-pinned, not SHA-pinned | Mutable major tag |
| `gptbrain-reference-checks.yml` | `actions/checkout@v4`, `actions/setup-python@v5` | Tag-pinned, not SHA-pinned | Mutable major tags |
| `lattice-kg-quality-gates.yml` | `actions/checkout@v4`, `actions/setup-python@v5` | Tag-pinned, not SHA-pinned | Mutable major tags |
| `markdown-lint.yml` | `actions/checkout@v4`, `DavidAnson/markdownlint-cli2-action@v18` | Tag-pinned, not SHA-pinned | Third-party mutable tag |
| `repo-hygiene-checks.yml` | `actions/checkout@v4` | Tag-pinned, not SHA-pinned | Mutable major tag |
| `secret-scan.yml` | `actions/checkout@v4`, `gitleaks/gitleaks-action@v2` | Tag-pinned, not SHA-pinned | Third-party mutable tag |

## Risk Assessment

- Current configuration is acceptable for baseline open-source repo hygiene.
- It is not ideal for high-assurance supply-chain hardening because tags can move.
- Highest-value future hardening: pin third-party actions to full commit SHA and document update cadence.

## Recommendation

Adopt a phased approach:
1. Pin all third-party actions to full commit SHAs.
2. Keep the source version tag in comments or documentation for readability.
3. Review pins quarterly or when Dependabot/GitHub alerts indicate change.
