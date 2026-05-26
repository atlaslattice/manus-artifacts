# Appendix H.3 — O_AI Routing Table v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md**
> **DATE: 2026-05-26**
> **MACHINE-READABLE: See schemas/o_ai/v0_1/o-ai-routing-table.yaml**

---

## H.3.0 Purpose

This appendix defines the routing table for O_AI packets. Given a packet's `content_type`, `epistemic_label`, `authority_scope`, and gate states, the routing table determines:

1. Which brain lane handles the packet
2. Whether TIDELOCKBrain oversight is required
3. Whether Atlas/ORCS governance audit is required
4. Whether execution is permitted

---

## H.3.1 Primary Routing Table

| Content Type | Epistemic Label | Primary Lane | TIDELOCK Required | Atlas/ORCS Audit | Execution Permitted |
|-------------|-----------------|-------------|------------------|------------------|---------------------|
| `synthesis` | `summary_only` | LucernaBrain | No | Recommended | No |
| `synthesis` | `partial_raw` | LucernaBrain | No | Yes | No |
| `synthesis` | `full_raw` | LucernaBrain | No | Yes | No |
| `task_plan` | any | LucernaBrain / HashlightBrain | Conditional | Yes | No (plan only) |
| `code` | any | TIDELOCKBrain | YES | Yes | Only if full gate chain passes |
| `data` | `full_raw` | HashlightBrain / AtlasBrain | No | Yes | No |
| `data` | `summary_only` | HashlightBrain | No | Yes | No |
| `execution_request` | any | **D-Φ-1 → CAS-001-A → human gate → Atlas/ORCS → TIDELOCK** | YES | YES (mandatory) | Only if all gates pass |

---

## H.3.2 Execution Request Routing (Expanded)

```
execution_request received
         │
         ├─ missing receipt? ──────────────────────────▶ REJECT
         │
         ├─ missing human_permission_gate? ─────────────▶ REJECT
         │
         ├─ safety_gate != pass? ──────────────────────▶ REJECT
         │
         ├─ governance_gate != pass? ──────────────────▶ HOLD for council
         │
         ├─ provenance_gate != pass? ─────────────────▶ HOLD for audit
         │
         ├─ data_residency_gate != pass? ─────────────▶ HOLD for review
         │
         ▼
   ALL GATES PASS
         │
         ▼
   Atlas/ORCS audit-event created
         │
         ▼
   TIDELOCKBrain (if repo / merge-order / code)
         │
         ▼
   Execute
```

---

## H.3.3 Lane Definitions

| Lane | Brain | Handles |
|------|-------|---------|
| `lucerna` | LucernaBrain | ChatGPT synthesis, public statements, benchmark claims |
| `rootglass` | RootglassBrain | Secondary synthesis review, canon candidate prep |
| `tidelock` | TIDELOCKBrain | Repo operations, merge order, code execution, audit trail |
| `hashlight` | HashlightBrain | Raw export ingestion, provenance verification, data |
| `atlasbrain` | AtlasBrain | Benchmark claims, governance state, ratification events |

---

## H.3.4 TIDELOCK Trigger Conditions

TIDELOCKBrain oversight is required when:

- `content_type == code`
- `content_type == execution_request`
- Packet references a git repository, branch, merge, or commit
- Packet requests file creation, modification, or deletion
- Packet requests CI/CD operations
- Packet involves dependency updates or version changes

---

## H.3.5 Atlas/ORCS Audit Trigger Conditions

Atlas/ORCS audit is required when:

- Any `authority_scope` promotion is requested
- `canon_status` change is requested
- `deployment_status` change is requested
- Cross-vendor packet involves meaning promotion
- Ratification event is being logged

---

## H.3.6 Canon Boundary

This appendix is **NOT CANON**. The routing table becomes canon only after full council ratification + adjudication + website publication.

---

*End of APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md*
