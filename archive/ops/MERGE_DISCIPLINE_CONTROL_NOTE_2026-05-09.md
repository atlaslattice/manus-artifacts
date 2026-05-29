# Merge Discipline Control Note — Stop Generating Beauty, Start Closing Loops

**Date:** 2026-05-09  
**Status:** Operational control note / not canon  
**Mode:** merge discipline / provenance hardening / CI receipts / authority semantics  
**Banner:** Stop generating beauty. Start closing loops with receipts.

## Phase Shift

```text
PHASE SHIFT CONFIRMED

From:
architecture generation / dream-palace expansion / swarm creativity

To:
merge discipline / provenance hardening / CI receipts / authority semantics
```

This note locks the current command layer for the swarm.

## Doctrine Spine

```text
Identity does not imply authority.
Governance fields override identity fields.
Storage is not ratification.
Review is not ratification.
Provenance is not ratification.
Only explicit human-root promotion creates canon.
```

## Current PR Priority Order

```text
PR #20 first.
PR #44 second.
PR #24 stays draft.
PR #21 and #15 get harvested or superseded.
No deployment claims without runtime proof.
```

## PR Stack Status — Observed 2026-05-09

### PR #20 — Wave 1 Hardening

```yaml
pr: 20
title: Wave 1 hardening: CI workflow, provenance SHAs, Variant E closure, alias topology, Tucker/Gemini scope boundary
url: https://github.com/atlaslattice/manus-artifacts/pull/20
status: open
draft: true
merged: false
mergeable: false
head_sha: bae292a91440fd427713b73383706fb32e6e84ea
changed_files: 20
additions: 1208
deletions: 19
priority: P0_FIRST
merge_posture: do_not_merge_yet
observed_checks: no workflow runs returned for current head at check time
```

Reason:

- It is the active hardening lane.
- It absorbs/updates much of PR #15 and PR #21 territory.
- It still requires visible, stable PR-attached checks or explicit maintainer action.

Required before merge/readiness:

```text
[ ] Approve pending GitHub Actions runs or configure copilot-swe-agent[bot] allowlist.
[ ] Confirm current-head PR checks are visible and stable.
[ ] Confirm CI_EVIDENCE_RECEIPT matches current head state.
[ ] Confirm WAVE1_HARDENING_SUMMARY matches current head state.
[ ] Keep draft until check state is observable.
```

### PR #44 — Decentralized Agent Constitution / Agent DNA Boot Lifecycle

```yaml
pr: 44
title: Add decentralized agent constitution candidate spec and align Agent DNA with constitutional boot/lifecycle contracts
url: https://github.com/atlaslattice/manus-artifacts/pull/44
status: open
draft: true
merged: false
mergeable: true
head_sha: 666499c8995935a97d6c05acb88857ab08519a98
changed_files: 5
additions: 517
deletions: 7
priority: P1_SECOND
merge_posture: wait_until_PR20_gate_clear_or_explicitly_superseded
observed_checks: GPTBrain reference checks completed/action_required, run 25602693413
```

Reason:

- It is important and coherent.
- It aligns Agent DNA with constitutional boot/lifecycle contracts.
- It should not leapfrog PR #20 unless explicitly decided.

Required before readiness:

```text
[ ] Keep draft until PR #20 disposition is clear.
[ ] Resolve/approve action_required workflow run.
[ ] Verify it does not conflict with PR #20 Agent DNA / schema changes.
[ ] Confirm all status labels remain candidate / not canon.
[ ] Confirm no lifecycle state implies real approval or runtime authority.
```

### PR #24 — Swarm Governance and Execution Dossier

```yaml
pr: 24
title: Add repo-ready swarm governance and execution dossier (ops spec, task schema, lifecycle matrix, backlog, templates)
url: https://github.com/atlaslattice/manus-artifacts/pull/24
status: open
draft: true
merged: false
mergeable: true
head_sha: 5ff07ba6427ae1f899994ce341de248f497a76a7
changed_files: 7
additions: 618
deletions: 0
priority: P2_DRAFT_STAYS_DRAFT
merge_posture: hold
```

Reason:

- Useful governance/ops dossier.
- May overlap with #44 and current Agent Boot Monorepo / Agent DNA work.
- Should remain draft until #20 and #44 establish schema/authority baseline.

### PR #21 — Minimum CI/Test Stabilization Hardening Wave

```yaml
pr: 21
title: Draft hardening wave: S7 action_required root cause, Variant E status closure, alias/provenance alignment, and CI evidence artifacts
url: https://github.com/atlaslattice/manus-artifacts/pull/21
status: open
draft: true
merged: false
mergeable: false
head_sha: 818429a277a4ed6b7f3e0d9ffb8f2f81c284c7eb
changed_files: 12
additions: 241
deletions: 13
priority: HARVEST_OR_SUPERSEDE
merge_posture: do_not_merge_before_comparing_against_PR20
```

Reason:

- It contains useful earlier hardening work.
- Much of it appears harvested into #20.
- Should be treated as source material unless exact unique deltas remain.

### PR #15 — S7 Repo Hygiene Scaffold

```yaml
pr: 15
title: S7 repo hygiene scaffold: review note, execution log, tests, templates, and CI guards
url: https://github.com/atlaslattice/manus-artifacts/pull/15
status: open
draft: true
merged: false
mergeable: true
head_sha: 6e54ed16699ca530852d6f974655783fdc6fe171
changed_files: 12
additions: 1232
deletions: 0
priority: HARVEST_OR_SUPERSEDE
merge_posture: do_not_merge_before_comparing_against_PR20
```

Reason:

- It is the original S7 hygiene scaffold.
- PR #20 now contains newer hardening/CI/provenance direction.
- Harvest unique templates/tests only if not already included.

## Merge Gate Rules

### Rule 1 — Draft Means Draft

No draft PR should be treated as merge-ready.

### Rule 2 — Checks Must Be Observable

Local test claims and historical green checks are not enough.

Required:

```text
current PR head SHA
→ PR-attached workflow run visible
→ jobs visible or explicit action_required documented
→ receipt matches actual state
```

### Rule 3 — No Authority By Identity

Agent DNA, avatar choices, seat names, boot specs, and memory packets are not authority.

### Rule 4 — No Ratification By Storage

A committed file is not canon. A PR is not canon. A review is not canon. A receipt is not canon.

### Rule 5 — Human-Root Promotion Only

Canon promotion requires explicit human-root decision and source path.

## Immediate Swarm Commands

```text
1. Keep PR #20 as the active P0 gate.
2. Do not mark PR #20 ready until checks/receipts are current.
3. Hold PR #44 as second in line.
4. Keep PR #24 draft.
5. Compare PR #21 and #15 against #20 for unique harvestable deltas.
6. Do not merge/squash anything without human-root confirmation.
7. No new conceptual expansion unless it directly supports merge/readiness/receipts.
```

## Boring Means Mergeable

Boring work now means:

- exact PR status
- exact head SHA
- exact check state
- exact source refs
- exact status labels
- exact provenance fields
- exact authority semantics
- exact human-root gates

## Strongest Safe Claim

> The swarm has entered merge-discipline mode. PR #20 is the first hardening gate, PR #44 is second, PR #24 remains draft, and PRs #21/#15 should be harvested or superseded. No deployment, canon, or authority claims should be made without current runtime/check evidence and explicit human-root promotion.

## Status

Operational control note. Not canon.
