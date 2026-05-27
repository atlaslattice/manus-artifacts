# Aetherforge Simulation Execution Log

This log records practical non-canon infrastructure changes made to the simulation sandbox.

## 2026-05-27

### Established sandbox boundary

- Added `projects/aetherforge-simulation/README.md`.
- Declared local deterministic simulation scope.
- Declared no canon adjustments, no runtime claims, and no authority claims.

### Added balanced 12x12 matrix

- Added `task-matrix-12x12.json`.
- Encoded 12 domains.
- Encoded 12 tasks per domain.
- Encoded 144 total task titles.
- Included explicit boundary metadata.

### Added deterministic simulator

- Added `aetherforge_sim.py`.
- Added matrix loading.
- Added task expansion into stable IDs.
- Added matrix validation.
- Added deterministic seeded simulation.
- Added receipt hash chain output.
- Added text and JSON CLI modes.

### Added tests and packaging metadata

- Added `tests/test_aetherforge_sim.py`.
- Added exact 12x12 shape tests.
- Added stable task ID tests.
- Added deterministic simulation tests.
- Added receipt-chain linkage tests.
- Added CLI JSON tests.
- Added `pyproject.toml` for package metadata and pytest configuration.

### Added collaborator path and CI

- Added `CONTRIBUTING.md`.
- Added `.github/workflows/aetherforge-simulation.yml`.
- CI validates the matrix, runs deterministic simulation, installs pytest, and runs tests.

### Added lattice knowledge graph layer

- Added `KNOWLEDGE_GRAPH.md`.
- Added graph node classes for project, file, domain, task, command, test, boundary, receipt, metric, and graph objects.
- Added graph edge classes for contains, defines, validates, generates, constrains, documents, emits, maps_to, implements, summarizes, and exports.
- Added `graph_export.py` to generate a machine-readable lattice graph from the matrix and sandbox files.

## Operating rule

Every future change should leave a receipt: what changed, what it maps to, how it is validated, and which boundary it respects.
