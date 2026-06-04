# Aetherforge

> **Status:** CANDIDATE  
> **Artifact Type:** system overview  
> **Date:** 2026-05-28  
> **Related:** [Aetherforge Game Loop Spec](../../projects/aetherforge-game-world/AETHERFORGE_GAME_LOOP_SPEC_v0.1.md), [Quest Types](./quest-types.md), [Questboard](./questboard-2026-05-28.md), [Playable Curation Loop](./playable-curation-loop-v0.1.md)

## What Aetherforge Is

<!-- METADATA
stable_id: AL-AF-101
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

Aetherforge is the **playable archive game layer** for Atlas Lattice. It turns curation, metadata repair, intake, validation, and ratification prep into explicit quests with rewards, receipts, and progression.

## How It Fits the Repository

Aetherforge sits on top of three existing layers:

1. The [mission charter](../../projects/AETHERFORGE_LATTICE_GPTDREAM_MISSION_CHARTER_v0.1.md), which defines the north-star objective.
2. The [knowledge graph registry](../knowledge-graph/artifact_registry.v0_1.json), which gives artifacts stable identities and links.
3. The [ratification and trust flow](../RATIFICATION_AND_TRUST_FLOW.md), which keeps candidate work auditable without pretending it is canon.

## Core Play Loop

1. Pull an open quest from the questboard.
2. Execute the curation task against a real repository need.
3. Run validation and emit a receipt.
4. Update board state, XP, and follow-up links.

## Primary Spec

- [Aetherforge Game Loop Spec v0.1](../../projects/aetherforge-game-world/AETHERFORGE_GAME_LOOP_SPEC_v0.1.md)
- [Aetherforge Rolling Sprints v0.1](../../projects/AETHERFORGE_ROLLING_SPRINTS_v0.1.md)
- [Aetherforge 144-Task Campaign](../../projects/aetherforge-144-task-campaign-2026-05-27.md)

## Curation Loop Artifacts in This Folder

- [Quest Types](./quest-types.md)
- [Quest-to-Task Map](./quest-to-task-map.md)
- [Questboard — 2026-05-28](./questboard-2026-05-28.md)
- [Curation Loops](./curation-loops.md)
- [Intake Quest Flow](./intake-quest-flow.md)
- [Cross-Link Quest Flow](./crosslink-quest-flow.md)
- [Metadata Backfill Quest Flow](./metadata-backfill-quest-flow.md)
- [Evidence Logging Quest Flow](./evidence-logging-quest-flow.md)
- [Public-Readiness Polish Quest Flow](./public-readiness-polish-quest-flow.md)
- [Playable Curation Loop v0.1](./playable-curation-loop-v0.1.md)

## Current Posture

Everything in this folder is candidate-state operating guidance for archive curation. Nothing here promotes an artifact to canon without the separate ratification path.
