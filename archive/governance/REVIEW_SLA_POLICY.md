# Review SLA Policy

*Atlas Lattice Foundation · Aetherforge Mission #6 · 2026-05-28*

status: candidate

> Defines expected turnaround times for reviews across artifact types, ensuring the repository operates at world-class velocity without sacrificing quality.

---

## SLA Tiers

### Tier 1 — Critical / Security (24 hours)

Applies to:
- Security vulnerability disclosures
- SECURITY.md or CODEOWNERS changes
- Secret scanning or dependency alert patches
- Canon ratification emergency blocks

Response: Acknowledgment within **4 hours**, resolution target **24 hours**.

---

### Tier 2 — Governance & Spec (72 hours)

Applies to:
- RFC proposals
- Canon status changes
- Schema breaking changes (`schemas/`)
- Governance policy documents (`archive/governance/`)

Response: First review within **24 hours**, merge/close target **72 hours**.

---

### Tier 3 — Standard Contribution (5 business days)

Applies to:
- Documentation additions and edits (`docs/`, `archive/`)
- Test additions
- Reference implementation changes (`reference_impl/`)
- New taskboard tasks or project updates

Response: First review within **2 business days**, merge/close target **5 business days**.

---

### Tier 4 — Housekeeping (10 business days)

Applies to:
- Typo fixes and formatting corrections
- Comment updates
- Non-functional CI config tweaks
- Dependency version bumps (non-security)

Response: Batch-reviewed weekly; merge/close within **10 business days**.

---

## Escalation Path

If an SLA is missed:
1. PR author may ping the **Section Owner** (see [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md)).
2. If still unresolved, escalate to **Council Chair**.
3. Final escalation: **@atlaslattice** as ratification authority.

---

## SLA Clock Rules

- Clock starts when PR is marked **Ready for Review** (not draft).
- Clock pauses when PR is in **changes-requested** state awaiting author response.
- SLAs apply to working days (Mon–Fri, UTC); not weekends or declared maintenance windows.

---

## Monitoring

SLA compliance will be tracked in the quarterly legal/trust audit (Mission #24) and surfaced in the monthly quality report (Mission #95).

---

## Related Documents

- [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md)
- [Council Review Cadence](./COUNCIL_REVIEW_CADENCE.md)
- [Change Classification Rules](./CHANGE_CLASSIFICATION_RULES.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
