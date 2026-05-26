# Continuity OS Execution Contract Protocol v0.1

```text
STATUS: SPRINT 0 PROTOCOL — DRY-RUN / FIXTURE-BACKED
CANON: no
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: local_dry_run_only
ISSUE: #129
```

## Purpose

Make action explicit before anything mutates.

An execution contract is the boundary object between a proposed artifact and an allowed action. It records what may happen, what may not happen, what approval exists, and what verification must follow.

```text
Repo intent is not repo state.
Simulation is not execution.
Receipt is not approval.
The lamp is not a green light.
```

## Sprint 0 operating rule

Sprint 0 defaults to:

```text
artifact -> review packet -> validation -> simulated write -> verification receipt
```

Live mutation is not the first-pass default. A repo write may occur only when the user explicitly commands it or the execution contract records approved write scope.

## Execution classes

```yaml
class_0_noop:
  meaning: inspect, summarize, or classify only
  mutation_allowed: false

class_1_draft:
  meaning: draft an artifact, plan, issue body, or patch text
  mutation_allowed: false

class_2_dry_run:
  meaning: simulate planned writes and emit a dry-run receipt
  mutation_allowed: false

class_3_repo_write:
  meaning: write an approved file or branch-scoped patch
  mutation_allowed: true
  approval_required: true
  verification_required: true

class_4_external_action:
  meaning: send, post, submit, invite, or mutate an external service
  mutation_allowed: blocked in Sprint 0

class_5_deployment:
  meaning: deploy infrastructure or runtime
  mutation_allowed: blocked in Sprint 0
```

## Required contract fields

```yaml
schema_version: continuity.execution_contract.v0.1
contract_id:
created_at:
requested_action:
execution_class:
mode:
authority_scope:
human_approval:
  required:
  status:
  approver:
  approval_ref:
target_repository:
target_branch:
base_branch:
planned_paths:
preconditions:
blocked_actions:
verification_plan:
post_action_receipt_required: true
canon_status: not_canon
deployment_status: not_deployable | local_dry_run_only
next_action:
```

## Approval rule

A contract must not treat context, memory, prior project direction, or model confidence as permission.

Valid approval sources:

```text
explicit user command in the active thread
reviewed issue checklist that names the action
human-root approval artifact
approved PR review/comment that names the action
```

Invalid approval sources:

```text
model preference
repo artifact presence
candidate packet language
source similarity
resonance across models
retrieved memory
unratified council signal
```

## Blocked actions by default

```text
canon_promotion
deployment
secret_access
database_mutation
external_send
public_post
sovereign_payload_routing
training_use
unverified_claim_promotion
lineage_erasure
```

## Repo write contract

For a class 3 repo write, the contract must declare:

```yaml
mode: approved_repo_write
authority_scope: approved_write_only
human_approval:
  required: true
  status: approved
post_action_receipt_required: true
verification_plan:
  method: github_fetch_after_write
  required_outputs:
    - repository
    - branch
    - path
    - commit_sha
    - file_sha
    - verification_receipt
    - next_action
```

## Verification rule

No action is complete until target state is checked.

For repository writes, verification means:

```text
1. Fetch the written path from the target branch.
2. Record repository, branch, path, commit SHA, and file SHA where available.
3. Record hash status honestly.
4. Emit a vault receipt.
5. State next safest action.
```

## Dry-run rule

A dry run should emit a receipt with:

```yaml
receipt_type: dry_run_write_plan
verification_status: simulated
verification_method: dry_run_simulation
paths:
  - path:
    path_status: simulated
canon_status: not_canon
deployment_status: local_dry_run_only
authority_scope: none | advisory | review
```

Dry-run receipt is not deployment, not proof, and not permission for a later live write.

## Failure behavior

If verification fails, emit:

```text
verification_status: mismatch | blocked
blocker_level: blocking
next_action: manual review / patch contract / retry only after approval
```

Do not silently retry external actions. Do not claim success from intended state.

## Keeper

```text
Intent drafts the play.
Contract marks the boundary.
Verification checks the field.
Receipt records the whistle.
Human-root owns the call.
```
