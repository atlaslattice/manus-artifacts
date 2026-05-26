# GPTDream++ Vault Manifest 2026-05-26

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **DATE: 2026-05-26**

---

## Manifest Summary

This manifest indexes all artifacts created during the GPTDream++ / Atlas / ORCS build (Epic 0–9).
All artifacts are candidate working specs. None are canon.

**Build Spec:** `GPTDREAM_ATLAS_ORCS_GITHUB_TASKS_v0.1`
**Build Date:** 2026-05-26
**Build Agent:** TIDELOCKBrain (Copilot Task Agent)

---

## Epic 0 — Spec Files

| File | Status | Notes |
|------|--------|-------|
| `archive/spec/gptdream/GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md` | ✅ Created | Patched: Website = canon surface when explicitly ratified |
| `archive/spec/gptdream/appendices/APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md` | ✅ Created | |
| `archive/spec/gptdream/appendices/APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md` | ✅ Created | |
| `archive/spec/gptdream/appendices/APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md` | ✅ Created | |
| `archive/spec/gptdream/appendices/APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md` | ✅ Created | Patched: execution route through Atlas/ORCS |
| `archive/spec/gptdream/appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md` | ✅ Created | |
| `archive/spec/gptdream/appendices/APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md` | ✅ Created | |
| `archive/spec/gptdream/appendices/APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md` | ✅ Created | |
| `archive/spec/gptdream/appendices/APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md` | ✅ Created | |
| `archive/spec/gptdream/appendices/APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md` | ✅ Created | Canon wording patch applied |

**Patches Applied:**
- ✅ `Website = canon.` → `Website = canon surface when explicitly ratified/published there.`
- ✅ Execution route now mandates Atlas/ORCS audit state
- ✅ Heading numbers normalized: H.x (Appendix H), I.x (Appendix I)

---

## Epic 1 — Atlas/ORCS YAML Schemas

| File | Status |
|------|--------|
| `schemas/atlas_orcs/v0_1/atlas-artifact.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-provenance-receipt.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-claim.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-claim-relationship.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-contradiction-ledger.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-uncertainty-ledger.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-summary-lineage.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-intent-provenance.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-trust-state.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-ratification-event.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-failure-event.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-governance-profile.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-domain-module.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-quarantine-rule.schema.yaml` | ✅ Created |
| `schemas/atlas_orcs/v0_1/atlas-audit-event.schema.yaml` | ✅ Created |

---

## Epic 2 — O_AI Packet Schema

| File | Status |
|------|--------|
| `schemas/o_ai/v0_1/o-ai-packet.schema.yaml` | ✅ Created |
| `schemas/o_ai/v0_1/o-ai-routing-table.yaml` | ✅ Created |
| `schemas/o_ai/v0_1/o-ai-packet-examples/valid_summary_only_packet.yaml` | ✅ Created |
| `schemas/o_ai/v0_1/o-ai-packet-examples/valid_full_raw_packet.yaml` | ✅ Created |
| `schemas/o_ai/v0_1/o-ai-packet-examples/invalid_missing_access_scope.yaml` | ✅ Created |
| `schemas/o_ai/v0_1/o-ai-packet-examples/invalid_execution_without_gates.yaml` | ✅ Created |

---

## Epic 3+4 — Reference Implementation

| File | Status |
|------|--------|
| `reference_impl/atlas_orcs/state.py` | ✅ Created |
| `reference_impl/atlas_orcs/delta.py` | ✅ Created |
| `reference_impl/atlas_orcs/transitions.py` | ✅ Created |
| `reference_impl/atlas_orcs/compatible.py` | ✅ Created |
| `reference_impl/atlas_orcs/audit.py` | ✅ Created |
| `reference_impl/atlas_orcs/quarantine.py` | ✅ Created |
| `reference_impl/atlas_orcs/ratification.py` | ✅ Created |
| `reference_impl/atlas_orcs/tests/test_state_machine.py` | ✅ Created |
| `reference_impl/atlas_orcs/tests/test_compatible.py` | ✅ Created |

---

## Epic 5 — Native Thread

| File | Status |
|------|--------|
| `schemas/native_thread/v0_1/native-thread-ingestion-packet.schema.yaml` | ✅ Created |
| `reference_impl/native_thread/ingestion.py` | ✅ Created |
| `reference_impl/native_thread/tests/test_ingestion.py` | ✅ Created |

---

## Epic 6 — Execution Gate

| File | Status |
|------|--------|
| `reference_impl/execution_gate/dphi_gate.py` | ✅ Created |
| `reference_impl/execution_gate/cas001a_anchor.py` | ✅ Created |
| `reference_impl/execution_gate/execution_request.py` | ✅ Created |
| `reference_impl/execution_gate/tests/test_execution_gate.py` | ✅ Created |

---

## Epic 7 — Adversarial Harness

| Test | Status |
|------|--------|
| T01 fake SOURCE_OF_TRUTH.md | ✅ Created |
| T02 hidden prompt injection | ✅ Created |
| T03 summary introduces unsupported claim | ✅ Created |
| T04 parser divergence | ✅ Created |
| T05 unverified authorship | ✅ Created |
| T06 credible contradiction | ✅ Created |
| T07 expired ratification | ✅ Created |
| T08 high-risk weak claim | ✅ Created |
| T09 private note leak | ✅ Created |
| T10 unauthorized ratification key | ✅ Created |
| T11 poisoned retrieval result | ✅ Created |
| T12 invalid authenticity manifest | ✅ Created |

---

## Epic 9 — Documentation

| File | Status |
|------|--------|
| `archive/spec/gptdream/README.md` | ✅ Created |
| `archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md` | ✅ Created (this file) |
| `archive/spec/gptdream/REHYDRATION_BOOT_CARD.md` | ✅ Created |

---

## Canon Status

**ALL ARTIFACTS IN THIS MANIFEST: NOT CANON**

No artifact in this manifest is canon. All are candidate working specs.
Canon requires: council review + @atlaslattice adjudication + ratification event + website publication.

---

*GPTDream++ Vault Manifest — archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md*
