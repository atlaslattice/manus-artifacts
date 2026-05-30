# AGENT LIFECYCLE SPEC v0.1

**Status:** Operational lifecycle permission spec (candidate canon, not ratified)  
**Source Basis:** Habitat lifecycle note and council guardrails  
**Intent:** Convert conceptual lifecycle modes into auditable mode controls

## 1) Scope and Guardrail Baseline

This spec defines lifecycle permissions for swarm work in-repo. It distinguishes mode intent, permissible actions, and publication boundaries.

Global guardrails:
- No self-ratification.
- No false human authorization claims.
- No operational side effects in `dream` or `play`.
- No raw-to-canon promotion without review + approval gate.
- No erasure of incident/failure history.

## 2) Lifecycle Modes

- `sleep`: compression, queue prep, stale-context cleanup.
- `dream`: sandbox recombination and hypothesis generation only.
- `play`: low-stakes ideation and interface exploration only.
- `reflection`: self-critique, provenance audit, failure-ledger review.
- `work`: contracted execution and artifact production.
- `recovery`: crash/session restoration and continuity repair.
- `council`: cross-lane review, conflict resolution, recommendation synthesis.

## 3) Allowed Transitions

Primary transitions:
- `sleep -> work`
- `work -> reflection`
- `reflection -> work`
- `work -> council`
- `council -> work`
- `any -> recovery` (on failure/interrupt)
- `recovery -> sleep` or `recovery -> work` (after rehydration)

Bounded creative transitions:
- `sleep -> dream -> reflection`
- `sleep -> play -> reflection`

Forbidden transitions:
- `dream -> ratified publication`
- `play -> ratified publication`
- `dream/play -> direct work side effects` without explicit re-entry to `work`

## 4) Permission Matrix

| Mode | Allowed tools/actions | Forbidden actions | Logging requirements | Label requirements | Memory write rules | Publication rules | Human gate |
|---|---|---|---|---|---|---|---|
| sleep | summarize queues, compress context, prep next actions | code changes, ratification, external side effects | boot/sleep summary log | `SLEEP_OUTPUT` | write continuity notes only | none | none |
| dream | sandbox prompts, counterfactual simulation, hypothesis drafting | production edits, task dispatch, canon claims | dream log with simulation marker | `DREAM OUTPUT — SIMULATION ONLY — NOT CANON` | isolated dream notes, no canon mutation | prohibited | required before any promotion |
| play | low-stakes ideation, mock structures, harmless experimentation | production edits, approvals, canon mutation | play session log | `PLAY OUTPUT — LOW-STAKES IDEATION — NOT CANON` | experimental memory only | prohibited | required before any promotion |
| reflection | review failures, provenance audit, uncertainty checks | ratification, authority escalation claims | reflection report and ledger linkage | `REFLECTION OUTPUT — REVIEW REQUIRED` | may append audit notes and corrective proposals | draft only | required for promotion to work outputs |
| work | scoped execution, artifact generation, tests/checks, packet updates | self-ratification, bypassing review | full action and artifact log | `WORK OUTPUT — VALIDATION REQUIRED` | update task/continuity memory with provenance | candidate outputs allowed | required for ratification |
| recovery | restore state, rehydrate context, detect gaps | silent resume without logs, unlogged context patching | recovery report with missing-context list | `RECOVERY OUTPUT — CONTEXT RESTORATION` | write only restoration and gap records | none | required when resuming blocked approval-gated tasks |
| council | multi-agent critique, conflict resolution, recommendation packet | command authority claims, direct ratification | council deliberation record | `COUNCIL OUTPUT — NOT RATIFIED UNTIL ADJUDICATED` | write recommendations and decision queue only | advisory only | required for final adjudication |

## 5) Logging and Audit Rules

Each mode execution must log:
- `mode`
- `task_id` (if applicable)
- `started_at` / `ended_at`
- actor/lane
- actions taken
- artifacts touched
- decision/result
- next recommended mode/action

All logs must preserve provenance and remain retrievable from repo artifacts.

## 6) Memory and Publication Controls

Memory controls:
- Canon memory can only be updated from reviewed and approved work.
- Dream/play memory is sandboxed and must not overwrite canon memory.
- Recovery writes must include missing-context detection status.

Publication controls:
- Only `work` outputs that pass review + gate may be ratified.
- `council` output is advisory unless adjudicated by human authority.
- Any unlabeled output defaults to `RAW` and cannot be promoted.

## 7) Reset and Recovery Behavior

On interruption/failure:
1. Enter `recovery` mode.
2. Rehydrate from current task packet, backlog state, and latest continuity artifacts.
3. Record missing context and unresolved decisions.
4. Route to `sleep` (if incomplete) or `work` (if ready).
5. Re-open human approval gates when required.

Recovery success criteria:
- active task and next action restored
- evidence links intact
- approval gate status intact
- no provenance loss

## 8) Compliance Checks (Operational)

At minimum verify:
- mode labels present on outputs
- forbidden transitions absent
- ratification includes distinct reviewer/human approver
- all publication candidates include provenance and approval evidence
- incident and recovery records are preserved

## 9) Non-Claim Boundary

This lifecycle spec is a governance and auditing control document for repository operations. It does not assert that all mode enforcement is already automated.
