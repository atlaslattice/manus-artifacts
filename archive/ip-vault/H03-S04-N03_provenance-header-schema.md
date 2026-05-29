---
hsn: H03-S04-N03
title: Provenance Header Schema
author: David Sheldon (@atlaslattice)
date: 2026-05-29
review_state: seed
license: MIT
canon: "no"
source_boundary: "Schema definition for provenance headers. Candidate standard."
---

# Provenance Header Schema

STATUS: SEED — NOT CANON

## Schema

```yaml
# ATLAS LATTICE PROVENANCE HEADER v0.1
hsn: H##-S##-N##           # lattice coordinate
title: ""                   # artifact title
author: ""                  # author handle
date: YYYY-MM-DD            # creation date
review_state: seed          # seed|candidate|reviewed|ratified|canon|quarantine
license: MIT                # license
canon: "no"                 # explicit non-canon flag
source_boundary: ""         # what this is / is not
dependencies: []            # H-S-N coords of dependencies
supersedes: []              # prior artifact IDs superseded
```

## Validation

- All fields required for `candidate` promotion.
- `source_boundary` must be non-empty.
- `canon: "no"` mandatory until ratification event exists.
