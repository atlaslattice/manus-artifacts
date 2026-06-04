# Appendix I.3 — Atlas / ORCS Schema Bundle v0.1

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.1
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md
MACHINE_READABLE: schemas/atlas_orcs/v0_1/
```

---

## I.3.0 Purpose

This appendix indexes the machine-readable Atlas / ORCS schema bundle. All schemas are in `schemas/atlas_orcs/v0_1/`.

## I.3.1 Schema index

| File | Purpose |
|---|---|
| `atlas-artifact.schema.yaml` | Core artifact record |
| `atlas-provenance-receipt.schema.yaml` | Verifiable event receipt |
| `atlas-claim.schema.yaml` | Epistemic claim record |
| `atlas-claim-relationship.schema.yaml` | Claim-to-claim relationship |
| `atlas-contradiction-ledger.schema.yaml` | Contradiction record (preserves both) |
| `atlas-uncertainty-ledger.schema.yaml` | Uncertainty and caveat ledger |
| `atlas-summary-lineage.schema.yaml` | Summary-to-source lineage |
| `atlas-intent-provenance.schema.yaml` | Intent and authorship provenance |
| `atlas-trust-state.schema.yaml` | Trust state snapshot |
| `atlas-ratification-event.schema.yaml` | Ratification event record |
| `atlas-failure-event.schema.yaml` | Failure and attack event record |
| `atlas-governance-profile.schema.yaml` | Governance context definition |
| `atlas-domain-module.schema.yaml` | Domain module definition |
| `atlas-quarantine-rule.schema.yaml` | Quarantine trigger rule |
| `atlas-audit-event.schema.yaml` | Audit trail event |

## I.3.2 Universal schema constraints

Every schema in this bundle:
- Has `schema_version: "0.1"`
- Defaults `canon_status` to `not_canon`
- Defaults `deployment_status` to `not_deployable`
- Does NOT allow self-ratification
- Parses as valid YAML

## I.3.3 Key inequalities (enforced by schema)

```text
summary ≠ source
receipt ≠ truth
ratification requires explicit ratification_event
```

## I.3.4 Test coverage

See `reference_impl/atlas_orcs/tests/` for:
- Tests proving summary ≠ source
- Tests proving receipt ≠ truth
- Tests proving ratification requires explicit event

---

```text
NOT CANON. NOT DEPLOYABLE.
```
