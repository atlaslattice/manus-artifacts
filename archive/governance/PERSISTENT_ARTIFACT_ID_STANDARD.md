---
artifact_id: KG-ARTIFACT-ID-STANDARD-001
title: Persistent Artifact ID Standard
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, artifact-ids, provenance, standards]
---

# Persistent Artifact ID Standard

> Defines the scheme for assigning stable, machine-readable identifiers to every artifact in the Atlas Lattice repository.

status: candidate

---

## Executive Summary

**Purpose:** Establishes a permanent, consistent identifier scheme for all artifacts to enable stable cross-linking, citation, and KG traversal.
**Audience:** Contributors, AI agents, knowledge graph systems.
**Status:** `candidate`
**Key Decisions:** IDs use a `DOMAIN-TYPE-SLUG-NNN` format; IDs are immutable once assigned; IDs live in YAML frontmatter.
**Action Required:** All new artifacts must include an `artifact_id` in frontmatter. Existing artifacts should be retrofitted per the schedule below.
**Related Artifacts:** [Metadata Headers Standard](../archive/governance/METADATA_HEADERS_STANDARD.md), [Canonical Path Map](../archive/governance/CANONICAL_PATH_MAP.md)

---

## ID Format

```
{DOMAIN}-{TYPE}-{SLUG}-{NNN}
```

| Component | Description | Examples |
|-----------|-------------|---------|
| `DOMAIN` | Top-level subject area (2–4 chars, CAPS) | `GOV`, `KG`, `SPEC`, `LEGAL`, `SEC`, `TEST`, `DOC` |
| `TYPE` | Document type (2–6 chars, CAPS) | `POLICY`, `REPORT`, `GUIDE`, `SCHEMA`, `TEMPLATE`, `MAP` |
| `SLUG` | Abbreviated title (2–4 words, UPPER_SNAKE) | `CANON_STATUS`, `DATA_RETENTION`, `RELEASE_NOTES` |
| `NNN` | 3-digit zero-padded sequence within the domain+type | `001`, `002`, `042` |

### Examples

| ID | Document |
|----|---------|
| `GOV-POLICY-CANON-STATUS-001` | Canon status model definition |
| `KG-SCHEMA-FRONTMATTER-001` | Frontmatter schema spec |
| `LEGAL-REPORT-LICENSE-AUDIT-001` | License audit report |
| `SEC-POLICY-VULN-DISCLOSURE-001` | Vulnerability disclosure policy |
| `SPEC-GUIDE-GPTDREAM-APPENDIX-A` | GPTDream++ Appendix A |

---

## Domain Registry

| Domain | Scope | Example documents |
|--------|-------|------------------|
| `GOV` | Governance, policy, ratification | Review SLA, Deprecation Policy |
| `KG` | Knowledge graph, schemas, indexes | Global Index, Frontmatter Schema |
| `SPEC` | Technical specifications and appendices | GPTDream++ Appendices, ORCS spec |
| `LEGAL` | Legal, compliance, privacy, trust | License Audit, PII Rubric |
| `SEC` | Security, supply chain, incident response | SBOM, Vuln Disclosure |
| `TEST` | Test plans, coverage reports, fixtures | Test Strategy, Quality Report |
| `DOC` | User-facing documentation | Glossary, FAQ, Project Briefs |
| `ARCH` | Architecture, navigation, layout | Taxonomy Map, Canonical Path Map |
| `LOG` | Work logs, dream journals, wake reports | TIDELOCKBrain logs |
| `PROD` | Product artifacts | Receipt Habitat |

---

## Frontmatter Field

Add `artifact_id` as the first field in every document's YAML frontmatter:

```yaml
---
artifact_id: GOV-POLICY-CANON-STATUS-001
title: Canon Status Model
status: candidate
created: 2026-05-28
owner: council
---
```

---

## Immutability Rule

**IDs are permanent once assigned.** They must never be changed, even if a document is renamed, moved, or updated. An artifact's ID is its stable identity across time, path changes, and version bumps.

If a document is replaced by a successor, the old document is deprecated (not deleted). The successor gets a new ID. The old document's frontmatter gains a `superseded_by` field pointing to the new ID.

---

## Assignment Process

1. Check the domain registry and type registry to choose `DOMAIN` and `TYPE`
2. Create a slug from the document title (2–4 key words, UPPER_SNAKE_CASE)
3. Find the next available sequence number within that `DOMAIN-TYPE-SLUG` prefix by searching existing `artifact_id` fields in the repository
4. Write the full `artifact_id` into frontmatter before committing the document

Automated assignment via `scripts/assign_artifact_ids.py` is planned for Q3 2026.

---

## Retrofit Schedule

| Wave | Documents | Target |
|------|-----------|--------|
| Wave 1 (Governance) | 12 docs | Q3 2026 |
| Wave 2 (Legal) | 12 docs | Q3 2026 |
| Wave 3 (Architecture) | 9 docs | Q3 2026 |
| Spec vault (GPTDream++) | 10 docs | Q3 2026 |
| All remaining | Rolling | Q4 2026 |

---

## Cross-Reference

When citing an artifact by ID in another document, use the format:

```markdown
See [artifact_id: GOV-POLICY-CANON-STATUS-001](../archive/governance/CANON_STATUS_MODEL.md).
```

This enables machine parsing even if the file path changes.

---

*Atlas Lattice Foundation · status: candidate*
