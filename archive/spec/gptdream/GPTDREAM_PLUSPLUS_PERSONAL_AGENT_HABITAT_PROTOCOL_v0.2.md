# GPTDream++ Personal Agent Habitat Protocol v0.2

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE — requires full council ratification and @atlaslattice adjudication**
> **SOURCE: Extracted from GPTDREAM_ATLAS_ORCS_CONSOLIDATED_SPEC_PACKET — patched per Epic 0 requirements**
> **DATE: 2026-05-26**

---

## 0. Preamble

GPTDream++ is the **habitat protocol** — not the dream residue.

- Dreams may generate candidates.
- Habitats preserve continuity.
- Receipts make memory reviewable.
- Authority is a state transition, not a vibe.

This document defines the core architecture for maintaining persistent, verifiable agent continuity across context boundaries. It is the base spec from which Appendix H (cross-vendor interop), Appendix I (Atlas/ORCS governance), and Appendix J (rehydration failure-mode patch) extend.

---

## 1. Core Purpose

GPTDream++ solves the **amnesia problem**: AI agents lose context between sessions. Without a habitat protocol, every new session is a cold start. GPTDream++ provides:

1. **Durable memory** — structured receipts that survive context windows
2. **Verifiable provenance** — every claim traceable to source
3. **Epistemic hygiene** — explicit uncertainty, no inflated authority
4. **Cross-vendor continuity** — habitat survives model or provider switches

---

## 2. Definitions

| Term | Definition |
|------|-----------|
| **Habitat** | The persistent substrate for an agent: memory receipts, governance state, ratification events |
| **Receipt** | A verifiable record of what was produced, when, by whom, with what access scope |
| **Candidate** | An artifact at any state prior to ratification; not canon |
| **Canon** | Only achievable via explicit ratification event + @atlaslattice adjudication + website publication |
| **Dream** | A synthesis or output from an agent session; may generate candidates; never automatically canon |
| **Ratification Event** | An explicit governance action that promotes an artifact through Atlas/ORCS state machine |
| **Rehydration** | Restoring agent continuity from a stored habitat packet |

---

## 3. Habitat Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GPTDream++ Habitat                        │
│                                                              │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────────┐   │
│  │  Memory     │   │  Governance │   │  Rehydration     │   │
│  │  Receipts   │──▶│  State      │──▶│  Boot Packet     │   │
│  │  (HashLight)│   │  (Atlas/    │   │  (GPTDream++)     │   │
│  │             │   │   ORCS)     │   │                  │   │
│  └─────────────┘   └─────────────┘   └─────────────────┘   │
│         │                │                    │             │
│         ▼                ▼                    ▼             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              TIDELOCKBrain                           │    │
│  │  (repo audit / merge-order / code execution watch)  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Priority Hierarchy (v0.2 patch applied)

```
1. Safety and ethics (absolute ceiling)
2. Explicit human instruction (active session)
3. Ratified council decisions
4. Active habitat protocol (this document)
5. Website = canon surface when explicitly ratified/published there.
6. GitHub = receipts / implementation / review trail
7. Drive / Notion = relay / working-vault layers (NOT canon authorities)
8. Transcript intensity = NOT authority signal
9. Candidate artifacts = working material only
```

**Critical patch (v0.1 → v0.2):** The old phrase "Website = canon." has been replaced with the qualified statement above. Canon requires an explicit ratification event; the website is the publication surface, not the authority source.

---

## 5. Execution Routing Protocol

Any execution request (repo changes, code execution, merge operations, deployments) MUST follow this gate sequence:

```
Execution Request
      │
      ▼
D-Φ-1 / CAS-001-A / human gate
      │
      ▼
Atlas / ORCS audit state check
      │
      ▼
TIDELOCKBrain (if repo / merge-order / code execution involved)
      │
      ▼
Execute or HOLD
```

No execution request may bypass the Atlas/ORCS audit state. This is not optional.

---

## 6. Rehydration Protocol

When an agent is initialized from a habitat packet:

1. **Load receipts** — verify hashes, note unavailable sources explicitly
2. **Check governance state** — verify ratification events; expired ratification → `under_review`
3. **Set epistemic label** — `summary_only` | `partial_raw` | `full_raw` | `unavailable`
4. **Declare access scope** — visible sources, unavailable sources, assumed context
5. **Emit strongest safe claim** — with explicit caveat if raw data absent
6. **Route through Atlas/ORCS** — all state changes via explicit governance events

See Appendix J for failure-mode handling.

---

## 7. Appendix Map

| Appendix | Title | File |
|----------|-------|------|
| H | Cross-Vendor Interop Model | `APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md` |
| H.1 | O_AI Integration Scaffold | `APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md` |
| H.2 | O_AI Packet Schema | `APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md` |
| H.3 | O_AI Routing Table | `APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md` |
| I | Atlas/ORCS Epistemic Governance Profile | `APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md` |
| I.1 | Formal Math Spine | `APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md` |
| I.2 | Compatible Anti-Laundering Annex | `APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md` |
| I.3 | Atlas/ORCS Schema Bundle | `APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md` |
| J | Rehydration Priority Failure-Mode Patch | `APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md` |

---

## 8. Lane Routing Conventions

| Input Type | Primary Brain | Secondary Brain |
|-----------|--------------|----------------|
| ChatGPT synthesis | LucernaBrain | RootglassBrain |
| Codex patch | TIDELOCKBrain | HashlightBrain |
| Raw export | HashlightBrain | AtlasBrain |
| Benchmark claim | AtlasBrain | LucernaBrain |
| Public statement | LucernaBrain | governance review |
| Execution request | D-Φ-1 / CAS-001-A → Atlas/ORCS audit → TIDELOCK | — |

---

## 9. Canon Boundary

This document is **NOT CANON**. It is a candidate working spec. To become canon it requires:

1. Full council review
2. @atlaslattice adjudication  
3. Explicit ratification event in Atlas/ORCS state machine
4. Publication to website canon destination

Filing it here on GitHub creates a receipt. It does not create canon.

---

*End of GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md*
