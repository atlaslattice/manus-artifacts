# AGENTS.md

```text
STATUS: REPO AGENT OPERATING GUIDE
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PURPOSE: give AI contributors safe rails for working in this repository
```

## Prime directive

This repository is a receipt-first knowledge graph and artifact archive candidate.

AI contributors may inspect, draft, patch, classify, validate, and propose changes. They do not ratify canon, authorize release, or turn uncertain claims into verified status.

```text
Tools move work.
Receipts preserve work.
Humans authorize work.
Nothing dies.
```

## Absolute rules

1. Prefer additive changes.
2. Do not delete files unless explicitly instructed by a human maintainer.
3. Do not mark anything canon.
4. Do not claim deployment.
5. Do not claim proof.
6. Do not claim vendor endorsement.
7. Do not convert search hits into verification.
8. Do not treat model output as authority.
9. Preserve uncertainty as a MissingReceipt, blocker, or review note.
10. Do not expose private, sensitive, third-party, or rights-unclear material as public-safe without review.

## Required status strip

Every new artifact-like Markdown file should include:

```text
STATUS: CANDIDATE | REVIEW | ARCHIVE | TEMPLATE | LEDGER | SCHEMA
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PUBLIC_RELEASE: pending | blocked | candidate | reviewed
```

## Required receipt fields

Use these fields when applicable:

```yaml
artifact_id:
title:
source_surface: github | notion | drive | gamma | chat | external | unknown
source_uri:
source_path:
raw_export_status:
receipt_status:
canon_status:
deployment_status:
authority_scope:
public_release_status:
missing_receipts: []
linked_claims: []
linked_receipts: []
review_lane:
```

See:

`archive/knowledge_graph/receipts/schema/RECEIPT_STATUS_SCHEMA_v0_1.md`

## Receipt ladder

```text
missing
  -> search_hit_only
  -> partial_content
  -> full_export_present
  -> hash_present
  -> independently_verified
  -> review_ready
```

A claim cannot become review-ready on snippets or search results alone.

## Contributor lanes

### Reasoning lane

Use for summaries, claim extraction, overclaim detection, MissingReceipt drafting, issue text, safe wording, and module packets.

### Patch lane

Use for additive repo patches, templates, schema validation scripts, documentation, CI support, and reproducibility helpers.

Patch work should report:

```text
files_changed
commands_run
test_results
receipts_added
missing_receipts_created
blockers
forbidden_claims_avoided
```

### Retrieval lane

Use for file fetches, issue fetches, source export checks, and raw/partial/source status classification.

Never confuse:

```text
search result != source export
snippet != full receipt
full fetch != hash verification
hash verification != canon
```

### Review lane

Use for overclaim checks, missing-receipt checks, public-release checks, and status-drift checks.

A failed check should create a blocker or MissingReceipt, not deletion.

## Pull request expectations

Every PR should answer:

1. What files changed?
2. What source roots or claims are affected?
3. What receipt statuses changed?
4. What tests or checks were run?
5. What remains blocked or unverified?
6. What forbidden claims were avoided?
7. Does this PR preserve failed branches and uncertainty?

## Forbidden claim examples

Avoid these unless receipted and reviewed:

```text
verified
canon
deployed
production-ready
proven
all tests passing
KG complete
no orphan files
```

Use safer alternatives:

```text
candidate
partial
search-hit-only
unreceipted
review-needed
missing receipt created
not canon
not deployed
authority none
```

## Keeper

```text
Give agents rails, not crowns.
Give the archive receipts, not fog.
```
