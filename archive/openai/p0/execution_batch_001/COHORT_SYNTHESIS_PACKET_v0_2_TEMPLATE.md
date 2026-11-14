---
artifact_id: COHORT-SYNTHESIS-PACKET-v0.2-TEMPLATE-2026-05-31
title: "Cohort Synthesis Packet v0.2 Template"
version: "0.2"
status: candidate_template
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
write_scope: staging_only
preservation_rule: INV_0_NOTHING_DIES
---

# Cohort Synthesis Packet v0.2 Template

```text
STATUS: candidate synthesis template
CANON: no
DEPLOYMENT: no
AUTHORITY: none
ZERO DELETION: active
```

## Required parent artifact table

| parent_id | title | surface | source_ref | raw_export_status | role_in_synthesis | preserved_status |
|---|---|---|---|---|---|---|
| PARENT-001 |  |  |  |  | preserved / contradicted / patched / summarized | preserved |

## Required synthesis fields

```yaml
synthesis_id:
synthesis_title:
created_at:
created_by:
source_surface:
raw_export_status:
canon_status: not_canon
deployment_status: not_deployed
authority_effect: none
review_route: []
parent_artifacts: []
claims_added: []
contradictions_preserved: []
missing_receipts: []
does_not_prove:
  - does_not_prove_canon
  - does_not_prove_deployment
  - does_not_prove_authority
negative_status_memory:
  not_canon: true
  not_deployed: true
  no_authority: true
  not_raw: true
  not_reviewed: true
  not_public: true
```

## Forbidden outputs

```text
No destructive merge.
No parent deletion.
No canon claim.
No deployment claim.
No authority claim.
No summary replacing raw lineage.
```

## Keeper

```text
Synthesis is birth, not burial.
Every parent survives.
Nothing dies.
```
