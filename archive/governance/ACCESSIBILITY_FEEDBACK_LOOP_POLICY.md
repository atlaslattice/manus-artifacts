---
artifact_id: A11Y-POLICY-ACCESSIBILITY-FEEDBACK-001
title: Accessibility Feedback Loop Policy
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, feedback, community, a11y, continuous-improvement]
---

# Accessibility Feedback Loop Policy

> Defines how Atlas Lattice receives and acts on accessibility feedback from contributors and users.

status: candidate

---

## Why a Feedback Loop?

An audit measures what we can see. A feedback loop captures what we miss — the lived experience of contributors using assistive technologies, working in non-English locales, or accessing the repository from constrained environments.

---

## How to Report an Accessibility Issue

Contributors experiencing or observing accessibility problems can:

1. **Open a GitHub issue** with the label `accessibility` and describe:
   - Document or page affected
   - What is inaccessible (and for whom, if known)
   - Suggested improvement (optional)

2. **Submit a PR** directly fixing the issue (preferred for small fixes like missing alt text)

3. **Post in Discussions** for systemic feedback or questions about the accessibility policy

---

## Accessibility Issue Labels

| Label | Use |
|-------|-----|
| `accessibility` | General accessibility issues |
| `a11y-alt-text` | Missing or inadequate image alt text |
| `a11y-language` | Inclusive language violations |
| `a11y-readability` | Readability/plain language issues |
| `a11y-mobile` | Mobile rendering issues |
| `a11y-low-bandwidth` | Content size / bandwidth issues |
| `translation-needed` | Translation gap identified |

---

## Response SLAs for Accessibility Issues

| Severity | Definition | Response SLA |
|---------|-----------|-------------|
| Critical | Content is completely inaccessible to a population of users | 7 days |
| High | Significant barrier; workaround exists | 30 days |
| Medium | Minor barrier; not blocking | 90 days |
| Low | Enhancement; cosmetic | Next wave sprint |

---

## Annual Review of Feedback

Accessibility issues received during the year are reviewed during the annual accessibility audit. Patterns in feedback are used to:
- Update the Docs Accessibility Rubric
- Identify areas needing systemic work
- Prioritize translation efforts

---

*Atlas Lattice Foundation · status: candidate*
