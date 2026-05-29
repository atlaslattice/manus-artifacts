# TIDELOCK Swarm — Batch-Label Taxonomy

```text
STATUS: COORDINATION ARTIFACT — CANDIDATE — NOT CANON
SCOPE: Label definitions and batch routing rules for TIDELOCK Swarm execution issues
AUTHORITY: NONE
```

---

## Purpose

Defines the label set, batch boundaries, and assignment routing rules used when opening
execution issues after the TIDELOCK Swarm Intake freeze (#232).

---

## Label families

### 1. Batch (execution group)

| Label | Meaning | Module coverage |
|---|---|---|
| `batch:A` | First execution group — foundation layers | Modules 1–3 |
| `batch:B` | Second execution group — integrity + governance | Modules 4–6 |
| `batch:C` | Third execution group — playability + parity | Modules 7–9 |
| `batch:D` | Fourth execution group — hardening + release | Modules 10–12 |

### 2. Wave (campaign wave alignment)

| Label | Meaning |
|---|---|
| `wave:01` … `wave:12` | Maps to the 12 waves in `aetherforge-next144-taskboard-2026-05-28.md` |
| `wave:next12-worldclass` | Overflow/new worldclass tasks beyond Wave 12 |

### 3. Difficulty

| Label | Meaning |
|---|---|
| `difficulty:low` | Estimated < 2 hours; no cross-lane dependencies |
| `difficulty:med` | Estimated 2–8 hours; up to 2 cross-lane dependencies |
| `difficulty:high` | Estimated > 8 hours; 3+ dependencies or novel work |

### 4. Status

| Label | Meaning |
|---|---|
| `status:unassigned` | Intake accepted; no owner yet |
| `status:assigned` | Owner confirmed |
| `status:blocked` | Waiting on a dependency |
| `status:in-progress` | Active work underway |
| `status:review` | PR or artifact in review |
| `status:done` | Completed with receipt |

### 5. Dependency

| Label | Meaning |
|---|---|
| `dep:none` | No blocking dependencies |
| `dep:internal` | Depends on another task in same batch |
| `dep:cross-batch` | Depends on a task in a different batch |
| `dep:external` | Depends on work outside this repository |

### 6. Owner / team routing

| Label | Meaning |
|---|---|
| `team:kg` | Knowledge graph + indexing work |
| `team:governance` | Canon, trust-state, ratification work |
| `team:playability` | Aetherforge quest-loop work |
| `team:schema` | GPTDream++ schema + reference impl work |
| `team:ci` | CI, quality gates, tooling work |
| `team:contributor-ux` | Onboarding, templates, contributor experience |
| `team:release` | Public release readiness and benchmarks |

### 7. Planning meta

| Label | Meaning |
|---|---|
| `planning` | Coordination or planning artifact |
| `coordination` | Cross-team coordination required |
| `blocker` | This task blocks others — resolve first |

---

## Batch boundaries and sequencing rules

```text
Batch A (Modules 1–3)  →  Foundation first
  - Prerequisites: none
  - Must complete: core graph contract, inventory, link integrity baseline
  - Gate to Batch B: all `dep:internal` tasks in Batch A resolved

Batch B (Modules 4–6)  →  Integrity + governance
  - Prerequisites: Batch A `status:done` tasks ≥ 80%
  - Must complete: metadata normalization, governance validators, navigation hardening
  - Gate to Batch C: Batch B `difficulty:high` tasks reviewed and receipted

Batch C (Modules 7–9)  →  Playability + parity
  - Prerequisites: Batch B foundation tasks done
  - Must complete: quest schema, GPTDream++ parity, adversarial coverage
  - Gate to Batch D: Batch C adversarial tests all green in CI

Batch D (Modules 10–12)  →  Hardening + public release
  - Prerequisites: Batch C CI gate green
  - Must complete: CI hardening, contributor UX, world-class release packet
  - Completion: publish state-of-graph v1 + world-class scorecard (NX-143, NX-144)
```

---

## Divvy algorithm (post-freeze pass)

1. **Dependency sort** — tasks with `dep:none` or `dep:internal` scheduled before `dep:cross-batch`
2. **Difficulty sort** — within a batch, `difficulty:low` opens first to clear quick wins
3. **Capacity routing** — `team:*` label determines which contributor pool sees the issue
4. **Blocker flag** — any task with `blocker` label jumps to top of its batch queue
5. **Owner assignment** — preferred owner from intake form set as GitHub assignee
6. **Unassigned fallback** — `status:unassigned` + `help wanted` added if no owner available

---

## Issue title format

```
[BATCH-X][NX-###] <Task short name> — <Module name>
```

Example:
```
[BATCH-A][NX-001] Freeze ontology v1 for nodes/edges — Core graph contract
```

---

## Linked surfaces

- Intake issue: [#232](https://github.com/atlaslattice/manus-artifacts/issues/232)
- Freeze comment template: [`projects/tidelock-swarm-intake-freeze-comment-template-2026-05-29.md`](./tidelock-swarm-intake-freeze-comment-template-2026-05-29.md)
- Execution board: [`projects/aetherforge-next144-taskboard-2026-05-28.md`](./aetherforge-next144-taskboard-2026-05-28.md)
- Campaign board: [`projects/aetherforge-144-task-campaign-2026-05-27.md`](./aetherforge-144-task-campaign-2026-05-27.md)
