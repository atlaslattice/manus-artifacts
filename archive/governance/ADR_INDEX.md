---
artifact_id: DX-POLICY-ADR-INDEX-001
title: Architecture Decision Record Index
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, architecture, adr, documentation, decisions]
---

# Architecture Decision Record Index

> Index of Architecture Decision Records (ADRs) for the Atlas Lattice project, capturing key design decisions and their rationale.

status: candidate

---

## What Is an ADR?

An **Architecture Decision Record (ADR)** is a document that captures an important architectural or design decision, the context in which it was made, the decision itself, and the consequences. ADRs are immutable — once recorded, they are never edited. Superseded ADRs are marked as such.

ADR format follows [Michael Nygard's template](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

---

## ADR Directory

ADRs are stored at: `archive/governance/decisions/ADR-NNNN-title.md`

---

## ADR Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| ADR-0001 | Use GitHub as canonical substrate | Accepted | 2026-05-09 |
| ADR-0002 | Markdown as primary document format | Accepted | 2026-05-09 |
| ADR-0003 | YAML frontmatter for machine-readable metadata | Accepted | 2026-05-26 |
| ADR-0004 | JSON-LD for KG export format | Accepted | 2026-05-26 |
| ADR-0005 | All artifacts are candidate until ratified by @atlaslattice | Accepted | 2026-05-26 |
| ADR-0006 | archive/ for source artifacts; docs/ for user-facing content | Accepted | 2026-05-28 |
| ADR-0007 | SCREAMING_SNAKE_CASE for governance docs | Accepted | 2026-05-28 |
| ADR-0008 | Keep a Changelog for CHANGELOG.md format | Accepted | 2026-05-28 |

---

## ADR Template

New ADRs use this template in `archive/governance/decisions/ADR-NNNN-title.md`:

```markdown
# ADR-NNNN: [Title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXXX

---

## Context

[What is the situation? What forces are at play? Why does this decision need to be made?]

## Decision

[What was decided? State the decision clearly and unambiguously.]

## Consequences

**Positive:**
- [Benefit 1]

**Negative:**
- [Trade-off 1]

**Neutral:**
- [Neutral consequence]
```

---

## Adding a New ADR

1. Determine the next ADR number from this index
2. Create `archive/governance/decisions/ADR-NNNN-short-title.md`
3. Add an entry to this index
4. Open a PR for council review

---

*Atlas Lattice Foundation · status: candidate*
