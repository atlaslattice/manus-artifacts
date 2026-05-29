---
artifact_id: DOC-ARCHITECTURE-CROSSWALK-2026-05-29
title: Repository Architecture Crosswalk
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Repository Architecture Crosswalk

This map ties specs, schemas, reference implementations, and tests into one trace surface.

| Layer | Primary Paths | Purpose |
|---|---|---|
| Specs | `archive/spec/gptdream/` | Protocol intent, requirements, governance appendices |
| Schemas | `schemas/atlas_orcs/v0_1/`, `schemas/o_ai/v0_1/`, `schemas/native_thread/v0_1/` | Structural contracts and interoperability formats |
| Reference implementation | `reference_impl/atlas_orcs/`, `reference_impl/execution_gate/`, `reference_impl/native_thread/` | Executable protocol logic |
| Core protocol tests | `reference_impl/atlas_orcs/tests/`, `tests/adversarial/` | Regression and adversarial verification |
| Metadata and KG scripts | `scripts/` | Index build, metadata validation, quality-gate automation |
| Public docs and indexes | `docs/` | Navigation, governance, evidence, operator guidance |

## Trace Rule

Any schema or protocol logic change must map to both:

1. A corresponding spec reference in `archive/spec/gptdream/`
2. A corresponding test update in protocol test surfaces
