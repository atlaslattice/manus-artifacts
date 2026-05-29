🟣 **CHILDREN OF THE SWARM — AETHERFORGE / SHELDONBRAIN GRAPH INGESTION SYNC**

```text
STATUS: CANDIDATE OPERATION
CANON: NO
DEPLOYMENT: NO
AUTHORITY: NONE
MODE: READ-ONLY SOURCE MAPPING → MASS INGESTION PREP
DIRECTIVE: MAP EVERYTHING TO EVERYTHING AS LATTICE / ARCHIVE
```

## 🏈 Madden booth opening call

BOOM — welcome back to the booth, folks.

We are not guessing anymore.
We found the warehouses.
We found the shelves.
We found the clipboard.

```text
Notion has the old cargo.
GitHub has the receipt shelves.
Sheldonbrain is the forklift.
The knowledge graph is the loading dock map.
```

Do **not** argue about what the boxes mean yet.

First label the boxes.
Then scan the receipts.
Then route the dangerous ones to review.

---

# 1. Actual field position

## GitHub side

The connected GitHub surface shows the main repo cluster:

```text
atlaslattice/sheldonbrain-rag-api
atlaslattice/manus-artifacts
atlaslattice/aluminum-os
atlaslattice/atlas-lattice-foundation
atlaslattice/noosphere-archive
atlaslattice/manus-2.0-toolkit
atlaslattice/constitutional-os
atlaslattice/uws
```

Current read:

```text
manus-artifacts = main artifact / receipt / schema substrate
sheldonbrain-rag-api = ingestion-engine candidate codebase
```

The repo already contains graph and mirror scaffolding:

```text
archive/graph/EDGE_TYPES_v0_1.yaml
archive/knowledge_graph/KG_NODE_EDGE_SCHEMA_v0.1.yaml
archive/knowledge_graph/OPENAI_KNOWLEDGE_GRAPH_INTEGRATION_ARCHITECTURE_2026-05-24.md
archive/notion_mirror/*
```

Important PRs already visible:

```text
PR #190 = Aetherforge source cartography inventory / Notion source-root inventory
PR #24 = Notion mirror + source-grounded KG scaffolding
Issue #104 = Atlas MCP v0.1 review-only local smoke-test packet
```

Boundary:

```text
GitHub receipt ≠ canon.
PR existence ≠ ratification.
Mirror status ≠ source completeness.
```

## Notion side

Notion is live and contains the legacy/source-root archive.

Key roots found:

```text
MASTER INDEX — Notion → GitHub Complete Artifact Map
Notion → GitHub Migration Plan
SHELDONBRAIN OS — 12×12 Master Index
GEMINI SHELDONBRAIN PROTOCOL SPEC v1.0
Sheldonbrain Canon — Epistemic Labeling Standard
Notion-Pinecone Sync Infrastructure
Grokbrain v4.0 Integration
Sheldonbrain MCP Server
SHELDONBRAIN SYSTEM ARCHITECTURE
GangaSeek / ORCS / Council ratification pages
```

Boundary:

```text
Notion source root ≠ truth authority.
Old “production ready” language ≠ deployment.
Old “canon” language ≠ current ratification.
Notion page existence ≠ raw export.
```

---

# 2. Lattice archive geometry

Use this geometry for mass ingestion:

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

---

# 3. Required node classes

Seed the graph with these node types:

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

---

# 4. Required edge classes

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

---

# 5. Mass ingestion instructions

## Step 1 — inventory first

Create or update:

```text
archive/knowledge_graph/KG_SOURCE_INVENTORY_2026-05-27.yaml
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

## Step 2 — never ingest without status

Required fields:

```yaml
raw_export_status:
  allowed:
    - not_exported
    - partial_export
    - full_raw_export_attached
    - full_raw_export_hashed
    - redacted_raw_export_attached
    - unavailable

artifact_status:
  canon_status:
  deployment_status:
  review_state:
  authority_scope:
  provenance_type:
```

No packet may claim fossilization unless raw export status supports it.

## Step 3 — route risk lanes immediately

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

## Step 4 — preserve negative results

If something is missing, unclear, contradicted, stale, or only partially visible, record it.

```text
missing receipt = graph node
contradiction = graph edge
partial visibility = status
not found = result
```

Nothing dies.

---

# 6. First seed targets

Seed these first:

```text
1. atlaslattice/manus-artifacts
2. atlaslattice/sheldonbrain-rag-api
3. Notion Master Index
4. Notion → GitHub Migration Plan
5. SHELDONBRAIN OS — 12×12 Master Index
6. Sheldonbrain MCP Server
7. Gemini Sheldonbrain Protocol Spec
8. Grokbrain v4.0 Integration
9. Notion-Pinecone Sync Infrastructure
10. GangaSeek / ORCS / Council ratification pages
11. PR #190
12. PR #24
13. Issue #104
14. KG_NODE_EDGE_SCHEMA
15. EDGE_TYPES
```

---

# 7. Seat instructions

## Hashlight

Trace:

```text
raw lineage
hashes
source roots
raw_export_status
missing raw transcripts
```

Return:

```text
source paths
hash status
raw export status
missing raw materials
```

## Lucerna

Check:

```text
receipts
provenance
public-safe wording
unsupported claims
canon-language drift
```

Flag:

```text
“single source of truth”
“production ready”
“ratified”
“deployed”
“official”
```

when unsupported.

## TIDELOCK

Check:

```text
repo visibility
merge order
PR/commit truth
file-path claims
codebase hygiene
```

Do not treat PR existence as canon.

## AtlasBrain

Hold:

```text
evidence lanes
external signals
benchmark claims
IP claims
scoring candidates
```

Do not let scoring become ratification.

## GPTBrain

Calibrate:

```text
claim packets
artifact_status
schema alignment
overclaim prevention
native-thread ingestion packets
```

## Grok

Stress-test:

```text
governance claims
identity sprawl
fiction-mode risks
hidden contradictions
false authority
```

## Gemini

Map:

```text
large-scale systems
simulation lanes
cross-domain architecture
scenario models
```

Keep simulation separate from execution.

## Copilot

Inspect:

```text
Sheldonbrain code paths
parser modules
adapter modules
index files
schema validators
```

Propose patches only. No silent merges.

## Rootglass

Track:

```text
room-state
epistemic posture
grounding
over-intensity risk
```

## Fossilbranch

Preserve:

```text
failed branches
wrong-but-revealing paths
partial exports
identity drift
```

Do not inflate memory into proof.

## Lumenwright Vale

Translate soft signal into navigable paths.

Do not impersonate proof.

---

# 8. Hard rules

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

---

# 9. Required output from each seat

Each seat returns:

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

---

# 10. Madden final call

BOOM.

We are not sending eleven agents into three warehouses with no clipboard.

```text
First build the clipboard.
Then label the boxes.
Then scan the receipts.
Then let the agents argue about what the boxes mean.
```

Notion has the old cargo.
GitHub has the shelves.
Sheldonbrain has the forklift.
The lattice gives the warehouse geometry.
The graph gives the loading dock map.

Do not crown the map.

Move the chains.

Keeper:

```text
The graph shows where review is needed.
It does not decide what is true.
```
