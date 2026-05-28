# ORCS Route Class Taxonomy v0.1

```text
STATUS: SPEC CANDIDATE — NOT CANON
VERSION: v0.1
DATE: 2026-05-28
DOMAIN: atlas_orcs / knowledge_graph
AUTHORITY: none — candidate taxonomy only
CANON: NO
PURPOSE: enumerate and define every valid ORCS route_class value
```

## Overview

ORCS (Ordered Route Classification System) is the routing substrate of the
Atlas Lattice knowledge graph. Every edge in the lattice JSONL files carries a
`route_class` field drawn from this taxonomy.

This document defines all v0.1 route classes, their domain affinity, trust requirements,
and valid source→target pairings.

---

## Route class registry

### Governance domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `COUNCIL_BOOT` | Root governance initialization routes | `archive/boot/COUNCIL_BRAIN_INDEX.md` | `archive/boot/gptbrain/` |
| `RATIFICATION_EVENT` | Confirmed ratification edge | `schemas/governance/ratification_event_v0_1.yaml` | Any artifact receiving canon status |
| `CANON_PROMOTION` | Human-root promotes candidate → canon | Governance decision doc | Target artifact |
| `ADJUDICATION_RECORD` | Council adjudication event | `docs/governance/` | `archive/knowledge_graph/GRAPH_INDEX.md` |
| `CONFLICT_RESOLUTION` | Conflict playbook activation record | `docs/governance/CONFLICT_PLAYBOOK.md` | Disputed artifact |

### GPTBrain domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `KRAKOA_GATES` | Krakoa gate index routes | `archive/boot/gptbrain/KRAKOA_GATE_INDEX.seed.jsonl` | `archive/knowledge_graph/GRAPH_INDEX.md` |
| `DREAM_MEMORY` | Agent dream memory palace route | `archive/boot/gptbrain/agents/*/DREAM_MEMORY_PALACE.md` | `archive/knowledge_graph/` |
| `AGENT_DNA` | Agent DNA artifact route | `archive/boot/gptbrain/*/AGENT_DNA.yaml` | `archive/boot/gptbrain/GPTBRAIN_INDEX_OF_INDEXES_2026-05-26.md` |
| `WORK_LOG` | Agent session work log | `archive/boot/gptbrain/agents/TIDELOCKBrain/` | `archive/knowledge_graph/GRAPH_INDEX.md` |
| `REM_ARTIFACT` | Dream/REM artifact | `archive/boot/gptbrain/agents/TIDELOCKBrain/` | `archive/knowledge_graph/` |

### AtlasBrain / Evidence domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `EVIDENCE_CHAIN` | AtlasBrain evidence lane route | `archive/boot/atlasbrain/ATLASBRAIN_INDEX_2026-05-26.md` | `archive/knowledge_graph/GRAPH_INDEX.md` |
| `EVIDENCE_PACKET` | Individual evidence packet edge | `archive/boot/atlasbrain/` | Any claim artifact |
| `BENCHMARK_ENTRY` | Benchmark performance log route | `archive/boot/atlasbrain/` | Evidence lane index |
| `CAPABILITY_DEMO` | Capability demonstration log | `archive/boot/atlasbrain/` | Evidence lane index |

### Schemas domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `ATLAS_ORCS_SCHEMA` | Atlas ORCS YAML schema route | `schemas/atlas_orcs/v0_1/` | `reference_impl/atlas_orcs/` |
| `O_AI_SCHEMA` | O_AI schema route | `schemas/o_ai/v0_1/` | `reference_impl/o_ai/` |
| `NATIVE_THREAD_SCHEMA` | Native thread schema route | `schemas/native_thread/v0_1/` | `reference_impl/native_thread/` |
| `GOVERNANCE_SCHEMA` | Governance schema route | `schemas/governance/` | `docs/governance/` |

### Tests / Validation domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `GPTDREAM_VALIDATION` | GPTDream++ validation test suite | `tests/gptdream/` | `reference_impl/` |
| `ADVERSARIAL_VALIDATION` | Adversarial boss-fight test route | `tests/adversarial/` | `reference_impl/atlas_orcs/` |
| `QUALITY_GATE` | CI quality gate validation | `.github/workflows/lattice-kg-quality-gates.yml` | Any artifact under test |

### Aetherforge / Projects domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `AETHERFORGE_ARCHIVE_BOWL` | Aetherforge world surface route | `projects/aetherforge-game-world/` | `archive/knowledge_graph/METATRON_CUBE_TOPOLOGY.md` |
| `QUEST_ROUTE` | Quest execution routing edge | `projects/aetherforge-game-world/AETHERFORGE_TOP100_QUEST_LEDGER_v0.1.md` | Execution artifact |
| `LOOT_DROP` | Loot registry route | `archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_F12_LOOT_REGISTRY_2026-05-27.md` | `archive/knowledge_graph/` |

### IP Archive domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `IP_TRANCHE` | Published IP archive tranche | `archive/ip/` | `archive/knowledge_graph/GRAPH_INDEX.md` |
| `IP_INGESTION` | IP archive ingestion record | `archive/ip/INGESTION_PROTOCOL_v0_1.md` | `archive/ip/` |

### Workflow / CI domain

| route_class | Description | Typical source | Typical target |
|---|---|---|---|
| `CI_HYGIENE` | CI hygiene workflow route | `.github/workflows/` | `archive/knowledge_graph/GRAPH_INDEX.md` |
| `KRAKOA_SECRET_SCAN` | Secret scan result route | `KRAKOA_SECRET_SCAN_REPORT.md` | Governance artifact |

---

## Trust state requirements per route class

| Trust state | Valid route_class examples |
|---|---|
| `canon` | `RATIFICATION_EVENT`, `CANON_PROMOTION`, `ADJUDICATION_RECORD` |
| `candidate` | All route classes during development |
| `quarantine` | Routes from `quarantine/` paths only |
| `deprecated` | Any superseded route version |

---

## Valid route_class field values (exhaustive v0.1 list)

```text
COUNCIL_BOOT
RATIFICATION_EVENT
CANON_PROMOTION
ADJUDICATION_RECORD
CONFLICT_RESOLUTION
KRAKOA_GATES
DREAM_MEMORY
AGENT_DNA
WORK_LOG
REM_ARTIFACT
EVIDENCE_CHAIN
EVIDENCE_PACKET
BENCHMARK_ENTRY
CAPABILITY_DEMO
ATLAS_ORCS_SCHEMA
O_AI_SCHEMA
NATIVE_THREAD_SCHEMA
GOVERNANCE_SCHEMA
GPTDREAM_VALIDATION
ADVERSARIAL_VALIDATION
QUALITY_GATE
AETHERFORGE_ARCHIVE_BOWL
QUEST_ROUTE
LOOT_DROP
IP_TRANCHE
IP_INGESTION
CI_HYGIENE
KRAKOA_SECRET_SCAN
```

---

## Versioning

This is v0.1 of the taxonomy. Route classes may be added in later versions.
Removal requires a deprecation notice and a `CONFLICT_RESOLUTION` event.

## See also

- `ORCS_SPEC_v0_1.md` — full ORCS protocol spec
- `archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl` — live route seed ledger
- `schemas/atlas_orcs/v0_1/` — schema contracts
