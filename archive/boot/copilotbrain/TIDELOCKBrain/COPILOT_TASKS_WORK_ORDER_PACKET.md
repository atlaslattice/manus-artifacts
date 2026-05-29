# Copilot Tasks Work-Order Packet

## Purpose

Use this packet for narrow, scoped execution tasks related to TIDELOCK artifacts.

## Task mode

```text
Scoped async task execution only.
```

## Default target shape

A task should point to:

- one PR, or
- one issue, or
- one exact file group

## Required output

```yaml
task_ref:
  task_id: ""
  task_url: ""
  task_uuid: ""
  source_surface: github_copilot_tasks | github_issue | github_pr | direct_request | unknown
  source_sha256: ""
verdict: approve | patch | block
blockers: []
patch_items: []
file_by_file_notes: []
raw_vs_parsed_status: ""
authority_boundary_status: ""
relation_to_linked_issues: ""
next_safest_action: ""
```

## Task lineage mapping

For durable rehydration, map GitHub task URLs into repo artifacts:

```text
task_url -> task_uuid -> raw receipt -> processed packet set -> intake pointer
```

Required minimum:

- `task_url` should preserve the original task link when available
- `task_uuid` should be extracted from `/tasks/<uuid>` when available
- `source_sha256` should identify the ingested source body or source receipt

If URL/UUID is unavailable, mark explicitly as empty or `unknown` rather than inferred.

## Do not

- infer hidden Copilot memory
- broaden into identity doctrine unless required by the scoped task
- claim canon
- claim deployment
- claim merge authority
- mutate beyond explicit task scope

## Boundary

```text
No merge.
No canon.
No deployment.
No authority.
```

## Good task examples

- Review PR #65 and return blockers and patch items.
- Compare PR #65 against issue #128 for missing implementation hooks.
- Check whether a schema distinguishes raw evidence from parsed output.
