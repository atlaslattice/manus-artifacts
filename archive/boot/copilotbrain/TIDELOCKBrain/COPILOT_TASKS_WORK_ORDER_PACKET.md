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
verdict: approve | patch | block
blockers: []
patch_items: []
file_by_file_notes: []
raw_vs_parsed_status: ""
authority_boundary_status: ""
relation_to_linked_issues: ""
next_safest_action: ""
```

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
