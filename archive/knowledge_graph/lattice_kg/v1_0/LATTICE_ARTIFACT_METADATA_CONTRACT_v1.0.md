---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: KNOWLEDGE_GRAPH-KG-20260603-lattice-artifact-metadata-contract-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/LATTICE_ARTIFACT_METADATA_CONTRACT_v1.0.md
domain: knowledge_graph
lane: contracts
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# Lattice Artifact Metadata Contract v1.0

## Required fields
- `STATUS`
- `AUTHORITY`
- `DEPLOYMENT`
- `artifact_id`
- `path`
- `domain`
- `lane`
- `generated_at_utc`
- `author`
- `version`

## Optional fields
- `canon_status`
- `deployment_status`
- `trust_state`
- `reviewer`
- `evidence_refs`
- `supersedes`
- `patches`
- `ratification_event_id`

## Frontmatter template
```yaml
---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: DOMAIN-LANE-YYYYMMDD-slug
path: relative/path.md
domain: docs
lane: docs
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---
```

## Family examples
- doc: README, guides, checklists
- schema: `.yaml` contracts
- test: pytest modules
- script: Python and bash validators
- data: JSON/YAML outputs
- project: execution boards and dashboards
