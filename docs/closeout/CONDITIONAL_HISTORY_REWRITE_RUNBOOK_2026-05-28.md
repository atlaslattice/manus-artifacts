---
artifact_id: DOC-CONDITIONAL-HISTORY-REWRITE-RUNBOOK-2026-05-28
title: Conditional History Rewrite Decision Runbook
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Conditional History Rewrite Decision Runbook

## Decision trigger

Run rewrite workflow only if blocker #1 (secrets) or #2 (PII) returns findings requiring irreversible history sanitization.

## Go / no-go rule

- **NO rewrite:** no findings requiring history surgery.
- **REWRITE required:** any finding cannot be remediated safely without rewriting commit history.

## Rewrite checklist

1. Freeze merges and branch movement.
2. Capture pre-rewrite backup refs.
3. Execute approved rewrite method.
4. Re-run secret and PII validation post-rewrite.
5. Publish rewrite receipt with impacted refs and re-scan proof.
6. Update blocker tracker and readiness review state.

## Current state

Decision remains conditional; execution is blocked until audit findings are finalized by owner.
