---
artifact_id: DOC-ARTIFACT-TYPE-NORMALIZATION-GUIDE-2026-05-29
title: Artifact Type Normalization Guide
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---

# Artifact Type Normalization Guide

> Wave 3 · Task 29 · 2026-05-29

This guide defines the canonical `type` field values for the artifact corpus and how
to assign them during metadata normalization. The `type` field is planned for the v0.2
schema (see `docs/SCHEMA_VERSION_MIGRATION_NOTES_v0_1.md`).

---

## Type taxonomy

| `type` value | Applies to | Example paths |
|---|---|---|
| `spec` | Technical specs, protocol definitions, interface designs | `archive/spec/**`, `archive/boot/seats/**` |
| `dream-journal` | REM/dream simulation artifacts, play output | `archive/boot/gptbrain/dreams/**`, `TIDELOCKBrain/*DREAM*` |
| `work-log` | Session logs, receipts, TIDELOCKBrain work logs | `TIDELOCKBrain/*WORK_LOG*`, `*_RECEIPT_*` |
| `governance` | Decision records, policy, ratification, ADRs | `docs/governance/**`, `docs/decisions/**` |
| `report` | Generated coverage, quality, status, drift reports | `docs/*REPORT*`, `projects/status-reports/**` |
| `schema` | Schema definitions (JSON, YAML) | `schemas/**` |
| `test` | Test suites, validation, adversarial test fixtures | `tests/**`, `reference_impl/**/test_*` |
| `readme` | Index, navigation, orientation documents | `**/README.md`, `docs/START_HERE.md` |
| `evidence` | AI systems evidence, claims, eval receipts | `docs/AI_SYSTEMS_EVIDENCE_INDEX.md`, evidence packs |
| `archive` | Historical artifacts, legacy content | `archive/chatlogs/**`, `archive/assessments/**` |
| `project` | Plans, taskboards, execution queues, campaigns | `projects/**` |
| `charter` | Mission, values, constitutional documents | `docs/NORTH_STAR_MISSION.md`, `docs/ATLAS_LATTICE_PUBLIC_CHARTER_500IP.md` |
| `template` | Reusable workflow/document templates | `archive/boot/gptbrain/templates/**`, `WAKE_REPORT_TEMPLATE.md` |
| `boot-packet` | Agent boot/rehydration packets | `archive/boot/**/*BOOT*`, `*REHYDRATION*` |
| `assessment` | Analysis, evaluation, or review documents | `archive/assessments/**`, `council-reviews/**` |

---

## Assignment rules

1. **One type per artifact.** Choose the most specific type that fits.
2. **`dream-journal`** takes precedence over `archive` for REM artifacts.
3. **`work-log`** takes precedence for TIDELOCKBrain session logs, even if they contain governance notes.
4. **`report`** applies to any machine-generated coverage or scoring document.
5. **`readme`** applies to any `README.md` or top-level navigation index.
6. **`governance`** applies to any document under `docs/governance/` or `docs/decisions/`.

---

## Normalization pass status

Wave 3 scope: type assignment is **planned for v0.2** (additive-optional).
No existing frontmatter has been modified to add `type` yet — this will be done in a
dedicated future batch pass using `scripts/backfill_frontmatter.py --add-type`.

### Sample assignments (top-50 surface)

| Path | Assigned type |
|---|---|
| `README.md` | `readme` |
| `docs/NORTH_STAR_MISSION.md` | `charter` |
| `docs/GOVERNANCE_OPERATIONS_HANDBOOK.md` | `governance` |
| `docs/AI_SYSTEMS_EVIDENCE_INDEX.md` | `evidence` |
| `docs/METADATA_COVERAGE_REPORT_2026-05-29.md` | `report` |
| `archive/spec/gptdream/README.md` | `spec` |
| `archive/boot/gptbrain/WAKE_REPORT_TEMPLATE.md` | `template` |
| `archive/boot/gptbrain/dreams/GPT_REM_COMPRESSED_8H_IN_2S_2026-05-09.md` | `dream-journal` |
| `archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_GPTDREAM_ATLAS_ORCS_2026-05-26.md` | `work-log` |
| `projects/aetherforge-next144-taskboard-2026-05-28.md` | `project` |
| `tests/test_schema_parsing.py` | `test` |
| `docs/decisions/README.md` | `governance` |

---

## Integration with search and discovery

Once `type` is backfilled:
- Filter in `LATTICE_GLOBAL_INDEX.md` by type column
- Enable type-based search facet (Wave 9, Task 104)
- Use type as a dimension in the lineage quality score (v0.2 extension)

---

*Maintained by TIDELOCKBrain — update when v0.2 schema is published.*
