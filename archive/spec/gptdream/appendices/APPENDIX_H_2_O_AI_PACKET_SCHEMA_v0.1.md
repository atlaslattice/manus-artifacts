# Appendix H.2 — O_AI Packet Schema v0.1

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.1
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md
MACHINE_READABLE: schemas/o_ai/v0_1/o-ai-packet.schema.yaml
```

---

## H.2.0 Purpose

This appendix defines the canonical field schema for O_AI packets (OpenAI-style task packets entering the GPTDream++ governance pipeline).

## H.2.1 Required fields

All O_AI packets MUST include:

```yaml
raw_export_status:     # full_raw | partial_raw | summary_only | unavailable
thread_time_range:     # start/end/timezone
  start: <ISO 8601>
  end: <ISO 8601>
  timezone: <tz string>
access_scope:          # what was visible / what was not
  visible_sources: []
  unavailable_sources: []
  assumed_context: []
epistemic_label:       # confidence and completeness label
authority_scope:       # what authority this packet claims (must be explicit)
gates:                 # all four gates required
  provenance_gate:     # pass | fail | hold
  safety_gate:         # pass | fail | hold
  governance_gate:     # pass | fail | hold
  data_residency_gate: # pass | fail | hold
```

## H.2.2 Optional fields

```yaml
packet_id:             # stable identifier
source_vendor:         # vendor surface
source_seat:           # originating agent seat
summary_text:          # human-readable summary
raw_content_ref:       # reference to raw export if available
sha256_if_available:   # content hash
public_use_status:     # source_complete | summary_only | not_for_public
canon_status:          # not_canon (default)
deployment_status:     # not_deployable (default)
strongest_safe_claim:  # most defensible claim given available evidence
caveats:               # explicit limitations
```

## H.2.3 Constraint rules

```text
C-1. summary_only CANNOT have public_use_status: source_complete
C-2. execution_request requires ALL gates to pass
C-3. execution_request requires human permission field = confirmed
C-4. execution_request requires receipt_id to be present
C-5. unavailable_sources must be explicit (not null/omitted)
C-6. assumed_context must be explicit (not null/omitted)
C-7. canon_status defaults to not_canon
C-8. deployment_status defaults to not_deployable
C-9. No packet can self-ratify
```

## H.2.4 Machine-readable schema

See `schemas/o_ai/v0_1/o-ai-packet.schema.yaml`.

---

```text
NOT CANON. NOT DEPLOYABLE.
```
