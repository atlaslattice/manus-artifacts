---
artifact_id: GOV-TERMINOLOGY-CONSISTENCY-REPORT-001
title: Terminology Consistency Report
status: candidate
created: 2026-05-28
owner: council
tags: [documentation, terminology, consistency, quality]
---

# Terminology Consistency Report

> Audit of terminology usage across the repository — identifying inconsistencies, synonyms, and recommended standard forms.

status: candidate · run_date: 2026-05-28

---

## Summary

This report documents terminology inconsistencies found across the Atlas Lattice archive as of 2026-05-28. Each finding includes the inconsistent forms observed, the recommended canonical form, and the scope of correction needed.

**Total findings:** 18
**Critical (must fix before ratification):** 4
**Advisory (should fix, rolling):** 14

---

## Critical Findings

### C-01: "canon" vs "canonical" vs "canonical status"

| Observed forms | Files affected |
|----------------|---------------|
| `canon`, `canonical`, `canonical status`, `canon status`, `is_canon` | ~40 files |

**Canonical form:** Use **`canonical`** as the adjective; **`canon`** only as a noun (e.g., "achieve canon", "enter canon"). Never "canon status" — use "canonical status" instead.

**Decision:** The `is_canon()` function name in code is acceptable as a contraction. In prose, always use `canonical`.

---

### C-02: "ratified" vs "ratification" vs "approved"

| Observed forms | Files affected |
|----------------|---------------|
| `ratified`, `approved`, `validated`, `confirmed`, `signed off` | ~25 files |

**Canonical form:** Use **`ratified`** (verb: "ratify") for the formal canon-acceptance event. Use `approved` only for informal reviews and PR approvals.

---

### C-03: "artifact" vs "document" vs "file" vs "resource"

| Observed forms | Files affected |
|----------------|---------------|
| `artifact`, `document`, `file`, `resource`, `item`, `asset` | ~60 files |

**Canonical form:**
- **`artifact`** — any versioned, provenance-tracked content unit in the archive
- **`document`** — a human-readable prose artifact (subset of artifact)
- **`file`** — a filesystem object (use only when referring to technical storage)
- **`resource`** — acceptable in HTTP/API contexts; avoid in governance prose

---

### C-04: "Knowledge Graph" capitalization

| Observed forms | Files affected |
|----------------|---------------|
| `Knowledge Graph`, `knowledge graph`, `KG`, `knowledge-graph` | ~35 files |

**Canonical form:** **`Knowledge Graph`** (title-case) on first mention in a document. **`KG`** as shorthand thereafter. Never hyphenated in prose.

---

## Advisory Findings

### A-01: "Atlas Lattice Foundation" vs "Atlas Lattice" vs "ALF"

**Canonical form:** **`Atlas Lattice Foundation`** on first mention; **`Atlas Lattice`** or **`ALF`** thereafter. Never "the lattice" as a standalone proper noun in formal docs (acceptable in informal/dream contexts).

---

### A-02: "task" vs "mission" vs "item"

**Canonical form:** In the Aetherforge game context, use **`mission`**. In CI/task-tracking context, use **`task`**. Never use "item" for tracked work units.

---

### A-03: "wave" vs "face" vs "sprint"

**Canonical form:** **`Face`** on the 12×12 campaign board (Face 01–12). **`Wave`** in execution/sprint context (Wave 01–12). Both are correct in their context — do not conflate. **`Sprint`** is not used in this repository.

---

### A-04: "candidate" vs "draft" vs "WIP" vs "pending"

**Canonical form:** **`candidate`** for all artifacts not yet ratified. Never `draft`, `WIP`, or `pending` in frontmatter `status` fields. `candidate` is the correct pre-ratification status per the canon status model.

---

### A-05: "frontmatter" vs "front matter" vs "YAML header"

**Canonical form:** **`frontmatter`** (one word, lowercase). Acceptable variant: **`YAML frontmatter`** when emphasizing format.

---

### A-06: "swarm" vs "Children of the Swarm" vs "agent collective"

**Canonical form:** **`Children of the Swarm`** for the formal proper noun. **`swarm`** (lowercase) as shorthand in context. Never "agent collective" in this repository.

---

### A-07: "session" vs "run" vs "cycle"

**Canonical form:** **`session`** for a bounded AI work context. **`cycle`** for a REM/dream cycle. **`run`** only in CI/testing context.

---

### A-08: "TIDELOCKBrain" casing

**Canonical form:** **`TIDELOCKBrain`** (no spaces, exact CamelCase). Never `TIDELOCK Brain`, `Tidelock Brain`, or `TidelockBrain`.

---

### A-09: "GPTDream++" styling

**Canonical form:** **`GPTDream++`** (exact). Never `GPT Dream`, `GPTDream`, `GPT-Dream`, or `GPTDream ++`.

---

### A-10: "Metatron's Cube" vs "Metatrons Cube" vs "metatrons cube"

**Canonical form:** **`Metatron's Cube`** (possessive, title-case). The conceptual shape behind the 144-sphere ontology.

---

### A-11: "README" vs "Readme" vs "readme"

**Canonical form:** **`README`** (all caps) for filenames. **`README.md`** with extension when citing the file. Never `Readme` in prose.

---

### A-12: "Aetherforge" vs "AetherForge" vs "aetherforge"

**Canonical form:** **`Aetherforge`** (title-case, single word). Never `AetherForge` or `aetherforge` in prose.

---

### A-13: Bullet list punctuation inconsistency

**Observation:** Some bullet lists end with periods; others do not.
**Canonical form:** No trailing period on bullets < 1 full sentence. Full sentences in bullets take a period.

---

### A-14: "open source" vs "open-source"

**Canonical form:** **`open-source`** (hyphenated) as an adjective before a noun ("open-source gift"). **`open source`** (no hyphen) as a standalone noun phrase ("release as open source"). Standard English compound-modifier rule.

---

## Correction Schedule

| Priority | Finding IDs | Target |
|----------|-------------|--------|
| Before any ratification PR | C-01 through C-04 | Rolling — fix at point of use |
| Documentation sprint | A-01 through A-06 | Q3 2026 |
| Advisory | A-07 through A-14 | Q4 2026 rolling |

---

## Enforcement

- **GLOSSARY.md** is the authoritative source; all terms above are now defined there.
- The Editorial Style Guide (`archive/governance/EDITORIAL_STYLE_GUIDE.md`) references this report.
- Future PRs should verify new documents against this report before submission.
- Next consistency pass scheduled: **2026-08-28** (90 days).

---

*Atlas Lattice Foundation · status: candidate*
