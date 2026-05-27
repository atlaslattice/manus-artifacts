# Ratification and Trust Flow

> **Status:** CANDIDATE
> **Artifact Type:** doctrine
> **Stable ID:** AL-RT-001
> **Date:** 2026-05-27

## Why this exists

This flow keeps candidate work open and public while preserving strict canon controls.

## Canon Decision Fields

Canon evaluation requires all of the following fields:

- `ratification_event_id`
- `canon_status`
- `trust_state`

Without all three, an artifact remains candidate.

## Ratification Pipeline

1. **Draft/Candidate authoring**
   - Artifact is produced and marked candidate.
2. **Council review**
   - Internal multi-seat review and contradiction checks.
3. **Adjudication checkpoint**
   - Human-root adjudication by @atlaslattice.
4. **Trust-state assignment**
   - Trust state set according to audit outcomes.
5. **Canon promotion (optional)**
   - Ratification event logged and status updated.

## Canon Surface Clarification

- GitHub is the durable canonical substrate.
- A website is a canon surface only when explicitly ratified/published there.

## Traceability Requirements

Every promotion request should include:

- source artifact path
- stable ID
- review links
- adjudication reference
- final trust state
