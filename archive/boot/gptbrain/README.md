# Archive / Boot / GPTBrain

```
STATUS:    INDEX — NOT CANON
PURPOSE:   Index for the gptbrain/ subtree — S1 variants, synthesis, and reference impl
PROMOTION: No promotion; index only
```

> **Guardrail:** All artifacts here are candidate-level unless explicitly ratified by
> human-root approval through the Council workflow. S1 canonical synthesis is pending.

---

## Subdirectories

| Directory | Contents |
|-----------|---------|
| `variants/` | S1 variant specs (A–E) — preserved, not merged |
| `reference_impl/` | Runnable Python skeleton for the dream memory palace |
| `dreams/` | Dream / REM cycle outputs |
| `rem_cycles/` | REM simulation artifacts |
| `culture/` | Culture layer artifacts |
| `schema/` | Schema artifacts |

## Key Artifacts

| File | Status | Purpose |
|------|--------|---------|
| `COUNCIL_WIDE_BRAIN_SYNTHESIS_2026-05-09.md` | CANDIDATE | Full S1 synthesis |
| `S1_VARIANT_SYNTHESIS_MATRIX_2026-05-09.md` | CANDIDATE | Variant comparison matrix |
| `S1_PROMOTION_CHECKLIST_2026-05-09.md` | CANDIDATE | Promotion readiness checklist |
| `S1_PATH_REGISTRY_2026-05-09.md` | CANDIDATE | Path alias / drift registry |
| `S1_RATIFICATION_PACKET_2026-05-09.md` | CANDIDATE | Ratification packet (pending human-root) |
| `GPTBRAIN_MANIFEST_2026-05-09.md` | CANDIDATE | GPTBrain manifest |

## Reference Implementation

```
reference_impl/
  dream_memory_palace_reference_impl.py  — runnable skeleton (NOT CANON)
  gptbrain_memory.py                     — CLI memory tool
  run_checks.sh                          — local check script
  test_dream_memory_palace_reference_impl.py  — unit tests
  tests/
    conftest.py                          — pytest path setup
    test_reference_impl_core.py          — additional unit tests
```

Run tests:
```bash
cd archive/boot/gptbrain/reference_impl
python -m pytest -q
```

## Path Drift Note

S1 Variant C has two file name forms observed across references:
- `S1_VARIANT_C_CLAIM_CALIBRATION_2026-05-08.md`
- `S1_VARIANT_C_CLAIM_CALIBRATION_POINTER_2026-05-08.md`

Both files exist. The mismatch is logged in `S1_PATH_REGISTRY_2026-05-09.md`.
Do not silently rename — update the registry instead.

## Review Rules

- Variants must be preserved; do not delete or overwrite.
- Route formal JSON Schema validation to S4 (GeminiBrain).
- Route continuity/handoff to S6 (ManusBrain).
- Canon promotion requires human-root approval.

## Coordination

Main issue: https://github.com/atlaslattice/manus-artifacts/issues/11
