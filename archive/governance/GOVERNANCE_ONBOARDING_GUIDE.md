# Governance Onboarding Guide

*Atlas Lattice Foundation · Aetherforge Mission #12 · 2026-05-28*

status: candidate

> The fast-track path for new contributors and council members to understand how Atlas Lattice governance works, what the canon model means, and how to participate effectively.

---

## Welcome to the Atlas Lattice Council

Atlas Lattice is a world-class open-source knowledge graph — a public gift to all human knowledge. It runs on a governance model designed for **transparency, provenance, and trust**. This guide gets you operational in under 30 minutes.

---

## Step 1 — Understand the Canon Model (5 min)

All artifacts in this repository carry a `status` field:

| Status | Meaning |
|--------|---------|
| `candidate` | Proposed; may change; not yet ratified |
| `canon` | Ratified by full council + @atlaslattice adjudication |
| `deprecated` | Superseded; still readable, no longer updated |
| `archived` | Frozen historical record |

**Key rule:** Nothing is canon until adjudicated by **@atlaslattice**. You can contribute freely at candidate status.

Read: [Archive Boot — Canonical Status Model](../boot/gptbrain/GPTBRAIN_MANIFEST_2026-05-09.md)

---

## Step 2 — Learn the Section Map (5 min)

Every folder is owned by a role. Before contributing, know which section you're touching.

Read: [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md)

---

## Step 3 — Classify Your Change (5 min)

Every PR needs a classification label: `[SEC]`, `[GOV]`, `[SCHEMA]`, `[FEAT]`, `[DOCS]`, `[TEST]`, `[CI]`, or `[CHORE]`.

Read: [Change Classification Rules](./CHANGE_CLASSIFICATION_RULES.md)

---

## Step 4 — Know the SLAs (3 min)

Your PR will be reviewed within a defined window based on its class. Don't let PRs go stale — if no review comes in the SLA window, escalate to the section owner.

Read: [Review SLA Policy](./REVIEW_SLA_POLICY.md)

---

## Step 5 — Understand Council Cadence (3 min)

Reviews happen weekly (triage), monthly (wave review), and quarterly (full council session). Canon ratification only happens at quarterly sessions or via emergency escalation.

Read: [Council Review Cadence](./COUNCIL_REVIEW_CADENCE.md)

---

## Step 6 — Use the RFC Template (5 min)

For significant changes, open a formal RFC before writing code or drafting docs. This protects your effort by getting alignment early.

Read: [RFC Proposal Template](../boot/gptbrain/templates/) *(see templates folder)*

---

## Step 7 — Add Proper Frontmatter (3 min)

Every artifact must have a metadata header:

```markdown
---
artifact_id: ALF-YYYY-NNNNN
title: "Your Title"
status: candidate
created: YYYY-MM-DD
owner: your-github-username
tags: [relevant, tags]
---
```

Read: [Frontmatter Schema](../../schemas/)

---

## Common Mistakes to Avoid

| Mistake | Correct Action |
|---------|---------------|
| Marking your own artifact as `canon` | Only @atlaslattice ratifies canon |
| Deleting files without a deprecation PR | Follow the [Deprecation Policy](./DEPRECATION_POLICY.md) |
| Pushing directly to `main` | Always use a PR; main is protected |
| Missing classification label | Add `[CLASS]` prefix to PR title |
| Opening large PRs without prior RFC | Open RFC first for big changes |

---

## Quick Reference Links

- [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md)
- [Review SLA Policy](./REVIEW_SLA_POLICY.md)
- [Council Review Cadence](./COUNCIL_REVIEW_CADENCE.md)
- [Change Classification Rules](./CHANGE_CLASSIFICATION_RULES.md)
- [Deprecation Policy](./DEPRECATION_POLICY.md)
- [Next-144 Taskboard](../../projects/aetherforge-next144-taskboard-2026-05-28.md)
- [README](../../README.md)

---

## Questions?

Open a GitHub Discussion or ping the section owner listed in the [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md).

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
