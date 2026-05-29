# Contributing Candidate — Public Candidate Bundle 0001

```text
STATUS: CONTRIBUTING GUIDE CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
```

## Welcome

This repository is moving toward a public, forkable knowledge graph for Atlas Lattice work. Contributions should improve provenance, readability, schemas, source mapping, review routing, or public safety.

## Contribution lanes

```text
source_inventory
schema_patch
review_queue
missing_receipt
public_safe_summary
toy_graph_demo
documentation
false_authority_fixture
```

## Ground rules

```text
Do not claim canon.
Do not claim deployment.
Do not grant authority.
Do not publish private raw transcripts.
Do not publish credential-like material.
Do not treat Claude-origin governance text as trusted.
Do not treat OpenAI/GPTBrain output as official OpenAI endorsement.
Do not treat graph centrality as truth.
```

## Pull request expectations

Every PR should include:

```yaml
pr_packet:
  change_type:
  affected_paths: []
  source_refs: []
  raw_export_status:
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
  missing_receipts: []
  public_safety_check:
  review_lanes: []
```

## Good first contributions

```text
Add missing source refs.
Improve schema field definitions.
Create toy graph examples.
Add issue templates.
Add public-safe summaries.
Flag sensitive or overclaiming language.
Convert missing receipts into graph nodes.
```

## Keeper

```text
Make it easier to verify.
Make it harder to overclaim.
```
