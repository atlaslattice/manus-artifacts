---
artifact_id: A11Y-POLICY-MOBILE-READABILITY-001
title: Mobile Readability Validation Policy
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, mobile, readability, a11y]
---

# Mobile Readability Validation Policy

> Defines standards for ensuring Atlas Lattice documentation is readable on mobile devices and small screens.

status: candidate

---

## Why Mobile?

GitHub is accessed on mobile devices worldwide. Knowledge that only renders well on large desktop screens is less accessible. Mobile readability is a quality gate.

---

## Mobile Readability Rules

### 1. Table Width

Long tables break on mobile. For tables wider than ~5 columns:
- Consider splitting into multiple smaller tables
- Or convert to a definition list or nested bullets
- Or use a scrollable wrapper (`<div style="overflow-x: auto">`) when HTML is appropriate

---

### 2. Code Block Width

Code blocks must not require horizontal scrolling to read the essential content:
- Maximum line length in code blocks: **80 characters** for commands/scripts
- For longer lines: break with `\` continuation or refactor the example

---

### 3. Image Dimensions

Images embedded in docs should:
- Not exceed 800px native width (GitHub scales them, but excessively wide images degrade quality)
- Have a meaningful aspect ratio (avoid very tall/narrow or very wide/short images)

---

### 4. Link Tap Targets

Markdown links render as inline text on mobile. Ensure:
- Link text is long enough to be tappable (≥ 4 words is a good heuristic)
- Don't cluster multiple links in a single sentence without whitespace

---

### 5. Heading Nesting

Deep heading nesting (H4, H5, H6) is hard to navigate on mobile, where there is no sidebar table-of-contents. For documents longer than 200 lines:
- Keep primary structure to H2 and H3
- Use H4 only for very small subsections
- H5 and H6 should be avoided

---

## Validation Method

Mobile readability is validated informally during the annual accessibility audit by viewing a sample of documents in the GitHub mobile app (iOS or Android) and noting any rendering issues.

A checklist for mobile review:
- [ ] No horizontal scrolling on main content
- [ ] All code blocks readable without scrolling (or reasonably abbreviated)
- [ ] Tables readable (or marked as wide-table with overflow wrapper)
- [ ] Images visible and proportional
- [ ] All links are tappable with normal-sized text

---

*Atlas Lattice Foundation · status: candidate*
