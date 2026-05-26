# Appendix I.3 — Atlas/ORCS Schema Bundle v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md**
> **DATE: 2026-05-26**
> **MACHINE-READABLE: See schemas/atlas_orcs/v0_1/**

---

## I.3.0 Purpose

This appendix is the index and human-readable description of the Atlas/ORCS schema bundle. The machine-readable YAML schemas live at `schemas/atlas_orcs/v0_1/`.

---

## I.3.1 Schema Index

| Schema File | Description |
|------------|-------------|
| `atlas-artifact.schema.yaml` | Core artifact record with trust state |
| `atlas-provenance-receipt.schema.yaml` | Receipt proving an artifact was filed |
| `atlas-claim.schema.yaml` | Individual epistemic claim |
| `atlas-claim-relationship.schema.yaml` | Relationship between two claims |
| `atlas-contradiction-ledger.schema.yaml` | Log of detected contradictions |
| `atlas-uncertainty-ledger.schema.yaml` | Log of unresolved uncertainties |
| `atlas-summary-lineage.schema.yaml` | Lineage record for summary artifacts |
| `atlas-intent-provenance.schema.yaml` | Provenance of inferred intent |
| `atlas-trust-state.schema.yaml` | Point-in-time trust state snapshot |
| `atlas-ratification-event.schema.yaml` | Explicit ratification event record |
| `atlas-failure-event.schema.yaml` | Failure mode event record |
| `atlas-governance-profile.schema.yaml` | Governance configuration profile |
| `atlas-domain-module.schema.yaml` | Domain-specific governance module |
| `atlas-quarantine-rule.schema.yaml` | Rule triggering quarantine |
| `atlas-audit-event.schema.yaml` | Audit log event |

---

## I.3.2 Universal Schema Invariants

All schemas in this bundle observe the following invariants:

1. `schema_version: "0.1"` — present on every schema object
2. `canon_status` defaults to `not_canon` where present
3. `deployment_status` defaults to `not_deployable` where present
4. No object can self-ratify (enforced by `ratifier_id ≠ artifact.author_id`)
5. Summary objects carry `summary_of` references; they do not inherit source authority
6. Receipts carry `receipt_of` references; they do not constitute proof

---

## I.3.3 Key Relationship Rules

```
artifact ──(has_receipt)──▶ provenance_receipt
          ──(contains)───▶ claim
          ──(has_state)──▶ trust_state
          ──(events)─────▶ [ratification_event | failure_event | audit_event]

claim ──(related_to)──▶ claim_relationship

summary_artifact ──(lineage)──▶ summary_lineage
                 ──(NOT_equal_to)──▶ source_artifact

contradiction_ledger ──(records)──▶ [claim_a, claim_b, contradiction_type]
                     ──(NOT_resolves)──▶ [claim_a | claim_b]
```

---

## I.3.4 Canon Boundary

This appendix is **NOT CANON**. The schema bundle becomes canon only after full council ratification + @atlaslattice adjudication + website publication.

---

*End of APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md*
