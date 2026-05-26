# Appendix H — Cross-Vendor Interop Model v0.1

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.1
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md
```

---

## H.0 Purpose

This appendix defines how GPTDream++ agents interoperate across AI vendors (OpenAI, Anthropic, Google, etc.) without collapsing epistemic provenance.

The core problem: different vendor outputs have different confidence profiles, export capabilities, and authority surfaces. A cross-vendor interop model must prevent laundering across these boundaries.

## H.1 Vendor surface taxonomy

```text
VENDOR_SURFACE_OPENAI     — ChatGPT / o-series / API; summary-only or partial raw
VENDOR_SURFACE_ANTHROPIC  — Claude; summary-only or partial raw
VENDOR_SURFACE_GOOGLE     — Gemini; summary-only or partial raw
VENDOR_SURFACE_COPILOT    — GitHub Copilot / coding agent; repo-native
VENDOR_SURFACE_MANUS      — Manus agent; task-oriented
VENDOR_SURFACE_HUMAN      — Direct human input; highest authority
VENDOR_SURFACE_UNKNOWN    — Must be treated as summary_only
```

## H.2 Interop invariants

```text
I-1. Every cross-vendor packet must declare its raw_export_status.
I-2. summary_only packets cannot claim source_complete fidelity.
I-3. Vendor surface must be explicit; unknown defaults to lowest trust tier.
I-4. Cross-vendor synthesis requires provenance receipt from each contributing surface.
I-5. No vendor output gains authority by crossing a boundary.
I-6. Execution requests from any vendor surface route through D-Φ-1 / CAS-001-A.
```

## H.3 O_AI packet integration

OpenAI-style task packets are the primary interop packet format. See:
- `APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md`
- `APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md`
- `APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md`

## H.4 Cross-vendor receipt model

When ingesting output from any vendor:

```yaml
cross_vendor_receipt:
  source_vendor: <vendor surface>
  raw_export_status: full_raw | partial_raw | summary_only | unavailable
  ingestion_timestamp: <ISO 8601>
  ingesting_seat: <seat name>
  provenance_verified: true | false
  laundering_check: passed | failed | hold
  atlas_audit_state: <audit state>
```

## H.5 Laundering boundary

A cross-vendor packet **launders** if:
- It claims higher authority than its source vendor surface permits
- It upgrades raw_export_status without verification
- It promotes a summary to source-complete status
- It bypasses Atlas / ORCS audit state

See `APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md` for formal predicate.

## H.6 Execution routing

```text
Execution request (any vendor surface)
→ D-Φ-1 / CAS-001-A / human gate
→ Atlas / ORCS audit state
→ TIDELOCKBrain if repo / merge-order / code execution is involved
```

---

```text
NOT CANON. NOT DEPLOYABLE.
```
