---
hsn: H09-S09-N01
title: Knowledge Graph System Architecture Seed
author: David Sheldon (@atlaslattice)
date: 2026-05-29
review_state: seed
license: MIT
canon: "no"
source_boundary: "Architecture seed for the KG system layer. Candidate design."
---

# Knowledge Graph System Architecture Seed

STATUS: SEED — NOT CANON

## Architecture layers

```text
Layer 1: Artifact Registry   → docs/knowledge-graph/artifact_registry.v0_1.json
Layer 2: Coordinate Map      → H-S-N assignments per artifact
Layer 3: Graph Export        → graph.json (nodes + edges)
Layer 4: Query Engine        → archive/spec/lattice-hypercube/data/
Layer 5: Explorer UI         → docs/graph-explorer.html
```

## Key scripts

- `scripts/build_lattice_global_index.py`
- `scripts/validate_lattice_quality_gates.py`
