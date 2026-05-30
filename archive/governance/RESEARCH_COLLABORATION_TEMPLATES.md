---
artifact_id: COMM-POLICY-RESEARCH-COLLAB-001
title: Research Collaboration Templates
status: candidate
created: 2026-05-28
owner: council
tags: [community, research, collaboration, academic, templates]
---

# Research Collaboration Templates

> Defines templates and process for academic and research collaborations with Atlas Lattice.

status: candidate

---

## Collaboration Types

### 1. Dataset Use

Researchers using Atlas Lattice as a dataset (e.g., studying knowledge graph design, AI governance, open-source archiving):
- No formal agreement needed for public data
- Citation format: see Attribution section below
- If you publish research using Atlas Lattice, please post in GitHub Discussions (Show and Tell) so we can learn from your work

---

### 2. Research Partnership

Researchers who want to collaborate on improving Atlas Lattice (e.g., applying novel KG algorithms, evaluating accessibility tools):
- Contact via GitHub Discussions (Ideas category)
- Brief project description: scope, timeline, expected outputs
- @atlaslattice reviews within 30 days

---

## Citation Format

For academic papers and research reports citing Atlas Lattice:

```
Atlas Lattice Foundation. (2026). manus-artifacts [Knowledge graph repository]. 
GitHub. https://github.com/atlaslattice/manus-artifacts
```

Or in BibTeX:
```bibtex
@misc{atlas-lattice-2026,
  title     = {manus-artifacts},
  author    = {{Atlas Lattice Foundation}},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/atlaslattice/manus-artifacts}
}
```

---

## Data Export for Research

Researchers needing bulk data exports:
- KG Index: `kg/global_index.json`
- JSON-LD export: see PROVENANCE_GRAPH_EXPORT_SPEC.md
- TSV edge list: see PROVENANCE_GRAPH_EXPORT_SPEC.md

For very large exports or custom dataset requests, contact via Discussions.

---

## Research Output Sharing

Researchers are encouraged (but not required) to share:
- Preprints or papers that use Atlas Lattice data
- Datasets derived from Atlas Lattice (with attribution)
- Code that builds on Atlas Lattice schemas or KG

Sharing outputs helps the community learn and improves the project.

---

*Atlas Lattice Foundation · status: candidate*
