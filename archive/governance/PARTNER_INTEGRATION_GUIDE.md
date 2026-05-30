---
artifact_id: COMM-POLICY-PARTNER-INTEGRATION-001
title: Partner Integration Guide
status: candidate
created: 2026-05-28
owner: council
tags: [community, partnerships, integration, open-source, collaboration]
---

# Partner Integration Guide

> Defines how external organizations and projects can integrate with or build on Atlas Lattice.

status: candidate

---

## Integration Tiers

### Tier 1: Consumer (read-only)

Organizations that consume Atlas Lattice data or reference its schemas:
- No approval needed
- Must attribute Atlas Lattice per the LICENSE
- Encouraged to file issues if they find problems

---

### Tier 2: Contributor Partner

Organizations that contribute back to the repository:
- Follow standard contributor process (issues, PRs, Discussions)
- May be listed in the Partners section of README if they make sustained contributions

---

### Tier 3: Ecosystem Partner

Organizations building tooling, visualizations, or complementary projects that formally reference Atlas Lattice:
- Contact @atlaslattice via GitHub Discussions (Ideas category)
- Mutual linking and acknowledgment
- Coordinated release timing where relevant

---

## KG Data Integration

External tools that want to consume the Atlas Lattice knowledge graph:

1. **KG Index:** Available at `kg/global_index.json` in the repository
2. **Export formats:** JSON-LD, TSV, DOT (see PROVENANCE_GRAPH_EXPORT_SPEC.md)
3. **API Roadmap:** See KG_PUBLIC_API_ROADMAP.md for the planned public API
4. **Schema references:** All schemas available in `schemas/` directory

---

## Schema Reuse

Organizations wishing to use Atlas Lattice schemas in their own systems:
- Schemas are released under the same open-source license as the repository
- Derivative schemas should retain the `$ref` to the original where possible for traceability
- Schema changes are versioned; see SCHEMA_VALIDATION_CI_POLICY.md

---

## Attribution Requirements

When referencing or building on Atlas Lattice in public-facing work, include:

```
Built with / Powered by Atlas Lattice (https://github.com/atlaslattice/manus-artifacts)
Licensed under [LICENSE name]
```

---

*Atlas Lattice Foundation · status: candidate*
