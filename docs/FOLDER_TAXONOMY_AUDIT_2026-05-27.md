---
artifact_id: DOC-TAXONOMY-AUDIT-2026-05-27
title: Folder Taxonomy Audit (Wave 1)
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---
# Folder Taxonomy Audit (2026-05-27)

## Current top-level domains

- `docs/` documentation and orientation surfaces
- `projects/` active initiatives and taskboards
- `archive/` historical + boot + protocol artifacts
- `reference_impl/` executable protocol logic
- `schemas/` formal validation schemas
- `tests/` repository validation tests
- `aluminum-os/`, `sheldonbrain/`, `bazinga/` core systems
- `research/`, `health/`, `council/`, `council-reviews/`, `manus-vault/`

## Wave 1 normalization recommendations

1. Keep one README-style orientation page per major top-level domain.
2. Keep taskboards under `projects/` and quality gates under `.github/workflows/`.
3. Keep executable validators in `scripts/` and test mirrors in `tests/`.
4. Keep metadata schemas versioned in `schemas/<domain>/<version>/`.
5. Keep dream artifacts explicitly NON CANON until ratified.
