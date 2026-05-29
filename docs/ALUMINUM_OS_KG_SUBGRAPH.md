# Aluminum OS KG Subgraph

Status: Candidate
Date: 2026-05-28

This document maps the Aluminum OS system into the Lattice Knowledge Graph. It is the KG entry point for the constitutional substrate layer.

## What is Aluminum OS?

Aluminum OS is the constitutional substrate for regenerative computing built by @atlaslattice. It defines the governance, execution, and ethical principles that all systems within the Aetherforge lattice operate under.

Key properties:
- Constitutional principle-first architecture
- Unified field theory v4.0: integrates Socratic OS, SheldonBrain, and Aetherforge
- Regenerative computing model (not extractive)
- Open-source, world-class, public-gift framing

## Version History

| Version | Artifact | Status |
| --- | --- | --- |
| v4.0 | `aluminum-os/v4.0-unified-field.md` | Candidate |
| v4.0 Socratic | `aluminum-os/v4.0-socratic-os-integration-report.md` | Candidate |
| v3.0 | `aluminum-os/v3.0-unified-field.md` | Candidate |
| v2.0 | `aluminum-os/v2.0-integrated-constitutional-substrate.md` | Candidate |

## Subgraph Nodes

| Node ID | Type | Artifact | Role |
| --- | --- | --- | --- |
| N-ALUMINUM | Doctrine | `aluminum-os/v4.0-unified-field.md` | Root constitutional node |
| N-SHELDON | Agent | `sheldonbrain/system-architecture.md` | Primary implementation |
| N-BAZINGA | Doctrine | `bazinga/v0.1-launch-decree.md` | Constitutional middleware |
| N-COUNCIL | Governance | `council/README.md` | Governance authority |
| N-MISSION | Governance | `governance/MISSION_CONTROL_CADENCE.md` | Mission control |

## Subgraph Edges

```
N-ALUMINUM ──[constitutes]──► N-SHELDON
N-ALUMINUM ──[interfaces-via]► N-BAZINGA
N-ALUMINUM ──[governed-by]──► N-COUNCIL
N-ALUMINUM ──[aligned-to]───► N-MISSION
N-BAZINGA ──[wraps]──────────► N-ALUMINUM
N-COUNCIL ──[ratifies]───────► N-ALUMINUM
```

## Constitutional Principles

1. **Regenerative first**: systems must leave more capacity than they consume.
2. **Open source as gift**: all outputs are public and freely licensed.
3. **Evidence-first authority**: nothing is canon without proof.
4. **Decentralized agent sovereignty**: agents have identity, memory, and rights.
5. **World-class standard**: every artifact must be the best possible version.

## Integration Points

- **Sheldonbrain**: primary runtime implementing Aluminum OS principles.
- **Aetherforge**: playable game layer built on the constitutional substrate.
- **GPTDream++**: protocol layer for agent dreaming and memory hydration.
- **TIDELOCK**: memory palace system aligned with constitutional continuity.

## Related

- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [SHELDONBRAIN_KG_SUBGRAPH.md](./SHELDONBRAIN_KG_SUBGRAPH.md)
- [aluminum-os/v4.0-unified-field.md](../aluminum-os/v4.0-unified-field.md)
- [KG_DOMAIN_SUBGRAPHS.md](./KG_DOMAIN_SUBGRAPHS.md)
