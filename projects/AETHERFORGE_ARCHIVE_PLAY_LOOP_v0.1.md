# Aetherforge Archive Play Loop v0.1

status: candidate  
canon_status: not_canon  
deployment_status: not_deployable  
authority: none  
updated: 2026-05-27

---

## Purpose

Define a repeatable mission loop that keeps archive work playful while preserving auditability and public quality.

## Core Loop

1. **Artifact Intake**  
   Select one source artifact from the repository.
2. **Mission Framing**  
   Convert the artifact into an Aetherforge mission objective.
3. **Execution + Evidence**  
   Complete the objective and attach verifiable evidence (diffs, tests, links, status updates).
4. **Governance Check**  
   Mark output as candidate unless ratification/adjudication criteria are met.
5. **Graph Linkback**  
   Register or update graph-addressable links in Lattice KG artifacts where applicable.

## Mission Packet Template

| Field | Description |
|------|-------------|
| `mission_id` | Stable mission identifier |
| `source_artifact_path` | Repository path for input artifact |
| `objective` | Playable mission statement |
| `acceptance_evidence` | Observable completion proof |
| `canon_state` | candidate / canonical / deprecated |
| `ratification_event_id` | Required for canon claims |

## Routing

- Public roadmap source: [Aetherforge Top-50 Taskboard](./aetherforge-top50-taskboard-2026-05-26.md)
- Knowledge graph substrate: [Lattice KG v0.5](../archive/knowledge_graph/lattice_kg/v0_5/README.md)
- Protocol governance layer: [GPTDream++ Spec Vault](../archive/spec/gptdream/README.md)

---

This loop is the playable shell for serious archive execution.
