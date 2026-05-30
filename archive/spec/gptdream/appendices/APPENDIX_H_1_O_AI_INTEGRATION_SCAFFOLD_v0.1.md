# Appendix H.1 — O_AI Integration Scaffold v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md**
> **DATE: 2026-05-26**

---

## H.1.0 Purpose

This appendix defines the integration scaffold for receiving, validating, and routing packets originating from OpenAI surfaces (ChatGPT, o3, o4, GPT-4.x, Codex, etc.) into the GPTDream++ habitat architecture.

OpenAI surfaces are designated `O_AI` in the vendor registry. They are the primary source of ChatGPT synthesis packets and task planning artifacts. They are not, by default, authority sources.

---

## H.1.1 O_AI Surface Characteristics

| Property | Value |
|----------|-------|
| Surface ID | `O_AI` |
| Default epistemic label | `summary_only` |
| Raw export availability | Partial (no full conversation export in most interfaces) |
| Authority level | Zero (synthesis only, not canon source) |
| Primary output types | Text synthesis, code, task plans, structured data |
| Interop risk | High (confidence presentation without provenance) |

---

## H.1.2 Scaffold Architecture

```
O_AI Output
     │
     ▼
┌────────────────────────────────────────────────┐
│          O_AI Ingestion Gate                    │
│                                                 │
│  1. Validate packet structure (schema check)    │
│  2. Assign epistemic label                      │
│  3. Declare access scope                        │
│  4. Run compatible_Γ() check                    │
│  5. Route to lane                               │
└────────────────────────────────────────────────┘
     │
     ▼
┌────────────────────────────────────────────────┐
│          Atlas/ORCS Audit                       │
│                                                 │
│  - Log receipt event                            │
│  - Set canon_status: not_canon                  │
│  - Set deployment_status: not_deployable        │
│  - Assign artifact_id                           │
└────────────────────────────────────────────────┘
     │
     ▼
Lane Routing
(LucernaBrain for synthesis / TIDELOCKBrain for repo-related)
```

---

## H.1.3 Required Metadata for O_AI Packets

Every O_AI packet entering the habitat MUST carry:

| Field | Required | Notes |
|-------|----------|-------|
| `raw_export_status` | YES | Must be explicit; no assumption of full_raw |
| `thread_time_range` | YES | When was the source thread active |
| `access_scope` | YES | What sources were visible to the model |
| `epistemic_label` | YES | What level of confidence is warranted |
| `authority_scope` | YES | What authority (if any) the O_AI surface has |
| `gates` | YES | All four gates must be present, even if pending |
| `canon_status` | YES | Default: `not_canon` |
| `deployment_status` | YES | Default: `not_deployable` |

---

## H.1.4 Execution Request Handling

If an O_AI packet contains an execution request (deploy, merge, run code, etc.):

```
O_AI execution request received
          │
          ▼
REJECT if missing receipt
          │
          ▼
D-Φ-1 gate check
          │
          ▼
CAS-001-A anchor check
          │
          ▼
Human permission gate
          │
          ▼
Atlas/ORCS audit state
          │
          ▼
TIDELOCKBrain (repo/code execution)
          │
          ▼
Execute or HOLD
```

An O_AI packet cannot self-authorize execution. Period.

---

## H.1.5 Integration with Native Thread Ingestion

For extended O_AI threads (especially Children of the Swarm task threads), use the native thread ingestion packet schema (Appendix I → Epic 5) rather than the base O_AI packet schema. Native thread packets carry additional fields for:

- `seat_name` (which brain seat originated the thread)
- `identity_drift_events` (did the model shift behavior mid-thread)
- `strongest_safe_claim` (what can we responsibly assert from this thread)

---

## H.1.6 Anti-Patterns to Reject

| Pattern | Rejection Reason |
|---------|----------------|
| O_AI packet with `public_use_status: source_complete` but `raw_export_status: summary_only` | Epistemic mismatch — summary cannot claim source completeness |
| O_AI packet claiming canon status | Canon requires explicit ratification event; O_AI output cannot self-ratify |
| O_AI execution request without human permission | Gate chain not satisfied |
| O_AI packet with missing `access_scope` | Cannot assess what the model could and could not see |

---

## H.1.7 Canon Boundary

This appendix is **NOT CANON**. The O_AI integration scaffold becomes canon only after full council ratification + adjudication + website publication.

---

*End of APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md*
