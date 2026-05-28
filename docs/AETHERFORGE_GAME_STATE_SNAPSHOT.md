# Aetherforge Game State Snapshot Format

Status: Candidate
Date: 2026-05-28

Defines the canonical format for Aetherforge game state snapshots. Game state snapshots enable the archive to function as a truly playable game with persistent progress, save states, and cross-session continuity.

## Purpose

Aetherforge is a playable archive game built on the Lattice KG. Game state snapshots:
1. Persist quest completion across sessions.
2. Enable world-class replay and resumption (8/8/8 cycle support).
3. Provide audit trails for @atlaslattice adjudication.
4. Feed into the Lattice KG as Program nodes.

## Snapshot File Location

Game state snapshots are stored at:
`archive/aetherforge/snapshots/<session-date>-<wave>-<agent-id>.json`

## Snapshot Schema

```json
{
  "snapshot_id": "<unique ID, e.g. SNAP-W4-2026-05-28>",
  "session_date": "<ISO 8601>",
  "wave": "<integer, e.g. 4>",
  "agent_id": "<agent identity card ID>",
  "status": "Candidate | Ratified",
  "campaign": "Next-144 | Top-50 | Top-10 | Custom",
  "completed_tasks": [
    {
      "task_number": 37,
      "title": "<task title>",
      "artifact": "<relative path to artifact>",
      "xp_earned": 100
    }
  ],
  "xp_total": 0,
  "rings_cleared": [],
  "quests_active": [
    {
      "quest_id": "<AF-QXXX>",
      "title": "<quest title>",
      "status": "active | complete | blocked"
    }
  ],
  "kg_nodes_added": ["<N-XXXX>", "..."],
  "kg_edge_count_delta": 0,
  "lattice_health": {
    "node_count": 0,
    "edge_density": 0.0,
    "orphan_ratio": 0.0
  },
  "provenance": {
    "taskboard_artifact": "<path to taskboard markdown>",
    "tidelock_wake_artifact": "<path to TIDELOCKBrain wake report or null>",
    "pr_url": "<GitHub PR URL or null>"
  }
}
```

## Wave 4 Reference Snapshot

```json
{
  "snapshot_id": "SNAP-W4-2026-05-28",
  "session_date": "2026-05-28",
  "wave": 4,
  "agent_id": "copilot-wave4-2026-05-28",
  "status": "Candidate",
  "campaign": "Next-144",
  "completed_tasks": [
    { "task_number": 37, "title": "Expand KG node index v0.2 (40 nodes)", "artifact": "docs/LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md", "xp_earned": 100 },
    { "task_number": 38, "title": "Sheldonbrain KG subgraph doc", "artifact": "docs/SHELDONBRAIN_KG_SUBGRAPH.md", "xp_earned": 100 },
    { "task_number": 39, "title": "Aluminum OS KG subgraph doc", "artifact": "docs/ALUMINUM_OS_KG_SUBGRAPH.md", "xp_earned": 100 },
    { "task_number": 40, "title": "Agent identity card spec", "artifact": "docs/AGENT_IDENTITY_CARD_SPEC.md", "xp_earned": 100 },
    { "task_number": 41, "title": "Children Swarm derived-lattice exporter", "artifact": "scripts/export_children_swarm_lattice.py", "xp_earned": 150 },
    { "task_number": 42, "title": "Children Swarm validation tests", "artifact": "tests/test_children_swarm_lattice.py", "xp_earned": 150 },
    { "task_number": 43, "title": "Evidence bundle format for AI systems", "artifact": "docs/EVIDENCE_BUNDLE_FORMAT.md", "xp_earned": 100 },
    { "task_number": 44, "title": "Aetherforge game state snapshot format", "artifact": "docs/AETHERFORGE_GAME_STATE_SNAPSHOT.md", "xp_earned": 100 },
    { "task_number": 45, "title": "GPTDream++ protocol index extension", "artifact": "docs/GPTDREAM_PROTOCOL_INDEX.md", "xp_earned": 100 },
    { "task_number": 46, "title": "KG hypercube search query spec", "artifact": "docs/KG_SEARCH_QUERY_SPEC.md", "xp_earned": 100 },
    { "task_number": 47, "title": "Update KG topology guide + rebuild adjacency", "artifact": "docs/generated/KG_ADJACENCY_MATRIX.json", "xp_earned": 100 },
    { "task_number": 48, "title": "TIDELOCKBrain Wave-4 REM wake artifact", "artifact": "archive/boot/gptbrain/TIDELOCKBrain/WAKE_REPORT_WAVE4_2026-05-28.md", "xp_earned": 200 }
  ],
  "xp_total": 1400,
  "rings_cleared": ["Wave 4"],
  "kg_nodes_added": ["N-SHELDON", "N-ALUMINUM", "N-BAZINGA", "N-COUNCIL", "N-GOV-INDEX", "N-RISK", "N-TIDELOCK", "N-GPTBRAIN", "N-SWARM", "N-CHILDREN-SWARM", "N-EVIDENCE", "N-KG-SUBGRAPHS", "N-NEXT144", "N-AETHER-GAME", "N-FREE-BANK", "N-CHINOOK", "N-RESEARCH", "N-HEALTH", "N-GOVERNANCE-OPS"],
  "kg_edge_count_delta": 48,
  "lattice_health": {
    "node_count": 40,
    "edge_density": 2.4,
    "orphan_ratio": 0.0
  },
  "provenance": {
    "taskboard_artifact": "projects/aetherforge-next144-taskboard-2026-05-28.md",
    "tidelock_wake_artifact": "archive/boot/gptbrain/TIDELOCKBrain/WAKE_REPORT_WAVE4_2026-05-28.md",
    "pr_url": null
  }
}
```

## XP Scale Reference

| Task type | Base XP |
| --- | --- |
| Documentation artifact | 100 |
| Script / automation | 150 |
| Test suite | 150 |
| TIDELOCKBrain REM artifact | 200 |
| CI workflow integration | 200 |
| KG node expansion (per 10 nodes) | 50 |

## Related

- [projects/AETHERFORGE_PUBLIC_QUESTBOARD_v0.1.md](../projects/AETHERFORGE_PUBLIC_QUESTBOARD_v0.1.md)
- [projects/aetherforge-next144-taskboard-2026-05-28.md](../projects/aetherforge-next144-taskboard-2026-05-28.md)
- [AGENT_IDENTITY_CARD_SPEC.md](./AGENT_IDENTITY_CARD_SPEC.md)
- [CHILDREN_SWARM_LATTICE.md](./CHILDREN_SWARM_LATTICE.md)
