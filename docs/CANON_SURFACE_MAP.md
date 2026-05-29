---
title: Canon Surface Map
artifact_id: GOVERNANCE-CANON-SURFACE-MAP-2026-05-29
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-29
provenance: Created from 7-pillar world-class execution plan (2026-05-29). Captures current governance authority map as stated by @atlaslattice.
---

# Canon Surface Map

## Purpose

One-page reference for every contributor: what is canon, what is workspace, and who has authority at each layer.

---

## Authority Layers

| Layer | Surface | Current Canon Status | Authority |
|-------|---------|---------------------|-----------|
| **L0 — Canon** | Website (`atlaslatticev5bot.manus.space`) | ✅ **Current canon surface** | @atlaslattice adjudication |
| **L1 — Workspace** | GitHub (`atlaslattice/manus-artifacts`) | 🔵 High-velocity candidate workspace | Enables lattice build; no self-canon |
| **L2 — Working Vault** | Notion | 🔵 Living workspace | Relay/working layer |
| **L3 — Working Vault** | Google Drive | 🔵 Living workspace | Relay/working layer |

---

## Canonization Path

```
Artifact Created (GitHub candidate)
       ↓
Indexing + Cleanup (GitHub workspace)
       ↓
Council Review (Pantheon Council AI review)
       ↓
Human Adjudication (@atlaslattice or qualified human)
       ↓
Ratification Event (ratification_event_id assigned)
       ↓
Canon Promotion (published to canon surface)
```

---

## What "Canon" Requires

Every artifact claiming canonical status **must** have all of the following:

| Field | Required Value |
|-------|---------------|
| `ratification_event_id` | Stable dated event ID (not `pending`) |
| `canon_status` | `ratified` or `canonical` |
| `trust_state` | `VERIFIED` |
| Adjudicator on record | `@atlaslattice` or qualified human delegate |

See [Canon Status Model](./CANON_STATUS_MODEL.md) for full field definitions.

---

## What This Means for Contributors

- **All GitHub artifacts are candidates** until explicitly ratified. This is correct behavior — not a deficiency.
- **GitHub is the right place to do the work.** The lattice build, the 12×12×12 KG, the swarm execution — all happen here.
- **Do not claim canonical status in documents.** Use `status: candidate` in frontmatter.
- **Do not modify `(Canonical)` artifacts** without opening an RFC issue first.

---

## Fork Synthesis Policy

See [FORK_POLICY.md](../archive/forks/FORK_POLICY.md) for rules on incorporating GitHub forks to synthesize missing components.

---

## Cross-References

- [Canon Status Model](./CANON_STATUS_MODEL.md)
- [Ratification Workflow](./RATIFICATION_WORKFLOW.md)
- [Canon Decision Ledger](./CANON_DECISION_LEDGER.md)
- [Adjudication Trail](./ADJUDICATION_TRAIL.md)
- [Universal Frontmatter Schema](./UNIVERSAL_FRONTMATTER_SCHEMA.md)

---

*Last updated: 2026-05-29 · Status: Candidate · License: MIT*
