---
artifact_id: DOC-DEPENDENCY-ALERT-RESPONSE-SLA-v0-1-2026-05-28
title: Dependency Alert Response SLA
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Dependency Alert Response SLA

## Purpose

Set response expectations for dependency and supply-chain alerts affecting reference implementations, workflows, or automation.

## SLA Table

| Severity | Response SLA | Resolution Target | Notes |
|---|---|---|---|
| Critical | 24 hours | 7 days | Immediate owner review required |
| High | 2 business days | 14 days | Prioritize before feature work |
| Medium | 5 business days | 30 days | Batch when safe |
| Low | 10 business days | 90 days | Track in backlog if non-exploitable |
| Informational | 30 days | As capacity allows | Document and review quarterly |

## Scope

In scope:
- GitHub Actions dependencies and third-party actions
- Python dependencies used by reference implementations
- Tooling dependencies required by CI validation

Out of scope:
- Links to external sites in markdown
- Non-executable archival references with no runtime path

## Escalation

- Any critical or high alert touching secret handling, CI execution, or schema validation must also be logged in the [Security Posture Report](./SECURITY_POSTURE_REPORT_2026-05-28.md).
- If a patch cannot be applied safely, create an entry in the [Security Exceptions Ledger](./SECURITY_EXCEPTIONS_LEDGER_2026-05-28.md).
