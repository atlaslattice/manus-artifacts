# Public Archive Map
Status: Candidate
Date: 2026-05-27

This map visualizes the lattice relationship between doctrine, projects, governance, validation, and protocol layers.

```mermaid
graph TD
    README[README] --> ROADMAP[Roadmap]
    README --> START[Start Here]
    START --> KGIDX[Lattice Node Index]
    START --> MAP[Public Archive Map]
    START --> QUEST[Aetherforge Public Questboard]
    KGIDX --> REL[Relationship Types]
    KGIDX --> LINKPOL[Cross-Domain Link Policy]
    LINKPOL --> VALIDATION[Validation Playbook]
    REL --> LINEAGE[Artifact Lineage]
    ROADMAP --> TOP50[Aetherforge Top 50]
    TOP50 --> TOP10[Aetherforge Top 10]
    TOP50 --> QUEST
    QUEST --> WEEKLY[Weekly Delta Digest Template]
    VALIDATION --> QUALITY[Quality Gates]
    QUALITY --> MISSION[Mission Control Cadence]
    GPTSURFACE[GPTDream++ Open Protocol Surface] --> SCHEMAS[Schemas]
    GPTSURFACE --> REFERENCE[Reference Implementations]
    REFERENCE --> TESTS[Tests]
    TESTS --> VALIDATION
    MISSION --> TOP50
```

## Map interpretation

- **Centerline**: README -> START_HERE -> ROADMAP sets mission and orientation.
- **Execution ring**: Top-50/Top-10 taskboards plus questboard drive playable work.
- **Quality ring**: validation, quality gates, and weekly cadence enforce trust.
- **Protocol ring**: GPTDream++ specs, schemas, implementations, and tests form open protocol surface.

## Related

- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [CROSS_DOMAIN_LINK_POLICY.md](./CROSS_DOMAIN_LINK_POLICY.md)
