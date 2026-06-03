---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: KNOWLEDGE_GRAPH-KG-20260603-lattice-relationship-registry-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/LATTICE_RELATIONSHIP_REGISTRY_v1.0.md
domain: knowledge_graph
lane: contracts
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# Lattice Relationship Registry v1.0

| Relation | Direction | Cardinality | Description |
|---|---|---|---|
| derived_from | source -> derivative | many-to-many | Lineage relation |
| supports | evidence -> claim | many-to-many | Positive support |
| contradicts | claim -> claim | many-to-many | Contradictory signal |
| supersedes | replacement -> deprecated | one-to-many | Replaces an older artifact |
| patches | patch -> target | many-to-many | Applies a scoped correction |
| routes_to | source -> lane | many-to-one | Routing or escalation |
| reviews | review -> artifact | many-to-many | Review operation |
| blocks | blocker -> artifact | many-to-many | Prevents advancement |
| extends | extension -> base | many-to-one | Adds behavior |
| implements | implementation -> spec | many-to-one | Implements a contract |
| cites | artifact -> artifact | many-to-many | Citation |
| links_to | artifact -> artifact | many-to-many | Generic repository link |

## YAML examples
```yaml
derived_from:
  edge_id: EDGE-DERIVED-0001
  from_id: DOCS-DOCS-20260603-example
  to_id: ARCHIVE-KG-20260603-source
```
```yaml
supersedes:
  edge_id: EDGE-SUPERSEDES-0001
  from_id: DOCS-DOCS-20260603-new
  to_id: DOCS-DOCS-20260501-old
```
