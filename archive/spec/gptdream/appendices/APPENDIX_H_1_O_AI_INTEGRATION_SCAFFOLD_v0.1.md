# Appendix H.1 — O_AI Integration Scaffold v0.1

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.1
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md
```

---

## H.1.0 Purpose

This appendix defines the integration scaffold for routing OpenAI-style task packets (`O_AI` packets) into the GPTDream++ / Atlas / ORCS governance pipeline.

The scaffold provides:
- Ingestion interface
- Validation hooks
- Atlas audit state binding
- Execution gate wiring

## H.1.1 O_AI packet lifecycle

```text
1. RECEIVE    — ingest raw O_AI packet
2. VALIDATE   — check required fields (see H.2)
3. LABEL      — assign epistemic_label and authority_scope
4. AUDIT      — emit atlas-audit-event
5. GATE       — check gates (provenance, safety, governance, human permission, receipt)
6. ROUTE      — route to appropriate brain lane (see H.3)
7. EXECUTE    — only if all gates pass AND human permission confirmed
8. RECORD     — emit receipt and update Atlas state
```

## H.1.2 Validation interface

```python
def validate_o_ai_packet(packet: dict) -> ValidationResult:
    """
    Validates an O_AI packet against required field schema.
    Returns ValidationResult with status, errors, and warnings.
    Required fields: raw_export_status, thread_time_range, access_scope,
                     epistemic_label, authority_scope, gates
    """
```

## H.1.3 Atlas audit binding

Every O_AI packet ingestion MUST emit an `atlas-audit-event`:

```yaml
atlas_audit_event:
  event_type: o_ai_packet_ingested
  packet_id: <packet id>
  epistemic_label: <label>
  authority_scope: <scope>
  raw_export_status: <status>
  gates_status:
    provenance_gate: pass | fail | hold
    safety_gate: pass | fail | hold
    governance_gate: pass | fail | hold
    data_residency_gate: pass | fail | hold
  execution_permitted: true | false
  tidelock_required: true | false
  timestamp: <ISO 8601>
```

## H.1.4 Execution gate wiring

```text
O_AI execution request
→ validate packet
→ D-Φ-1 check (receipt present?)
→ CAS-001-A check (safety pass?)
→ human permission check
→ Atlas / ORCS audit state update
→ if repo/merge/code: TIDELOCKBrain routing
→ execute or reject with reason
```

## H.1.5 Failure modes

```text
MISSING_REQUIRED_FIELD    — reject; emit atlas-failure-event
GATES_NOT_PASSED          — hold; emit audit-event; require human review
EXECUTION_WITHOUT_RECEIPT — reject; log attempted bypass
SUMMARY_ONLY_OVERCLAIM    — reject; emit laundering-warning
UNAUTHORIZED_RATIFICATION — reject; quarantine; emit alert
```

---

```text
NOT CANON. NOT DEPLOYABLE.
```
