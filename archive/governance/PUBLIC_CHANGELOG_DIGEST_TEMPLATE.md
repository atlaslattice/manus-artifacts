---
artifact_id: LAUNCH-TEMPLATE-CHANGELOG-DIGEST-001
title: Public Changelog Digest Template
status: candidate
created: 2026-05-29
owner: council
tags: [launch, changelog, digest, communication, template]
---

# Public Changelog Digest Template

> Template for a public-facing digest that summarizes major repository changes in plain language.

status: candidate

---

## Purpose

`CHANGELOG.md` is the system of record, but a public digest makes the same movement easier to scan for contributors, observers, and press. The digest should translate raw changes into narrative momentum without losing traceability.

---

## Publishing Rules

- Publish after each quarterly release and after any milestone release.
- Source every item from `CHANGELOG.md`.
- Prefer grouped themes over raw file lists.
- Link back to the root changelog and any major release-note artifact.

---

## Digest Template

```markdown
# Atlas Lattice — Public Changelog Digest

**Coverage window:** [Start date] to [End date]  
**Release context:** [Quarterly release / milestone release / special update]

## What changed

- [Major theme 1]
- [Major theme 2]
- [Major theme 3]

## Highlights by area

### Governance
- [Notable governance changes]

### Knowledge Graph
- [Notable KG changes]

### Reliability / Security / CI
- [Operational changes]

### Community
- [Community and ecosystem changes]

## Why it matters

[2-4 sentence plain-language summary]

## Read the source artifacts

- `CHANGELOG.md`
- [Release notes or milestone artifact links]
```

---

## Digest Quality Bar

A digest is ready when it:

- covers the full reporting window,
- includes at least one item from each materially changed area,
- uses language understandable to a first-time reader, and
- links back to the authoritative artifacts.

---

## Archive Location

Store published digests at:

- `archive/governance/CHANGELOG_DIGEST_YYYY_QN.md` for quarterly digests
- `archive/governance/CHANGELOG_DIGEST_V1_LAUNCH.md` for the v1.0 digest

---

*Atlas Lattice Foundation · status: candidate*
