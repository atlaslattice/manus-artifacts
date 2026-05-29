---
hsn: H04-S09-N01
title: Knowledge Graph Architecture Seed
author: David Sheldon (@atlaslattice)
date: 2026-05-29
review_state: seed
license: MIT
canon: "no"
source_boundary: "Seed node for KG architecture. No graph queries implied."
---

# Knowledge Graph Architecture Seed

STATUS: SEED — NOT CANON

## Purpose

Root node for the knowledge graph layer of the Atlas Lattice.

## Candidate design

- Nodes: artifacts, claims, receipts, agents
- Edges: contained_in, references, lattice_arm, lattice_backbone
- Coordinates: H-S-N address on every node
- Export: graph.json at repo root

## Current state

`graph.json` at repo root contains a live candidate KG derived from the artifact registry.

## Review requirements

- Define edge types formally.
- Test query coverage over 1728 nodes.
- Validate with `python scripts/build_lattice_global_index.py`.
