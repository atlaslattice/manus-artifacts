# Aetherforge Quest-Loop Task-to-Artifact Playability Contract v0.1

```text
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DATE: 2026-05-28
SPRINT: AX-17
SCOPE: Defines the binding contract between sprint tasks and verifiable repo artifacts
```

## Executive Summary

Every Aetherforge sprint task must produce a verifiable chain from **task definition** → **in-repo artifact** → **validation receipt**. This contract specifies the minimum binding fields required to consider a task "playable" (auditable end-to-end by any council member or agent from cold boot).

---

## 1. Playability definition

A task is **playable** if and only if:

1. **Task card exists** in a committed sprint board (e.g. `projects/aetherforge-top10-taskboard-2026-05-28.md`)
2. **At least one artifact** was produced or mutated in-repo as a direct result of the task
3. **Validation passed** — tests or quality gates ran and passed after the change
4. **TIDELOCK receipt** exists under `archive/boot/copilotbrain/TIDELOCKBrain/` with:
   - `TIDELOCK_ACTIVITY_RECEIPT_<date>_<task_id>.md`
5. **Task card is checked** (`- [x]`) in the sprint board

If any of the five conditions is unmet, the task is **incomplete** and must not advance to ratification review.

---

## 2. Minimum playability fields per task

| Field | Required | Where stored |
|-------|----------|-------------|
| `task_id` | yes | Sprint board + receipt |
| `bounded_objective` | yes | Sprint board description |
| `artifacts_changed` | yes | Receipt — list of file paths |
| `tests_run` | yes | Receipt — list of commands + pass/fail |
| `blockers` | yes (empty list if none) | Receipt |
| `next_safest_action` | yes | Receipt |
| `receipt_path` | yes | Sprint board completion receipts section |
| `canon_status` | yes — must be `not_canon` | Receipt header |
| `deployment_status` | yes — must be `not_deployable` | Receipt header |

---

## 3. Artifact contract hierarchy

```
Sprint board (task card)
    └── In-repo artifact (doc / script / test / data)
            └── Validation receipt (quality gate output)
                    └── TIDELOCK triplet
                            ├── DREAM_JOURNAL_...md
                            ├── WAKE_REPORT_...md
                            └── DELTA_EXTRACTION_...md
```

Each layer is traceable upward (child → parent) and downward (parent → child) via explicit file links.

---

## 4. Playability quality gate (automated)

The following CI-equivalent check is enforced by `scripts/validate_lattice_quality_gates.py`:

- Required sprint board surfaces (`projects/aetherforge-top10-taskboard-2026-05-28.md`) must be present and root-reachable.
- REQUIRED_LINK_RELATIONSHIPS enforces navigation graph integrity between task boards.
- Metadata consistency checks verify candidate/no-authority markers on all sprint surfaces.

Manual playability audit (not yet automated):
- [ ] All `[x]` tasks in the sprint board have a matching `receipt_path` entry
- [ ] All `receipt_path` entries resolve to real files in the repo
- [ ] All receipts list `artifacts_changed` as non-empty

---

## 5. Known playability gaps (as of 2026-05-28)

| Gap | Impact | Resolution path |
|-----|--------|-----------------|
| 96.7% of markdown artifacts are under-linked | Graph traversal from root reaches only 44/780 artifacts | AX-13 remediation — systematic backlink seeding pass |
| No automated receipt-to-task-card validation | Manual audit required | Future NX-031 multi-hop lineage check |
| TIDELOCK receipts in `TIDELOCKBrain/` not cross-linked to task cards | Receipt exists but not discoverable from task | Add receipt_path entries to sprint board |

---

## 6. Metatron's Cube alignment

This contract maps to the **Metatron's Cube** framing:
- **Centre node**: `projects/aetherforge-top10-taskboard-2026-05-28.md` (active sprint)
- **6 fruit-of-life nodes**: six active tasks (AX-13 → AX-19)
- **Outer ring**: artifact receipts + TIDELOCKBrain logs
- **Connecting edges**: explicit `receipt_path` links in sprint board

Every task is an edge in the cube; every receipt is a vertex that locks the edge in place.

---

## 7. Related surfaces

- Sprint board: [`projects/aetherforge-top10-taskboard-2026-05-28.md`](../../../projects/aetherforge-top10-taskboard-2026-05-28.md)
- Quest loop cadence: [`LATTICE_QUEST_LOOP_CADENCE_v0.1.md`](./LATTICE_QUEST_LOOP_CADENCE_v0.1.md)
- Quest quality gate: [`AETHERFORGE_QUEST_QUALITY_GATE_v0.1.md`](./AETHERFORGE_QUEST_QUALITY_GATE_v0.1.md)
- Under-linked detector: [`scripts/detect_underlinked_artifacts.py`](../../../scripts/detect_underlinked_artifacts.py)
- Quarantine directive: [`quarantine/README.md`](../../../quarantine/README.md)
