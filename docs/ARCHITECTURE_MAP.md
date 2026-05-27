---
artifact_id: DOC-ARCH-MAP-2026-05-27
title: Atlas Lattice Architecture Map
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---

# Architecture Map — Atlas Lattice

## Layered System Map

```mermaid
flowchart TD
  A[Public Entry Layer\nREADME + START_HERE] --> B[Documentation Layer\ndocs/]
  B --> C[Core Systems\naluminum-os + sheldonbrain + bazinga]
  B --> D[Governance\ncouncil + council-reviews]
  B --> E[Research + Health + Projects]
  C --> F[GPTBrain Substrate\narchive/boot/gptbrain]
  F --> G[Reference Implementations\nreference_impl/ + schemas/]
  G --> H[Validation Layer\ntests/ + CI workflows]
  H --> I[Publication Readiness\nroadmap + quality gates]
```

## Domain Boundaries

- **Canonical substrate:** GitHub repository content.
- **Artifact lifecycle:** DRAFT → CANDIDATE → CANONICAL (or ARCHIVED).
- **Quality interface:** workflows and test suites enforce baseline integrity.
- **Gameplay framing:** Aetherforge task waves map work into progressive rings.
