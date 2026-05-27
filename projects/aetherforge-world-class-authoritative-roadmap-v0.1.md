# Aetherforge World-Class Authoritative Roadmap v0.1 (2026-05-27)

```text
STATUS: AUTHORITATIVE EXECUTION ROADMAP — CANDIDATE — NOT CANON
AUTHORITATIVE ROADMAP: true
SCOPE: repository execution sequencing for world-class Lattice/Aetherforge/GPTDream++ delivery
AUTHORITY: NONE
```

## Purpose

This is the single authoritative roadmap for sequencing world-class execution in this repository.

Historical boards are preserved for lineage and context, but execution priority and sequencing decisions should resolve here first.

## Historical boards (preserved, not deleted)

- `projects/aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md` (historical source board)

## World-class measurable targets by domain

| Domain | Target | Measure | Cadence |
|---|---|---|---|
| Quality | 100% pass on lattice quality gates for scoped changes | Workflow + validator pass/fail | Per PR |
| Retrieval | 100% deterministic lookup on required graph artifacts | Retrieval checks in validator | Per PR |
| Governance | 100% candidate boundary integrity until explicit ratification | Candidate boundary checks and receipts | Per PR |
| Usability | Contributor can complete first compliant change from docs only | Start-here + glossary + cookbook completeness | Weekly |
| Velocity | Ship one bounded, validated quest-loop increment per cycle | Weekly state-of-graph report | Weekly |

## High-impact maturity lift focus (M0/M1 -> M2+)

1. Graph index integrity and freshness.
2. Retrieval reliability for required artifacts.
3. Evidence quality and receipt completeness.

## Non-negotiable artifact contract fields

Every candidate artifact record must carry:

- stable `artifact_id`
- provenance class (`claim_class`)
- lifecycle state (`lifecycle_state`)
- contradiction links (`contradiction_links`)
- supersedes links (`supersedes_links`)
- test receipts (`tests_required`, `tests_run`)
- blockers and `next_safest_action`

## Next 10 sprint tasks (authoritative)

- [ ] AX-01: Mark this roadmap as the single execution authority and align navigation links.
- [ ] AX-02: Publish contributor start-here guidance with acceptance gates and receipts.
- [ ] AX-03: Publish glossary of graph/mission terms for consistent vocabulary.
- [ ] AX-04: Publish query cookbook for deterministic lookup by `artifact_id`, path, and filters.
- [ ] AX-05: Publish weekly public state-of-graph report with risks and next wave.
- [ ] AX-06: Extend validator checks for artifact lifecycle and relationship contract fields.
- [ ] AX-07: Extend fixture contract record to include lifecycle + supersedes fields.
- [ ] AX-08: Add tests covering roadmap authority and contributor UX surfaces.
- [ ] AX-09: Expand CI gate to execute execution-surface tests with lattice checks.
- [ ] AX-10: Rebuild index and validate all lattice gates after contract hardening.

## Quest-loop receipt standard (required every increment)

1. Bounded scope
2. Validation command + result
3. Blockers
4. Next safest action

## Definition of done for this roadmap loop

Execution is unambiguous, world-class targets are measurable, contract checks are enforced in CI, and contributor onboarding surfaces are present and linked.
