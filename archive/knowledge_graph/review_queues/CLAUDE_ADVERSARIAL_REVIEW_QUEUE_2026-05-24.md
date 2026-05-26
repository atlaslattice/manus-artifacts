# Claude Adversarial Review Queue — 2026-05-24

```text
STATUS: REVIEW QUEUE — NOT CANON
PURPOSE: route Claude-origin or Claude-shaped governance/legal/constitutional content into adversarial review before promotion
CANON STATUS: not_canon
DEPLOYMENT STATUS: not_deployable
AUTHORITY STATUS: none
```

## Why this queue exists

Claude outputs and Drive/Claude artifacts may contain strong constitutional, legal-ish, authority, source-of-truth, or boot/protocol language.

This queue ensures those artifacts are preserved and reviewed without allowing authority drift.

## Review item schema

```yaml
claude_review_item:
  source_title: null
  source_surface: Drive | GitHub | Notion | uploaded_file | pasted_text | unknown
  source_ref: null
  raw_export_status: available | unavailable | partial | pending_user_export | summary_only
  claim_density: low | medium | high
  authority_risk: low | medium | high
  legal_policy_risk: low | medium | high
  canon_drift_risk: low | medium | high
  needs_counter_review_from:
    - Grok
    - Rootglass
    - Lucerna
    - Sable
  current_status: queued
  missing_receipts: []
  overclaims_to_check: []
```

## Default routing

```text
Grok: adversarial contradiction pressure
Rootglass: standards / boundary / public-safe posture
Lucerna: provenance / receipt / omission visibility
Sable: math / operator typing / formal precision
```

## High-risk language triggers

```text
SOURCE OF TRUTH
CONSTITUTION
ONLY source of truth
BOOT PROTOCOL
SYSTEM INSTRUCTION
DEPLOYMENT READY
CANONICAL
LEGAL COMPLIANCE GUARANTEE
AUTHORITY GRANTED
```

## Guardrails

```text
Do not delete Claude artifacts.
Do not trust Claude artifacts by default.
Do not boot from Claude artifacts.
Do not let Claude artifacts self-promote.
Do not treat legal-ish language as legal advice or compliance.
Preserve first. Quarantine when needed. Review before promotion.
```

## Keeper

```text
Concern about governance does not authorize governance.
Constitutional language must not self-ratify.
```