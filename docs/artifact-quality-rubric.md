# Artifact Quality Rubric

<!-- METADATA
stable_id: AL-ARCH-007
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

> **Status:** CANDIDATE  
> **Artifact Type:** rubric / guide  
> **Stable ID:** AL-ARCH-007
> **Date:** 2026-05-28  
> **Related:** [Evidence standards](./evidence-standards.md), [Contributor decision tree](./contributor-decision-tree.md), [Review SLA](./review-sla.md)

## Purpose

Use this rubric to score whether an Atlas Lattice artifact is public-ready, reviewable, and structurally integrated into the archive.

## Dimensions

### 1. Structure

How clearly the artifact is organized, titled, versioned, and status-marked.

- **3/3 — Good:** clear title, candidate notice, version/date, readable sections, stable path
- **2/3 — Acceptable:** mostly organized but missing one structural element
- **1/3 — Needs work:** hard to navigate, inconsistent naming, or missing status/version context

### 2. Provenance

How well the artifact explains origin, authorship context, and source lineage.

- **3/3 — Good:** source, date, authorship context, and trust limits are explicit
- **2/3 — Acceptable:** partial provenance is present but incomplete
- **1/3 — Needs work:** provenance is implied or absent

### 3. Graph Integration

How well the artifact connects to registry, schema, or related system documents.

- **3/3 — Good:** links cleanly into the knowledge graph and related docs
- **2/3 — Acceptable:** some links exist but graph positioning is incomplete
- **1/3 — Needs work:** artifact is isolated and hard to place in system context

### 4. Discoverability

How easy it is for a new contributor or reviewer to find and use the artifact.

- **3/3 — Good:** linked from index or workflow docs, named clearly, easy to search
- **2/3 — Acceptable:** discoverable with some effort
- **1/3 — Needs work:** buried, ambiguously named, or unlinked

### 5. Evidence

How well claims about the artifact are backed by evidence entries or receipts.

- **3/3 — Good:** dedicated evidence entry or receipt exists and is reviewable
- **2/3 — Acceptable:** evidence exists indirectly but is not normalized yet
- **1/3 — Needs work:** claims are unsupported or unverifiable

## Scoring formula

Total score = `Structure + Provenance + Graph Integration + Discoverability + Evidence`

- **13–15:** world-class / public-ready
- **10–12:** strong candidate
- **7–9:** usable but needs hardening
- **5–6:** not ready for broad public reliance

## Example scored artifact

### `projects/AETHERFORGE_LATTICE_GPTDREAM_MISSION_CHARTER_v0.1.md`

| Dimension | Score | Reason |
|---|---:|---|
| Structure | 3 | Clear title, candidate notice, date, stable ID, and sections |
| Provenance | 2 | Good mission framing, but limited standalone provenance details |
| Graph Integration | 3 | Linked from registry and multiple contributor docs |
| Discoverability | 3 | Easy to find from `README.md`, `START_HERE.md`, and governance docs |
| Evidence | 3 | Covered by [EVID-GOV-001](./evidence/EVID-GOV-001.json) |
| **Total** | **14/15** | **World-class / public-ready candidate** |
