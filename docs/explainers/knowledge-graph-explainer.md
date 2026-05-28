# Knowledge Graph Explainer

> **Status:** CANDIDATE  
> **Artifact Type:** public explainer  
> **Date:** 2026-05-28  
> **Related:** [Artifact Registry](../knowledge-graph/artifact_registry.v0_1.json), [Knowledge Graph Topic](../topics/knowledge-graph.md), [Mission Charter](../../projects/AETHERFORGE_LATTICE_GPTDREAM_MISSION_CHARTER_v0.1.md)

## What Is a Knowledge Graph?

<!-- METADATA
stable_id: AL-SYS-322
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

A knowledge graph is like a **library card catalog plus a subway map**. Each artifact gets a stable identity, and the links tell you how to move from one idea to the next.

## How Atlas Lattice Uses It

Atlas Lattice uses the graph to assign **stable IDs**, record explicit relations, and maintain a central **registry** of candidate artifacts. That lets mission docs, governance docs, game-loop docs, and evidence docs point to one another in a machine-readable way.

## Why Stable IDs Matter

Stable IDs keep long-lived knowledge from becoming ambiguous. A filename can move or be renamed; an ID like `AL-KG-003` gives readers and tools a durable handle for the same artifact across time.

## How to Navigate It

### Example Traversal 1
`AL-MISSION-001` → `AL-AF-001`  
Start at the mission charter, then follow the link to the Aetherforge game loop to see how the mission becomes playable work.

### Example Traversal 2
`AL-KG-002` → `AL-RT-001`  
Start at the registry, then move to the ratification flow to understand how graph entries stay candidate until review.

### Example Traversal 3
`AL-GP-001` → `AL-GP-002`  
Start at the GPTDream++ open gift guide, then move to the vault manifest to inspect the actual package contents.

## Why It Is Open Source

Making the graph public helps others audit claims, reuse structures, and contribute without relying on hidden context. Openness turns the archive from a private pile of files into a navigable commons.
