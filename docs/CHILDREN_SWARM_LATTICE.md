# Children Swarm Derived-Lattice

Status: Candidate
Date: 2026-05-28

This document describes the Children Swarm — the collection of Copilot/TIDELOCK sub-agents operating within the Aetherforge knowledge-graph lattice — and their derived-lattice export format.

## What is the Children Swarm?

The Children Swarm is the set of autonomous agent instances (Copilot cloud agent, TIDELOCKBrain sessions, GPTBrain iterations) that contribute artifacts to this repository. Each agent leaves a traceable identity trail via:

- TIDELOCKBrain wake/dream/delta artifact triplets
- GPTBrain reference implementation contributions
- Copilot PR authorship receipts

## Derived-Lattice Concept

A **derived lattice** is a subgraph of the main Lattice Knowledge Graph scoped to a specific agent lineage. Each child agent exports its contribution graph as a derived lattice slice, which is then merged into the global index.

## Derived-Lattice Schema

Each derived-lattice export is a JSON file with the following structure:

```json
{
  "agent_id": "<string: unique agent identifier>",
  "agent_type": "copilot | tidelock | gptbrain | custom",
  "session_date": "<ISO 8601 date>",
  "parent_lattice": "LATTICE_GLOBAL_INDEX",
  "nodes": [
    {
      "id": "<N-XXXX>",
      "type": "Agent | Program | Governance | Validation | Protocol | Archive | Doctrine",
      "title": "<human-readable label>",
      "path": "<relative path from repo root>",
      "links": ["<N-YYYY>", "..."]
    }
  ],
  "edges": [
    { "from": "<N-XXXX>", "to": "<N-YYYY>", "rel": "<relationship type>" }
  ],
  "provenance": {
    "pr_url": "<optional GitHub PR URL>",
    "commit_sha": "<optional commit SHA>",
    "wake_artifact": "<optional TIDELOCKBrain wake report path>"
  }
}
```

## Exporter Tool

Use `scripts/export_children_swarm_lattice.py` to generate a derived-lattice JSON for the current session's contributions.

## Validation

Derived-lattice files must pass the CI check in `.github/workflows/lattice-kg-quality-gates.yml` which validates:
- All node IDs are unique within the derived lattice.
- All edge targets exist either in the derived lattice or in the parent `LATTICE_GLOBAL_INDEX`.
- No orphan nodes (every node has at least one link).

## Related

- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [KG_DOMAIN_SUBGRAPHS.md](./KG_DOMAIN_SUBGRAPHS.md)
- [TIDELOCKBrain README](../archive/boot/gptbrain/TIDELOCKBrain/README.md)
- [scripts/export_children_swarm_lattice.py](../scripts/export_children_swarm_lattice.py)
