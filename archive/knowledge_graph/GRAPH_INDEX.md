# Metatron Awakening — Repo Graph Index

```text
STATUS: GRAPH INDEX — NOT CANON
DATE: 2026-05-28
CANON STATUS: candidate
AUTHORITY: generated navigation and linkage index
PURPOSE: provide a repo-wide node map for governance, specs, code, tests, workflows, and project lanes
SOURCE: scripts/build_lattice_global_index.py
```

## Graph summary

- Nodes: **15**
- Edges: **12**
- ORCS routes: **10**

## Node kinds

- `code_dir` — 4
- `document` — 5
- `project_doc` — 1
- `repository` — 1
- `seed_jsonl` — 2
- `test_dir` — 1
- `test_file` — 1

## Edge relations

- `contains` — 4
- `frames` — 1
- `indexes` — 1
- `maps` — 1
- `routes_to` — 3
- `stress_tests` — 1
- `validates` — 1

## Seed nodes

- `code:atlas-orcs` · **Atlas ORCS impl** (code_dir) → `reference_impl/atlas_orcs`
- `code:native-thread` · **Native thread impl** (code_dir) → `reference_impl/native_thread`
- `code:o-ai` · **O_AI impl** (code_dir) → `reference_impl/o_ai`
- `code:reference-impl` · **Reference Implementation** (code_dir) → `reference_impl`
- `doc:atlasbrain-index` · **AtlasBrain Index** (document) → `archive/boot/atlasbrain/ATLASBRAIN_INDEX_2026-05-26.md`
- `doc:council-index` · **Council Brain Index** (document) → `archive/boot/COUNCIL_BRAIN_INDEX.md`
- `doc:gptbrain-index` · **GPTBrain Index of Indexes** (document) → `archive/boot/gptbrain/GPTBRAIN_INDEX_OF_INDEXES_2026-05-26.md`
- `doc:metatron-topology` · **Metatron Cube Topology** (document) → `archive/knowledge_graph/METATRON_CUBE_TOPOLOGY.md`
- `doc:readme` · **Repository README** (document) → `README.md`
- `project:aetherforge-world` · **Aetherforge Game World** (project_doc) → `projects/aetherforge-game-world/README.md`
- `repo:root` · **manus-artifacts** (repository) → `/tmp/workspace/atlaslattice/manus-artifacts`
- `seed:gates` · **Krakoa Gate Index** (seed_jsonl) → `archive/boot/gptbrain/KRAKOA_GATE_INDEX.seed.jsonl`
- `seed:orcs-routes` · **Knowledge Graph ORCS Route Index** (seed_jsonl) → `archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl`
- `test:adversarial` · **Adversarial T13-T20 tests** (test_file) → `tests/adversarial/test_t13_t20_failure_modes.py`
- `test:gptdream` · **GPTDream tests** (test_dir) → `tests/gptdream`

## ORCS route domains

### atlasbrain

- `KG-ORCS-2026-0528-0003` · `EVIDENCE_CHAIN` · `archive/boot/atlasbrain/ATLASBRAIN_INDEX_2026-05-26.md` → `archive/knowledge_graph/GRAPH_INDEX.md` · seat `S1`

### governance

- `KG-ORCS-2026-0528-0001` · `COUNCIL_BOOT` · `archive/boot/COUNCIL_BRAIN_INDEX.md` → `archive/boot/gptbrain/GPTBRAIN_INDEX_OF_INDEXES_2026-05-26.md` · seat `S1`

### gptbrain

- `KG-ORCS-2026-0528-0002` · `KRAKOA_GATES` · `archive/boot/gptbrain/KRAKOA_GATE_INDEX.seed.jsonl` → `archive/knowledge_graph/GRAPH_INDEX.md` · seat `S7`

### projects

- `KG-ORCS-2026-0528-0009` · `AETHERFORGE_ARCHIVE_BOWL` · `projects/aetherforge-game-world/README.md` → `archive/knowledge_graph/METATRON_CUBE_TOPOLOGY.md` · seat `S6`

### schemas

- `KG-ORCS-2026-0528-0004` · `ATLAS_ORCS_SCHEMA` · `schemas/atlas_orcs/v0_1` → `reference_impl/atlas_orcs` · seat `S7`
- `KG-ORCS-2026-0528-0005` · `O_AI_SCHEMA` · `schemas/o_ai/v0_1` → `reference_impl/o_ai` · seat `S7`
- `KG-ORCS-2026-0528-0006` · `NATIVE_THREAD_SCHEMA` · `schemas/native_thread/v0_1` → `reference_impl/native_thread` · seat `S7`

### tests

- `KG-ORCS-2026-0528-0007` · `GPTDREAM_VALIDATION` · `tests/gptdream` → `reference_impl` · seat `S3`
- `KG-ORCS-2026-0528-0008` · `ADVERSARIAL_VALIDATION` · `tests/adversarial/test_t13_t20_failure_modes.py` → `reference_impl/atlas_orcs` · seat `S3`

### workflows

- `KG-ORCS-2026-0528-0010` · `CI_HYGIENE` · `.github/workflows/repo-hygiene-checks.yml` → `archive/knowledge_graph/GRAPH_INDEX.md` · seat `S7`

## Integrity notes

- Graph seed paths should resolve within the repository root.
- Edge records should only reference existing `node_id` values.
- ORCS routes should target concrete repo surfaces and carry a seat assignment.
