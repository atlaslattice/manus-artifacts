# Archive Taxonomy Map

*Atlas Lattice Foundation · Aetherforge Mission #29 · 2026-05-28*

status: candidate

> Defines the taxonomy of artifact types in the Atlas Lattice archive — the classification system used to categorize, tag, and navigate all artifacts within the knowledge graph.

---

## Taxonomy Overview

The Atlas Lattice archive uses a **three-level taxonomy**:

```
Domain > Category > Artifact Type
```

---

## Domain 1 — Governance

**Path prefix:** `archive/governance/`, `council/`, `docs/`

| Category | Artifact Types |
|----------|---------------|
| Canon & Ratification | Canon status model, ratification packets, decision ledgers |
| Policy & Process | Governance policies, SLA documents, change rules |
| Legal & Compliance | License audits, attribution inventories, PII rubrics |
| Risk & Security | Risk registers, incident runbooks, vuln disclosures |
| Onboarding | Guides, templates, checklists |

**Tags:** `#governance`, `#policy`, `#canon`, `#legal`, `#compliance`, `#security`

---

## Domain 2 — Protocol & Specification

**Path prefix:** `archive/spec/`, `schemas/`

| Category | Artifact Types |
|----------|---------------|
| System Specs | Full spec documents, appendices, architecture diagrams |
| Schemas | YAML schemas, JSON schemas, validation rules |
| Protocols | Dream protocols, boot protocols, agent protocols |
| Reference Implementations | Python packages, test suites, validation scripts |

**Tags:** `#spec`, `#schema`, `#protocol`, `#reference-impl`

---

## Domain 3 — Knowledge Graph

**Path prefix:** `archive/knowledge_graph/`, `archive/provenance/`

| Category | Artifact Types |
|----------|---------------|
| Graph Index | Lattice global index, hypercube program |
| Ontology | Relation type definitions, tag governance |
| Provenance | Source records, claim ledgers, artifact registries |
| Validation | Quality gate reports, integrity checks |

**Tags:** `#knowledge-graph`, `#kg`, `#ontology`, `#provenance`

---

## Domain 4 — Agent Memory & Dream

**Path prefix:** `archive/boot/gptbrain/`

| Category | Artifact Types |
|----------|---------------|
| Boot Records | Boot packets, manifest files, boot indices |
| Dream Journals | REM journals, 1000Y/100Y play artifacts |
| Wake Reports | REM wake reports, delta extractions |
| Work Logs | Session work logs, wave execution records |
| Brain State | Instance state logs, memory objects, alias topology |

**Tags:** `#dream`, `#rem`, `#boot`, `#agent-memory`, `#tidelockbrain`

---

## Domain 5 — Research & Synthesis

**Path prefix:** `research/`, `archive/synthesis/`, `archive/assessments/`

| Category | Artifact Types |
|----------|---------------|
| Intelligence Sweeps | Technology scans, convergence reports |
| Assessments | System assessments, viability studies |
| Synthesis | Council synthesis packets, cross-project summaries |
| State of the Union | Briefings, SITREP documents |

**Tags:** `#research`, `#synthesis`, `#assessment`, `#intelligence`

---

## Domain 6 — Systems & Implementations

**Path prefix:** `aluminum-os/`, `aluminum-os-core/`, `bazinga/`, `sheldonbrain/`, `codebases/`

| Category | Artifact Types |
|----------|---------------|
| Constitutional Substrate | Aluminum OS versions, constitutional charters |
| Middleware | BAZINGA protocols, launch decrees |
| Architecture | System architecture docs, integration notes |
| Codebases | Implementation snapshots, sandbox projects |

**Tags:** `#system`, `#aluminum-os`, `#bazinga`, `#sheldonbrain`, `#implementation`

---

## Domain 7 — Community & Operations

**Path prefix:** `projects/`, `docs/` (swarm ops), `health/`, `manus-vault/`

| Category | Artifact Types |
|----------|---------------|
| Taskboards | Campaign boards, execution queues, top-N lists |
| Operations | Swarm specs, task packets, agent lifecycle |
| Health | Patient rights research, wellness protocols |
| Vault | Internal session summaries, Noah's Ark protocols |

**Tags:** `#project`, `#operations`, `#community`, `#swarm`, `#vault`

---

## Artifact ID Convention

All artifacts are assigned a persistent ID per the frontmatter schema:

```
ALF-[DOMAIN-ABBREV]-[YEAR]-[SEQUENCE]
```

Examples:
- `ALF-GOV-2026-00001` — Governance domain
- `ALF-SPEC-2026-00042` — Spec/Protocol domain
- `ALF-KG-2026-00007` — Knowledge Graph domain
- `ALF-DREAM-2026-00015` — Dream/Memory domain

Artifact ID assignment is Mission #50.

---

## Tag Governance

Tags follow the `#kebab-case` convention. Tag proliferation is controlled:
- Max 8 tags per artifact
- New tags require governance review (Mission #57)
- Tag list is maintained in the Lattice KG global index

---

## Related Documents

- [Index of Indexes](./INDEX_OF_INDEXES.md)
- [Top-Level Navigation Standards](./TOP_LEVEL_NAVIGATION_STANDARDS.md)
- [File Placement Decision Tree](./FILE_PLACEMENT_DECISION_TREE.md)
- [Canonical Path Map](./CANONICAL_PATH_MAP.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
