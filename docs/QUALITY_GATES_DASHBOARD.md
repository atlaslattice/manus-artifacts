---
artifact_id: DOC-QUALITY-GATES-DASHBOARD-2026-05-29
title: Quality Gates Dashboard
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Quality Gates Dashboard

## Workflow Status

- [Repo Hygiene](https://github.com/atlaslattice/manus-artifacts/actions/workflows/repo-hygiene-checks.yml)
- [Docs Links](https://github.com/atlaslattice/manus-artifacts/actions/workflows/docs-link-checks.yml)
- [Lattice KG Quality Gates](https://github.com/atlaslattice/manus-artifacts/actions/workflows/lattice-kg-quality-gates.yml)
- [GPTBrain Reference Checks](https://github.com/atlaslattice/manus-artifacts/actions/workflows/gptbrain-reference-checks.yml)
- [Secret Scan](https://github.com/atlaslattice/manus-artifacts/actions/workflows/secret-scan.yml)

## Local Gate Commands

| Gate | Command |
|---|---|
| Build lattice index | `python3 scripts/build_lattice_global_index.py` |
| Validate artifact metadata | `python3 scripts/validate_artifact_metadata.py` |
| Validate lattice quality gates | `python3 scripts/validate_lattice_quality_gates.py` |
| Lattice protocol tests | `python3 -m pytest -q tests/test_lattice_kg_hypercube_program.py` |
| Adversarial tests | `python3 -m pytest -q tests/adversarial` |

## Policy

A task is only `Done` when all required gates for its touched surfaces pass.
