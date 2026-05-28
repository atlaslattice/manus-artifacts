---
artifact_id: DOC-SECURITY-POSTURE-REPORT-2026-05-28
title: Security Posture Report
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Security Posture Report

## Reporting Window

Snapshot date: 2026-05-28

## Current Controls

| Control | State | Evidence |
|---|---|---|
| Secret scanning on pushes and PRs | Present | [`secret-scan.yml`](../../.github/workflows/secret-scan.yml) |
| Workflow YAML linting | Present | [`repo-hygiene-checks.yml`](../../.github/workflows/repo-hygiene-checks.yml) |
| Docs link validation | Present | [`docs-link-checks.yml`](../../.github/workflows/docs-link-checks.yml) |
| Markdown lint visibility | Present (non-blocking) | [`markdown-lint.yml`](../../.github/workflows/markdown-lint.yml) |
| Metadata/lattice validation | Present | [`lattice-kg-quality-gates.yml`](../../.github/workflows/lattice-kg-quality-gates.yml) |
| Private vulnerability reporting path | Present | [`SECURITY.md`](../../SECURITY.md) |

## Risks / Gaps

| Gap | Severity | Notes |
|---|---|---|
| GitHub Actions are tag-pinned, not SHA-pinned | Medium | Supply-chain hardening gap |
| No documented dependency-alert SLA prior to this pack | Medium | Now addressed in policy artifact |
| No formal security exceptions ledger prior to this pack | Medium | Now addressed in ledger artifact |
| No branch protection recommendation document prior to this pack | Medium | Now addressed in recommendation artifact |
| No scheduled secret-scan run | Low | Current push/PR coverage still broad |

## Open Recommendations

1. Adopt SHA pinning for third-party actions.
2. Apply recommended required checks and branch protections.
3. Review exceptions ledger quarterly.
4. Add scheduled rescans if repo risk profile increases.
