# Appendix H.3 — O_AI Routing Table v0.1

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.1
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md
MACHINE_READABLE: schemas/o_ai/v0_1/o-ai-routing-table.yaml
```

---

## H.3.0 Purpose

This appendix defines how O_AI packets are routed to the correct brain lane after validation.

## H.3.1 Lane routing rules

| Packet type / content | Primary lane | Secondary lane | Gate required |
|---|---|---|---|
| ChatGPT synthesis | LucernaBrain | RootglassBrain | provenance |
| Codex / code patch | TIDELOCKBrain | HashlightBrain | provenance + safety |
| Raw export | HashlightBrain | AtlasBrain | provenance |
| Benchmark claim | AtlasBrain | LucernaBrain | provenance + governance |
| Public statement | LucernaBrain | governance review | all gates |
| Execution request | D-Φ-1 / CAS-001-A | Atlas/ORCS audit | all gates + human |
| Repo / merge / code execution | TIDELOCKBrain | D-Φ-1 gate | all gates + human |

## H.3.2 Execution routing (canonical)

```text
Execution request
→ D-Φ-1 / CAS-001-A / human gate
→ Atlas / ORCS audit state
→ TIDELOCKBrain if repo / merge-order / code execution is involved
```

This routing is non-negotiable. No execution request bypasses Atlas / ORCS audit state.

## H.3.3 TIDELOCK routing trigger

A packet is routed to TIDELOCKBrain if ANY of:
- `execution_type` contains `repo`, `merge`, `code`, `deploy`
- `authority_scope` claims write access to repository
- `gates.provenance_gate` involves a commit or PR
- `source_vendor` is `VENDOR_SURFACE_COPILOT`

## H.3.4 Fallback routing

If no lane match:
```text
→ HashlightBrain (triage)
→ emit atlas-audit-event with routing_decision: fallback
→ require human review before promotion
```

## H.3.5 Label assignment

After routing, assign lane label per Epic 8 label taxonomy:

```text
gptdream, atlas-orcs, o-ai, native-thread-ingestion,
schema, validator, compatible, anti-laundering,
dphi, cas-001-a, tidelock, hashlight, lucerna, rootglass,
atlasbrain, not-canon, not-deployable, needs-review
```

Every execution issue gets: `not-canon` + `not-deployable` until explicitly promoted.

---

```text
NOT CANON. NOT DEPLOYABLE.
```
