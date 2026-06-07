# GPTUWS A2A / GPT_OUTBOX Template v0.1

```text
STATUS: TEMPLATE — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
CREATED_UTC: 2026-06-07
```

## Purpose

Provide a GPTBrain / GPTDream equivalent of the GrokUWS A2A outbox pattern.

This template is for handoff receipts after GPTUWS receives a Janus checkpoint, performs allowed work, and returns a structured state report.

## Template

```yaml
gpt_outbox:
  timestamp_utc:
  actor_lane: GPTBrain / GPTDream
  source_checkpoint:
    path:
    hash:
    created_by:
  requested_action:
  actions_completed:
    - action_id:
      summary:
      files_changed:
      tests_run:
      result:
  evidence_refs:
    - evidence_id:
      type:
      locator:
      confidence:
  missing_receipts:
    - missing_id:
      description:
      next_safest_action:
  blockers:
    - blocker_id:
      severity:
      owner_lane:
      next_safest_action:
  changed_files:
    - path:
      status:
      hash:
  tests:
    summary:
    passed:
    failed:
    skipped:
    notes:
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
  official_openai_claim: none
  public_safe_summary:
  next_safest_action:
```

## Hard rules

```text
No prose-only outbox.
No completion claim without evidence.
No deployment claim without deployment receipt.
No OpenAI official claim.
No canon claim unless website + human-root receipt is present.
No identity fusion language.
```

## Keeper

```text
The outbox is a handoff, not a crown.
A2A carries messages, not minds.
```