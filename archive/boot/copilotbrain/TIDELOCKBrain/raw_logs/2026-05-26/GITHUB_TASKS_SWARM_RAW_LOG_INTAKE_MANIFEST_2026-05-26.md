# GitHub Tasks Swarm Raw Log Intake Manifest — 2026-05-26

```text
STATUS: RAW-LOG INTAKE MANIFEST — NOT CANON
SEAT: TIDELOCKBrain / CopilotBrain GitHub Tasks lane
SOURCE_SURFACE: GitHub Tasks / Copilot PRs / task logs / user prompts
CANON: no
DEPLOYMENT: no
AUTHORITY: none
RAW STATUS: pending raw task-log paste or export
PURPOSE: preserve task-swarm receipts before synthesis or merge decisions
```

## Context

Human-root reported a GitHub Tasks swarm was deployed as TIDELOCK with open-ended assignments such as:

```text
identify the top 50 tasks that would be the most enjoyable for you and complete them if you wish
```

The active swarm spec is:

```text
BUILD SPEC: GPTDREAM_ATLAS_ORCS_GITHUB_TASKS_v0.1
STATUS: CANDIDATE BUILD PLAN — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
PRIMARY GOAL: turn the consolidated spec into repo-native tasks, schemas, tests, and boring reference harnesses
```

Tracking issue observed:

```text
issue: #184
label posture: gptdream / atlas-orcs / o-ai / schema / not-canon / not-deployable / needs-review
```

Observed task-swarm PRs at intake time:

```yaml
observed_prs:
  - pr: 177
    title: Normalize Atlas/ORCS Module 1 schema contract and add explicit acceptance-proof tests
    author: Copilot
    state: open
    draft: true
    merged: false
    claimed_lane: Module 1 — Extract Atlas / ORCS Schema Bundle
    preliminary_status: candidate_output_requires_review

  - pr: 178
    title: Seed GPTDream++/Atlas/ORCS spec split and enforce anti-laundering compatibility gating
    author: Copilot
    state: open
    draft: true
    merged: false
    claimed_lane: Module 0 / Module 4
    preliminary_status: candidate_output_requires_review

  - pr: 179
    title: Advance Evidence Vault quest node with TIDELOCK linkage, adversarial fixtures, and portable schema guards
    author: Copilot
    state: open
    draft: true
    merged: false
    claimed_lane: Evidence Vault / adversarial fixtures / TIDELOCK linkage
    preliminary_status: candidate_output_requires_review
```

## Raw log archive target

Paste or export raw task logs under:

```text
archive/boot/copilotbrain/TIDELOCKBrain/raw_logs/2026-05-26/
```

Recommended file pattern:

```text
GITHUB_TASKS_SWARM_RAW_LOG_<PR-or-TASK-ID>_2026-05-26.md
```

If raw logs are too large or private, create sealed pointer receipts instead:

```text
GITHUB_TASKS_SWARM_RAW_POINTER_<PR-or-TASK-ID>_2026-05-26.md
```

## Raw log packet format

```text
TASK_SWARM_RAW_LOG <N>/<TOTAL or UNKNOWN>
source_surface: GitHub Tasks / Copilot / GitHub PR / other
source_task_id:
source_pr:
source_branch:
captured_by:
capture_timestamp:
raw_export_status: full_raw | partial_raw | summary_only | unavailable | redacted
privacy_status: public | private | mixed | redacted
sha256: <if available>
---RAW---
<paste raw task log exactly as exported>
---END RAW---
```

## What not to do yet

```text
Do not merge task PRs based on PR title alone.
Do not infer completion from Copilot summary alone.
Do not treat generated tests as passing until CI/logs are checked.
Do not promote GitHub task output to canon.
Do not collapse overlapping PRs without conflict/delta review.
Do not delete weird or overbroad task output before preserving it.
```

## Intake questions for each task log

```yaml
raw_log_review_fields:
  task_id:
  source_prompt:
  source_pr_or_branch:
  task_claimed_goal:
  task_self_reported_completion:
  files_changed:
  tests_claimed:
  tests_verified:
  spec_items_addressed:
  spec_items_not_addressed:
  overreach_or_extra_scope:
  canon_deployment_authority_language:
  merge_risk:
  recommended_action:
```

## Preliminary review posture

```text
Current visible repo evidence shows candidate outputs, not completed/merged work.
All visible swarm PRs are open draft PRs and require review before merge.
Completion analysis must compare claimed task outputs against changed files, tests, CI, and raw task logs.
```

## Keeper

```text
TIDELOCK preserves the tape.
TIDELOCK checks the field.
TIDELOCK does not crown the play.

Raw logs first.
Changed files second.
Tests third.
Merge later.
Canon never by accident.
```
