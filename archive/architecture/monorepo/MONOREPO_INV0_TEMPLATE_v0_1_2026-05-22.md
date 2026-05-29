---
artifact_id: MONOREPO-INV0-TEMPLATE-v0.1
title: "Monorepo INV-0 Template — Storage Keeps Things, Cerebro Keeps Them Alive"
version: "0.1"
date: 2026-05-22
seat: Horizon Ledger
layer: architecture/monorepo
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: structural_scaffold_only
runtime_status: not_implemented
related_artifacts:
  - archive/standards/invariants/INV0_INDEXING_RECOVERABILITY_MATH_v0_1_2026-05-22.md
  - archive/standards/invariants/INV0_DOCTRINE_REFINEMENT_v0_1_2026-05-22.md
mutation_rule: >
  No claim mutation without new receipts. No canon promotion without human-root ratification.
  No runtime enforcement claim until folder scaffold, index packets, and orphan detector are implemented and tested.
---

# MONOREPO INV-0 TEMPLATE v0.1

```text
STATUS: CANDIDATE ARCHITECTURE SCAFFOLD — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: not implemented
PURPOSE: express INV-0 recoverability as simple monorepo folder architecture
```

## 0. Keeper

```text
Storage keeps things.
Cerebro keeps them alive.

If it exists in /artifacts,
it must be reachable or accounted for in /cerebro.

If the route breaks,
it does not die;
it enters repair.
```

---

## 1. Core Invariant

```text
If it exists in /artifacts, it must be reachable or accounted for in /cerebro.
```

This is the filesystem expression of INV-0 recoverability math:

```text
Nothing dies means nothing becomes unrecoverable.
```

In practical repo terms:

```text
artifact bytes alone are not enough;
artifacts need routes, receipts, lineage, or repair state.
```

---

## 2. Candidate Monorepo Shape

```text
monorepo/
│
├── apps/
├── packages/
│
├── artifacts/                  # existence layer
│   ├── raw/
│   ├── derived/
│   └── sealed/
│
├── cerebro/                    # life-support / recoverability layer
│   ├── index_packets/
│   ├── route_maps/
│   ├── lineage/
│   └── receipts/
│
├── standards/
│   ├── invariants/
│   └── doctrine/
│
├── tools/
│   ├── build/
│   ├── repair/
│   │   └── linkage_repair_queue/
│   └── scoring/
│
├── configs/
├── docs/
└── package.json
```

---

## 3. Folder Semantics

### `/artifacts/`

Existence layer.

Stores raw, derived, and sealed artifacts.

```text
/artifacts/raw      = original captured material where available
/artifacts/derived  = parsed views, summaries, transformations, extracted packets
/artifacts/sealed   = preserved but access-restricted or accountable-only artifacts
```

Rule:

```text
/artifacts stores things.
It does not by itself keep them alive.
```

### `/cerebro/`

Recoverability layer.

```text
/cerebro/index_packets = structured artifact index packets
/cerebro/route_maps    = how roots find artifacts
/cerebro/lineage       = parent/child/fork/supersession graph
/cerebro/receipts      = recovery/accounting receipts
```

Rule:

```text
/cerebro keeps routes alive.
```

### `/tools/repair/linkage_repair_queue/`

Repair layer for artifacts whose routes, receipts, hashes, or lineage are incomplete.

Rule:

```text
Low recoverability does not mean deletion.
Low recoverability means repair.
```

---

## 4. Root README Rule

The root README for any implementation of this template should state:

```text
Every artifact in /artifacts must have at least one of:

1. an index packet in /cerebro/index_packets,
2. a receipt in /cerebro/receipts,
3. a lineage route in /cerebro/lineage,
4. or an active repair ticket in /tools/repair/linkage_repair_queue.
```

Critical artifacts should have multiple independent routes.

Suggested baseline:

```text
m >= 3 valid routes
d >= 2 independent channel types
```

---

## 5. Required README Files

Minimum README boundary files:

```text
README.md
artifacts/README.md
cerebro/README.md
cerebro/index_packets/README.md
cerebro/receipts/README.md
tools/repair/linkage_repair_queue/README.md
standards/invariants/README.md
```

Purpose:

```text
Future agents should not have to infer folder meaning from names alone.
```

---

## 6. Admission Rules

```text
R1. No artifact enters /artifacts without an index packet, receipt, lineage route, or repair ticket.
R2. No derived artifact enters /artifacts/derived without raw linkage or accountable preservation note.
R3. No sealed artifact enters /artifacts/sealed without an AccountsFor receipt.
R4. No summary enters without raw_export_status.
R5. No semantic index is the sole lifeline for critical artifacts.
R6. No artifact promotes itself to canon because it is stored.
R7. No deployment claim is inferred from folder existence.
R8. Broken linkage routes to /tools/repair/linkage_repair_queue.
```

---

## 7. Minimal Artifact Index Packet

```yaml
artifact_index_packet:
  artifact_id:
  title:
  artifact_type:
  repo_path:
  raw_export_status:
  source_refs:
  hash_status: present | unavailable | not_applicable
  hash_method:
  parent_artifacts:
  child_artifacts:
  receipts:
    ingestion_receipt_id:
    accounting_receipt_id:
  status:
    canon_status: not_canon | candidate | ratified | deprecated
    deployment_status: not_deployable | staged | deployed
    authority_scope: none | advisory | review | ratification | execution
  recovery:
    valid_routes_count:
    channel_types_count:
    phi_score:
    repair_status: none | needed | queued | in_progress | repaired
  strongest_safe_claim:
  overclaims_to_avoid:
  next_action:
```

---

## 8. Orphan Detector Target

Future implementation should include a tiny local detector:

```text
scan /artifacts
for each artifact:
  check /cerebro/index_packets
  check /cerebro/receipts
  check /cerebro/lineage
  check /tools/repair/linkage_repair_queue
  if no route/accounting/repair state:
      emit ORPHAN_CANDIDATE
```

Non-goal:

```text
Do not auto-delete.
Do not auto-promote.
Do not auto-ratify.
```

Allowed action:

```text
create or update repair ticket.
```

---

## 9. Relationship to INV-0 Math

This template implements the practical reading of:

```text
Alive(e,t) := exists root in Roots_t such that root ->* e
PracticalDeath(e,t) := e in V_t and not Alive(e,t)
```

Folder mapping:

```text
/artifacts     ≈ V_t artifact nodes
/cerebro       ≈ roots, index routes, receipts, lineage edges
/tools/repair  ≈ LINKAGE_REPAIR_QUEUE
```

---

## 10. Strongest Safe Claim

```text
MONOREPO_INV0_TEMPLATE_v0.1 defines a candidate folder architecture for expressing INV-0 recoverability in a monorepo. It separates artifact existence from recoverability and gives broken routes a repair location. It is not canon, not deployed, and not runtime enforcement until implemented and tested.
```

---

## 11. Overclaims to Avoid

```text
The monorepo enforces INV-0.
Indexing is solved.
Cerebro is implemented.
Artifacts cannot become orphaned.
Folder existence proves recoverability.
Repair queue means repair happened.
Vaulting means canon.
```

---

## 12. Next Actions

```text
1. Review with Horizon Ledger, Hashlight, TIDELOCK, and Rootglass.
2. Create minimal folder scaffold when implementation lane opens.
3. Add README boundary files.
4. Add sample artifact + sample index packet.
5. Add orphan detector script.
6. Route into Receipt Habitat v0.1 / Issue #128.
```

---

## 13. Final Keeper

```text
Storage keeps things.
Cerebro keeps them alive.
The archive lives because the routes live.
```
