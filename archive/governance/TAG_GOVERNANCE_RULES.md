---
artifact_id: KG-POLICY-TAG-GOVERNANCE-001
title: Tag Governance Rules
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, tags, governance, taxonomy]
---

# Tag Governance Rules

> Defines the controlled vocabulary for tags used in artifact frontmatter and how tags are governed.

status: candidate

---

## Executive Summary

**Purpose:** Prevents tag proliferation and ensures tags are meaningful, consistent, and machine-traversable.
**Audience:** All contributors, KG automation systems.
**Status:** `candidate`
**Key Decisions:** Tags come from a controlled vocabulary; new tags require review; tags are kebab-case; each artifact has 2–8 tags.
**Action Required:** Use only tags from the approved vocabulary below. New tag proposals go through the lightweight approval process.
**Related Artifacts:** [Metadata Headers Standard](./METADATA_HEADERS_STANDARD.md), [Terminology Consistency Report](./TERMINOLOGY_CONSISTENCY_REPORT.md)

---

## Tag Format Rules

- **Case:** `kebab-case` (all lowercase, hyphens for spaces)
- **Length:** 2–30 characters
- **Count per artifact:** Minimum 2, maximum 8
- **Specificity:** Tags should be general enough to group related artifacts (not hyper-specific one-artifact tags)

---

## Approved Tag Vocabulary

### Domain Tags
| Tag | When to use |
|-----|-------------|
| `governance` | Policy, ratification, council rules |
| `legal` | Licensing, compliance, privacy |
| `security` | Vulnerability, incident response, supply chain |
| `knowledge-graph` | KG schemas, indexes, relations, density |
| `documentation` | Writing standards, templates, editorial |
| `testing` | Test plans, coverage, reliability |
| `ci-cd` | Workflows, automation, pipelines |
| `accessibility` | Language, localization, readability |
| `community` | Contribution guides, communication |
| `architecture` | Repository layout, navigation, taxonomy |

### Type Tags
| Tag | When to use |
|-----|-------------|
| `policy` | A formal policy document |
| `standard` | A normative standard |
| `guide` | A practical how-to guide |
| `template` | A fill-in template |
| `report` | An audit, analysis, or status report |
| `spec` | A technical specification |
| `schema` | A data schema (YAML, JSON) |
| `roadmap` | Future plans and timelines |
| `index` | An index or registry document |
| `checklist` | An action-item checklist |

### Status Tags
| Tag | When to use |
|-----|-------------|
| `candidate` | Artifact is in candidate state (mirrors status field) |
| `ratified` | Artifact has been ratified |
| `deprecated` | Artifact is deprecated |

### Project Tags
| Tag | When to use |
|-----|-------------|
| `aetherforge` | Aetherforge game layer documents |
| `gptdream` | GPTDream++ protocol documents |
| `tidelockbrain` | TIDELOCKBrain memory artifacts |
| `atlas-orcs` | Atlas/ORCS schema system |
| `lattice-kg` | Lattice KG implementation |
| `receipt-habitat` | Receipt Habitat product |

### Special Tags
| Tag | When to use |
|-----|-------------|
| `quality-gates` | Automated quality enforcement |
| `provenance` | Provenance tracking and citation |
| `cross-links` | Cross-link and relationship management |
| `onboarding` | Newcomer and contributor onboarding |
| `public-facing` | Content intended for public/external audience |
| `ai-evidence` | Evidence of AI-built systems |

---

## Proposing New Tags

If your artifact requires a tag that isn't in the vocabulary:

1. **Check first** — is there an existing tag that covers the concept?
2. **Propose** — open a PR adding the new tag to this document in the Approved Vocabulary table with a clear description
3. **Review** — any council member may approve tag additions (no @atlaslattice ratification required for minor tag additions)
4. **Use** — once merged, the tag is approved for use

---

## Tag Sprawl Prevention

Tags that appear on fewer than 3 artifacts after 90 days are candidates for consolidation or removal. The quarterly tag audit (`scripts/validate_lattice_quality_gates.py` tag report) identifies these.

---

## Anti-Patterns

Avoid these tagging mistakes:

| Anti-pattern | Example | Preferred |
|-------------|---------|-----------|
| Too specific | `wave-4-doc-42` | Use `documentation` + `candidate` |
| Duplicate domain | `docs` + `documentation` | Use only `documentation` |
| Uppercase | `Governance` | `governance` |
| Description not taxonomy | `important` | Use type or status tags |
| Verb as tag | `reviewing` | `policy` or `guide` |

---

*Atlas Lattice Foundation · status: candidate*
