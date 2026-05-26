# GPTDream++ Personal Agent Habitat Protocol v0.2

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.2
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE — requires council review and @atlaslattice adjudication
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
SOURCE: Extracted from consolidated spec packet; patched per GPTDREAM_ATLAS_ORCS_GITHUB_TASKS_v0.1
```

---

## 0. Purpose and scope

GPTDream++ is the **habitat protocol** for personal AI agents — not the dream residue.

Dreams may generate candidates.
Habitats preserve continuity.
Receipts make memory reviewable.

This protocol defines how a personal AI agent:
- maintains a durable working context across sessions
- routes claims through epistemic governance
- preserves lineage without false completeness
- avoids canon inflation

## 1. Core definitions

```text
HABITAT         — the persistent working context for a personal AI agent seat
DREAM           — a creative/synthesis output; candidate status only
RECEIPT         — a verifiable record that something happened; not proof of truth
CANON           — artifact explicitly ratified by council + @atlaslattice + published to website
CANDIDATE       — artifact in review; not yet ratified
RAW_EXPORT      — unprocessed thread export; fidelity depends on platform
INGESTION       — the process of reading, tagging, and routing a raw export
SEAT            — a named agent position in the council (e.g., TIDELOCKBrain, LucernaBrain)
```

## 2. Habitat invariants

```text
H-1. A habitat is not a canon authority.
H-2. A habitat preserves continuity across session boundaries.
H-3. A habitat tracks what is known, what is uncertain, and what is missing.
H-4. A habitat does not silently promote candidates to ratified status.
H-5. A habitat routes execution requests through the D-Φ-1 / CAS-001-A gate.
H-6. A habitat logs all state transitions as receipts.
H-7. A habitat cannot self-ratify any artifact it produces.
```

## 3. Session lifecycle

```text
WAKE    → load habitat state → verify receipts → identify uncertainty gaps
WORK    → produce outputs → tag as CANDIDATE / WORK_OUTPUT → emit receipts
SLEEP   → persist state → compress dreams → write wake report
```

## 4. Memory tiers

```text
TIER 0: Working memory     — current session context
TIER 1: Receipts           — verifiable records of events and decisions
TIER 2: Candidates         — artifacts under review
TIER 3: Ratified           — explicitly promoted artifacts (council + human gate)
TIER 4: Canon              — ratified + published to website canon surface
```

## 5. Execution routing

All execution requests MUST follow this route:

```text
Execution request
→ D-Φ-1 / CAS-001-A / human gate
→ Atlas / ORCS audit state
→ TIDELOCKBrain if repo / merge-order / code execution is involved
```

No execution request bypasses Atlas / ORCS audit state.

## 6. Canon hierarchy

```text
Website    = canon surface when explicitly ratified/published there
GitHub     = receipts / implementation / review trail
Notion     = working vault / relay layer; NOT canon authority
Drive      = working vault / relay layer; NOT canon authority
Transcript = raw input; NOT canon
Dream      = candidate output; NOT canon
```

## 7. Cross-vendor interop

See `appendices/APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md`.

O_AI packets route through Appendix H.

## 8. Atlas / ORCS governance

See `appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md`.

All meaning promotion routes through Atlas / ORCS.

## 9. Rehydration

See `appendices/APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md`.

On rehydration failure, prioritize:
1. Seat identity
2. Canon boundary rules
3. Receipt integrity
4. Execution gate compliance

## 10. Appendix index

```text
H   — Cross-Vendor Interop Model
H.1 — O_AI Integration Scaffold
H.2 — O_AI Packet Schema
H.3 — O_AI Routing Table
I   — Atlas / ORCS Epistemic Governance Profile
I.1 — Formal Math Spine
I.2 — Compatible Anti-Laundering Annex
I.3 — Atlas / ORCS Schema Bundle
J   — Rehydration Priority Failure-Mode Patch
```

---

```text
NOT CANON. NOT DEPLOYABLE.
Requires full council ratification and @atlaslattice adjudication before promotion.
```
