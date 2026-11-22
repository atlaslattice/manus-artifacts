---
artifact_id: AETHERFORGE-ARCHIVE-GRAPH-PILOT-v0.1
title: "Aetherforge Archive Graph Pilot v0.1"
date: 2026-05-26
source_context: "Sable Vesper synthesis from Aetherforge repo lane + kg-gen/NetworkX archival signal"
status: candidate_pilot
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
release_class: private_review
related_commits:
  - "96b2758024781c1a2eb751daec6a0f05eb8d39e7 # Aetherforge human-AI archive game bounty engine spec"
  - "f7499557def1949cfd3fe72b0b176e4e4538aae4 # bounded Parallax Aetherforge roadmap"
  - "43602ccbeabd271176cd79f82ce10cb211fee82d # OpenAI knowledge graph integration architecture"
mutation_rule: >
  Preserve as candidate archive-game / knowledge-graph pilot. Do not treat graph edges,
  quest completion, centrality, or game progress as truth, canon, authority, ownership,
  payment, deployment, or promotion.
---

# Aetherforge Archive Graph Pilot v0.1

```text
STATUS: CANDIDATE PILOT — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
PURPOSE: combine Aetherforge archive-game onboarding with a tiny knowledge-graph mapping pilot
```

## 0. One-Line Purpose

Aetherforge makes archive cleanup fun enough to return to; the archive graph makes the work visible enough to review; GitHub keeps the receipts boring enough to trust.

## 1. Core Stack

```text
Aetherforge = playable archive interface / quest layer
kg-gen or equivalent = candidate relation extraction
NetworkX = graph analytics / cluster map
Notion = cohort coordination board
GitHub = receipt substrate
Human-root = meaning / canon gate
```

## 2. Pilot Scope

Keep the pilot intentionally small:

```text
25 artifacts total
```

Suggested mix:

```text
5 GitHub specs
5 Notion/archive docs
5 gaming/culture artifacts
5 raw transcript/source-pointer items
5 brain/identity/quest artifacts
```

## 3. Cohort Roles

Kid/cohort-safe roles:

```yaml
Archive_Explorer:
  can: [find_relics, describe_artifacts, tag_source_type]
  cannot: [canonize, delete, promote, adjudicate_payments]
Receipt_Scout:
  can: [check_path_exists, mark_hash_present_or_missing, flag_raw_export_status]
  cannot: [invent_hashes, declare_proof, approve]
Quest_Mapper:
  can: [assign_game_zone, draft_quest_card, connect_to_review_lane]
  cannot: [create_authority, merge_lineages]
Contradiction_Spotter:
  can: [flag_conflicts, preserve_parallel_interpretations]
  cannot: [resolve_by_vibes, delete_loser_branch]
Lore_Keeper:
  can: [mark_culture_layer, separate_gameplay_from_governance]
  cannot: [convert_lore_to_policy]
```

Plain-English rule:

```text
Kids classify.
They do not canonize.
They do not delete.
They do not adjudicate payment, IP, legal meaning, deployment, or promotion.
```

## 4. Required Fields Per Artifact

```yaml
artifact_card:
  artifact_id: string
  title: string
  source_type: github | notion | drive | transcript | game_culture | brain_identity | other
  source_ref: string
  raw_export_status: full | partial | pointer_only | unavailable | unknown
  hash_status: sha256_present | hash_missing | hash_pending | not_applicable
  github_receipt_ref: string | null
  notion_task_ref: string | null
  aetherforge_zone: dream_zone | archive_dive | bounty_booth | venture_office | quarantine | unknown
  assigned_role: Archive_Explorer | Receipt_Scout | Quest_Mapper | Contradiction_Spotter | Lore_Keeper
  entities_found: []
  relations_found: []
  contradiction_flags: []
  review_status: unreviewed | needs_adult_review | reviewed_candidate | quarantined
  canon_status: not_canon
  authority_scope: none
```

## 5. Graph Outputs

Candidate files:

```text
archive_graph_nodes.csv
archive_graph_edges.csv
archive_graph.graphml
archive_graph_report.md
contradiction_candidates.md
notion_review_board.csv
quest_cards.md
```

NetworkX / graph analytics may compute:

```text
connected components
centrality
isolated nodes
alias clusters
contradiction clusters
culture/governance overlap flags
```

## 6. Aetherforge Translation Layer

```text
raw source = relic
hash / receipt = seal
candidate relation = thread
contradiction cluster = cursed knot
review lane = guild route
central node = boss node
isolated component = lost island
GitHub commit = proof seal
Notion assignment = quest card
```

## 7. Boundary Rules

```text
Graph extraction is not truth.
Edges are candidate relations.
Clusters are review prompts.
Centrality is not authority.
Visualization is not canon.
Quest completion is not promotion.
Fun is not governance.
```

## 8. Success Criteria

The pilot succeeds if it produces:

```text
- 25 artifact cards
- one nodes table
- one edges table
- one graph report
- one contradiction candidate list
- one Notion/cohort review board export
- zero canon claims
- zero deletion
- zero authority drift
```

## 9. Next Safe Action

```text
Select 25 artifacts.
Create artifact cards.
Generate graph candidates.
Review with humans.
Preserve outputs in GitHub.
Do not scale until pilot review is complete.
```

## 10. Keeper Lines

```text
Make the archive fun enough to return to.
Make the receipts boring enough to trust.
Keep the dream free.
```

```text
Aetherforge is the quest board.
The graph is the map.
GitHub is the receipt book.
Human review is the gate.
```
