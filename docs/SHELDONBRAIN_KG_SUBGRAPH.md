# Sheldonbrain KG Subgraph

Status: Candidate
Date: 2026-05-28

This document maps the Sheldonbrain system into the Lattice Knowledge Graph. It is the KG entry point for the Sheldonbrain multi-AI knowledge ecosystem.

## What is Sheldonbrain?

Sheldonbrain is a multi-AI knowledge ecosystem that autonomously discovers, validates, and organizes information across 144 knowledge spheres. Built by @atlaslattice, it is the substrate for the world-class knowledge graph goal.

Key capabilities:
- 7,964+ knowledge vault entries across 144 domains
- 6-model council deliberation pipeline
- Autonomous research organism (arXiv / X / Drive → Hunter → Council → Vault)
- Cross-referenced taxonomy with physics to philosophy to nutrition

## Subgraph Nodes

| Node ID | Type | Artifact | Role |
| --- | --- | --- | --- |
| N-SHELDON | Agent | `sheldonbrain/system-architecture.md` | Root system node |
| N-ALUMINUM | Doctrine | `aluminum-os/v4.0-unified-field.md` | Constitutional substrate |
| N-KG-SUBGRAPHS | Program | `docs/KG_DOMAIN_SUBGRAPHS.md` | Domain subgraph registry |
| N-TIDELOCK | Agent | `archive/boot/gptbrain/TIDELOCKBrain/README.md` | Memory palace / log layer |
| N-GPTBRAIN | Agent | `archive/boot/gptbrain/GPTBRAIN_MANIFEST_2026-05-09.md` | GPTBrain agent lineage |

## Subgraph Edges

```
N-SHELDON ──[implements]──► N-ALUMINUM
N-SHELDON ──[logs-to]──────► N-TIDELOCK
N-SHELDON ──[maps-to]──────► N-KG-SUBGRAPHS
N-SHELDON ──[sibling-of]───► N-GPTBRAIN
N-ALUMINUM ──[governs]─────► N-SHELDON
N-TIDELOCK ──[inherits]────► N-GPTBRAIN
```

## 144-Sphere Taxonomy Mapping

Sheldonbrain organizes knowledge across 144 spheres. These map to the Aetherforge 144-task campaign categories:

| Sphere Group | Lattice Domain | Key Node |
| --- | --- | --- |
| Physics → Cosmology | Research | N-RESEARCH |
| Governance → Policy | Governance | N-GOV-INDEX |
| AI → Agents | Agent | N-GPTBRAIN |
| Systems → Architecture | Doctrine | N-ALUMINUM |
| Health → Wellness | Archive | N-HEALTH |
| Creative → Game | Program | N-AETHER-GAME |

## Ingestion Plan

Phase 1 (Wave 4): Register core Sheldonbrain nodes in global KG index.
Phase 2 (Wave 5): Ingest 144-sphere taxonomy as KG node stubs.
Phase 3 (Wave 6): Auto-generate edges from Council deliberation records.
Phase 4 (Wave 7): Build Obsidian-compatible export for local navigation.

## Quality Gate

- All Sheldonbrain nodes must have `exists: true` in the global index.
- Each node must have at least 2 outbound links.
- Orphan rate target: 0%.

## Related

- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [KG_DOMAIN_SUBGRAPHS.md](./KG_DOMAIN_SUBGRAPHS.md)
- [sheldonbrain/system-architecture.md](../sheldonbrain/system-architecture.md)
- [CHILDREN_SWARM_LATTICE.md](./CHILDREN_SWARM_LATTICE.md)
