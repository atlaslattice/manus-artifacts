---
artifact_id: ARTIFACT-ARCHIVE-BOOT-PENDRAGON-PENDRAGON-TO-COUNCIL-ROUTING-MAP-2026-05-09-MD-2026-05-29
title: Pendragon OS → Council Brain Routing Map
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Pendragon OS → Council Brain Routing Map

```text
STATUS: ROUTING MAP — NOT CANON
PURPOSE: define how Pendragon OS artifacts route through Council Brain review
DATE: 2026-05-09
ISSUE: manus-artifacts#23
```

## 1. Routing principle

Pendragon material must be routed by function, not absorbed wholesale.

```text
No direct-to-canon path.
No direct-to-kernel path.
No defense-grade execution path without explicit human-root and safety review.
```

## 2. Intake flow

```text
Pendragon source / claim / artifact
  -> S6 continuity log
  -> S1 claim calibration
  -> S2 constitutional review
  -> S3 adversarial risk review
  -> S4 engineering mapping
  -> S5 sovereignty / deployment review
  -> S7 code integration review
  -> Human-root decision
```

## 3. Routing table

| Pendragon input type | Primary route | Review route | Output |
|---|---|---|---|
| Raw Pendragon note | S6 + S1 | S2 if governance-impacting | artifact registry entry |
| Architecture claim | S1 | S2/S3 | claim ledger entry |
| Defense-grade workflow pattern | S2 + S5 | S3/S4 | safety/risk review packet |
| Agent specialization pattern | S1 + S4 | S6/S7 | integration candidate |
| Tucker Gemini lineage note | S6 + S1 | S4/S7 | lineage/compatibility note |
| Aegis/Morpheus upgrade concept | S2 + S4 | S1/S3/S5 | federation candidate |
| Code scaffold request | S7 | S1/S4/S6 | PR/test plan |
| Public framing | S1 + S2 | S3/S5 | public-safe wording |

## 4. Forbidden shortcuts

```text
Pendragon claim -> ratified canon
Pendragon defense metaphor -> execution authority
Pendragon architecture -> Aluminum kernel authority
Pendragon lineage -> deployment proof
Pendragon agent role -> autonomous command authority
```

## 5. Required packet shape

```yaml
packet_id: PENDRAGON-PACKET-YYYYMMDD-NNN
status: candidate / review_required / blocked / superseded
source_refs: []
input_type: raw_note / claim / workflow / agent_pattern / code / public_framing
primary_route: S1 | S2 | S3 | S4 | S5 | S6 | S7
review_route: []
claim_class: raw_user_report | raw_model_output | parsed_artifact | candidate_canon | ratified_canon
confidence: C0 | C1 | C2 | C3 | C4 | C5
safety_flags: []
human_root_required: true
recommended_action: null
```

## 6. First recommended packets

```text
PENDRAGON-PACKET-20260509-001 — lineage map
PENDRAGON-PACKET-20260509-002 — Aluminum compatibility frame
PENDRAGON-PACKET-20260509-003 — safety / command hierarchy risk review
PENDRAGON-PACKET-20260509-004 — Tucker Gemini lineage note
```

## 7. Closing line

```text
Pendragon enters through the gates, not through the throne room.
```
