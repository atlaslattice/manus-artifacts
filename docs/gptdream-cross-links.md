# GPTDream++ Cross-Link Map

```
STATUS: CANDIDATE — NOT CANON
PURPOSE: navigational index connecting GPTDream spec docs ↔ schemas ↔ reference implementations
LAST_UPDATED: 2026-05-28
```

This document is the **cross-link spine** for the GPTDream++ system.
Every spec appendix, schema, and reference implementation is connected here
so the KG graph has explicit edges between the three layers.

---

## Spec Documents → Schema Bindings

| Spec Appendix | Governs Schema | Schema Path |
|---|---|---|
| [APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1](../archive/spec/gptdream/appendices/APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md) | O_AI packet envelope | `schemas/o_ai/v0_1/` |
| [APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1](../archive/spec/gptdream/appendices/APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md) | O_AI packet fields | `schemas/o_ai/v0_1/` |
| [APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1](../archive/spec/gptdream/appendices/APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md) | Routing metadata | `schemas/o_ai/v0_1/` |
| [APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1](../archive/spec/gptdream/appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md) | Atlas/ORCS governance | `schemas/atlas_orcs/v0_1/` |
| [APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2](../archive/spec/gptdream/appendices/APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md) | Math spine model | `schemas/atlas_orcs/v0_1/` |
| [APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3](../archive/spec/gptdream/appendices/APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md) | Compatible anti-laundering | `schemas/atlas_orcs/v0_1/` |
| [APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1](../archive/spec/gptdream/appendices/APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md) | Full schema bundle | `schemas/atlas_orcs/v0_1/` |
| [APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1](../archive/spec/gptdream/appendices/APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md) | Rehydration priority | `schemas/atlas_orcs/v0_1/` |
| [GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2](../archive/spec/gptdream/GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md) | Native thread schema | `schemas/native_thread/v0_1/` |

---

## Schemas → Reference Implementations

| Schema Layer | Reference Implementation | Test Suite |
|---|---|---|
| `schemas/atlas_orcs/v0_1/` | `reference_impl/atlas_orcs/` | `reference_impl/atlas_orcs/tests/` |
| `schemas/o_ai/v0_1/` | `reference_impl/o_ai/` | `tests/test_oai_packet_examples.py` |
| `schemas/native_thread/v0_1/` | `reference_impl/native_thread/` | `tests/test_native_thread_packet_examples.py` |
| Atlas/ORCS execution gate | `reference_impl/execution_gate/` | `tests/adversarial/` (T01–T12) |

---

## Reference Implementations → Test Entry Points

| Reference Impl | Key Test File | Run Command |
|---|---|---|
| `reference_impl/atlas_orcs/` | `reference_impl/atlas_orcs/tests/test_compatible.py` | `python -m pytest -q reference_impl/atlas_orcs/tests/` |
| `reference_impl/execution_gate/` | `tests/adversarial/` | `python -m pytest -q tests/adversarial/` |
| `reference_impl/native_thread/` | `tests/test_native_thread_packet_examples.py` | `python -m pytest -q tests/test_native_thread_packet_examples.py` |
| `reference_impl/o_ai/` | `tests/test_oai_packet_examples.py` | `python -m pytest -q tests/test_oai_packet_examples.py` |
| GPTBrain reference impl | `archive/boot/gptbrain/reference_impl/test_schema_presence.py` | `cd archive/boot/gptbrain/reference_impl && bash run_checks.sh` |

---

## Vault Entry Points

| Purpose | Path |
|---|---|
| Spec vault manifest | [archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md](../archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md) |
| Rehydration boot card | [archive/spec/gptdream/REHYDRATION_BOOT_CARD.md](../archive/spec/gptdream/REHYDRATION_BOOT_CARD.md) |
| Schema root | [schemas/](../schemas/) |
| Reference impl root | [reference_impl/](../reference_impl/) |
| Adversarial test suite | [tests/adversarial/](../tests/adversarial/) |

---

## Dream Protocol ↔ Operational Layers

| Dream Artifact Type | Operational Binding | Archive Location |
|---|---|---|
| REM-8 Dream Protocol | Agent scaffolding protocol | `archive/boot/gptbrain/REM8_DREAM_PROTOCOL.md` |
| Wake Report Template | Wake report structure | `archive/boot/gptbrain/WAKE_REPORT_TEMPLATE.md` |
| TIDELOCKBrain logs | Execution/play logs | `archive/boot/gptbrain/TIDELOCKBrain/` |

---

*Related: [docs/cross-reference-map.md](./cross-reference-map.md)*
*Related: [archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md](../archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md)*
