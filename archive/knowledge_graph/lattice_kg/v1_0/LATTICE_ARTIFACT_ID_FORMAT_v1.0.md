---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: KNOWLEDGE_GRAPH-KG-20260603-lattice-artifact-id-format-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/LATTICE_ARTIFACT_ID_FORMAT_v1.0.md
domain: knowledge_graph
lane: contracts
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# Lattice Artifact ID Format v1.0

Format: `{DOMAIN}-{LANE}-{YYYYMMDD}-{SLUG}`

## Examples
- `KNOWLEDGE_GRAPH-KG-20260603-lattice-ontology-v1-0`
- `DOCS-DOCS-20260603-public-release-readiness-checklist`
- `TOOLS-TOOLING-20260603-build-lattice-global-index-v2`

## Uniqueness rules
- Domain and lane are uppercase and machine-derivable.
- Date is the artifact birth date, not the latest modified date.
- Slug is lowercase kebab-case.
- Collisions are resolved by extending the slug with a stable suffix derived from the path.

## Regex
`^[A-Z0-9]+-[A-Z0-9_]+-[0-9]{8}-[a-z0-9-]+$`
