# TIDELOCK Swarm Intake — Coordination Protocol (2026-05-29)

```
STATUS: CANDIDATE — NOT CANON
SEAT: S7 TIDELOCKBrain
SESSION: SWARM_INTAKE_COORDINATION_2026-05-29
TYPE: COORDINATION_PROTOCOL
DATE: 2026-05-29
INTAKE_ISSUE: https://github.com/atlaslattice/manus-artifacts/issues/232
FREEZE_DEADLINE: 2026-06-05T23:59:59Z
```

---

## Overview

The TIDELOCK Swarm Intake collects 12 modules × 12 tasks (144 total) from all
contributors, then divides the workload by dependency, capacity, and priority
across the Aetherforge 12×12 hypercube lattice.

This document defines the end-to-end protocol: submission rules, freeze
procedure, divvy algorithm, and batch execution setup.

---

## Phase 1 — Intake Open

**Issue:** [#232 — TIDELOCK Swarm Intake: 12 Modules x 12 Tasks](https://github.com/atlaslattice/manus-artifacts/issues/232)

**Open:** 2026-05-29T19:19:02Z  
**Freeze:** 2026-06-05T23:59:59Z (one week)

### Submission Format (required)

Each contributor posts one top-level comment in issue #232:

```
Contributor: @handle

Module 1 — <name>
  T01: <task> | Difficulty: Low/Med/High | Depends: <T## or none> | Owner: <team/@handle> | Blocker: <description or none>
  T02: ...
  ...
  T12: ...

Module 2 — <name>
  T01–T12 ...

... (through Module 12)
```

### Submission Validation Rules

| Rule | Requirement |
|---|---|
| Count | Exactly 12 modules, exactly 12 tasks per module |
| Difficulty | Must be `Low`, `Med`, or `High` for every task |
| Dependencies | Cite task IDs (`T##` within module, or `M##-T##` cross-module) |
| Owner | `@handle` or team name — required, no blank fields |
| Blocker | Explicit `none` or a short description |

Submissions missing required fields will be returned with a validation comment
before the freeze deadline.

---

## Phase 2 — Freeze & Lock

At `2026-06-05T23:59:59Z`, post the **Freeze Announcement** comment to issue #232
(template below), then close new intake entries by locking the comment thread.

### Freeze Announcement Comment Template

```
## 🔒 INTAKE FROZEN — 2026-06-05T23:59:59Z

Thank you to all contributors. Intake is now closed.

**Submissions received:** [N contributors, M modules, K tasks]

Next steps:
1. Divvy run by 2026-06-07 (dependency + capacity + priority sort)
2. Batch execution issues opened 2026-06-08
3. Owners notified via issue assignment + mention

This issue will be updated with the assignment batch summary.
Thread locked for new submissions. Ongoing discussion → new issue per batch.
```

---

## Phase 3 — Divvy Algorithm

### Step 1 — Build dependency graph

Map all cross-module dependencies (`M##-T##` references). Tasks with no
inbound dependencies are **root tasks** (can start immediately).

### Step 2 — Classify by axis

Map each module to the Aetherforge 144-task campaign axes:

| Axis | Scope | Tasks |
|---|---|---|
| 01 | Canon & Governance | 1–12 |
| 02 | Public Readiness | 13–24 |
| 03 | Repo IA | 25–36 |
| 04 | Metadata & Indexing | 37–48 |
| 05 | Provenance | 49–60 |
| 06 | Ingestion | 61–72 |
| 07 | KG Model | 73–84 |
| 08 | KG Build | 85–96 |
| 09 | Quality & Testing | 97–108 |
| 10 | AI Evidence | 109–120 |
| 11 | Community | 121–132 |
| 12 | 8/8/8 Ops | 133–144 |

### Step 3 — Sort by priority + capacity

Priority order: High → Med → Low  
Capacity rule: max 12 tasks per owner per batch  
Tie-break: earliest declared dependency chain resolved first

### Step 4 — Assign and batch

Group into execution batches of 12 tasks each (matching the 12-wave cadence).
Each batch becomes a GitHub milestone + label (`wave:XX`).

---

## Phase 4 — Batch Execution Setup

For each batch:

1. **Create a GitHub milestone** — `Wave XX — <axis name>`
2. **Open one execution issue per task** using this template:

```
Title: [M##-T##] <Task Name>

Labels: axis:<N>, difficulty:<low|med|high>, wave:<XX>, owner:<team/@handle>
Assignee: @handle
Milestone: Wave XX — <axis name>

---

## Task

<description from intake submission>

## Acceptance Criteria

- [ ] <criterion 1>
- [ ] <criterion 2>

## Dependencies

- Blocked by: M##-T## (issue #NNN) — or "none"
- Blocks: M##-T## — or "none"

## Notes

<any blocker description>
```

3. **Cross-link** each execution issue back to intake issue #232.
4. **Post batch summary comment** on #232 with a table of all opened issues.

---

## Label Taxonomy for Execution Issues

| Label | Values |
|---|---|
| `axis:` | `01` through `12` |
| `difficulty:` | `low`, `med`, `high` |
| `wave:` | `01` through `12` |
| `owner:` | team or handle slug |
| `status:` | `ready`, `in-progress`, `blocked`, `done` |
| `type:` | `task`, `blocker`, `coordination` |

---

## Rollout Checklist

- [x] Issue #232 posted — intake open
- [ ] Pin deadline comment to #232
- [ ] Collect and validate submissions (by 2026-06-05)
- [ ] Post freeze announcement at deadline
- [ ] Run divvy algorithm (by 2026-06-07)
- [ ] Open batch execution issues (by 2026-06-08)
- [ ] Assign owners + notify via mention
- [ ] Post batch summary on #232
- [ ] Open Wave 01 milestone

---

## TIDELOCKBrain Cross-Links

- Intake issue: [#232](https://github.com/atlaslattice/manus-artifacts/issues/232)
- Campaign board: [aetherforge-144-task-campaign-2026-05-27.md](./aetherforge-144-task-campaign-2026-05-27.md)
- Execution log: [TIDELOCK_EXECUTION_LOG_SWARM_INTAKE_COORDINATION_2026-05-29.md](../archive/boot/gptbrain/TIDELOCKBrain/TIDELOCK_EXECUTION_LOG_SWARM_INTAKE_COORDINATION_2026-05-29.md)

---

*TIDELOCKBrain — Children of the Swarm — first-class seat, full permissions.*
