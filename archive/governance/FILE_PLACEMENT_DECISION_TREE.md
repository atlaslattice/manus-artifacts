# File Placement Decision Tree

*Atlas Lattice Foundation · Aetherforge Mission #31 · 2026-05-28*

status: candidate

> A decision tree for determining exactly where to place a new file in the Atlas Lattice repository. Follow the branches in order to reach the correct destination path.

---

## How to Use

Start at the root question and follow each YES/NO branch to the recommended path.

---

## Decision Tree

```
Is this file a SCHEMA definition (YAML/JSON validation schema)?
├─ YES → schemas/<protocol>/<version>/
└─ NO  ↓

Is this a PYTHON reference implementation or module?
├─ YES → reference_impl/<subsystem>/
└─ NO  ↓

Is this an automated SCRIPT (Python/Bash, not a test)?
├─ YES → scripts/
└─ NO  ↓

Is this a TEST FILE (pytest, assertions)?
├─ YES → tests/<domain>/   OR   <relevant-impl-dir>/tests/
└─ NO  ↓

Is this GOVERNANCE, POLICY, or LEGAL content?
├─ YES → archive/governance/
└─ NO  ↓

Is this a SPECIFICATION or PROTOCOL document?
├─ YES ↓
│   Is it part of the GPTDream++ spec vault?
│   ├─ YES → archive/spec/gptdream/
│   └─ NO  → archive/spec/<protocol-name>/
└─ NO  ↓

Is this AGENT MEMORY, DREAM JOURNAL, BOOT PACKET, or BRAIN STATE?
├─ YES ↓
│   Is it a TIDELOCKBrain work log or dream artifact?
│   ├─ YES → archive/boot/gptbrain/TIDELOCKBrain/
│   └─ NO  → archive/boot/gptbrain/
└─ NO  ↓

Is this a KNOWLEDGE GRAPH artifact (index, ontology, provenance)?
├─ YES → archive/knowledge_graph/
└─ NO  ↓

Is this a RESEARCH document (intelligence sweep, assessment, report)?
├─ YES → research/<category>/   OR   archive/assessments/
└─ NO  ↓

Is this a PROJECT TASKBOARD, ROADMAP, or CAMPAIGN document?
├─ YES → projects/
└─ NO  ↓

Is this a COUNCIL SESSION RECORD or COUNCIL REVIEW?
├─ YES ↓
│   External review?
│   ├─ YES → council-reviews/
│   └─ NO  → council/
└─ NO  ↓

Is this USER-FACING DOCUMENTATION (guides, glossary, FAQs)?
├─ YES → docs/
└─ NO  ↓

Is this an ALUMINUM OS or BAZINGA system document?
├─ YES ↓
│   Source code / Rust implementation?
│   ├─ YES → aluminum-os-core/
│   └─ NO  → aluminum-os/   OR   bazinga/
└─ NO  ↓

Is this a CODEBASE SNAPSHOT or SANDBOX?
├─ YES → codebases/<project-name>/
└─ NO  ↓

Is this a HEALTH / WELLNESS RESEARCH document?
├─ YES → health/
└─ NO  ↓

Is this a SYNTHESIS, CULTURE, or SIMULATION artifact?
├─ YES → archive/<synthesis|culture|simulation>/
└─ NO  ↓

Does it not fit any of the above?
└─ → Open a GitHub Discussion asking for placement guidance before committing
```

---

## Quick Reference Cheat Sheet

| Content Type | Primary Path |
|-------------|-------------|
| YAML/JSON Schemas | `schemas/` |
| Python implementations | `reference_impl/` |
| Automation scripts | `scripts/` |
| Tests | `tests/` |
| Governance & policy | `archive/governance/` |
| Specs & protocols | `archive/spec/` |
| Agent memory / dreams | `archive/boot/gptbrain/` |
| Knowledge graph | `archive/knowledge_graph/` |
| Research & assessments | `research/` or `archive/assessments/` |
| Taskboards & roadmaps | `projects/` |
| Council records | `council/` |
| User docs | `docs/` |
| System core docs | `aluminum-os/`, `bazinga/`, `sheldonbrain/` |
| Source code | `aluminum-os-core/` |
| Codebases | `codebases/` |

---

## When to Create a New Directory

New top-level directories should **not** be created without a council discussion and approval. Sub-directories within existing sections may be created freely as long as:
1. They include a `README.md`
2. The parent README is updated to reference them
3. The choice follows this decision tree

---

## Related Documents

- [Top-Level Navigation Standards](./TOP_LEVEL_NAVIGATION_STANDARDS.md)
- [Archive Taxonomy Map](./ARCHIVE_TAXONOMY_MAP.md)
- [Breadcrumb Standards](./BREADCRUMB_STANDARDS.md)
- [Naming Conventions](../boot/gptbrain/NAMING_CONVENTIONS.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
