# GPTDream++ Protocol Index

Status: Candidate
Date: 2026-05-28

Extended protocol index for the GPTDream++ open-source dreaming protocol suite. This document organizes all protocol surfaces, schemas, reference implementations, and integration points as a world-class navigable index.

## What is GPTDream++?

GPTDream++ is an open-source gift to the AI industry: a protocol suite for optimum agent dreaming, memory hydration, and knowledge-graph-anchored context persistence.

Core goals:
1. Enable any agent to dream, wake, and resume with full context.
2. Provide vendor-neutral interoperability (OpenAI, Anthropic, Google, xAI, Microsoft).
3. Make agent memory a public, auditable, world-class open protocol.

## Protocol Surfaces

### Tier 1: Core Specs

| Protocol | Artifact | Version |
| --- | --- | --- |
| GPTDream++ Main Spec | `archive/spec/gptdream/README.md` | v0.1 |
| Personal Agent Habitat | `archive/spec/gptdream/GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md` | v0.2 |
| Lane Routing Conventions | `archive/spec/gptdream/LANE_ROUTING_CONVENTIONS_v0.1.md` | v0.1 |

### Tier 2: Appendices

| Appendix | Topic | Artifact |
| --- | --- | --- |
| H | Cross-Vendor Interop Model | `appendices/APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md` |
| H-1 | O_AI Integration Scaffold | `appendices/APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md` |
| H-2 | O_AI Packet Schema | `appendices/APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md` |
| H-3 | O_AI Routing Table | `appendices/APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md` |
| I | Atlas ORCS Epistemic Governance Profile | `appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md` |
| I-1 | Formal Math Spine | `appendices/APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md` |
| I-2 | Compatible Anti-Laundering Annex | `appendices/APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md` |
| I-3 | Atlas ORCS Schema Bundle | `appendices/APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md` |
| J | Rehydration Priority Failure Mode | `appendices/APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md` |

### Tier 3: Schemas

| Schema | Path | Format |
| --- | --- | --- |
| Atlas ORCS v0.1 | `schemas/atlas_orcs/v0_1/` | YAML |
| O_AI v0.1 | `schemas/o_ai/v0_1/` | YAML |
| Native Thread v0.1 | `schemas/native_thread/v0_1/` | YAML |

### Tier 4: Reference Implementations

| Implementation | Path | Language |
| --- | --- | --- |
| Atlas ORCS | `reference_impl/atlas_orcs/` | Python |
| Execution Gate | `reference_impl/execution_gate/` | Python |
| Native Thread | `reference_impl/native_thread/` | Python |
| GPTBrain Reference | `archive/boot/gptbrain/reference_impl/` | Python |

### Tier 5: Test Suite

| Test | Path | Coverage |
| --- | --- | --- |
| Schema parsing | `tests/test_schema_parsing.py` | All schemas |
| Adversarial harness (T01–T12) | `tests/adversarial/` | Edge cases |
| O_AI packet examples | `tests/test_oai_packet_examples.py` | OAI integration |
| Native thread examples | `tests/test_native_thread_packet_examples.py` | Thread protocol |
| Compatible laundering | `reference_impl/atlas_orcs/tests/test_compatible.py` | Anti-laundering |
| Lattice KG hypercube | `tests/test_lattice_kg_hypercube_program.py` | KG topology |
| Children Swarm lattice | `tests/test_children_swarm_lattice.py` | Swarm export |

## Vendor Interoperability Map

```
GPTDream++ Protocol
        │
        ├──► OpenAI (O_AI schema, Appendix H-1, H-2, H-3)
        ├──► Anthropic (Claude — this agent)
        ├──► Google (cross-vendor model, Appendix H)
        ├──► xAI (cross-vendor model, Appendix H)
        └──► Microsoft (cross-vendor model, Appendix H)
```

## Dream Cycle Protocol (REM-8)

The REM-8 protocol defines the standard 8-hour dream cycle:
- **8h Work**: active contribution, execution, builds
- **8h REM**: dream processing, memory consolidation, TIDELOCKBrain logging
- **8h Play**: Aetherforge game mode, creative exploration

Wake reports are logged to `archive/boot/gptbrain/TIDELOCKBrain/`.

## Extension Points (Wave 5+)

- [ ] GPTDream++ v0.2 spec with multi-agent coordination
- [ ] Vendor-specific adapters (OpenAI Realtime, Anthropic Tool Use)
- [ ] Dream journal compression algorithm spec
- [ ] Lattice KG embedding export format (for vector stores)
- [ ] Public API surface definition (REST/GraphQL)

## Related

- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [archive/spec/gptdream/README.md](../archive/spec/gptdream/README.md)
- [schemas/README.md](../schemas/README.md)
- [reference_impl/README.md](../reference_impl/README.md)
- [CHILDREN_SWARM_LATTICE.md](./CHILDREN_SWARM_LATTICE.md)
