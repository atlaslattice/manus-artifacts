---
title: Fork Synthesis Policy
artifact_id: GOVERNANCE-FORK-POLICY-2026-05-29
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-29
provenance: Created from 7-pillar world-class execution plan (2026-05-29). Defines policy for selectively forking GitHub repos to synthesize missing lattice components.
---

# Fork Synthesis Policy

## Purpose

Define when and how Atlas Lattice may fork external GitHub repositories to incorporate missing components into the lattice. Forking is a powerful synthesis tool — used selectively and with full governance discipline.

---

## Core Principle

> Fork only when it **reduces time-to-capability** and does **not** weaken governance, auditability, or provenance integrity.

Forks are a synthesis tool — not a shortcut that bypasses governance.

---

## Decision Criteria (All Must Be Met)

Before forking any external repository, all of the following must be satisfied:

| # | Criterion | Required? |
|---|-----------|-----------|
| 1 | **License compatibility** — upstream license is compatible with MIT (Apache 2.0, MIT, BSD, CC0, etc.) | ✅ Mandatory |
| 2 | **Gap fills a specific lattice node** — a documented H-S-N coordinate or KG node is missing this capability | ✅ Mandatory |
| 3 | **Upstream is maintained / not abandoned** — last commit ≤12 months ago OR maintainer has declared it stable | ✅ Mandatory |
| 4 | **Security review passed** — no known CVEs or supply chain risks in the repo | ✅ Mandatory |
| 5 | **Adaptation plan documented** — what will be changed from upstream, and why | ✅ Mandatory |
| 6 | **@atlaslattice approval** — explicit direction from human root authority | ✅ Mandatory |
| 7 | **Provenance doc created** — `archive/forks/<repo-name>/PROVENANCE.md` committed | ✅ Mandatory |

---

## Prohibited Patterns

- ❌ Copy-pasting upstream code without attribution or provenance
- ❌ Forking to circumvent quality gates or canon review
- ❌ Importing forks as canonical without ratification
- ❌ Forking non-open-source repositories
- ❌ Forking under a different license without legal review

---

## Preferred Integration Method

In order of preference:

1. **Git subtree / submodule** with pinned version — best traceability, easiest upstream sync
2. **Vendored copy in `archive/forks/<name>/`** with version pin and provenance doc
3. **Package dependency** (pip, npm, etc.) with pinned version in `requirements.txt` / `package.json`

Avoid: uncontrolled copy-paste without version tracking.

---

## Required Provenance Document

Every fork must have `archive/forks/<repo-name>/PROVENANCE.md` with:

```yaml
---
title: Fork Provenance — <repo-name>
artifact_id: FORK-<REPO-NAME>-<YYYY-MM-DD>
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: YYYY-MM-DD
provenance: Fork of <upstream-url> under <license>
---
```

And the following required sections:

```markdown
## Upstream Source
- URL: https://github.com/<org>/<repo>
- Commit/Tag: <pinned version>
- License: <license name>
- Accessed: YYYY-MM-DD

## Gap Filled
- Lattice Node: H##-S##-N## (or domain description)
- Problem Statement: <what capability was missing>

## License Compatibility
- Upstream: <license>
- This repo: MIT
- Compatible: Yes/No — <rationale>

## Security Review
- Date: YYYY-MM-DD
- Reviewer: <identity>
- Findings: <none / list of issues>
- Resolution: <n/a / what was done>

## Adaptation Plan
- What is changed from upstream: <description>
- What is kept verbatim: <description>
- Future sync strategy: <manual / automated PR / pinned and frozen>

## Approval
- Approved by: @atlaslattice
- Date: YYYY-MM-DD
- Ratification event: <pending / event ID>
```

---

## Integration into KG

After a fork is incorporated:

1. Add the fork node to `archive/knowledge_graph/lattice_kg/v0_6/` with the appropriate H-S-N coordinate
2. Update [KG Coverage Dashboard](../../docs/KG_COVERAGE_DASHBOARD.md) — mark the gap as addressed
3. Add cross-link from the KG node to `archive/forks/<repo-name>/PROVENANCE.md`
4. Update [Archive Index](../../docs/ARCHIVE_INDEX.md)

---

## Current Fork Inventory

| Fork | Upstream | License | Gap Filled | Status |
|------|----------|---------|-----------|--------|
| dragonseek-os | TBD | TBD | TBD | Provenance pending |

*See `archive/forks/` for all current forks.*

---

## Cross-References

- [Canon Surface Map](../../docs/CANON_SURFACE_MAP.md)
- [KG Coverage Dashboard](../../docs/KG_COVERAGE_DASHBOARD.md)
- [Contribution Playbooks — PB-04](../../docs/CONTRIBUTION_PLAYBOOKS.md#pb-04-propose-a-fork-synthesis)
- [Ratification Workflow](../../docs/RATIFICATION_WORKFLOW.md)

---

*Last updated: 2026-05-29 · Status: Candidate · License: MIT*
