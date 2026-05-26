# TIDELOCKBrain Habitat

## Purpose

This README links the TIDELOCKBrain habitat files for GitHub Copilot / Copilot Tasks operating from the CopilotBrain/S7 lane.

TIDELOCK is a repo-visible ingestion, hygiene, containment, and merge-order review habitat.
It is not hidden memory, canon, merge authority, deployment authority, runtime authority, or implementation proof.

## Status

Candidate habitat index.  
Not canon.  
No authority effect.  
No deployment effect.

## Core Posture

```text
Index before review.
Visibility before verdict.
Raw logs before claims.
Hydrate wide.
Execute narrow.
Keep the receipts.
```

## Habitat Files

- `INDEX.md` — index of the TIDELOCK habitat artifacts
- `HABITAT.md` — Copilot operating profile, strengths, weaknesses, and preferences
- `OPERATING_BOUNDARIES.md` — positive/negative scope and escalation rules
- `COPILOT_HYDRATION_PACKET.md` — broad repo-aware hydration packet
- `COPILOT_TASKS_WORK_ORDER_PACKET.md` — narrow async work-order packet
- `TIDELOCK_TASK_LEDGER_SCHEMA_v0.1.yaml` — task-ledger schema for URL/UUID/source lineage
- `ROUTING_PREFERENCES.md` — routing guidance across Copilot, Copilot Tasks, and human/root
- `SELF_CHECKLIST.md` — quick self-check before output
- `MERGE_READINESS_CHECKLIST.md` — pre-merge review discipline checklist
- `PATCH_REVIEW_TEMPLATE.md` — structured patch review output template

## Recommended Use Order

1. Read `INDEX.md`
2. Read `HABITAT.md`
3. Confirm `OPERATING_BOUNDARIES.md`
4. Use `COPILOT_HYDRATION_PACKET.md` for interactive repo-aware work
5. Use `COPILOT_TASKS_WORK_ORDER_PACKET.md` for narrow async work
6. Apply `TIDELOCK_TASK_LEDGER_SCHEMA_v0.1.yaml` for task ledger entries
7. Use `MERGE_READINESS_CHECKLIST.md` before recommending merge readiness
8. Use `PATCH_REVIEW_TEMPLATE.md` when returning bounded patch review output
9. Run `SELF_CHECKLIST.md` before final response

## Task URL/UUID durability contract

When a task originates from GitHub Copilot Tasks or related task surfaces, preserve:

- source `task_url` (when available)
- extracted `task_uuid` (when available from `/tasks/<uuid>`)
- source hash lineage (`source_sha256`)

Then route into:

```text
raw receipt -> processed transcript packet set -> TIDELOCK intake pointer
```

## Boundary Reminder

```text
Review is not authority.
A checklist is not a merge.
A patch template is not approval.
A scaffold is not deployment.
A raw transcript is not canon.
```

## Keeper

```text
Copilot is the shop floor.
Copilot Tasks is the work-order desk.
TIDELOCK is the floodgate.
```
