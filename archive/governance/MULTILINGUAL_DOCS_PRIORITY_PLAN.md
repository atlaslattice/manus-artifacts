---
artifact_id: A11Y-POLICY-MULTILINGUAL-001
title: Multilingual Documentation Priority Plan
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, multilingual, i18n, globalization, a11y]
---

# Multilingual Documentation Priority Plan

> Defines the Atlas Lattice approach to multilingual documentation and sets priorities for translation effort.

status: candidate

---

## Vision

Atlas Lattice is an open-source gift to the world. While the primary language of development is English, the council recognizes that world-class reach requires lowering language barriers. This plan defines a phased approach.

---

## Language Tiers

### Tier 0 — English (Current)

All primary documentation is authored in English. This is the authoritative source language.

### Tier 1 — Priority Languages (Target: 2027)

Languages with the highest potential contributor reach, based on GitHub user demographics and open-source contributor communities:

| Language | ISO 639-1 | Target |
|---------|----------|--------|
| Spanish | `es` | 2027 Q1 |
| Mandarin Chinese | `zh` | 2027 Q1 |
| Portuguese (Brazil) | `pt-BR` | 2027 Q2 |
| Hindi | `hi` | 2027 Q3 |
| French | `fr` | 2027 Q4 |

### Tier 2 — Extended Languages (Target: 2028)

Arabic (`ar`), Japanese (`ja`), German (`de`), Russian (`ru`), Korean (`ko`)

---

## What Gets Translated First

Priority order within each language:
1. `README.md` — the public face of the repository
2. `docs/GLOSSARY.md` — key terms
3. `docs/NEWCOMER_FAQ.md` — contributor onboarding
4. `docs/GOVERNANCE_ONBOARDING_GUIDE.md` — governance overview
5. Wave 1 governance documents (canonical framework)

---

## Translation Workflow

1. **Source change:** English source document is updated
2. **Flag:** Open a translation issue with label `translation-needed` + language code
3. **Translate:** Community contributor translates; files go in `docs/i18n/{lang_code}/`
4. **Review:** At least one native speaker reviews the translation
5. **Merge:** Approved translation is merged; status set to `candidate` until reviewed by @atlaslattice
6. **Sync:** When English source changes, re-open translation issue to keep translations current

---

## Locale and Language Tags

All documents include a `lang` field in frontmatter to declare the language:

```yaml
lang: en
# or
lang: es
lang: zh
lang: pt-BR
```

English documents that don't have a `lang` field are assumed to be `lang: en`.

---

## Directory Structure

```
docs/
├── GLOSSARY.md          # English (source)
├── i18n/
│   ├── es/
│   │   └── GLOSSARY.md  # Spanish translation
│   ├── zh/
│   │   └── GLOSSARY.md  # Chinese translation
│   └── ...
```

---

*Atlas Lattice Foundation · status: candidate*
