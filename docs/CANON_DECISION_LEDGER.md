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
| CDL-2026-05-29-004 | 2026-05-29 | docs/CANON_SURFACE_MAP.md | — | candidate | pending | @atlaslattice (pending adjudication) | WORK | New artifact: authority map capturing website=canon, GitHub=workspace governance state. |
| CDL-2026-05-29-003 | 2026-05-29 | docs/ADJUDICATION_TRAIL.md | — | candidate | pending | @atlaslattice (pending adjudication) | WORK | New artifact: durable append-only governance event log. |
| CDL-2026-05-29-002 | 2026-05-29 | projects/LIVING_EXECUTION_BOARD.md | — | candidate | pending | @atlaslattice (pending adjudication) | WORK | New artifact: always-current single-source execution board. |
| CDL-2026-05-29-001 | 2026-05-29 | (multiple — 7-pillar plan) | candidate | candidate | pending | @atlaslattice (directed execution) | WORK | 7-pillar world-class plan executed: 8 new artifacts, 5 updates. No canon promotion; all candidate. |
| CDL-2026-05-28-001 | 2026-05-28 | projects/aetherforge-144-task-campaign-2026-05-27.md | candidate | candidate | pending | @atlaslattice (pending adjudication) | WORK | Mission-tracking updates only; no canon promotion. |

## Rules

- Do not delete prior decisions.
- Use append-only updates.
- Include `ratification_event_id` for every non-candidate promotion.
