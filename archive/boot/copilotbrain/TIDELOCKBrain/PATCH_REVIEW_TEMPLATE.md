# Patch Review Template

## Purpose

Use this template when GitHub Copilot or Copilot Tasks needs to return a bounded patch review for TIDELOCK-related artifacts.

This template is for review and recommendation. It is not merge approval.

## Status

Candidate review artifact.  
Not canon.  
No authority effect.  
No deployment effect.

## Template

```yaml
target: ""
verdict: approve | patch | block

summary: ""

blockers: []
patch_items: []
file_by_file_notes: []

raw_vs_parsed_status:
  status: ""
  notes: []

boundary_check:
  hidden_memory_claims: pass | fail
  canon_claims: pass | fail
  merge_authority_claims: pass | fail
  deployment_authority_claims: pass | fail
  runtime_authority_claims: pass | fail
  notes: []

relation_to_linked_issues:
  issues: []
  notes: []

open_questions: []
next_safest_action: ""
```

## Usage Notes

- Keep patch items minimal
- Prefer concrete file references
- State uncertainty explicitly
- Do not convert a review template into an authority claim
- If receipts are missing, say so directly

## Keeper

```text
Patch narrowly.
Name the blocker.
Keep the boundary.
```
