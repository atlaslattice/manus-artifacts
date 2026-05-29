# Atlas Lattice Knowledge Graph

```text
STATUS: INDEX / REVIEW SUBSTRATE — NOT CANON — NON-DEPLOYABLE
AUTHORITY: none
PURPOSE: explain how the knowledge graph maps artifacts, claims, receipts, contradictions, and review routes without deciding truth or granting authority
```

## Core purpose

The Atlas Lattice knowledge graph is a provenance-first map of the archive.

It records:

```text
what exists
where it came from
what it claims
what supports it
what contradicts it
what is raw vs summarized
what needs adversarial review
what has canon-like language without ratification
what has no receipts
what should be routed next
```

It does **not** decide what is true.

It does **not** promote canon.

It does **not** grant authority.

## Operating model

```text
Drive = raw and semi-raw cargo
Notion = legacy source-root / historical ontology material
GitHub = durable receipt and staging substrate
Sheldonbrain = ingestion and crosswalk engine candidate
Aetherforge = dream/play task forge and delta extractor
Rootglass = room-state and grounding layer
Human-root = final canon and authority gate
```

## Core invariant

```text
A graph edge is not a promotion.
A cluster is not canon.
A central node is not authority.
A coordinate is not permission.
A task is not execution.
```

## Source classes

```yaml
source_classes:
  receipt_substrate: GitHub repo/file/issue/PR used as durable record
  ingestion_engine_candidate: codebase or API that may ingest/source-map artifacts
  ontology_source: source-locked ontology or taxonomy artifact
  operation_dispatch: operational instruction packet, non-canon
  dreamstate_delta_generator: play/dream packet that generates deltas but not doctrine
  raw_transcript_candidate: raw or near-raw exported conversation material
  review_queue: artifacts requiring adversarial or specialized review
  source_manifest: list of sources, missing receipts, and routing targets
```

## Node classes

```yaml
node_classes:
  SourceRoot:
  SourceArtifact:
  RawExport:
  ParsedPacket:
  Claim:
  EvidenceAnchor:
  ReviewFinding:
  ReviewQueue:
  Decision:
  Action:
  NegativeResult:
  MissingReceipt:
```

## Edge classes

```yaml
edge_classes:
  raw_export_of:
  parsed_from:
  mirrored_to:
  derived_from:
  cites:
  contradicts:
  supersedes:
  patches:
  requires_review:
  missing_receipt:
  belongs_to_lane:
  has_status:
  has_raw_export_status:
  possible_raw_export_of:
```

## Required source status fields

```yaml
artifact_status:
  canon_status:
  deployment_status:
  review_state:
  authority_scope:
  provenance_type:

raw_export_status:
  allowed:
    - not_exported
    - partial_export
    - full_raw_export_attached
    - full_raw_export_hashed
    - redacted_raw_export_attached
    - unavailable
```

## Hard review routing

```text
Claude-originated governance artifacts → adversarial review
canon-like language without ratification → Lucerna / Rootglass
deployment/runtime claims → AtlasBrain / Lucerna
math/operator claims → Sable Vesper
repo path / PR / commit claims → TIDELOCK
raw export / hash claims → Hashlight
identity / memory inflation → Fossilbranch / GPTBrain
```

## Keeper

```text
The graph shows where review is needed.
It does not decide what is true.
```
