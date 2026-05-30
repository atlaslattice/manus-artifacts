---
artifact_id: GOV-READABILITY-QUALITY-THRESHOLDS-001
title: Readability Quality Thresholds
status: candidate
created: 2026-05-28
owner: council
tags: [documentation, readability, quality, accessibility]
---

# Readability Quality Thresholds

> Defines readability targets and measurement standards for all documentation in the Atlas Lattice repository.

status: candidate

---

## Rationale

World-class documentation must be accessible to its intended audience. Readability scores provide an objective baseline. This policy sets thresholds by document category and defines how violations are handled.

---

## Document Categories and Targets

### Category A: Public Onboarding Docs
**Location:** `docs/` (user-facing)
**Audience:** Any contributor or visitor, including non-native English speakers
**Target:** Flesch Reading Ease ≥ 50 (plain language, broadly accessible)
**Grade level:** ≤ Grade 12

**Examples:** NEWCOMER_FAQ.md, PROJECT_BRIEFS.md, GLOSSARY.md, TOP_ARTIFACTS.md

---

### Category B: Governance Policy Docs
**Location:** `archive/governance/`
**Audience:** Council members, contributors, legal reviewers
**Target:** Flesch Reading Ease ≥ 35 (professional but not academic)
**Grade level:** ≤ Grade 14

**Examples:** GOVERNANCE_ONBOARDING_GUIDE.md, REVIEW_SLA_POLICY.md, PII_REDACTION_RUBRIC.md

---

### Category C: Technical Specification Docs
**Location:** `archive/spec/`, `schemas/`, `reference_impl/`
**Audience:** Engineers and AI system integrators
**Target:** Flesch Reading Ease ≥ 20 (technical but not impenetrable)
**Grade level:** ≤ Grade 16

**Examples:** GPTDream++ appendices, Atlas/ORCS schema specifications

---

### Category D: Legal and Compliance Docs
**Location:** `archive/governance/` (legal subset)
**Audience:** Legal reviewers, compliance officers
**Target:** No Flesch minimum — legal precision takes priority over readability score
**Grade level:** No maximum — clarity and precision over simplicity

**Examples:** LICENSE_AUDIT_REPORT.md, EXPORT_CONTROL_SCREENING_CHECKLIST.md

---

### Category E: AI Dream/Memory Artifacts
**Location:** `archive/boot/gptbrain/TIDELOCKBrain/`
**Audience:** AI agents (future hydration)
**Target:** No Flesch minimum — structured data density preferred over prose readability

---

## Additional Readability Guidelines (All Categories)

### Sentence length
- Average sentence length ≤ 20 words
- No sentence exceeds 45 words without restructuring

### Paragraph density
- Average paragraph ≤ 5 sentences
- No paragraph exceeds 8 sentences

### Active voice
- ≥ 70% active voice sentences in Category A and B docs
- Passive voice acceptable in legal and technical definitions

### Acronym discipline
- Any acronym used ≥ 3 times must be expanded on first use
- All acronyms used in the document must appear in [GLOSSARY.md](../docs/GLOSSARY.md)

### Heading hierarchy
- No document may skip a heading level (e.g., `##` to `####` without `###`)
- Every document must have at least one `##` section header

---

## Measurement

Readability should be checked before submitting a PR for Category A or B docs. Recommended tools:

| Tool | Platform | Free? |
|------|----------|-------|
| `textstat` Python library | Local | Yes |
| Hemingway Editor | hemingwayapp.com | Yes (browser) |
| `readable` CLI | npm install -g readable-cli | Yes |

### Using textstat locally

```python
import textstat
text = open("docs/NEWCOMER_FAQ.md").read()
print(textstat.flesch_reading_ease(text))
print(textstat.flesch_kincaid_grade(text))
```

---

## Enforcement

| Phase | Mechanism |
|-------|-----------|
| Now | Manual check — author responsibility |
| Q3 2026 | Semi-automated — bot comment on PR with score |
| Q4 2026 | Gate 6 in CI — block on Category A docs below threshold |

---

## Exception Process

If a governance document cannot meet the target without sacrificing precision:
1. Document the exception in the PR description
2. Explain why precision requires lower readability
3. Summarize the key points in a plain-language callout box at the top of the document
4. Get section owner sign-off

---

*Atlas Lattice Foundation · status: candidate*
