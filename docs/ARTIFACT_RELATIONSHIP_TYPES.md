---
artifact_id: DOC-REL-TYPES-2026-05-27
title: Artifact Relationship Types
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---

# Artifact Relationship Types

## Core relationship vocabulary

- `derives_from` — artifact synthesized from one or more source artifacts.
- `implements` — artifact operationalizes a policy/specification.
- `validates` — artifact checks quality or rule compliance of another artifact.
- `supersedes` — artifact replaces older version as preferred candidate/canon.
- `indexes` — artifact maps a set of artifacts for discovery.
- `governs` — artifact defines ratification or process constraints.
- `depends_on` — artifact needs another artifact to execute or evaluate.
- `references` — artifact cites another artifact without lifecycle dependency.

## Usage notes

- Use explicit relationship verbs in index and governance docs.
- Prefer stable path citations over narrative references.
- Do not treat dream outputs as authoritative relationships until ratified.
