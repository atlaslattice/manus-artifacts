---
artifact_id: DOC-SCHEMA-VERSION-MIGRATION-NOTES-V0-1-2026-05-27
title: Schema Version Migration Notes v0.1
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---

# Schema Version Migration Notes v0.1

## Current baseline

- Artifact metadata currently uses `schemas/artifact_metadata/v0_1/artifact-metadata.schema.json`.
- The minimum required fields are `artifact_id`, `title`, `status`, `owner`, `created`, `last_updated`, and `source_of_truth`.
- Historical markdown backfills may use the normalization date when original authorship dates are not yet reconstructed.

## Migration rule

When a future schema version lands:

1. Preserve existing `artifact_id` values.
2. Add new fields as additive defaults before making them required.
3. Regenerate metadata coverage and provenance drift reports in the same commit.
4. Record any non-additive changes in a versioned migration note before validator enforcement changes.

## Compatibility expectation

- v0.1 remains the active compatibility floor until a newer schema is published and linked from the roadmap, quickstart, and quality-gate scripts.
