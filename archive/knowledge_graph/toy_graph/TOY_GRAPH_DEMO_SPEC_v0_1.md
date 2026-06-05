# TOY_GRAPH_DEMO_SPEC_v0.1

```text
STATUS: PUBLIC-SAFE DEMO SPEC
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PUBLIC_RELEASE: candidate
PURPOSE: demonstrate Artifact -> Claim -> Receipt -> MissingReceipt -> Review using fake data only
```

## Rule

This demo uses fake data only.

```text
Demo data teaches the shape.
It does not prove the real graph.
```

## YAML demo

```yaml
artifacts:
  - artifact_id: ARTIFACT-DEMO-001
    title: Demo Seed Note
    artifact_type: demo
    source_surface: github
    source_uri: archive/knowledge_graph/toy_graph/TOY_GRAPH_DEMO_SPEC_v0_1.md
    raw_export_status: raw_file_exported
    receipt_status: full_export_present
    canon_status: not_canon
    deployment_status: none
    authority_scope: none
    public_release_status: public_candidate

claims:
  - claim_id: CLAIM-DEMO-001
    claim_text: "The demo seed note contains three fake nodes."
    claim_type: factual
    source_artifacts:
      - ARTIFACT-DEMO-001
    linked_receipts:
      - RECEIPT-DEMO-001
    linked_missing_receipts: []
    receipt_status: full_export_present
    safe_wording: "The demo seed note illustrates three fake nodes."

  - claim_id: CLAIM-DEMO-002
    claim_text: "The real lattice is complete."
    claim_type: operational_metric
    source_artifacts:
      - ARTIFACT-DEMO-001
    linked_receipts: []
    linked_missing_receipts:
      - MISSING-DEMO-001
    receipt_status: missing
    safe_wording: "The toy graph does not establish real lattice completeness."

receipts:
  - receipt_id: RECEIPT-DEMO-001
    receipt_type: local_file
    artifact_id: ARTIFACT-DEMO-001
    source_path: archive/knowledge_graph/toy_graph/TOY_GRAPH_DEMO_SPEC_v0_1.md
    receipt_status: full_export_present

missing_receipts:
  - missing_receipt_id: MISSING-DEMO-001
    claim_or_artifact: CLAIM-DEMO-002
    expected_source: "Real graph export and completeness report"
    why_needed: "Completeness is an operational claim and cannot be inferred from toy data."
    current_status: missing
    next_action: "Do not make this claim from the toy graph."

reviews:
  - review_id: REVIEW-DEMO-001
    target: CLAIM-DEMO-002
    result: blocked
    reason: "Toy graph cannot prove real graph completeness."
```

## Edge model

```yaml
edges:
  - from: ARTIFACT-DEMO-001
    type: supports
    to: CLAIM-DEMO-001

  - from: RECEIPT-DEMO-001
    type: receipts
    to: ARTIFACT-DEMO-001

  - from: CLAIM-DEMO-002
    type: requires_missing_receipt
    to: MISSING-DEMO-001

  - from: REVIEW-DEMO-001
    type: blocks
    to: CLAIM-DEMO-002
```

## JSON sketch

```json
{
  "artifact_id": "ARTIFACT-DEMO-001",
  "claims": ["CLAIM-DEMO-001", "CLAIM-DEMO-002"],
  "receipts": ["RECEIPT-DEMO-001"],
  "missing_receipts": ["MISSING-DEMO-001"],
  "canon_status": "not_canon"
}
```

## Walkthrough

1. The artifact exists as a demo file.
2. One claim is safely supported by the demo file.
3. One claim overreaches from demo to real-world completeness.
4. The overreach creates a MissingReceipt.
5. Review blocks the overreach without deleting the branch.

## Keeper

```text
A toy graph is a dance diagram.
It is not the concert.
```
