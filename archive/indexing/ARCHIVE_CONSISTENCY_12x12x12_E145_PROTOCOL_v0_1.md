# Archive Consistency Protocol — 12×12×12 Hypercube + E145 v0.1

```text
STATUS: CANDIDATE INDEXING PROTOCOL — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
PURPOSE: Normalize archives across Website, GitHub, Notion, Drive/OneDrive, chat exports, and model outputs into a House × Sphere × Node index with full 12D artifact metadata and E145 meta-coordination.
HUMAN-ROOT: REQUIRED FOR CANON / DEPLOYMENT / AUTHORITY CHANGES
```

## Correction note

Earlier wording incorrectly treated the third coordinate axis as `Z = state / authority / data-nature type`.

Correct model:

```text
12×12×12 index coordinate = House × Sphere × Node.
Full artifact semantics = 12D metadata envelope around that coordinate.
```

So:

```text
Hxx.Syy.Nzz = indexing coordinate only.
```

Authority, provenance, review state, raw-export state, deployment state, resonance state, and canon status are **not** the third coordinate axis. They are typed dimensions in the 12D artifact envelope.

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

## 12×12×12 indexing coordinate model

Each indexed item receives a coordinate:

```text
Hxx.Syy.Nzz
```

Where:

```yaml
H_axis:
  name: House / functional domain
  range: H01-H12
  purpose: What major functional domain does this artifact belong to?

S_axis:
  name: Sphere / semantic subdomain
  range: S01-S12 per house
  purpose: What semantic container or subdomain does this artifact occupy?

N_axis:
  name: Node / item slot / local cell
  range: N01-N12 per sphere
  purpose: Which local indexed node, artifact slot, or cell within the House/Sphere does this occupy?
```

Hard rule:

```text
House/Sphere/Node is an address, not authority.
A coordinate can locate an artifact, but it cannot promote the artifact.
```

## Full 12D artifact envelope

Every H/S/N coordinate should be wrapped in a broader 12D metadata envelope. Candidate dimensions:

```yaml
artifact_12d_envelope:
  D01_coordinate:
    field: Hxx.Syy.Nzz
    purpose: House/Sphere/Node index address.

  D02_source_surface:
    field: website | github | notion | drive_onedrive | chat_transcript | model_output | external_web
    purpose: Where the artifact came from.

  D03_raw_export:
    field: raw_export_status
    purpose: Whether source tape exists.

  D04_hash_provenance:
    field: sha256 | commit_sha | blob_sha | checksum_manifest
    purpose: Whether content can be verified.

  D05_lineage_state:
    field: raw | parsed | summarized | superseded | quarantined | fossilized
    purpose: Whether this is source, derivative, or preserved history.

  D06_claim_state:
    field: raw_source | parsed_fact | claim_packet | evidence | contradiction | review_note
    purpose: What epistemic role the item plays.

  D07_review_state:
    field: unreviewed | in_review | reviewed | blocked | approved | contradicted
    purpose: Review progress.

  D08_authority_scope:
    field: none | advisory | review | ratification | execution
    purpose: What authority, if any, the artifact may carry.

  D09_canon_state:
    field: not_canon | candidate | ratified | canon
    purpose: Canon status, never inferred from coordinate alone.

  D10_deployment_state:
    field: not_deployed | simulated | staging | deployed
    purpose: Runtime/deployment status.

  D11_resonance_overlay:
    field: tone | polarity | chiral_dissonance | creative_overlay | not_applicable
    purpose: Optional interpretive/spectral metadata; not authority.

  D12_e145_meta:
    field: e145_index_status | route | gap | duplicate | contradiction | dashboard_node
    purpose: E145 read-across/meta-coordination status.
```

## Authority firewall

```text
Governance authority cannot be inferred from House, Sphere, Node, resonance, centrality, or graph connectivity.
```

Canon or deployment movement requires explicit status evidence in the 12D envelope and human-root review where applicable:

```text
D08_authority_scope + D09_canon_state + D10_deployment_state + D04_hash_provenance + human-root receipt.
```

## E145 role

E145 is the meta-coordinator across the H/S/N index and the full 12D artifact envelope.

```yaml
E145:
  role:
    - read across all House/Sphere/Node coordinates
    - read across the 12D metadata envelope
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
    N:
  artifact_12d_envelope:
    D01_coordinate:
    D02_source_surface:
    D03_raw_export:
    D04_hash_provenance:
    D05_lineage_state:
    D06_claim_state:
    D07_review_state:
    D08_authority_scope:
    D09_canon_state:
    D10_deployment_state:
    D11_resonance_overlay:
    D12_e145_meta:
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
Website page → rendered export → hash → source artifact → H/S/N coordinate + 12D envelope.
GitHub file → commit/blob SHA → artifact packet → H/S/N coordinate + 12D envelope.
Notion page → export or API fetch → raw_export_status → H/S/N coordinate + 12D envelope.
Drive/OneDrive file → file inventory + hash → H/S/N coordinate + 12D envelope.
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
Coordinate ≠ authority.
Resonance ≠ approval.
E145 coordination ≠ E145 authority.
```

## First implementation order

```text
1. Build surface inventory manifests.
2. Add raw_export_status to every packet.
3. Assign provisional H/S/N coordinates.
4. Wrap each coordinate in the 12D artifact envelope.
5. Hash raw exports where possible.
6. Create contradiction and duplicate queues.
7. Route high-risk claims to review seats.
8. Create E145 dashboard index.
9. Only after review, prepare human-root promotion packets.
```

## Keeper

```text
The archive becomes world-class when every source has a House/Sphere/Node coordinate,
every coordinate has a 12D envelope,
every envelope has status and receipts,
and no receipt crowns itself.
```
