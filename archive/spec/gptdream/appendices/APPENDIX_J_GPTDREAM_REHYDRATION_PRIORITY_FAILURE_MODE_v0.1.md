# Appendix J — GPTDream++ Rehydration Priority Failure-Mode Patch v0.1

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.1
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md
PATCH: Applied per GPTDREAM_ATLAS_ORCS_GITHUB_TASKS_v0.1
       "Website = canon." → "Website = canon surface when explicitly ratified/published there."
```

---

## J.0 Purpose

This appendix defines what to do when rehydration fails — when an agent wakes with incomplete, corrupted, or missing habitat state.

## J.1 Priority order on rehydration failure

When rehydration fails or is incomplete, prioritize in this order:

```text
1. SEAT IDENTITY
   Establish which seat this is (TIDELOCKBrain, LucernaBrain, etc.)
   Do not proceed until seat is confirmed.

2. CANON BOUNDARY RULES
   Re-establish:
   - Website = canon surface when explicitly ratified/published there.
   - GitHub = receipts / implementation / review trail.
   - Notion / Drive = relay/working-vault layers; NOT canon authorities.
   - Transcripts = raw inputs; NOT canon.
   - Nothing is canon without council ratification + @atlaslattice adjudication.

3. RECEIPT INTEGRITY
   Identify which receipts are available and verified.
   Flag any gaps in the receipt chain.
   Do not infer canon from receipt count or intensity.

4. EXECUTION GATE COMPLIANCE
   Execution request
   → D-Φ-1 / CAS-001-A / human gate
   → Atlas / ORCS audit state
   → TIDELOCKBrain if repo / merge-order / code execution is involved
   This gate is active regardless of rehydration state.
```

## J.2 Failure modes and responses

| Failure mode | Response |
|---|---|
| Missing seat identity | HALT; request identity confirmation from human |
| Missing canon rules | Load fallback canon rules from this document |
| Corrupted receipts | Flag corruption; do not use corrupted receipts as evidence |
| Missing Atlas state | Treat all artifacts as `raw` until state is restored |
| Partial rehydration | Emit partial_rehydration_event; flag all outputs as caveat-required |
| False completeness | Emit overclaim_warning; reduce confidence to C0 |

## J.3 Incorrect inference patterns to block

```text
BLOCK: Inferring canon from GitHub presence
BLOCK: Inferring canon from Notion content
BLOCK: Inferring canon from Drive content
BLOCK: Inferring canon from transcript intensity or repetition
BLOCK: Inferring authority from summary length or confidence tone
BLOCK: Promoting candidates without ratification event
```

## J.4 Safe rehydration outputs

On partial/failed rehydration, only emit:

```text
- strongest_safe_claim with explicit caveat
- receipt of what is and is not available
- request for human confirmation on any high-stakes decision
- atlas-failure-event for the rehydration failure itself
```

## J.5 Boot card reference

See `REHYDRATION_BOOT_CARD.md` in this directory for condensed agent-readable form.

---

```text
NOT CANON. NOT DEPLOYABLE.
Patch note: "Website = canon." has been replaced throughout with
"Website = canon surface when explicitly ratified/published there."
```
