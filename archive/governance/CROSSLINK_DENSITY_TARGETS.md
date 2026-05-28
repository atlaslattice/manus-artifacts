---
artifact_id: KG-POLICY-CROSSLINK-DENSITY-001
title: Cross-Link Density Targets
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, cross-links, density, quality-gates]
---

# Cross-Link Density Targets

> Defines minimum cross-linking requirements for artifacts to maintain a well-connected knowledge graph.

status: candidate

---

## Executive Summary

**Purpose:** Prevents orphan artifacts and ensures every document participates meaningfully in the knowledge graph.
**Audience:** Contributors, KG automation systems.
**Status:** `candidate`
**Key Decisions:** Minimum outbound links by document category; orphan detection in CI by Q3 2026.
**Action Required:** Review your PR's new documents against the minimum link targets before submission.
**Related Artifacts:** [Persistent Artifact ID Standard](./PERSISTENT_ARTIFACT_ID_STANDARD.md), [Docs Lint Quality Gates](./DOCS_LINT_QUALITY_GATES.md)

---

## What Is Cross-Link Density?

Cross-link density measures how many outbound links (references to other artifacts in this repository) a document contains. Well-linked documents make the knowledge graph traversable; isolated documents become orphans that are hard to discover and maintain.

---

## Targets by Document Category

| Category | Document type | Min outbound links | Notes |
|----------|--------------|-------------------|-------|
| **A — Governance Policy** | `archive/governance/` | 3 | Link to related policies, relevant specs, owning index |
| **B — Specification** | `archive/spec/` | 2 | Link to schema, reference implementation, related appendix |
| **C — User Docs** | `docs/` | 2 | Link to at least one governance doc and one spec |
| **D — Work Logs** | `archive/boot/gptbrain/*/` | 1 | Link to taskboard or session context document |
| **E — Schemas** | `schemas/` | 1 | Link to reference implementation or spec |
| **F — Reference Impl** | `reference_impl/` | 1 | Link to corresponding schema or spec |
| **G — Project Boards** | `projects/` | 2 | Link to README and relevant campaign board |
| **H — Templates** | `*TEMPLATE*` | 1 | Link to the policy that mandates this template |

---

## Inbound Link Targets (Hub Documents)

Certain documents should be linked to from many other documents. These are "hub" artifacts in the KG. They have **inbound link targets**:

| Hub Document | Min inbound links target | Notes |
|-------------|------------------------|-------|
| `docs/GLOSSARY.md` | 20 | Every new term introduced should link back |
| `archive/governance/COMPLIANCE_EVIDENCE_INDEX.md` | 10 | Legal/compliance docs should cite this index |
| `archive/governance/CANONICAL_PATH_MAP.md` | 8 | Architecture and nav docs should reference it |
| `README.md` | 5 | Major new sections should link back to root |
| `projects/aetherforge-144-task-campaign-2026-05-27.md` | 5 | Completion docs should link to campaign board |

---

## Orphan Node Definition

An artifact is considered an **orphan** if:
- It has 0 outbound links to other artifacts in the repository, **and**
- It has 0 inbound links from other artifacts in the repository

Orphans are automatically detected by `scripts/validate_lattice_quality_gates.py`.

---

## Enforcement Schedule

| Phase | Mechanism | Target Date |
|-------|-----------|-------------|
| Manual review | PR reviewers check for links | Now |
| Soft gate | Bot comment on PRs with < minimum links | Q3 2026 |
| Hard gate | CI blocks on severe orphans (0 inbound + 0 outbound) | Q4 2026 |

---

## How to Add Cross-Links

For inline references:
```markdown
See [Cross-Link Density Targets](../archive/governance/CROSSLINK_DENSITY_TARGETS.md) for link requirements.
```

For "Related Artifacts" sections:
```markdown
## Related Artifacts

- [Persistent Artifact ID Standard](./PERSISTENT_ARTIFACT_ID_STANDARD.md)
- [Docs Lint Quality Gates](./DOCS_LINT_QUALITY_GATES.md)
- [Canonical Path Map](./CANONICAL_PATH_MAP.md)
```

---

*Atlas Lattice Foundation · status: candidate*
