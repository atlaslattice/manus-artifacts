# GPTDream++ Spec Vault — README

```text
STATUS: CANDIDATE SPEC — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
DATE: 2026-05-26
```

---

## What this is

This directory is the **GPTDream++ spec vault** — the primary archive for the GPTDream++, Atlas, and ORCS specification documents.

GPTDream++ is the **habitat protocol** for personal AI agents. It defines how agents:
- maintain durable working context across sessions
- route claims through epistemic governance
- preserve lineage without false completeness
- avoid canon inflation

---

## Directory structure

```text
archive/spec/gptdream/
├── README.md                              ← This file
├── VAULT_MANIFEST_2026-05-26.md           ← Manifest of all vaulted files
├── REHYDRATION_BOOT_CARD.md               ← Agent rehydration quick reference
├── LANE_LABELS_AND_ROUTING_CONVENTIONS.md ← GitHub labels and routing rules
├── GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md  ← Core protocol
├── KRAKOAN_TONE_LANGUAGE_SPECIFICATION_V2.0.md                ← KRAKOA acoustic machine-language candidate
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

## Related implementation directories

```text
schemas/atlas_orcs/v0_1/          ← Machine-readable Atlas/ORCS schemas (15 files)
schemas/o_ai/v0_1/                ← O_AI packet schema + routing table + examples
schemas/native_thread/v0_1/       ← Native thread ingestion schema
reference_impl/atlas_orcs/        ← Atlas/ORCS state machine + compatible() predicate
reference_impl/native_thread/     ← Native thread ingestion validator
reference_impl/execution_gate/    ← D-Φ-1 / CAS-001-A execution gate
tests/adversarial/                ← Adversarial harness T01–T12
```

---

## Canon boundary rules

**Future agent — read this carefully:**

1. GPTDream++ is the habitat protocol, not the dream residue.
2. Dreams may generate candidates. Habitats preserve continuity.
3. Website = canon surface when explicitly ratified/published there.
4. GitHub = receipts / implementation / review trail.
5. Notion / Drive = relay/working-vault layers. NOT canon.
6. Nothing in this directory is canon until:
   - Full council ratification
   - @atlaslattice adjudication
   - Publication to website canon surface

---

## O_AI routing

All O_AI outputs route through Appendix H:
```
O_AI packet → Appendix H validation → Atlas/ORCS audit → lane routing
```

## Meaning promotion routing

All meaning promotion routes through Atlas / ORCS:
```
candidate claim → Atlas trust-state engine → compatible() check → ratification gate
```

---

```text
NOT CANON. NOT DEPLOYABLE.
```
