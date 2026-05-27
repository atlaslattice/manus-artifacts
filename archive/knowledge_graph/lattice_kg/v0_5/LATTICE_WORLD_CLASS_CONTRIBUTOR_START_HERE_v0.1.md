# Lattice World-Class Contributor Start Here v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none

## 1) Use one roadmap

Execution sequencing starts at:

- `projects/aetherforge-world-class-authoritative-roadmap-v0.1.md`

Historical boards are lineage only and must not override authoritative sequencing.

## 2) Ship one bounded change

Declare bounded scope before changes.

## 3) Validate before and after

Required lattice commands:

- `python scripts/build_lattice_global_index.py --repo-root .`
- `python scripts/validate_lattice_quality_gates.py --repo-root . --index archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json --max-age-days 7`
- `python -m pytest -q tests/test_lattice_kg_hypercube_program.py tests/test_world_class_execution_surfaces.py`

## 4) Preserve candidate boundary

- No self-promotion to canon.
- No self-promotion to deployable.
- Governance requires explicit adjudication/ratification.

## 5) Enforce artifact contract

Candidate artifact records must include:

- `artifact_id`
- `claim_class`
- `lifecycle_state`
- `contradiction_links`
- `supersedes_links`
- `tests_required`
- `tests_run`
- `blockers`
- `next_safest_action`

## 6) Publish quest-loop receipt fields

Every increment must state:

1. Bounded scope
2. Validation result
3. Blockers
4. Next safest action

## 7) Use navigation support docs

- `LATTICE_KG_GLOSSARY_v0.1.md`
- `LATTICE_KG_QUERY_COOKBOOK_v0.1.md`
- `LATTICE_STATE_OF_GRAPH_WEEKLY_REPORT_2026-05-27.md`
