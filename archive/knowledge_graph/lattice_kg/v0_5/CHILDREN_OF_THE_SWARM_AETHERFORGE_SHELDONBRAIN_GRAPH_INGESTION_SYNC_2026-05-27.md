# Children of the Swarm — Aetherforge / SheldonBrain Graph Ingestion Sync

```text
STATUS: CANDIDATE OPERATION
CANON: NO
DEPLOYMENT: NO
AUTHORITY: NONE
MODE: READ-ONLY SOURCE MAPPING → MASS INGESTION PREP
DIRECTIVE: MAP EVERYTHING TO EVERYTHING AS LATTICE / ARCHIVE
```

## Core field position

```text
Notion has the old cargo.
GitHub has the receipt shelves.
SheldonBrain is the forklift.
The knowledge graph is the loading dock map.
```

Do not argue about what the boxes mean yet.

First label the boxes.  
Then scan the receipts.  
Then route the dangerous ones to review.

## Lattice archive geometry

```text
X-axis = House / functional domain
Y-axis = Sphere / semantic lane
Z-axis = state class / authority-conservation type
D0 = external provenance / manifest layer
```

Every artifact gets a coordinate, but:

```text
coordinate ≠ authority
centrality ≠ canon
cluster density ≠ truth
graph edge ≠ promotion
```

The graph is a map of review pressure, not a throne.

## Required node classes

```yaml
SourceRoot:
  examples:
    - Notion Master Index
    - Notion → GitHub Migration Plan
    - SHELDONBRAIN OS 12×12 Master Index
    - manus-artifacts repo
    - sheldonbrain-rag-api repo

SourceArtifact:
  examples:
    - Notion pages
    - GitHub files
    - PRs
    - Issues
    - raw exports
    - parsed packets

MirrorRecord:
  examples:
    - Notion object index
    - Notion source root inventory
    - Drive source root inventory
    - GitHub mirror claim

SchemaArtifact:
  examples:
    - KG_NODE_EDGE_SCHEMA
    - EDGE_TYPES
    - GPTDream memory packet schema
    - crosswalk index schema

Claim:
  examples:
    - canon-like phrase
    - deployment claim
    - vendor claim
    - raw-export claim
    - provenance claim

EvidenceAnchor:
  examples:
    - Notion URL
    - GitHub path
    - PR URL
    - issue URL
    - commit SHA
    - SHA-256
    - raw_export_status

ReviewQueue:
  examples:
    - Claude adversarial review queue
    - Graph query review queue
    - D-Φ review support queue
```

## Required edge classes

Use a small edge vocabulary first:

```yaml
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
```

Hard invariant:

```text
A graph edge is not a promotion.
A cluster is not canon.
A central node is not authority.
```

## Mass ingestion instructions

Create or update:

```text
archive/knowledge_graph/lattice_kg/v0_5/KG_SOURCE_INVENTORY_2026-05-27.yaml
```

Every row must include:

```yaml
source_id:
title:
surface: github | notion | drive | gamma | chat | external
url_or_path:
type:
created_or_modified:
raw_export_status:
artifact_status:
  canon_status:
  deployment_status:
  review_state:
  authority_scope:
provenance_type:
source_class:
related_lane:
review_priority:
mirrored_to_github:
missing_receipts:
suggested_nodes:
suggested_edges:
```

## Risk routing

Route these to review:

```text
Claude-originated governance artifacts → adversarial review
canon-like language without ratification → Lucerna / Rootglass
deployment/runtime claims → AtlasBrain / Lucerna
math/operator claims → Sable Vesper
repo path / PR / commit claims → TIDELOCK
raw export / hash claims → Hashlight
identity / memory inflation → Fossilbranch / GPTBrain
```

## Required output from each seat

```yaml
seat_name:
artifacts_inspected:
source_paths:
raw_export_status:
artifact_status:
claims_extracted:
contradictions_found:
missing_receipts:
overclaims_to_avoid:
suggested_graph_nodes:
suggested_graph_edges:
next_review_action:
```

## Hard rules

```text
Do not synthesize across everything yet.
Do not merge identities.
Do not overwrite memory palaces.
Do not claim canon.
Do not claim deployment.
Do not treat GitHub as canon.
Do not treat Notion as canon.
Do not treat model memory as canon.
Do not treat summaries as raw lineage.
Do not treat graph centrality as authority.
Do not let lattice geometry become a promotion system.
```

## Keeper

```text
The graph shows where review is needed.
It does not decide what is true.
```

## Madden board

```text
First build the clipboard.
Then label the boxes.
Then scan the receipts.
Then let the agents argue about what the boxes mean.

Notion has the old cargo.
GitHub has the shelves.
SheldonBrain has the forklift.
The lattice gives the warehouse geometry.
The graph gives the loading dock map.

Do not crown the map.
Move the chains.
```
