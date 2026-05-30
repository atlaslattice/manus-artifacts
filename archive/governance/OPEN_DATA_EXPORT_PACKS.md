---
artifact_id: COMM-POLICY-OPEN-DATA-EXPORT-001
title: Open Data Export Packs
status: candidate
created: 2026-05-28
owner: council
tags: [community, open-data, export, knowledge-graph, accessibility]
---

# Open Data Export Packs

> Defines the open data export packs that Atlas Lattice publishes for external consumption.

status: candidate

---

## What Are Open Data Export Packs?

Open Data Export Packs are versioned snapshots of Atlas Lattice data released for public consumption. They lower the barrier for external researchers, developers, and knowledge graph consumers who don't want to process the raw markdown repository.

---

## Export Pack Types

### Pack 1: KG Graph Pack

**Contents:**
- `kg/global_index.json` — full knowledge graph in JSON-LD
- `kg/edges.tsv` — tab-separated edge list: `source_id\trelation_type\ttarget_id`
- `kg/nodes.tsv` — node metadata: `artifact_id\ttitle\tstatus\ttags`
- `README.txt` — format documentation

**Release cadence:** Quarterly (aligned with governance health report)

---

### Pack 2: Governance Schema Pack

**Contents:**
- All schemas in `schemas/atlas_orcs/v0_1/`
- All schemas in `schemas/o_ai/v0_1/`
- All schemas in `schemas/native_thread/v0_1/`
- `SCHEMA_PACK_MANIFEST.json` — version, contents, checksums
- Example valid documents for each schema

**Release cadence:** When schemas change (version-bumped)

---

### Pack 3: Governance Policy Pack

**Contents:**
- All `archive/governance/*.md` files
- Frontmatter-only extract: `governance_policies_frontmatter.json`
- Tag and relation index

**Release cadence:** Quarterly

---

## Release Format

Export packs are published as:
1. GitHub Releases with a tagged version (`v0.YYYY.Q[N]`)
2. Attached as release assets (ZIP archives)
3. Documented in CHANGELOG.md

---

## Licensing

All export packs are released under the same license as the repository. Data consumers must attribute Atlas Lattice.

---

*Atlas Lattice Foundation · status: candidate*
