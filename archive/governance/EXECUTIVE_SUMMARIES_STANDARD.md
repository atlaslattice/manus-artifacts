---
artifact_id: GOV-EXEC-SUMMARY-STANDARD-001
title: Executive Summaries Standard
status: candidate
created: 2026-05-28
owner: council
tags: [documentation, quality, standards, executive-summary]
---

# Executive Summaries Standard

> Defines when and how executive summaries must appear in core governance and specification documents.

status: candidate

---

## Purpose

Long governance, legal, and specification documents require executive summaries so that busy reviewers, council members, and onboarding contributors can rapidly orient themselves. This standard mandates the format, placement, and required content of executive summaries across the archive.

---

## Applicability

An executive summary is **required** in all documents meeting any of the following:

| Condition | Threshold |
|-----------|-----------|
| Document length | ≥ 400 lines or ≥ 3,000 words |
| Governance scope | Policy, compliance, legal, trust, or ratification |
| Audience breadth | Addressed to external, council, or cross-team audiences |
| Review gate | Documents submitted for council ratification |

Executive summaries are **optional but encouraged** in:
- Architectural design records (ADRs)
- Wave execution reports
- Knowledge graph schemas

Executive summaries are **not required** in:
- Glossaries, indexes, and checklists (no prose body)
- Work logs and dream journals
- Small configuration or template files

---

## Format Template

Place the executive summary immediately after the YAML frontmatter, before any table of contents or section headers.

```markdown
## Executive Summary

**Purpose:** One sentence explaining what this document does.

**Audience:** Who this is for (e.g., Council, Contributors, External Reviewers).

**Status:** `candidate | ratified | deprecated`

**Key Decisions:**
- Decision 1
- Decision 2
- Decision 3

**Action Required:** What the reader must do after reading this document (or "None — reference only").

**Related Artifacts:**
- [Artifact Name](../path/to/artifact.md)
```

---

## Content Requirements

### Purpose (required)
Single sentence. Answer: "What does this document establish or define?"

### Audience (required)
Name the primary audience. Examples: "Council and ratification reviewers", "All contributors", "Engineering team", "External compliance auditors".

### Status (required)
Must match the document's frontmatter `status` field. Use `candidate`, `ratified`, or `deprecated`.

### Key Decisions (required if applicable)
Bullet list of the 2–5 most important things a reader needs to know. Omit if the document is purely procedural with no decisions.

### Action Required (required)
Tell the reader what to do: review and ratify, complete the checklist, escalate if X condition is met, etc. "None — reference only" is acceptable for reference docs.

### Related Artifacts (required if applicable)
Link to 1–5 most closely related documents. Omit only if the document is entirely self-contained.

---

## Retrofit Schedule

Governance and legal documents created before this standard was adopted should be retrofitted on the following schedule:

| Wave | Documents | Target Date |
|------|-----------|-------------|
| Wave 2 (Legal/Trust) | 12 documents | Q3 2026 |
| Wave 1 (Governance) | 12 documents | Q3 2026 |
| Wave 3 (Architecture) | 9 documents | Q4 2026 |
| All others | As needed | Rolling |

---

## Quality Gate

CI lint checks (`scripts/check_docs_layout_structure.py`) will flag documents ≥ 3,000 words that lack an `## Executive Summary` section.

---

## Governance

| Role | Responsibility |
|------|---------------|
| Document author | Add executive summary at creation time |
| Section owner | Verify summary is accurate before ratification |
| @atlaslattice | Ratify departures from this standard |

---

*Atlas Lattice Foundation · status: candidate*
