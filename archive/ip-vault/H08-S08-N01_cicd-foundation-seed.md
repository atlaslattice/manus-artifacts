---
hsn: H08-S08-N01
title: CI/CD Foundation Seed
author: David Sheldon (@atlaslattice)
date: 2026-05-29
review_state: seed
license: MIT
canon: "no"
source_boundary: "Seed index for CI/CD workflows. Not a deployment system."
---

# CI/CD Foundation Seed

STATUS: SEED — NOT CANON

## Current workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| repo-hygiene-checks.yml | push/PR | Conflict markers, YAML lint, file checks |
| docs-link-checks.yml | push/PR | Dead link detection |
| gptbrain-reference-checks.yml | push/PR | GPTBrain pytest suite |
| metadata-provenance-checks.yml | push/PR | Provenance header validation |
| docs.yml | push main | MkDocs GitHub Pages deploy |

## Candidate additions

- `atlas-lattice-package.yml` — build + publish to PyPI on tag
- `graph-export.yml` — regenerate graph.json on artifact change
