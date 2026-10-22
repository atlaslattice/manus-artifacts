---
artifact_id: AETHERFORGE-WORLD-CLASS-12x12-TASK-MATRIX-v0.1
title: "Aetherforge / Sheldonbrain World-Class 12x12 Task Matrix v0.1"
date: 2026-05-26
source_context: "User request for 144 enjoyable tasks in a 12x12 matrix to make the operation world-class"
status: candidate_task_matrix
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
release_class: private_review
related_context:
  - "Children of the Swarm — Aetherforge / Sheldonbrain Graph Ingestion Sync"
  - "Aetherforge Archive Graph Pilot v0.1"
  - "Sheldonbrain / graph ingestion / adversarial review lane"
mutation_rule: >
  Preserve as a candidate task matrix. These tasks are review prompts and workflow candidates,
  not canon, deployment, employment assignments, legal obligations, or authority transfers.
---

# Aetherforge / Sheldonbrain World-Class 12x12 Task Matrix v0.1

```text
STATUS: CANDIDATE TASK MATRIX — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
PURPOSE: identify 144 bounded tasks for turning the archive operation into a world-class, reviewable, playful, provenance-first system
```

## 0. Operating Rule

```text
The graph shows where review is needed.
It does not decide what is true.
```

This matrix is built for Aetherforge + Sheldonbrain + GPTDream++ archive work.

It supports:

```text
source mapping
raw lineage
knowledge graph construction
Notion coordination
GitHub receipts
kids/cohort quest work
adversarial review
public-safe extraction
small automation
fresh synthesis
```

It does not grant canon, deployment, authority, ownership, payment, or officiality.

---

## House 01 — Source Roots & Warehouse Mapping

| Slot | Task |
|---|---|
| H01-S01 | Inventory the top-level GitHub repos relevant to Sheldonbrain, Aetherforge, GPTDream++, ORCS, and archive work. |
| H01-S02 | Inventory Notion source-root pages and classify each as index, spec, migration plan, protocol, or historical substrate. |
| H01-S03 | Inventory Drive/Gamma/export surfaces and mark whether they have raw export access. |
| H01-S04 | Create a SourceRoot node for `atlaslattice/manus-artifacts`. |
| H01-S05 | Create a SourceRoot node for `atlaslattice/sheldonbrain-rag-api`. |
| H01-S06 | Create SourceRoot nodes for active Notion master indexes. |
| H01-S07 | Create SourceRoot nodes for active game/culture archive clusters. |
| H01-S08 | Mark source roots with `raw_export_status`. |
| H01-S09 | Mark source roots with `canon_status`, `deployment_status`, and `authority_scope`. |
| H01-S10 | Flag source roots with unsupported `production ready`, `canon`, or `official` language. |
| H01-S11 | Build a source-root priority queue for the first 25-artifact pilot. |
| H01-S12 | Produce a one-page warehouse map for humans: GitHub shelves, Notion cargo, Drive crates, chat tapes. |

## House 02 — Manifests, Receipts, and Raw Lineage

| Slot | Task |
|---|---|
| H02-S01 | Define a manifest row format for archive artifacts. |
| H02-S02 | Generate a SHA-256 manifest for the first pilot batch. |
| H02-S03 | Record which artifacts have full raw export, partial export, pointer-only, or unavailable raw. |
| H02-S04 | Separate raw transcript, summary, parser output, and claim packet status. |
| H02-S05 | Create missing-receipt nodes for any artifact lacking a source/hash/path. |
| H02-S06 | Create EvidenceAnchor nodes for commit SHAs, issue URLs, PR URLs, Notion URLs, and raw export hashes. |
| H02-S07 | Flag summaries that imply raw access without proof. |
| H02-S08 | Add `raw_export_status` to every artifact card. |
| H02-S09 | Add `hash_status` to every artifact card. |
| H02-S10 | Build a missing raw transcript report. |
| H02-S11 | Build a raw-vs-summary confusion report. |
| H02-S12 | Write a short cohort guide: “Summary is not raw. Pointer is not proof.” |

## House 03 — Artifact Status & Schema Discipline

| Slot | Task |
|---|---|
| H03-S01 | Define a minimal `artifact_card` schema for the pilot. |
| H03-S02 | Define allowed values for `canon_status`. |
| H03-S03 | Define allowed values for `deployment_status`. |
| H03-S04 | Define allowed values for `authority_scope`. |
| H03-S05 | Define allowed values for `review_state`. |
| H03-S06 | Define allowed values for `source_type`. |
| H03-S07 | Define allowed values for `raw_export_status`. |
| H03-S08 | Define allowed values for `provenance_type`. |
| H03-S09 | Create a JSON Schema candidate for `artifact_card`. |
| H03-S10 | Create fixtures for valid and invalid artifact cards. |
| H03-S11 | Validate 25 pilot artifact cards against the schema. |
| H03-S12 | Produce a schema drift report after pilot entry. |

## House 04 — Knowledge Graph Nodes & Edges

| Slot | Task |
|---|---|
| H04-S01 | Seed node classes: SourceRoot, SourceArtifact, MirrorRecord, SchemaArtifact, Claim, EvidenceAnchor, ReviewQueue. |
| H04-S02 | Seed edge classes: raw_export_of, parsed_from, mirrored_to, derived_from, cites, contradicts. |
| H04-S03 | Add `supersedes`, `patches`, `requires_review`, `missing_receipt`, `belongs_to_lane`. |
| H04-S04 | Create node entries for the first 25 artifacts. |
| H04-S05 | Create edge entries for obvious source/ref relationships only. |
| H04-S06 | Create `missing_receipt` edges where proof is absent. |
| H04-S07 | Create `contradicts` edges only where text actually conflicts. |
| H04-S08 | Create `requires_review` edges for canon-like language. |
| H04-S09 | Export `archive_graph_nodes.csv`. |
| H04-S10 | Export `archive_graph_edges.csv`. |
| H04-S11 | Export `archive_graph.graphml`. |
| H04-S12 | Write `graph_report.md` with centrality caveats. |

## House 05 — Notion Cohort Board & Human Workflow

| Slot | Task |
|---|---|
| H05-S01 | Create or update a Notion cohort review board. |
| H05-S02 | Add columns for Relic Name, Source Type, Source Ref, Raw Export Status, Hash Status. |
| H05-S03 | Add columns for Aetherforge Zone, Assigned Explorer, Review Status, Needs Adult Review. |
| H05-S04 | Add a view grouped by cohort role. |
| H05-S05 | Add a view grouped by review priority. |
| H05-S06 | Add a view for missing receipts. |
| H05-S07 | Add a view for culture/game artifacts. |
| H05-S08 | Add a view for canon-like language needing review. |
| H05-S09 | Add a view for contradiction candidates. |
| H05-S10 | Import the 25 pilot artifact cards into Notion. |
| H05-S11 | Export Notion board state to CSV for GitHub receipt. |
| H05-S12 | Write the cohort onboarding note: “First label boxes. Then scan receipts.” |

## House 06 — GitHub Receipts, PRs, Issues, and Codebase Hygiene

| Slot | Task |
|---|---|
| H06-S01 | Map current Aetherforge commits into a receipt timeline. |
| H06-S02 | Map current PRs/issues connected to Aetherforge, Sheldonbrain, and knowledge graph work. |
| H06-S03 | Verify file-path truth for claimed artifacts. |
| H06-S04 | Flag any claimed file path not found in GitHub. |
| H06-S05 | Create GitHub issue for the 25-artifact pilot if needed. |
| H06-S06 | Create draft PR for pilot outputs only after files exist. |
| H06-S07 | Keep game/culture artifacts under creative/archive lanes. |
| H06-S08 | Keep schemas under knowledge_graph or schema lanes. |
| H06-S09 | Keep raw exports / receipts distinct from parsed packets. |
| H06-S10 | Add PR body guardrails: not canon, not deployment, no authority. |
| H06-S11 | Run repo search for duplicate or conflicting Aetherforge specs. |
| H06-S12 | Produce merge-order recommendation after pilot review. |

## House 07 — Aetherforge Game Layer & Quest Design

| Slot | Task |
|---|---|
| H07-S01 | Convert each pilot artifact into a kid-safe quest card. |
| H07-S02 | Define Archive Explorer quest type. |
| H07-S03 | Define Receipt Scout quest type. |
| H07-S04 | Define Quest Mapper quest type. |
| H07-S05 | Define Contradiction Spotter quest type. |
| H07-S06 | Define Lore Keeper quest type. |
| H07-S07 | Create a glossary: relic, seal, thread, cursed knot, guild route, lost island. |
| H07-S08 | Create a simple score that rewards return/fun but grants no authority. |
| H07-S09 | Create a “no work inside dream zone” reminder card. |
| H07-S10 | Create a bounty-booth warning card for adults only. |
| H07-S11 | Create a quest completion receipt template. |
| H07-S12 | Create a “fun is not governance” poster line. |

## House 08 — Cohort Safety, Roles, and Learning Design

| Slot | Task |
|---|---|
| H08-S01 | Write kid-safe role rules in plain English. |
| H08-S02 | Define what kids can classify. |
| H08-S03 | Define what kids must escalate to adults. |
| H08-S04 | Define “do not delete” behavior. |
| H08-S05 | Define “do not decide canon” behavior. |
| H08-S06 | Define privacy and sensitive-file handling. |
| H08-S07 | Define how to mark a file as confusing without fixing it. |
| H08-S08 | Define how to mark a contradiction without resolving it. |
| H08-S09 | Define how to handle gaming/culture artifacts. |
| H08-S10 | Define how to handle possible IP/payment language. |
| H08-S11 | Create a lightweight training checklist. |
| H08-S12 | Create a “successful silence/rest counts” norm for cohort pacing. |

## House 09 — Adversarial Review & Overclaim Control

| Slot | Task |
|---|---|
| H09-S01 | Route Claude-originated governance artifacts to adversarial review. |
| H09-S02 | Flag `production-ready` without deployment receipt. |
| H09-S03 | Flag `canon` without ratification receipt. |
| H09-S04 | Flag `official` without official source. |
| H09-S05 | Flag `ownership`, `IP`, or `revenue share` claims without contract basis. |
| H09-S06 | Flag graph centrality mistaken for authority. |
| H09-S07 | Flag Notion page existence mistaken for canon. |
| H09-S08 | Flag GitHub commit existence mistaken for ratification. |
| H09-S09 | Flag model memory mistaken for raw lineage. |
| H09-S10 | Flag play/culture artifacts reused as policy. |
| H09-S11 | Write an overclaim report for the pilot. |
| H09-S12 | Write a “strongest safe claims” report for the pilot. |

## House 10 — Public-Safe Extraction & Story Layer

| Slot | Task |
|---|---|
| H10-S01 | Extract public-safe description of Aetherforge. |
| H10-S02 | Extract public-safe description of Sheldonbrain graph ingestion. |
| H10-S03 | Extract public-safe explanation for parents/cohort adults. |
| H10-S04 | Extract public-safe explanation for technical reviewers. |
| H10-S05 | Extract public-safe explanation for potential funders/partners without promises. |
| H10-S06 | Create a one-page “What this is not” statement. |
| H10-S07 | Create a one-page “Why game mechanics help archives” statement. |
| H10-S08 | Create a one-page “Graph edges are candidate relations” statement. |
| H10-S09 | Create a glossary of non-governance game terms. |
| H10-S10 | Create screenshots/diagrams only after source permissions are clear. |
| H10-S11 | Draft a private demo script for the 25-artifact pilot. |
| H10-S12 | Draft a public-safe demo script with no private data. |

## House 11 — Automation, Parsers, and Tiny Tools

| Slot | Task |
|---|---|
| H11-S01 | Write a tiny artifact-card validator. |
| H11-S02 | Write a CSV exporter for artifact cards. |
| H11-S03 | Write a simple nodes/edges generator from artifact cards. |
| H11-S04 | Write a NetworkX loader for nodes/edges. |
| H11-S05 | Compute connected components. |
| H11-S06 | Compute centrality with a warning label. |
| H11-S07 | Export GraphML. |
| H11-S08 | Generate a contradiction-candidates report. |
| H11-S09 | Generate a missing-receipts report. |
| H11-S10 | Generate a Notion import CSV. |
| H11-S11 | Generate quest cards from artifact cards. |
| H11-S12 | Add tests proving graph metrics do not change canon_status. |

## House 12 — Fresh Synthesis, Review, and World-Class Finish

| Slot | Task |
|---|---|
| H12-S01 | Review the 25-artifact pilot outputs with humans. |
| H12-S02 | List what worked. |
| H12-S03 | List what confused people. |
| H12-S04 | List which fields were missing most often. |
| H12-S05 | List which graph relations were useful. |
| H12-S06 | List which graph relations were noisy. |
| H12-S07 | Decide whether to expand to 50 artifacts. |
| H12-S08 | Decide whether to formalize schemas. |
| H12-S09 | Decide whether to build a small UI. |
| H12-S10 | Decide whether to create a real bounty pilot, with adult/legal review only. |
| H12-S11 | Preserve the failed paths and negative results. |
| H12-S12 | Write the world-class operating memo: “The archive became playable without losing the receipts.” |

---

## Final Compression

```text
144 tasks.
12 houses.
One rule:
The graph shows where review is needed.
It does not decide what is true.
```
