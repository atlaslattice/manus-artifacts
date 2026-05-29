---
artifact_id: ARTIFACT-ARCHIVE-SPEC-GPTDREAM-APPENDICES-APPENDIX-H-CROSS-VENDOR-INTEROP-MODEL-V0-1-MD-2026-05-29
title: STATUS: CANDIDATE WORKING SPEC — NOT CANON
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix H — Cross-Vendor Interop Model v0.1

## Appendix H — Cross-Vendor Interop Model

```text
TYPE: cross-vendor interop model
STATUS: candidate working specification
CANON: no
```

### H.0 — Purpose

GPTDream++ operates across multiple model providers.

This appendix defines the interop layer: how a habitat-conformant agent communicates work packets, routing decisions, and status to and from agents running on other providers (OpenAI, Anthropic, Google, etc.).

### H.1 — O_AI Scaffold

The O_AI scaffold is the OpenAI-side task surface for cross-vendor GPTDream++ coordination.

```text
O_AI scaffold purpose:
  Accept incoming work packets from vendor-neutral coordinator
  Route tasks to appropriate model thread
  Return outputs with canonical runtime labels
  Preserve receipt lineage across provider boundary
```

O_AI scaffold minimum interface:

```yaml
o_ai_task_surface:
  accept_packet: true
  packet_schema_version: "1.0"
  runtime_label_required: true
  canon_status_required: true
  receipt_required: true
  human_root_flag_passthrough: true
```

O_AI scaffold invariants:

```text
1. O_AI scaffold accepts packets; it does not generate canon.
2. O_AI outputs must carry runtime label from originating scaffold.
3. O_AI scaffold does not resolve cross-vendor authority conflicts unilaterally.
4. Receipt lineage must be preserved through all scaffold hops.
```

### H.2 — Packet Schema

Cross-vendor work packets use a vendor-neutral schema:

```yaml
gptdream_packet:
  version: "1.0"
  packet_id: <uuid>
  source_agent:
    seat: <seat identifier>
    provider: <openai | anthropic | google | other>
    session_label: <runtime label>
  destination_agent:
    seat: <seat identifier>
    provider: <openai | anthropic | google | other>
  payload:
    task_type: <work | dream | play | review | route>
    artifact_refs:
      - <repo path or receipt id>
    instructions: <plain text>
    human_root_required: <true | false>
  canon_status: <not_canon | candidate | ratified>
  timestamp: <ISO 8601>
  receipt_chain:
    - <prior receipt id>
```

Packet schema invariants:

```text
1. canon_status must be explicitly set; default is not_canon.
2. human_root_required must not be silently set to false.
3. receipt_chain must include all prior hops; do not truncate.
4. destination_agent seat must be confirmed before routing.
```

### H.3 — Routing Table

Cross-vendor routing table (candidate):

```text
Task type              → Preferred provider surface
─────────────────────────────────────────────────────
Long-form synthesis    → GPT-4-class / Claude-opus-class
Code generation        → Codex / Claude-sonnet-class / Gemini-pro-class
Document retrieval     → Tool-augmented surface
Schema validation      → Deterministic tool surface
Canon ratification     → Human-root only (no model surface)
Dream / play output    → Any surface; label DREAM / PLAY
Security review        → Human-root required before any action
```

Routing table update rule:

```text
This table is a candidate. It must not be used as an authority routing table
without human-root review. Provider capabilities change; routing rules must
be re-verified against current provider documentation before deployment.
```

---
