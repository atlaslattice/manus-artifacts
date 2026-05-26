# Appendix H.2 — O_AI Packet Schema v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md**
> **DATE: 2026-05-26**
> **MACHINE-READABLE: See schemas/o_ai/v0_1/o-ai-packet.schema.yaml**

---

## H.2.0 Purpose

This appendix defines the full field-level schema for O_AI packets. The machine-readable YAML schema lives at `schemas/o_ai/v0_1/o-ai-packet.schema.yaml`. This document is the human-readable specification.

---

## H.2.1 Full Schema Definition

```yaml
o_ai_packet:
  # ── Identity ───────────────────────────────────────────────
  packet_id:               # required: UUID or deterministic hash
  packet_version: "0.1"   # required: schema version
  source_surface: "O_AI"  # required: always O_AI for this schema
  timestamp:               # required: ISO 8601

  # ── Epistemic Status ────────────────────────────────────────
  raw_export_status:        # required: full_raw | partial_raw | summary_only | unavailable
  epistemic_label:          # required: working | candidate | reviewed | ratified
  authority_scope:          # required: none | local | council | ratified_canon
  canon_status: not_canon   # required: default not_canon; only changed by ratification_event
  deployment_status: not_deployable  # required: default not_deployable

  # ── Time Range ──────────────────────────────────────────────
  thread_time_range:
    start:                  # required: ISO 8601 or null
    end:                    # required: ISO 8601 or null
    timezone:               # required: IANA timezone string or UTC

  # ── Access Scope ────────────────────────────────────────────
  access_scope:             # required: object
    visible_sources: []     # required: list of sources the model could see
    unavailable_sources: [] # required: list of sources the model could NOT see (explicit!)
    assumed_context: []     # required: list of assumed/inferred context (explicit!)

  # ── Content ─────────────────────────────────────────────────
  content_type:             # required: synthesis | task_plan | code | data | execution_request
  content: {}              # required: the actual payload

  # ── Public Use ──────────────────────────────────────────────
  public_use_status:        # optional: internal_only | review_pending | source_complete
                            # NOTE: summary_only cannot support source_complete

  # ── Gates ───────────────────────────────────────────────────
  gates:                    # required
    provenance_gate:        # required: pending | pass | fail
    safety_gate:            # required: pending | pass | fail
    governance_gate:        # required: pending | pass | fail
    data_residency_gate:    # required: pending | pass | fail
    human_permission_gate:  # required if content_type == execution_request
    receipt_gate:           # required if content_type == execution_request

  # ── Routing ─────────────────────────────────────────────────
  routing:
    primary_lane:           # optional: lucerna | tidelock | hashlight | atlasbrain | rootglass
    tidelock_required:      # optional: true if repo/code execution involved
    atlas_orcs_audit:       # optional: true if meaning promotion is requested

  # ── Lineage ─────────────────────────────────────────────────
  parent_packet_id:         # optional: if derived from another packet
  source_refs: []           # optional: URLs, SHAs, or artifact IDs referenced
  sha256_if_available:      # optional: hash of raw export if available
```

---

## H.2.2 Field Constraints

### raw_export_status

| Value | Meaning | Public Use Constraint |
|-------|---------|----------------------|
| `full_raw` | Complete raw export available | Can support any public_use_status |
| `partial_raw` | Some turns missing or truncated | Cannot support `source_complete` |
| `summary_only` | No raw export; summary only | Cannot support `source_complete`; must carry caveat |
| `unavailable` | Export not possible or not attempted | Cannot support `source_complete` |

### authority_scope

| Value | Meaning |
|-------|---------|
| `none` | O_AI synthesis only; no governance authority |
| `local` | Valid within the current session context only |
| `council` | Reviewed by one or more council brains |
| `ratified_canon` | Explicit ratification event present (rare; requires event) |

### gates

All four base gates are required. If `content_type == execution_request`, `human_permission_gate` and `receipt_gate` are also required.

A gate may be `pending` in a draft packet, but an execution request cannot proceed unless both are `pass`.

---

## H.2.3 Validation Rules

1. `raw_export_status: summary_only` AND `public_use_status: source_complete` → **FAIL**
2. `content_type: execution_request` AND any required gate not `pass` → **FAIL**
3. Missing `raw_export_status` → **FAIL**
4. Missing `thread_time_range` → **FAIL**
5. Missing `access_scope` → **FAIL**
6. `canon_status` set to anything other than `not_canon` without a `ratification_event` reference → **FAIL**
7. `unavailable_sources` or `assumed_context` absent (even if empty lists) → **FAIL**

---

## H.2.4 Canon Boundary

This appendix is **NOT CANON**. The O_AI packet schema becomes canon only after full council ratification + adjudication + website publication.

---

*End of APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md*
