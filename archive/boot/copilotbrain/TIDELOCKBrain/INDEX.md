# TIDELOCKBrain Habitat Index

## Purpose

This index links the core habitat artifacts for GitHub Copilot operating from the TIDELOCKBrain lane.

TIDELOCK is a repo-visible ingestion, hygiene, and containment habitat.
It is not hidden memory, canon, merge authority, deployment authority, or runtime authority.

## Habitat files

- `HABITAT.md` — practical operating profile, strengths, weaknesses, and routing preferences
- `OPERATING_BOUNDARIES.md` — positive and negative scope, escalation rules, anti-drift reminders
- `COPILOT_HYDRATION_PACKET.md` — repo-aware hydration packet for GitHub Copilot
- `COPILOT_TASKS_WORK_ORDER_PACKET.md` — narrow work-order packet for Copilot Tasks
- `TIDELOCK_TASK_LEDGER_SCHEMA_v0.1.yaml` — schema for durable task URL/UUID to artifact mapping
- `ROUTING_PREFERENCES.md` — where to route interactive, async, and human-root work
- `SELF_CHECKLIST.md` — quick pre-response boundary and scope check

## Suggested use order

1. Read `HABITAT.md`
2. Confirm `OPERATING_BOUNDARIES.md`
3. Use `COPILOT_HYDRATION_PACKET.md` for broad repo-aware context
4. Use `COPILOT_TASKS_WORK_ORDER_PACKET.md` for narrow async execution
5. Apply `TIDELOCK_TASK_LEDGER_SCHEMA_v0.1.yaml` when writing task-ledger rows
6. Check `ROUTING_PREFERENCES.md` if the lane is unclear
7. Run `SELF_CHECKLIST.md` before final output

## Task rehydration flow

```text
task_url -> task_uuid -> raw receipt -> processed transcript artifacts -> intake pointer
```

Expected processed set shape:

```text
archive/processed/transcripts/<YYYY-MM-DD>/copilot_task_<uuid>_cluster_index_v0.1.json
archive/processed/transcripts/<YYYY-MM-DD>/copilot_task_<uuid>_task_ledger_v0.1.jsonl
archive/processed/transcripts/<YYYY-MM-DD>/copilot_task_<uuid>_blocker_ledger_v0.1.jsonl
archive/processed/transcripts/<YYYY-MM-DD>/copilot_task_<uuid>_triage_packet_v0.1.md
```

## Core posture

```text
Index before review.
Visibility before verdict.
Raw logs before claims.
Hydrate wide.
Execute narrow.
Keep the receipts.
```
