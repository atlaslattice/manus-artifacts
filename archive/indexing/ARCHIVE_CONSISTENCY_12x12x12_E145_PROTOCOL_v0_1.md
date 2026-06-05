# Archive Consistency Protocol — 12×12×12 Hypercube + E145 v0.1

```text
STATUS: CANDIDATE INDEXING PROTOCOL — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
PURPOSE: Normalize archives across Website, GitHub, Notion, Drive/OneDrive, chat exports, and model outputs into a 12×12×12 lattice with E145 meta-coordination.
HUMAN-ROOT: REQUIRED FOR CANON / DEPLOYMENT / AUTHORITY CHANGES
```

## Core rule

```text
Everything can connect to everything.
Nothing can promote itself.
```

The archive index maps source material into coordinates. It does not decide truth, canon, ownership, deployment, or authority.

## Source surfaces

```yaml
source_surfaces:
  website_canon:
    role: public / ratified surface when explicitly human-root approved
    caution: rendered export required before fossilization

  github:
    role: receipt workbench / code / issues / PRs / commits / CI
    caution: Git visibility is not canon

  notion:
    role: working archive / planning surface / pre-GitHub synthesis
    caution: Notion page is not ratification

  drive_onedrive:
    role: file archive substrate / raw exports / bulk corpus
    caution: file presence is not review

  chat_transcript:
    role: raw conversation source when exported
    caution: memory reconstruction is not source tape

  model_output:
    role: assessment / synthesis / candidate delta
    caution: model output is not authority
```

## 12×12×12 coordinate model

Each indexed item receives a coordinate:

```text
Hxx.Syy.Zzz
```

Where:

```yaml
H_axis:
  name: House / functional domain
  range: H01-H12
  purpose: What domain does this artifact belong to?

S_axis:
  name: Sphere / semantic layer
  range: S01-S12 per house
  purpose: What semantic container or subdomain does this artifact occupy?

Z_axis:
  name: State / authority / data-nature type
  range: Z01-Z12
  purpose: What kind of state is this? What can it NOT infer?
```

## Z-axis authority firewall

```yaml
Z_axis_candidate:
  Z01_RAW_SOURCE:
    description: Fossil/raw export/source tape.
    authority_effect: none

  Z02_PARSED_VIEW:
    description: Parser-derived representation.
    authority_effect: none

  Z03_CLAIM:
    description: Atomic assertion extracted from source.
    authority_effect: none

  Z04_EVIDENCE:
    description: Evidence supporting or contradicting a claim.
    authority_effect: none

  Z05_REVIEW:
    description: Review packet, adversarial note, or critique.
    authority_effect: review_only

  Z06_CANDIDATE:
    description: Candidate artifact or doctrine.
    authority_effect: none

  Z07_RATIFICATION_RECEIPT:
    description: Human-root or defined governance gate receipt.
    authority_effect: scoped_ratification_possible

  Z08_CANON_SURFACE:
    description: Public canon surface after explicit promotion.
    authority_effect: canon_scope_defined_by_receipt

  Z09_RUNTIME_RECEIPT:
    description: Test/CI/smoke/runtime proof artifact.
    authority_effect: runtime_evidence_only

  Z10_QUARANTINE:
    description: Blocked, unsafe, incomplete, or contradicted item.
    authority_effect: block_promotion

  Z11_DREAM_PLAY_CULTURE:
    description: Simulation, morale, myth, play, creative overlay.
    authority_effect: none

  Z12_META_COORDINATION:
    description: E145/read-across/index/meta-routing surfaces.
    authority_effect: coordinate_only
```

Hard rule:

```text
Governance authority cannot be inferred from H or S alone.
Only explicit Z07/Z08 evidence with human-root receipt can support canon movement.
```

## E145 role

E145 is the meta-coordinator across the 12×12×12 lattice.

```yaml
E145:
  role:
    - read across all H/S/Z coordinates
    - detect gaps, duplicates, contradictions, and missing receipts
    - recommend review routes
    - emit index packets
    - maintain dashboard / map coherence

  may_not:
    - ratify canon
    - deploy runtime
    - erase source lineage
    - infer authority from centrality
    - rewrite raw exports
    - collapse multiple identities into one
```

E145 sees the lattice. It does not own the lattice.

## Required archive packet fields

```yaml
archive_packet:
  packet_id:
  title:
  source_surface:
  source_path_or_url:
  raw_export_status:
  hash_status:
  sha256:
  coordinate:
    H:
    S:
    Z:
  e145_index_status:
  artifact_status:
    canon_status:
    deployment_status:
    authority_scope:
    review_status:
    lineage_status:
  linked_claims:
  linked_artifacts:
  linked_concepts:
  contradictions:
  supersedes:
  superseded_by:
  review_lane:
  human_root_review_required: true
  next_safe_action:
```

## Required raw export status values

```text
RAW_EXPORTED
RAW_PARTIAL
RAW_NOT_EXPORTED
RAW_UNAVAILABLE
UNKNOWN
```

## Surface normalization rules

```text
Website page → rendered export → hash → source artifact → coordinate.
GitHub file → commit/blob SHA → artifact packet → coordinate.
Notion page → export or API fetch → raw_export_status → coordinate.
Drive/OneDrive file → file inventory + hash → coordinate.
Chat thread → raw export if available → summary/parse marked derived.
Model output → candidate assessment only unless source-backed.
```

## Forbidden collapses

```text
Summary ≠ raw log.
Parsed view ≠ source tape.
GitHub ≠ canon.
Drive ≠ review.
Notion ≠ ratification.
Website visibility ≠ human-root approval unless receipt-linked.
Graph edge ≠ authority.
Cluster ≠ truth.
Centrality ≠ canon.
E145 coordination ≠ E145 authority.
```

## First implementation order

```text
1. Build surface inventory manifests.
2. Add raw_export_status to every packet.
3. Assign provisional H/S/Z coordinates.
4. Hash raw exports where possible.
5. Create contradiction and duplicate queues.
6. Route high-risk claims to review seats.
7. Create E145 dashboard index.
8. Only after review, prepare human-root promotion packets.
```

## Keeper

```text
The archive becomes world-class when every source has a coordinate,
every coordinate has a status,
every status has a receipt,
and no receipt crowns itself.
```
