# Aetherforge Game Loop Specification v0.1

> **Status:** CANDIDATE
> **Artifact Type:** spec
> **Stable ID:** AL-AF-001
> **Date:** 2026-05-27

## Purpose

Define Aetherforge as the default interaction layer for archive work so curation is consistently playable and auditable.

## Core Loop

1. **Quest Intake**
   - Pull candidate tasks from taskboards, issues, or curation backlog.
   - Assign quest class: `taxonomy`, `cross-link`, `quality-gate`, `project-polish`, `governance`.
2. **Archive Challenge**
   - Perform targeted artifact edits tied to quest objectives.
   - Preserve provenance and candidate/canon boundaries.
3. **Validation Gate**
   - Run existing repository checks relevant to touched surfaces.
   - Record pass/fail and unresolved risk notes.
4. **Reward and Progression**
   - Mark quest complete in sprint board.
   - Link outputs into artifact registry.
   - Promote to next ring/sprint queue.

## Quest Definition Contract

Each quest should include:

- quest_id
- objective
- target artifacts
- acceptance checks
- ratification implications
- follow-up links

## Progression Model

- **Ring I:** Canon + structure
- **Ring II:** Quality gates + reliability
- **Ring III:** Discoverability + graph depth
- **Ring IV:** Governance + trust
- **Ring V:** Public showcase + adoption

## Required Outputs per Quest

- Updated artifact(s)
- Updated links in `artifact_registry.v0_1.json` when net-new mission artifacts are added
- Validation evidence (commands + outcomes)
