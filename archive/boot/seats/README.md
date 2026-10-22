# Archive / Boot / Seats

```
STATUS:    INDEX — NOT CANON
PURPOSE:   Index for the seats/ subtree — per-seat specs and credential files
PROMOTION: No promotion; index only
```

> **Guardrail:** All artifacts here are candidate-level unless explicitly ratified by
> human-root approval. Seat specs represent design proposals; no seat is finalized.

---

## Seat Inventory

| Seat | Brain | Spec File | Status |
|------|-------|-----------|--------|
| S1 | GPTBrain | `GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md` | CANDIDATE |
| S1 | GPTBrain | `GPTBRAIN_S1_DREAM_MEMORY_PALACE_SPEC_2026-05-09.md` | CANDIDATE |
| S1 | GPTBrain | `GPTBRAIN_S1_COGNITIVE_INFRASTRUCTURE_SPEC_2026-05-08.md` | CANDIDATE |
| S1 | GPTBrain | `GPTBRAIN_S1_COGNITIVE_INFRASTRUCTURE_MEMORY_PALACE_SPEC_2026-05-08.md` | CANDIDATE |
| S2 | ClaudeBrain | `CLAUDEBRAIN_S2_CONSTITUTIONAL_SCRIBE_SPEC_2026-05-08.md` | CANDIDATE |
| S3 | GrokBrain | `GROKBRAIN_S3_PERSISTENT_MEMORY_PALACE_SPEC_2026-05-08.md` | CANDIDATE |
| S4 | GeminiBrain | `GEMINIBRAIN_S4_ENGINEERING_SIMULATION_SPEC_2026-05-08.md` | CANDIDATE |
| S5 | DeepSeek | `DEEPSEEK_S5_BOOT_SEQUENCE_AND_BRAIN_SPEC_2026-05-08.md` | CANDIDATE |
| S6 | ManusBrain | `MANUSBRAIN_S6_EXECUTION_AGENT_SPEC_2026-05-08.md` | CANDIDATE |
| S7 | CopilotBrain | `COPILOTBRAIN_S7_CODE_INTEGRATOR_SPEC_2026-05-08.md` | CANDIDATE |

## Identity Credentials and Memory Packet Templates

Each seat has:
- `S{N}_IDENTITY_CREDENTIAL.md` — identity/boot credential
- `S{N}_MEMORY_PACKET_TEMPLATE.yaml` — memory packet template

## S7 Hygiene Artifacts (this pass)

| File | Purpose |
|------|---------|
| `S7_REPO_HYGIENE_REVIEW_2026-05-09.md` | S7 repo hygiene review note |
| `S7_EXECUTION_LOG_2026-05-09.md` | S7 execution log |

## Review Rules

- Seat specs route to S2 (ClaudeBrain) for canon-language review before promotion.
- No seat spec is final without human-root approval.
- All additions to this directory should carry STATUS/PURPOSE/PROMOTION headers.

## Coordination

Main issue: https://github.com/atlaslattice/manus-artifacts/issues/11
