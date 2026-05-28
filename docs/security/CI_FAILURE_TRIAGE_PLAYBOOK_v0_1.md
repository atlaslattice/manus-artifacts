---
artifact_id: DOC-CI-FAILURE-TRIAGE-PLAYBOOK-v0-1-2026-05-28
title: CI Failure Triage Playbook
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# CI Failure Triage Playbook

## Purpose

Standardize first-response steps when GitHub Actions fail.

## Triage Flow

1. Identify failing workflow and job.
2. Classify failure type:
   - content/metadata failure,
   - link failure,
   - lint failure,
   - test failure,
   - infrastructure/transient failure,
   - secret/security failure.
3. Determine whether the failure is:
   - introduced by the current PR, or
   - pre-existing / unrelated.
4. Fix immediately if directly caused by the current change.
5. If unrelated, document it and avoid broad unrelated edits.

## Workflow-Specific Hints

| Workflow | Likely failure surface |
|---|---|
| `repo-hygiene-checks.yml` | merge markers, invalid workflow YAML |
| `docs-link-checks.yml` | broken relative markdown links |
| `markdown-lint.yml` | markdown formatting or layout warnings |
| `lattice-kg-quality-gates.yml` | metadata/frontmatter, lattice report integrity |
| `secret-scan.yml` | committed secrets or false positives |
| `gptbrain-reference-checks.yml` | missing Python deps, failing reference tests |

## Escalation Rules

- Secret findings escalate immediately to the security path.
- Repeated transient infra failures should be tracked separately from content bugs.
- Failures blocking release evidence should be noted in the [Security Posture Report](./SECURITY_POSTURE_REPORT_2026-05-28.md).
