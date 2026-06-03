---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: KNOWLEDGE_GRAPH-KG-20260603-lattice-contract-policies-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/LATTICE_CONTRACT_POLICIES_v1.0.md
domain: knowledge_graph
lane: contracts
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# Lattice Contract Policies v1.0

## Changelog policy
- Semantic versioning applies to ontology, schema, and lifecycle contracts.
- Patch: examples or clarifications only.
- Minor: additive fields or relations.
- Major: incompatible state-machine or schema changes.
- Every major bump must include migration guidance and dual-read compatibility notes.

## Deprecation policy
- Minimum notice period: one weekly cycle for candidate assets, four weeks for ratified assets.
- Sunset schedule must state cutover date and replacement artifact.
- Backward compatibility remains required during the notice period.
- Deprecated contracts must point to `supersedes` or `patches` artifacts.
