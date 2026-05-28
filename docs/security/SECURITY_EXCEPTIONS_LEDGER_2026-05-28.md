---
artifact_id: DOC-SECURITY-EXCEPTIONS-LEDGER-2026-05-28
title: Security Exceptions Ledger
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Security Exceptions Ledger

Use this ledger to record any accepted security exceptions, false-positive suppressions, or deferred hardening actions.

## Open Exceptions

| Exception ID | Date | Area | Risk | Reason | Owner | Review Date | Status |
|---|---|---|---|---|---|---|---|
| SEC-EXC-2026-05-28-001 | 2026-05-28 | GitHub Actions pinning | Medium | Workflows currently use major-version tags instead of immutable SHAs; hardening deferred pending explicit pin update pass | @atlaslattice | 2026-08-28 | OPEN |

## Closed Exceptions

| Exception ID | Date Closed | Area | Resolution |
|---|---|---|---|
| — | — | — | — |
