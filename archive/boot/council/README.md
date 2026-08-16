# Archive / Boot / Council

```
STATUS:    INDEX — NOT CANON
PURPOSE:   Index for the council/ subtree — coordination packets and schemas
PROMOTION: No promotion; index only
```

> **Guardrail:** All artifacts here are candidate-level unless explicitly ratified by
> human-root approval.

---

## Contents

| File | Purpose |
|------|---------|
| `COUNCIL_WIDE_BOOT_PACKET_2026-05-09.md` | Council-wide boot packet (candidate) |
| `EVIDENCE_JUDGMENT_EXECUTION_PLANES_2026-05-09.md` | Evidence/judgment framework (candidate) |
| `schemas/` | Candidate YAML schema templates |

## Schemas Subdirectory

```
schemas/
  COUNCIL_PACKET_SCHEMA_2026-05-09.yaml
  ROUTE_TO_SEAT_PACKET_SCHEMA_2026-05-09.yaml
  CONTRADICTION_LEDGER_SCHEMA_2026-05-09.yaml
```

**Schema status:** These are descriptive YAML templates, not formal validation schemas.
They are machine-readable as YAML documents. A CI check parses them for valid YAML.

Proposed next step (S4 route): Add companion JSON Schema files for formal validation.

## Review Rules

- Route schema formal validation to S4 (GeminiBrain).
- Route canon-language wording to S2 (ClaudeBrain).
- Do not rewrite candidate artifacts into ratified canon.

## Coordination

Main issue: https://github.com/atlaslattice/manus-artifacts/issues/11
