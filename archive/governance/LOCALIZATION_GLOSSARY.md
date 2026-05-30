---
artifact_id: A11Y-POLICY-LOCALIZATION-GLOSSARY-001
title: Localization Glossary
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, localization, glossary, i18n, translation]
---

# Localization Glossary

> Defines terminology for localization and translation work in the Atlas Lattice project, and provides a controlled list of key terms that must be translated consistently.

status: candidate

---

## Localization Terminology

| Term | Definition |
|------|-----------|
| **i18n** (internationalization) | Designing software/docs to support multiple languages without code changes |
| **l10n** (localization) | Adapting content for a specific locale, including translation and cultural adaptation |
| **locale** | A combination of language and region (e.g., `en-US`, `pt-BR`, `zh-CN`) |
| **source language** | The authoritative language of a document (English for this project) |
| **translation** | Converting text from one language to another |
| **transliteration** | Converting text character-by-character between scripts (e.g., Cyrillic to Latin) |
| **back-translation** | Translating a translated text back to the original language to check accuracy |
| **fuzzy match** | A translation memory hit that is partially but not exactly matching |
| **TM** (translation memory) | A database of previously translated segments for reuse |
| **MT** (machine translation) | AI-assisted translation (acceptable as a first pass; requires human review) |

---

## Key Terms — Translation Reference

The following terms have approved translations. Translators **must** use these translations consistently.

| English | Spanish (es) | Chinese (zh) | Portuguese BR (pt-BR) |
|---------|-------------|-------------|----------------------|
| Atlas Lattice | Atlas Lattice | Atlas Lattice | Atlas Lattice |
| Knowledge Graph | Grafo de Conocimiento | 知识图谱 | Grafo de Conhecimento |
| Aetherforge | Aetherforge | Aetherforge | Aetherforge |
| GPTDream++ | GPTDream++ | GPTDream++ | GPTDream++ |
| canon / canonical | canon / canónico | 正典 | canon / canônico |
| candidate | candidato | 候选 | candidato |
| ratification | ratificación | 批准 | ratificação |
| governance | gobernanza | 治理 | governança |
| artifact | artefacto | 制品 | artefato |
| wave | oleada | 浪潮 | onda |
| council | consejo | 委员会 | conselho |
| frontmatter | frontmatter | 前置元数据 | frontmatter |
| TIDELOCKBrain | TIDELOCKBrain | TIDELOCKBrain | TIDELOCKBrain |

**Note:** Proper nouns (Atlas Lattice, Aetherforge, GPTDream++, TIDELOCKBrain) are never translated — they are retained verbatim in all languages.

---

## Do Not Translate (DNT) List

The following must never be translated:
- Repository name: `atlaslattice/manus-artifacts`
- File paths and command-line syntax
- Code blocks
- URLs and links
- Artifact IDs (e.g., `GOV-POLICY-CANON-STATUS-001`)
- Proper nouns listed in the table above

---

## Machine Translation Policy

Machine translation (MT) is acceptable as a draft, but:
1. Every MT draft must be reviewed by a fluent human speaker
2. MT drafts must be labeled `<!-- MT draft — review needed -->` until human-reviewed
3. MT output for the DNT list must be corrected to retain original terms

---

*Atlas Lattice Foundation · status: candidate*
