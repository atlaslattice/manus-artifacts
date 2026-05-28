# Change Classification Rules

*Atlas Lattice Foundation · Aetherforge Mission #8 · 2026-05-28*

status: candidate

> Defines how proposed changes to Atlas Lattice artifacts are classified, determining the required review path, SLA tier, and canon-impact level.

---

## Classification Matrix

| Class | Label | Description | SLA Tier | Canon Impact |
|-------|-------|-------------|----------|--------------|
| **SEC** | `security` | Security fixes, CVE patches, secret remediation | Tier 1 | High |
| **GOV** | `governance` | Policy, ratification, RFC, ownership changes | Tier 2 | High |
| **SCHEMA** | `schema-change` | Schema additions, removals, or breaking field changes | Tier 2 | High |
| **SPEC** | `spec-change` | Spec vault additions or amendments | Tier 2 | Medium |
| **FEAT** | `feature` | New functional artifact, script, or capability | Tier 3 | Medium |
| **DOCS** | `documentation` | Documentation additions or revisions | Tier 3 | Low |
| **TEST** | `tests` | Test additions, fixes, or reorganization | Tier 3 | Low |
| **CI** | `ci-cd` | Workflow, automation, Dependabot changes | Tier 3 | Low |
| **CHORE** | `chore` | Typos, formatting, housekeeping | Tier 4 | None |

---

## Classification Rules

### Rule 1 — Single Dominant Class

Assign the **highest-impact class** that applies. A PR touching both a schema and documentation is classified as **SCHEMA**, not **DOCS**.

### Rule 2 — Breaking vs Non-Breaking

Any change labeled `schema-change` or `spec-change` must additionally carry:
- `breaking` — if existing consumers or validators would fail
- `non-breaking` — if purely additive or backward-compatible

### Rule 3 — Canon-Touching Changes

Any change that alters the `status` field of an artifact from `candidate` to `canon` (or vice versa) must include the `ratification` label and requires **@atlaslattice** approval.

### Rule 4 — Automated Detection

CI workflows should auto-suggest classification labels based on file paths changed:
- Changes under `schemas/` → suggest `schema-change`
- Changes under `.github/` → suggest `ci-cd`
- Changes under `archive/governance/` or `council/` → suggest `governance`
- Changes to `SECURITY.md` or `CODEOWNERS` → suggest `security`

Label suggestions are informational; the PR author confirms the final classification.

---

## Classification in Practice

**Pull Request Title Format:**

```
[CLASS] Short description of change
```

Examples:
- `[SCHEMA] Add artifact_id field to frontmatter schema`
- `[GOV] Publish deprecation policy`
- `[DOCS] Expand glossary with KG terms`
- `[SEC] Rotate expired token reference in CI`

---

## Escalation for Unclassified PRs

PRs open for more than 48 hours without a classification label will be automatically flagged with `needs-triage`. The section owner (see [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md)) is responsible for applying the correct label.

---

## Related Documents

- [Review SLA Policy](./REVIEW_SLA_POLICY.md)
- [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md)
- [Deprecation Policy](./DEPRECATION_POLICY.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
