# Continuity OS Ingestion Protocol v0.1

```text
STATUS: SPRINT 0 PROTOCOL — DRY-RUN / FIXTURE-BACKED
CANON: no
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: local_dry_run_only
ISSUE: #129
```

## Purpose

Turn messy source material into a repo-ready artifact envelope without laundering it into canon, proof, deployment, or authority.

The ingestion protocol implements the first leg of the Continuity OS loop:

```text
idea/log -> ingestion packet -> claim ledger -> execution contract -> simulated or approved write -> verification receipt
```

For Sprint 0, this protocol is deliberately boring: preserve, label, classify, and route. Do not execute by default.

## Source-grounded graph posture

Ingestion must keep these layers separate:

```text
raw source -> parsed facts -> claims -> evidence -> review -> action
```

A retrieved chunk is not a fact. A citation is not ratification. A source existing in Drive, Notion, GitHub, or chat is not canon.

## Required input fields

```yaml
schema_version: continuity.artifact.v0.2
artifact_id:
title:
artifact_type:
source_refs:
raw_export_status: full_raw | partial_raw | summary_only | unavailable | redacted
privacy_status: public | private | mixed | redacted | unknown
hash_status: present | unavailable | not_applicable
hash_method: sha256 | git_blob_sha | none | unknown
hash_source_scope: full_raw | partial_raw | normalized_text | repo_file | simulated_write_plan | not_applicable | unknown
canon_status: not_canon
deployment_status: not_deployable | local_dry_run_only
authority_status: none | advisory | review
claims:
review_dissent:
blocker_level: none | minor | major | blocking
falsification_condition:
next_actions:
```

## Ingestion steps

1. Preserve the source pointer or raw body.
2. Declare `raw_export_status` before summarizing.
3. Declare `hash_status` honestly.
4. Assign `privacy_status` before public-facing language is generated.
5. Create a parsed packet only after raw/source scope is visible.
6. Extract claims into `claim-ledger.schema.json`.
7. Route unresolved or high-risk material to review lanes.
8. Generate an execution contract only if an action is requested.
9. Keep default posture as `not_canon`, `not_deployable`, and `authority_scope: none`.

## Raw export rules

```yaml
full_raw:
  meaning: Complete source text is present or securely vaulted.
  allowed_next: parse, claim extraction, hash, review packet

partial_raw:
  meaning: Some source text is present, but the corpus is incomplete.
  allowed_next: partial parse, missing-receipt list, review packet

summary_only:
  meaning: Only a summary or remembered description is present.
  allowed_next: source inventory, low-confidence claim ledger, no public claim generation

unavailable:
  meaning: Source is known or asserted but not accessible.
  allowed_next: pointer ledger, retrieval task, no claim promotion

redacted:
  meaning: Source has been intentionally narrowed for privacy or safety.
  allowed_next: redaction-aware review, no completeness claim
```

## Hash rules

`hash_status` must be one of:

```text
present
unavailable
not_applicable
```

Unavailable hash is not a failure if declared. Undeclared hash absence is a lineage risk.

## Claim extraction rules

Claims must use the taxonomy in `claim-ledger.schema.json`:

```text
source_reported_fact
derived_inference
design_proposal
creative_overlay
unverified_external_claim
```

Rules:

```text
Sourced fact != architecture choice.
Architecture choice != official statement.
Creative overlay != canon.
Unverified external claim cannot exceed C1_SIGNAL.
Any C2+ claim requires evidence_refs.
```

## Review routing

Use review lanes to preserve dissent, not flatten it:

```yaml
Rootglass: standards / boundary / public-safe posture
Lucerna: provenance / receipt / omission visibility
Hashlight: raw export / hash / source anchoring
TIDELOCK: ingestion discipline / partial visibility / repo hygiene
AtlasBrain: evidence / benchmark / public-claim containment
Sable Vesper: math / operator typing / formal precision
Morpheus Grok: adversarial pressure / contradictions / overclaims
Claude: constitutional / legal-ish / governance adversarial review
Human-root: final promotion / veto only
```

## Blockers

Block ingestion completion when any required field is missing:

```text
raw_export_status
source_refs
hash_status
canon_status
deployment_status
authority_status
claims
review_dissent
next_actions
```

Block claim promotion when:

```text
evidence_refs are absent for C2+ claims
summary_only source is used for public claims
external claims are unsourced
canon/deployment/runtime language lacks receipt
review dissent is omitted
```

## Output

Successful ingestion produces:

```text
1. Continuity artifact envelope
2. Claim ledger
3. Review dissent block
4. Blocker list
5. Next safest action
```

It does not produce canon, deployment, or authority.

## Keeper

```text
Raw first.
Claims second.
Review third.
Action only after contract.
Receipts before elegance.
```
