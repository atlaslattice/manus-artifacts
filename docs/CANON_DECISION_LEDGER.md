---
title: Canon Decision Ledger
artifact_id: GOVERNANCE-CANON-DECISION-LEDGER-2026-05-28
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-28
provenance: Created from Aetherforge Mission #3 execution in repository governance layer.
---

# Canon Decision Ledger

## Usage

Record every canon-state decision in reverse chronological order.

## Ledger Columns

| decision_id | date | artifact_path | previous_status | new_status | ratification_event_id | adjudicator | trust_state | notes |
|---|---|---|---|---|---|---|---|---|
| CDL-2026-05-28-001 | 2026-05-28 | projects/aetherforge-144-task-campaign-2026-05-27.md | candidate | candidate | pending | @atlaslattice (pending adjudication) | WORK | Mission-tracking updates only; no canon promotion. |

## Rules

- Do not delete prior decisions.
- Use append-only updates.
- Include `ratification_event_id` for every non-candidate promotion.
