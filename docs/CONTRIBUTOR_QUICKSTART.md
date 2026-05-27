---
artifact_id: DOC-CONTRIB-QUICKSTART-2026-05-27
title: Contributor Quickstart
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---
# Contributor Quickstart

1. Read `/tmp/workspace/atlaslattice/manus-artifacts/docs/START_HERE.md`.
2. Read `/tmp/workspace/atlaslattice/manus-artifacts/.github/CONTRIBUTING.md`.
3. Pick a task from `/tmp/workspace/atlaslattice/manus-artifacts/projects/aetherforge-top50-taskboard-2026-05-26.md`.
4. Mark new outputs as **CANDIDATE** unless ratified.
5. Run local validation commands before opening a PR.
6. Use clear provenance and citations in every artifact edit.

## Wave 1 validation commands

```bash
cd /tmp/workspace/atlaslattice/manus-artifacts
python scripts/build_lattice_global_index.py
python scripts/build_metadata_reports.py
python scripts/validate_artifact_metadata.py
python scripts/validate_lattice_quality_gates.py
python -m pytest -q tests/test_lattice_kg_hypercube_program.py tests/test_metadata_wave3_reports.py
```
