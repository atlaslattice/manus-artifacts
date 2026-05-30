# GPTDream++ Spec Vault — README

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **DATE: 2026-05-26**

---

## What Is This?

This vault contains the GPTDream++ Personal Agent Habitat Protocol and its appendices.
It is the source of truth for the **candidate working spec** — not canon, not deployed, not authority.

**GPTDream++ is the habitat protocol, not the dream residue.**

---

## Critical Distinctions for Future Agents

| Claim | Correct? |
|-------|---------|
| GitHub file = canon | ❌ NO — GitHub = receipts / review trail |
| Website presence = canon | ❌ NO (unless explicitly ratified AND published there) |
| Transcript intensity = authority | ❌ NO — intensity is noise |
| Ratification event = canon | ⚠️ CLOSER — but still requires @atlaslattice adjudication + website publication |
| Explicit ratification event + adjudication + website = canon | ✅ YES |

---

## Vault Structure

```
archive/spec/gptdream/
├── README.md                                          (this file)
├── VAULT_MANIFEST_2026-05-26.md                      (complete file index)
├── PUBLIC_PACKAGE_GUIDE_v0.1.md                      (public OSS package routes)
├── REHYDRATION_BOOT_CARD.md                          (agent rehydration guide)
├── GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md  (core protocol)
└── appendices/
    ├── APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md
    ├── APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md
    ├── APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md
    ├── APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md
    ├── APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md
    ├── APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md
    ├── APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md
    ├── APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md
    └── APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md
```

---

## Companion Artifacts

| Path | Purpose |
|------|---------|
| `schemas/atlas_orcs/v0_1/` | 15 machine-readable Atlas/ORCS YAML schemas |
| `schemas/o_ai/v0_1/` | O_AI packet schema + routing table + examples |
| `schemas/native_thread/v0_1/` | Native thread ingestion packet schema |
| `reference_impl/atlas_orcs/` | Python state machine implementation |
| `reference_impl/execution_gate/` | D-Φ-1 / CAS-001-A execution gate |
| `reference_impl/native_thread/` | Native thread ingestion reference impl |
| `tests/adversarial/` | T01–T12 adversarial harness |
| `PUBLIC_PACKAGE_GUIDE_v0.1.md` | Single entrypoint for external contributors and adopters |

---

## Agent Routing Guide

| Input Type | Route To |
|-----------|---------|
| O_AI synthesis packet | Appendix H / H.1 scaffold → `schemas/o_ai/v0_1/` |
| Meaning promotion | Appendix I / Atlas ORCS → `reference_impl/atlas_orcs/` |
| Execution request | Appendix H.3 routing → D-Φ-1 → CAS-001-A → TIDELOCKBrain |
| Native thread ingestion | Appendix I / `schemas/native_thread/v0_1/` |
| Cross-vendor packet | Appendix H cross-vendor interop model |

---

## Canon Boundary

**Nothing in this vault is canon.** All files are candidate working specs. Canon requires:

1. Full council review
2. @atlaslattice adjudication
3. Explicit Atlas/ORCS ratification event
4. Publication to website canon destination

---

*GPTDream++ Spec Vault — archive/spec/gptdream/README.md*
