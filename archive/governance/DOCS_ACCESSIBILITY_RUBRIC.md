---
artifact_id: A11Y-POLICY-DOCS-RUBRIC-001
title: Docs Accessibility Rubric
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, documentation, standards, a11y]
---

# Docs Accessibility Rubric

> Defines the accessibility standards all Atlas Lattice documentation must meet.

status: candidate

---

## Why Accessibility?

World-class open-source documentation is usable by everyone — including people using assistive technologies, people with cognitive differences, and people on constrained connections. Accessibility is not optional; it is a quality requirement.

---

## Accessibility Dimensions

### Dimension 1: Readability

| Criterion | Standard |
|-----------|---------|
| Reading level | Aim for Flesch-Kincaid Grade 8 or below for conceptual docs |
| Sentence length | Average ≤ 20 words per sentence |
| Paragraph length | ≤ 5 sentences per paragraph |
| Jargon | Define all technical terms on first use; link to GLOSSARY.md |
| Acronyms | Spell out on first use: "Knowledge Graph (KG)" |

---

### Dimension 2: Visual Accessibility

| Criterion | Standard |
|-----------|---------|
| Heading hierarchy | Must be sequential (H1 → H2 → H3); never skip levels |
| Color information | Never convey meaning by color alone; use text labels |
| Contrast (when rendered) | ≥ 4.5:1 for normal text; ≥ 3:1 for large text (WCAG AA) |
| Images | Every image must have descriptive alt text (see Alt Text Policy) |
| Tables | Every table must have a header row |

---

### Dimension 3: Navigation & Structure

| Criterion | Standard |
|-----------|---------|
| Document title | Every document must have exactly one H1 matching the frontmatter `title` |
| Section anchors | Major sections should have clear, unique heading text for deep linking |
| Table of contents | Required for documents longer than 500 lines |
| Cross-references | Link text must be descriptive ("see Glossary" not "click here") |

---

### Dimension 4: Format Accessibility

| Criterion | Standard |
|-----------|---------|
| Code blocks | Must include language hint (` ```python `, ` ```bash `, etc.) |
| Lists | Use unordered lists for unordered items; ordered lists only for sequential steps |
| Bold/italic | Bold for UI elements and key terms; italic for titles and emphasis only |
| Emoji | Acceptable for decoration; must not be the sole conveyor of information |

---

## Rubric Scoring

Documents are scored 0–3 on each dimension:

| Score | Meaning |
|-------|---------|
| 3 | Fully meets all criteria in the dimension |
| 2 | Meets most criteria; minor gaps |
| 1 | Significant gaps; needs work |
| 0 | Does not meet this dimension at all |

Minimum acceptable total score: **10/12** (at least 2 on every dimension).

---

## Audit Process

The annual accessibility audit (see ANNUAL_ACCESSIBILITY_AUDIT.md) applies this rubric to a sample of 10% of documents. Newly created documents are not audited until their first anniversary.

---

*Atlas Lattice Foundation · status: candidate*
