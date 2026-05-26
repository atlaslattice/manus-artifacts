# Continuity OS Repo Write -> Verify -> Receipt Protocol v0.1

```text
STATUS: SPRINT 0 PROTOCOL — DRY-RUN FIRST
CANON: no
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: local_dry_run_only
ISSUE: #129
```

## Purpose

Define the smallest trustworthy repository loop for Continuity OS / O_AI work:

```text
approved artifact -> scoped repo write -> fetch verification -> vault receipt -> next action
```

This protocol prevents a common failure mode:

```text
planned write == claimed landed state
```

Repo intent is not repo state. A file is not considered landed until fetched back or otherwise verified.

## Minimum loop

```text
1. Confirm execution contract.
2. Confirm write scope.
3. Write only the approved paths.
4. Fetch each written path from the target branch.
5. Record commit SHA and file SHA where available.
6. Emit vault receipt.
7. State next safest action.
```

## Pre-write checklist

```yaml
execution_contract_present: true
human_approval_status: approved | not_required_for_dry_run
mode: local_dry_run | simulated_write | approved_repo_write
blocked_actions_checked: true
canon_status: not_canon
deployment_status: not_deployable | local_dry_run_only
planned_paths_declared: true
verification_plan_declared: true
post_action_receipt_required: true
```

## Allowed Sprint 0 write targets

Allowed:

```text
schemas/
docs/
examples/
archive/product/
archive/knowledge_graph/ only for candidate inventories/review queues
```

Not allowed without a separate explicit approval contract:

```text
website canon surfaces
production config
secrets
deployment workflows
CI release gates
database migrations
external publication files
ratification records
```

## Verification receipt fields

Every repo write receipt should include:

```yaml
schema_version: continuity.vault_receipt.v0.1
receipt_id:
receipt_type: repo_write | post_write_fetch | verification_bundle
created_at:
repository:
branch:
commit_sha:
paths:
  - path:
    path_status: written | fetched | missing | simulated
    file_sha:
    sha256:
    hash_status: present | unavailable | not_applicable
source_refs:
hash_status:
hash_method:
hash_source_scope:
verification_status: fetch_verified | hash_verified | mismatch | blocked | simulated
verification_method: github_fetch | hash_compare | dry_run_simulation
canon_status: not_canon
deployment_status: not_deployable | local_dry_run_only
authority_scope: none | advisory | review | approved_write_only
summary:
blockers:
next_action:
```

## Branch and PR posture

Preferred path:

```text
feature branch -> draft PR -> review -> merge only after human-root / maintainer action
```

A branch or PR does not imply ratification, deployment, or canon.

## Mismatch handling

If fetch verification does not match the intended state:

```yaml
verification_status: mismatch
blockers:
  - fetched state did not match planned path/content
next_action: stop and patch contract or inspect branch state
```

Never summarize a mismatch as success.

## Hash handling

If a GitHub file SHA is available but a SHA-256 is not computed:

```yaml
hash_status: present
hash_method: git_blob_sha
hash_source_scope: repo_file
```

If a raw source hash is unavailable:

```yaml
hash_status: unavailable
hash_method: unknown
hash_source_scope: unknown
```

If hashing does not apply to the artifact:

```yaml
hash_status: not_applicable
hash_method: none
hash_source_scope: not_applicable
```

## Human-facing final receipt format

Final responses after a write should include:

```text
repository:
branch:
paths:
commit_sha:
file_sha_if_available:
verification_status:
canon_status:
deployment_status:
authority_scope:
next_action:
```

## Keeper

```text
Write small.
Fetch back.
Name the branch.
Name the path.
Name the receipt.
No touchdown until replay confirms the ball crossed the line.
```
