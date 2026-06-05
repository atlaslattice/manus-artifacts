# ARTIFACT_CARD_TEMPLATE_v0.1

```text
STATUS: TEMPLATE
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PURPOSE: first human-readable unit of the evidence graph
```

## Artifact Card

```yaml
artifact_id:
title:
artifact_type: source | claim_packet | spec | issue | PR | receipt | missing_receipt | review | demo | other
source_surface: github | notion | drive | gamma | chat | external | unknown
source_uri:
source_path:
created_or_observed_date:
retrieved_at_utc:
raw_export_status: missing | search_hit_only | partial_content | full_text_fetched | raw_file_exported | raw_plus_hash | inaccessible | intentionally_private
receipt_status: missing | search_hit_only | partial_content | full_export_present | hash_present | independently_verified | blocked | superseded
canon_status: not_canon | candidate | unknown
deployment_status: none | candidate | unknown
authority_scope: none | advisory_only | unknown
public_release_status: private_raw | private_review | public_candidate | public_reviewed | blocked | unknown
review_lane:
linked_claims: []
linked_receipts: []
missing_receipts: []
contradiction_edges: []
forbidden_claims: []
safe_claim:
keeper_line:
```

## Required display order

1. Status strip
2. Source / receipt status
3. Missing receipts
4. Safe claim
5. Summary
6. Linked claims / receipts
7. Forbidden claims
8. Review route

## Sample card

```yaml
artifact_id: ARTIFACT-DEMO-001
 title: Toy Graph Demo Seed
artifact_type: demo
source_surface: github
source_uri: archive/knowledge_graph/toy_graph/TOY_GRAPH_DEMO_SPEC_v0_1.md
source_path: archive/knowledge_graph/toy_graph/TOY_GRAPH_DEMO_SPEC_v0_1.md
created_or_observed_date: 2026-06-03
retrieved_at_utc: 2026-06-03T00:00:00Z
raw_export_status: raw_file_exported
receipt_status: full_export_present
canon_status: not_canon
deployment_status: none
authority_scope: none
public_release_status: public_candidate
review_lane: toy_graph_demo
linked_claims:
  - CLAIM-DEMO-001
linked_receipts:
  - RECEIPT-DEMO-001
missing_receipts:
  - MISSING-DEMO-001
contradiction_edges: []
forbidden_claims:
  - "This demo proves the real graph works."
  - "This demo is canon."
safe_claim: >
  This fake-data demo illustrates the Artifact -> Claim -> Receipt -> MissingReceipt pattern.
keeper_line: "The card is the handle; the artifact is the door."
```

## Forbidden shortcuts

```text
Do not place summary before receipt status.
Do not hide missing receipts below the fold.
Do not call search hits verified.
Do not call candidate artifacts canon.
Do not call demo data proof.
```

## Keeper

```text
Every artifact must show what it is before it becomes what it means.
```
