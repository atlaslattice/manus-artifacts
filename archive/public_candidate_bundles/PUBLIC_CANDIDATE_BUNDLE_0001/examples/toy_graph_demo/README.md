# Toy Graph Demo

Status: candidate staging material  
Canon: no  
Deployment: no  
Authority: none  
Data: SAMPLE ONLY — no private cargo, no real lineage  

## Purpose

Demonstrate the Atlas Lattice graph schema using entirely fake/sample data.  
This demo contains no private data, no real source lineage, and no claims
about actual artifacts in the archive.

It exists so that reviewers can inspect the graph format before real cargo
is attached.

## Demo graph: three nodes, four edges

### Nodes

```yaml
nodes:

  - node_id: DEMO-ART-001
    node_type: Artifact
    label: "Sample Source Document A"
    public_release_status: unknown
    canon_status: not_canon
    source_receipt_status: missing
    review_state: unreviewed
    note: SAMPLE DATA ONLY

  - node_id: DEMO-ART-002
    node_type: Artifact
    label: "Sample Synthesis Export B"
    public_release_status: unknown
    canon_status: not_canon
    source_receipt_status: partial
    review_state: review_pending
    note: SAMPLE DATA ONLY

  - node_id: DEMO-CLAIM-001
    node_type: Claim
    label: "Sample claim: system was built by Dave"
    claim_type: attribution
    evidence_required: true
    evidence_receipt: missing
    overclaim_risk: low
    note: SAMPLE DATA ONLY

  - node_id: DEMO-RECEIPT-001
    node_type: Receipt
    label: "Sample GitHub commit receipt"
    receipt_type: github_commit
    commit_sha: "abc1234_FAKE"
    receipt_status: present
    note: SAMPLE DATA ONLY
```

### Edges

```yaml
edges:

  - edge_id: DEMO-EDGE-001
    from: DEMO-ART-002
    to: DEMO-ART-001
    edge_type: derived_from
    note: synthesis export derived from source doc — SAMPLE ONLY

  - edge_id: DEMO-EDGE-002
    from: DEMO-CLAIM-001
    to: DEMO-ART-001
    edge_type: cites
    note: claim cites source doc — SAMPLE ONLY

  - edge_id: DEMO-EDGE-003
    from: DEMO-CLAIM-001
    to: DEMO-RECEIPT-001
    edge_type: missing_receipt
    note: claim lacks receipt — SAMPLE ONLY

  - edge_id: DEMO-EDGE-004
    from: DEMO-ART-002
    to: DEMO-CLAIM-001
    edge_type: requires_review
    note: synthesis export contains unverified claim — SAMPLE ONLY
```

## What this demo shows

1. **Nodes carry status fields.** Every node has `public_release_status`,
   `canon_status`, and `review_state`. None are `public_ready` in this demo.

2. **Edges are not promotions.** `derived_from` means lineage, not endorsement.
   `cites` means reference, not proof. `missing_receipt` means gap, not failure.

3. **Centrality is not authority.** DEMO-CLAIM-001 has three edges but carries
   no authority. Centrality means review pressure, not truth.

4. **Missing receipts are graph objects.** `DEMO-EDGE-003` makes the gap
   visible without deleting the claim. The gap is data.

## What this demo does NOT show

- Real archive artifacts
- Real source lineage
- Real claim evidence
- Canon status
- Deployment readiness
- Any authority of any kind

## Graph doctrine recap

```text
A graph edge is not a promotion.
A cluster is not canon.
A central node is not an authority.
Public GitHub is not proof.
Model output is not authority.
Human-root owns the whistle.
```

## Keeper

The demo is a door, not a destination.  
Real cargo requires real receipts.  
The graph shows where to look; it does not decide what is true.
