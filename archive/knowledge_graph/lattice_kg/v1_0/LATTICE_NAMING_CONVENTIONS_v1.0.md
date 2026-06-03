---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: KNOWLEDGE_GRAPH-KG-20260603-lattice-naming-conventions-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/LATTICE_NAMING_CONVENTIONS_v1.0.md
domain: knowledge_graph
lane: contracts
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# Lattice Naming Conventions v1.0

- Docs: `SCREAMING_SNAKE_CASE.md`
- Scripts and data: `snake_case.py`, `snake_case.yaml`, `snake_case.json`
- Project boards: `kebab-case.md`
- `artifact_id`: `{DOMAIN}-{LANE}-{YYYYMMDD}-{SLUG}`
- `edge_id`: `EDGE-{RELATION}-{NNNNN}`
- Domains and lanes use lowercase repo names and uppercase identifiers when embedded in IDs.
- Directory structure should prefer `/archive`, `/docs`, `/scripts`, `/tests`, `/schemas`, `/projects`.
