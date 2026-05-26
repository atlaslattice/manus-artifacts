# AtlasBrain — Index

```text
STATUS: EVIDENCE-LANE INDEX — NOT CANON
DATE: 2026-05-26
PURPOSE: fast routing index for AtlasBrain evidence, benchmark, quarantine, and public-claim gates
```

## Root and doctrine

- `archive/boot/atlasbrain/README.md`

## Lane map

- `archive/boot/atlasbrain/raw_logs/README.md`
- `archive/boot/atlasbrain/evidence_packets/README.md`
- `archive/boot/atlasbrain/benchmarks/README.md`
- `archive/boot/atlasbrain/evaluator_reactions/README.md`
- `archive/boot/atlasbrain/learning_claims/README.md`
- `archive/boot/atlasbrain/public_claims/README.md`
- `archive/boot/atlasbrain/quarantine/README.md`
- `archive/boot/atlasbrain/schemas/ATLASBRAIN_EVIDENCE_PACKET_SCHEMA_v0.1.yaml`

## Gate + test surfaces

- Gate validator: `archive/boot/gptbrain/reference_impl/atlasbrain_gate.py`
- Gate tests: `archive/boot/gptbrain/reference_impl/test_atlasbrain_gate.py`
- Shared checks: `archive/boot/gptbrain/reference_impl/run_checks.sh`

## Current operating boundary

- Evidence can inform action.
- Evidence cannot self-authorize public claims or canon status.
- Human-root approval remains required for claim promotion.

