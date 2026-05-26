# Appendix I — Atlas / ORCS Epistemic Governance Profile v0.1

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

## I.0 Purpose

This appendix defines the epistemic governance profile for Atlas / ORCS — the system that tracks, routes, and audits artifact trust states within GPTDream++.

**Core rule:** Authority is a state transition, not a vibe.

## I.1 What Atlas does

```text
- Tracks artifact trust state (raw → ratified → active → ...)
- Records every state transition as an auditable event
- Prevents unauthorized promotion
- Preserves contradiction records
- Audits execution requests
- Routes governance decisions to human gate
```

## I.2 What ORCS does

```text
- Routes artifacts to correct lane/brain
- Enforces routing invariants
- Prevents cross-lane laundering
- Tags artifacts with route class and authority scope
- Emits routing receipts
```

## I.3 Trust state model

See `APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md` for formal definition.

Core states:
```text
raw → parsed → candidate → reviewed → ratified → active
                                                ↓
                                          under_review
                                          superseded
                                          revoked
                                          quarantined
                                          rejected
```

## I.4 Governance invariants

```text
G-1. Artifact cannot move to ratified without ratification_event.
G-2. Deployment status cannot change without governance_event.
G-3. Quarantined artifact preserves lineage.
G-4. Contradiction creates contradiction_record, not overwrite.
G-5. Summary cannot replace source.
G-6. Expired ratification moves artifact to under_review.
G-7. No artifact can self-ratify.
G-8. Authority is explicit, not implied.
G-9. All transitions are logged.
G-10. Human gate required for ratification.
```

## I.5 Compatible predicate

See `APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md`.

```text
compatible_Γ(edge) ∈ {TRUE, FALSE, HOLD}
compatible_path_Γ(path) = all edges TRUE AND NOT launder(path)
```

## I.6 Schema bundle

See `APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md` for machine-readable schemas.

## I.7 Adversarial test coverage

See `tests/adversarial/` for T01–T12 test coverage (Appendix I.10 tests).

## I.8 Public-safe translation

```text
Atlas      → artifact trust-state tracking engine
ORCS       → ontology-routed context spine (routing layer)
ratified   → explicitly promoted by council + human gate
canon      → ratified + published to website
quarantine → isolated pending review; lineage preserved
compatible → path does not launder authority
```

---

```text
NOT CANON. NOT DEPLOYABLE.
```
