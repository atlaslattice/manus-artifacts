# Toy Graph Demo — PUBLIC_CANDIDATE_BUNDLE_0001

```text
STATUS: CANDIDATE STAGING MATERIAL
CANON: no
DEPLOYMENT: no
AUTHORITY: none
DATA: fake/sample only
MODULE: 11 — Public GitHub / Forkability Excellence
```

## Purpose

This demo shows how Atlas Lattice graph packets can model sources, claims, evidence, missing receipts, and review routes without exposing private archive cargo.

The demo uses fake/sample nodes only.

## Toy graph

```yaml
nodes:
  - node_id: SRC-DEMO-001
    node_type: SourceArtifact
    title: Demo Source Packet
    surface: sample
    raw_export_status: full_raw_export_hashed
    receipt_status: present
    canon_status: not_canon
    deployment_status: not_deployed
    authority_scope: none
    public_release_status: public_ready

  - node_id: CLAIM-DEMO-001
    node_type: Claim
    text: Demo source proposes a public-safe graph structure.
    derived_from: SRC-DEMO-001
    receipt_status: present
    canon_status: not_canon
    deployment_status: not_deployed
    authority_scope: none
    review_state: review_pending

  - node_id: EVIDENCE-DEMO-001
    node_type: EvidenceAnchor
    anchor_type: sha256
    value: sample-not-real-sha256
    supports_or_locates: SRC-DEMO-001
    receipt_status: present

  - node_id: REVIEW-DEMO-001
    node_type: ReviewQueue
    lane: Lucerna
    reason: public-safe wording review
    status: open

  - node_id: MISSING-DEMO-001
    node_type: MissingReceipt
    missing_receipt: human_root_release_decision
    status: missing
```

```yaml
edges:
  - edge_id: EDGE-DEMO-001
    from: CLAIM-DEMO-001
    edge_type: derived_from
    to: SRC-DEMO-001
    promotion_effect: none

  - edge_id: EDGE-DEMO-002
    from: CLAIM-DEMO-001
    edge_type: cites
    to: EVIDENCE-DEMO-001
    promotion_effect: none

  - edge_id: EDGE-DEMO-003
    from: CLAIM-DEMO-001
    edge_type: requires_review
    to: REVIEW-DEMO-001
    promotion_effect: none

  - edge_id: EDGE-DEMO-004
    from: SRC-DEMO-001
    edge_type: missing_receipt
    to: MISSING-DEMO-001
    promotion_effect: none
```

## What this demonstrates

- A source can be public-ready without being canon.
- A claim can cite evidence without becoming proven.
- A review edge routes attention; it does not grant authority.
- A missing receipt is preserved as a graph object.
- Human-root release decision is separate from source existence.

## What this does not demonstrate

- No private archive cargo.
- No real IP claim.
- No deployment proof.
- No endorsement.
- No canon.

## Keeper

```text
A toy graph teaches the route.
It does not carry the crown.
```
