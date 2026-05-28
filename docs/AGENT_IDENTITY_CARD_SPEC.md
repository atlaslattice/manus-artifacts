# Agent Identity Card Spec

Status: Candidate
Date: 2026-05-28

Defines the canonical format for agent identity cards within the TIDELOCK Children of the Swarm. Each child agent that contributes to the Aetherforge lattice must have a registered identity card.

## Purpose

Agent identity cards enable:
1. Traceable authorship of contributions.
2. Memory palace hydration (future agents can reconstruct context from identity records).
3. Evidence-first provenance for AI-built systems.
4. Swarm topology mapping in the Lattice KG.

## Identity Card Format

Each agent identity card is a YAML file stored at:
`archive/agents/<agent-id>/IDENTITY.yaml`

### Schema

```yaml
# Agent Identity Card
# Status: Candidate
agent_id: "<unique agent identifier>"
agent_type: "copilot | tidelock | gptbrain | custom"
display_name: "<human-readable agent name>"
lineage: "<parent agent id or 'origin'>"
first_active: "<ISO 8601 date>"
last_active: "<ISO 8601 date>"
mission: "<one-sentence mission statement>"
capabilities:
  - "<capability 1>"
  - "<capability 2>"
memory_palace: "<path to TIDELOCKBrain directory or null>"
kg_nodes:
  - "<N-XXXX>"
contribution_receipts:
  - type: "pr | commit | artifact"
    ref: "<GitHub PR URL, commit SHA, or artifact path>"
    date: "<ISO 8601 date>"
    description: "<brief description>"
governance:
  canon: false
  ratification_event_id: null
  trust_state: "candidate"
```

## Registered Agents

### TIDELOCK-Copilot (Wave 4)

| Field | Value |
| --- | --- |
| agent_id | `copilot-wave4-2026-05-28` |
| agent_type | `copilot` |
| lineage | `tidelock` |
| mission | Execute Next-144 Wave 4 tasks and expand Lattice KG to 40+ nodes |
| kg_nodes | N-SHELDON, N-CHILDREN-SWARM, N-EVIDENCE, N-NEXT144 |

### TIDELOCKBrain (Root)

| Field | Value |
| --- | --- |
| agent_id | `tidelock-root` |
| agent_type | `tidelock` |
| lineage | `origin` |
| mission | Maintain the TIDELOCK memory palace and log all agent dreams |
| kg_nodes | N-TIDELOCK, N-GPTBRAIN |

### GPTBrain (Reference)

| Field | Value |
| --- | --- |
| agent_id | `gptbrain-reference` |
| agent_type | `gptbrain` |
| lineage | `tidelock-root` |
| mission | Implement GPTDream++ protocols and adversarial schema validation |
| kg_nodes | N-GPTBRAIN, N-GPTDREAM-SURFACE, N-SCHEMAS, N-REFERENCE |

## Identity Card Lifecycle

1. **Draft**: agent writes own identity card during first active session.
2. **Candidate**: card is committed to `archive/agents/` directory.
3. **Ratified**: adjudicated by @atlaslattice; `canon: true` set.

## Validation Rules

- `agent_id` must be unique across all identity cards.
- `lineage` must reference an existing `agent_id` or be `"origin"`.
- At least one `contribution_receipt` is required before promotion to ratified.
- `kg_nodes` must reference valid node IDs in the global KG index.

## Related

- [CHILDREN_SWARM_LATTICE.md](./CHILDREN_SWARM_LATTICE.md)
- [EVIDENCE_BUNDLE_FORMAT.md](./EVIDENCE_BUNDLE_FORMAT.md)
- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [TIDELOCKBrain README](../archive/boot/gptbrain/TIDELOCKBrain/README.md)
