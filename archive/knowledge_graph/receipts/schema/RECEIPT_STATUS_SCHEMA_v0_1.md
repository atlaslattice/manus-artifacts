# RECEIPT_STATUS_SCHEMA_v0.1

```text
STATUS: CANDIDATE RECEIPT SCHEMA
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PURPOSE: make source / receipt / export state visible before synthesis, promotion, or public-release claims
```

## Why this exists

The archive needs a durable way to distinguish:

- a search hit
- a partial fetch
- a full raw export
- a hash-bearing receipt
- independent verification
- blocked or intentionally private evidence

Without this distinction, a model or contributor can accidentally convert visibility into authority.

```text
Visibility is not verification.
Receipt is not ratification.
Search result is not source possession.
Graph edge is not canon promotion.
```

## Core fields

Every artifact, claim, source root, evidence log, and public candidate bundle should expose these fields before any summary text:

```yaml
artifact_id:
title:
source_surface: github | notion | drive | gamma | chat | external | unknown
source_uri:
source_path:
created_or_observed_date:
retrieved_at_utc:
raw_export_status:
receipt_status:
review_status:
canon_status:
deployment_status:
authority_scope:
public_release_status:
missing_receipts: []
linked_claims: []
linked_receipts: []
```

## `raw_export_status` enum

```yaml
raw_export_status:
  none:
    meaning: No source export or content fetch is available.
    allowed_claim: "source not yet obtained"
    forbidden_claim: "verified"

  title_only:
    meaning: Only a title/name is known.
    allowed_claim: "title observed"
    forbidden_claim: "content reviewed"

  metadata_only:
    meaning: Metadata exists but body/content is unavailable.
    allowed_claim: "metadata observed"
    forbidden_claim: "artifact inspected"

  excerpt_only:
    meaning: Search snippet/highlight or short excerpt exists.
    allowed_claim: "snippet observed"
    forbidden_claim: "source verified"

  full_text_fetched:
    meaning: Full text/content was fetched through a connector or API.
    allowed_claim: "content fetched"
    forbidden_claim: "raw export preserved with hash"

  raw_file_exported:
    meaning: Raw file/export exists in archive or repo.
    allowed_claim: "raw export present"
    forbidden_claim: "independently verified"

  raw_plus_hash:
    meaning: Raw export exists and SHA-256/hash receipt is present.
    allowed_claim: "hash-bearing receipt present"
    forbidden_claim: "canon"

  inaccessible:
    meaning: Source exists or is referenced but currently inaccessible.
    allowed_claim: "blocked/inaccessible"
    forbidden_claim: "missing means false"

  intentionally_private:
    meaning: Source is intentionally withheld for privacy, safety, rights, or confidentiality.
    allowed_claim: "private source exists / not public"
    forbidden_claim: "publicly reusable"
```

## `receipt_status` enum

```yaml
receipt_status:
  missing:
    meaning: No usable receipt is present.
    next_action: Create MissingReceipt node.

  search_hit_only:
    meaning: Search found a reference, but no full content is available.
    next_action: Fetch or export source.

  partial_content:
    meaning: Partial content, snippet, or truncated result is available.
    next_action: Obtain full fetch/export.

  full_export_present:
    meaning: Full raw content/export is present.
    next_action: Hash and link claims.

  hash_present:
    meaning: SHA-256 or comparable content hash is present.
    next_action: Independent review or reproduction.

  independently_verified:
    meaning: A second route/person/tool reproduced the receipt or result.
    next_action: Mark review-ready if other gates pass.

  blocked:
    meaning: Receipt cannot currently be obtained due to access, privacy, rights, or technical blocker.
    next_action: Document blocker and safe fallback.

  superseded:
    meaning: Source has been replaced by a newer artifact, but remains preserved for lineage.
    next_action: Link successor and preserve fossil branch.
```

## Receipt upgrade path

```text
missing
  -> search_hit_only
  -> partial_content
  -> full_export_present
  -> hash_present
  -> independently_verified
  -> review_ready
```

Rule: **no claim may move to `review_ready` on search snippets alone.**

## MissingReceipt node format

```yaml
node_type: MissingReceipt
missing_receipt_id:
claim_or_artifact:
expected_source:
why_needed:
current_status:
blocking_condition:
risk_if_unresolved:
next_action:
preferred_owner:
review_lane:
created_at_utc:
status: open | resolved | blocked | superseded
```

## Public candidate bundle gate

Before any public candidate bundle can be labeled `public_reviewed` or stronger, it must show:

```yaml
required_visible_fields:
  - raw_export_status
  - receipt_status
  - canon_status
  - deployment_status
  - authority_scope
  - public_release_status
  - missing_receipts
```

## OpenAI-first operating note

This schema is designed to work cleanly with OpenAI-native workflows:

- ChatGPT: extract claims, classify receipt states, draft MissingReceipt nodes.
- Codex: add schema files, patch validators, build manifest scripts, open PRs.
- Agents/tools: run only with explicit permission and bounded scope.
- Humans: adjudicate canon, public release, rights, and authority.

```text
OpenAI moves work.
Governance grants authority.
Receipts preserve lineage.
Humans ratify.
```

## Keeper

```text
A missing receipt is not a dead branch.
It is a lantern hook.
```
