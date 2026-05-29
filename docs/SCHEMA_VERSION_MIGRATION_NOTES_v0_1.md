---
artifact_id: DOC-SCHEMA-VERSION-MIGRATION-NOTES-V0-1-2026-05-27
title: Schema Version Migration Notes v0.1
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-29
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

---

## Planned v0.2 additions (Wave 3 proposals)

The following fields are planned for v0.2. They will be **additive-optional** on introduction and become **required** only after a full backfill pass of the top-500 corpus.

| Field | Type | Description | Rationale |
|---|---|---|---|
| `type` | string enum | Artifact type classification (see below) | Enables search facets and filtering |
| `lineage_score` | integer 0–4 | Computed lineage quality score | Auto-populated by `scripts/score_lineage_quality.py` |
| `related_to` | list of artifact_ids | Explicit KG edge declarations | Graph integrity; replaces implicit linking |
| `upstream` | list of artifact_ids | Parent/source artifact references | Provenance chain tracing |
| `tags` | list of strings | Topical semantic keywords | Discovery and search |
| `version` | string | Semantic version of the artifact | Supports lineage diff and rollback |

### Proposed `type` enum values

| Value | Applies to |
|---|---|
| `spec` | Technical specifications, protocol definitions |
| `dream-journal` | REM/dream simulation artifacts |
| `work-log` | Session work logs and receipts |
| `governance` | Decision records, policy docs, ratification artifacts |
| `report` | Generated coverage, quality, or status reports |
| `schema` | Schema definition files |
| `test` | Test suites and validation artifacts |
| `readme` | Index and navigation documents |
| `evidence` | AI systems evidence and claims |
| `archive` | Historical artifacts, legacy content |
| `project` | Project plans, taskboards, execution queues |
| `charter` | Foundational mission or values documents |
| `template` | Reusable workflow templates |

### Migration execution steps for v0.2

1. Publish this note as evidence of planned change before any enforcement.
2. Add `type` to `REQUIRED_KEYS` in `scripts/metadata_inventory.py` once backfill script supports it.
3. Run `scripts/backfill_frontmatter.py` with `--add-type` flag (to be implemented).
4. Update `scripts/validate_artifact_metadata.py` to enforce new fields on top-50 paths first.
5. Regenerate all reports in the same PR.
6. Publish v0.2 schema JSON at `schemas/artifact_metadata/v0_2/`.

