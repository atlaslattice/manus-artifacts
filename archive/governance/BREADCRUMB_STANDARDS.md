# Breadcrumb Standards

*Atlas Lattice Foundation · Aetherforge Mission #27 · 2026-05-28*

status: candidate

> Defines the standard breadcrumb navigation format to be included at the top of all significant documentation files, enabling readers to orient themselves within the knowledge graph.

---

## Why Breadcrumbs?

Atlas Lattice is a large repository designed to function as a knowledge graph. Readers landing deep inside the archive (e.g., via search or a direct link) need to quickly understand:
1. Where they are in the repository
2. How to navigate up to parent context
3. What section owns this content

Breadcrumbs provide this orientation at a glance.

---

## Standard Breadcrumb Format

Place the breadcrumb as the **first line** of the document body, before the title or any other content.

### Single-Level Deep

```markdown
[📁 Root](../../README.md) › [Section Name](../README.md) › This Document
```

### Multi-Level Deep

```markdown
[📁 Root](../../../README.md) › [Top Section](../../README.md) › [Sub-Section](../README.md) › This Document
```

### Emoji Anchors by Section Type

| Section Type | Emoji |
|-------------|-------|
| Root README | 📁 |
| Archive | 🗃️ |
| Governance | ⚖️ |
| Spec Vault | 📐 |
| Projects | 🎯 |
| Docs | 📚 |
| KG / Knowledge Graph | 🕸️ |
| Boot / Brain | 🧠 |
| Security | 🔒 |
| CI/CD | ⚙️ |

---

## Examples

### Example 1 — Governance document

```markdown
[📁 Root](../../README.md) › [⚖️ Governance](./README.md) › Deprecation Policy
```

### Example 2 — Spec vault appendix

```markdown
[📁 Root](../../../README.md) › [🗃️ Archive](../../README.md) › [📐 GPTDream++ Spec](../README.md) › Appendix J
```

### Example 3 — Project taskboard

```markdown
[📁 Root](../README.md) › [🎯 Projects](./README.md) › Next-144 Taskboard
```

---

## Application Scope

Breadcrumbs are **required** for:
- All files under `archive/` (any depth)
- All files under `docs/`
- All files under `projects/`
- Spec vault appendices
- Schema documentation files

Breadcrumbs are **optional** for:
- Root-level files (`README.md`, `SECURITY.md`, etc.) — they are already at root
- Auto-generated files (seed data, JSON schemas)
- Test files

---

## Rollout

Breadcrumbs will be added to existing files as part of Mission #37 (standardize metadata headers) and ongoing contributions. New files must include breadcrumbs per scope above before merging.

---

## CI Enforcement

A future CI check (Mission #63 — metadata completeness) will flag newly added files in required-scope directories that lack a breadcrumb line.

---

## Related Documents

- [Top-Level Navigation Standards](./TOP_LEVEL_NAVIGATION_STANDARDS.md)
- [File Placement Decision Tree](./FILE_PLACEMENT_DECISION_TREE.md)
- [Canonical Path Map](./CANONICAL_PATH_MAP.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
