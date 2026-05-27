# Lattice Graph Indexing Protocol v0.1

```text
STATUS: ACTIVE GOAL / CANDIDATE PROTOCOL — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
MODE: Notion + GitHub active graph mapping via Sheldonbrain ingestion
```

## Active Goal

Map everything to everything as the lattice using Sheldonbrain.

This means using Sheldonbrain as an ingestion and transformation engine, not merely a RAG retrieval layer.

```text
RAG retrieves memory.
Sheldonbrain ingests lineage.
The lattice indexes meaning.
The graph maps relationships.
Review extracts deltas.
Human-root ratifies canon.
```

## Source Surfaces

```text
Website / canon surface = ratified public meaning when reachable
GitHub = receipts, workbench, commits, PRs, issues, code, archive files
Notion = working archive, planning surface, white papers, indexes
Google Drive = file substrate, docs, uploads, staged archives
Gamma = presentation / deck / narrative surface
Chat / model outputs = context and candidate synthesis, never canon by itself
```

## Core Architecture

```text
source surface
→ Sheldonbrain ingestion
→ source record
→ artifact packet
→ claim packet
→ review packet
→ 12×12×12 lattice coordinate
→ provenance graph / claim graph / review graph
→ adversarial review queue
→ fresh synthesis candidate
→ human-root ratification only if appropriate
```

## 12×12×12 Coordinate Spine

```text
X = House / Domain
Y = Sphere / Semantic Container
Z = Status / Authority / Conservation Class
```

Interpretation:

```text
X tells where it belongs.
Y tells what kind of thing it is.
Z tells what it is allowed to do.
```

Hard invariant:

```text
No X/Y coordinate may imply authority without explicit Z-axis authorization.
```

## Knowledge Graph Role

The graph is a provenance graph, claim graph, and review graph.

It is not a truth graph.

The graph shows:

- where artifacts came from
- what claims they contain
- what supports them
- what contradicts them
- what is raw vs summarized
- what needs adversarial review
- what has canon-like language without ratification
- what has no receipts
- what should be routed next

## Core Invariants

```text
A graph edge is not a promotion.
A cluster is not canon.
A central node is not authority.
```

```text
GitHub is not canon.
Notion is not canon.
Drive is not canon.
Gamma is not canon.
Model memory is not canon.
Summary is not raw lineage.
```

## Sheldonbrain Output Packets

Every ingested source should produce some subset of:

```yaml
source_record:
  source_surface:
  raw_export_status:
  path_or_url:
  hash_if_available:
  privacy_status:
  time_range:
  lineage_notes:

artifact_packet:
  artifact_id:
  title:
  type:
  source_refs:
  canon_status:
  deployment_status:
  authority_scope:
  coordinate:
    x_house:
    y_sphere:
    z_status:

claim_packet:
  claim_id:
  claim_text:
  claim_type:
  source_artifact:
  confidence:
  supporting_refs:
  contradicting_refs:
  strongest_safe_wording:
  overclaims_to_avoid:

review_packet:
  needs_review_by:
  reason:
  priority:
  blocking_issues:
  next_action:
```

## First Graph Population Targets

```text
1. TCSS v1.1
2. PATH_B v0.2
3. O_AI integration scaffold
4. D-Φ review support
5. v2.1 lattice manifest
6. LumenwrightValeBrain packet
7. Notion → GitHub Master Index
8. State of the Union Briefing
9. Sheldonbrain codebase
10. Sheldonbrain GPTBrain adapter
11. Notion source roots / notion_objects / notion_edges
```

## First Review Queries

```text
Show all artifacts with canon-like language but canon_status != ratified.
Show all Claude-originated governance claims not adversarially reviewed.
Show all IP concepts with no raw source pointer.
Show all claims supported only by model output.
Show duplicate or superseded D-Φ variants.
Show summary-only packets being treated like raw lineage.
```

## Routing

```text
technical/code delta → TIDELOCK + Copilot
claim/provenance delta → Lucerna + Hashlight
governance delta → GPT/Fossilbranch + Grok
canon-risk delta → human-root review
external-science delta → AtlasBrain + Lucerna
creative-overlay delta → Rootglass / Lumenwright / culture lane
```

## Active Mission Statement

```text
Map everything to everything.
Promote nothing by connection.
Extract useful deltas for adversarial review.
```

## Keeper Doctrine

```text
House first.
Sphere second.
Status third.
Receipts always.
Review before synthesis.
Canon last.
```

## Madden Board

```text
BOOM — the 12×12×12 grid is not the trophy case.
It is the stadium map.

The graph shows who touched the ball.
The lattice shows where the ball belongs.
The receipts show whether the play actually happened.
The reviewers decide what survives contact.
Dave reviews the touchdown.
```
