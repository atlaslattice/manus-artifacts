# Questboard — 2026-05-28

> **Status:** CANDIDATE  
> **Artifact Type:** active questboard  
> **Date:** 2026-05-28  
> **Related:** [Quest Types](./quest-types.md), [Quest-to-Task Map](./quest-to-task-map.md), [Benchmark Scorecard](../benchmark/scorecard-2026-05-28.md)

## Open Quests

### QST-001 — Backfill Stable IDs for High-Value Docs
<!-- METADATA
stable_id: AL-AF-104
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

- **Type:** `BACKFILL`
- **Description:** Add stable IDs, lifecycle state, owner, and creation date blocks to priority `docs/` and `projects/` artifacts still missing metadata.
- **Acceptance Criteria:** Touched files include the required fields and validation output is captured.
- **Linked Artifact:** [Metadata Coverage Report](../metadata-coverage-report-2026-05-28.md)
- **Status:** `OPEN`

### QST-002 — Repair Aluminum OS ↔ Core Cross-Links
- **Type:** `CROSSLINK`
- **Description:** Improve navigation between Aluminum OS concept docs and the Rust implementation entry point.
- **Acceptance Criteria:** Concept, implementation, and test entry points link to one another clearly.
- **Linked Artifact:** [Domain Normalization Matrix](../domain-normalization-matrix-2026-05-28.md)
- **Status:** `OPEN`

### QST-003 — Intake Next External Archive Drop
- **Type:** `INTAKE`
- **Description:** Pull the next Notion/Drive artifact into the repo using the intake standards, receipt template, and triage classes.
- **Acceptance Criteria:** Imported artifact has provenance, kebab-case naming, receipt, and registry-ready metadata.
- **Linked Artifact:** [Intake Standards](../intake/migration-standards-v0.1.md)
- **Status:** `OPEN`

### QST-004 — Add Evidence for the ID/Lifecycle Contract
- **Type:** `EVIDENCE`
- **Description:** Create an evidence record for `AL-KG-003` so the contract has explicit build provenance.
- **Acceptance Criteria:** Evidence entry references the artifact, the agent/process, and at least one validation run.
- **Linked Artifact:** [Artifact ID and Lifecycle Contract](../knowledge-graph/ARTIFACT_ID_AND_LIFECYCLE_CONTRACT_v0_1.md)
- **Status:** `OPEN`

### QST-005 — Normalize `docs/` Landing Surface
- **Type:** `POLISH`
- **Description:** Create or improve a domain README for `docs/` so new readers can orient quickly.
- **Acceptance Criteria:** README exists, uses standard navigation sections, and links to `START_HERE` and `ARCHIVE_INDEX`.
- **Linked Artifact:** [Domain Normalization Matrix](../domain-normalization-matrix-2026-05-28.md)
- **Status:** `OPEN`

### QST-006 — Normalize `projects/` Landing Surface
- **Type:** `POLISH`
- **Description:** Create a standard README for the `projects/` domain so initiative overviews are easier to browse.
- **Acceptance Criteria:** README exists and points to flagship projects plus contribution paths.
- **Linked Artifact:** [Archive Index](../ARCHIVE_INDEX.md)
- **Status:** `OPEN`

### QST-007 — Mark Superseded Artifacts with Replacement Links
- **Type:** `DEPRECATE`
- **Description:** Identify any superseded candidate artifacts and add deprecation notices that preserve inbound links.
- **Acceptance Criteria:** Deprecated files state the replacement path and reason without deleting history.
- **Linked Artifact:** [Deprecation Policy](../deprecation-policy.md)
- **Status:** `OPEN`

### QST-008 — Run Metadata and Provenance Sweep
- **Type:** `VALIDATE`
- **Description:** Execute metadata completeness and provenance validation as a recurring hygiene quest.
- **Acceptance Criteria:** Commands, outcomes, date, and follow-up actions are recorded in a receipt.
- **Linked Artifact:** [Validation Receipt Format](../validation-receipt-format-v0.1.md)
- **Status:** `OPEN`

### QST-009 — Capture Full Archive Validation Receipt
- **Type:** `VALIDATE`
- **Description:** Run artifact graph and reference checks after significant curation work.
- **Acceptance Criteria:** Graph validator, adversarial suite, and GPTBrain checks are all logged in one dated receipt.
- **Linked Artifact:** [Archive Health Status](../archive-health-status-2026-05-28.md)
- **Status:** `OPEN`

### QST-010 — Prepare Ratification Packet for AL-MISSION-001
- **Type:** `RATIFY`
- **Description:** Assemble the mission charter packet with evidence, validation, and blocking issues resolved.
- **Acceptance Criteria:** Packet meets the ratification requirements and is ready for `@atlaslattice` review.
- **Linked Artifact:** [Mission Charter](../../projects/AETHERFORGE_LATTICE_GPTDREAM_MISSION_CHARTER_v0.1.md)
- **Status:** `OPEN`

### QST-011 — Prepare Ratification Packet for AL-KG-003
- **Type:** `RATIFY`
- **Description:** Move the ID/lifecycle contract from candidate to review-ready packet status.
- **Acceptance Criteria:** Packet contains validation evidence, metadata checks, and a completed checklist.
- **Linked Artifact:** [AL-KG-003 Contract](../knowledge-graph/ARTIFACT_ID_AND_LIFECYCLE_CONTRACT_v0_1.md)
- **Status:** `OPEN`

### QST-012 — Prepare Ratification Packet for AL-RT-001
- **Type:** `RATIFY`
- **Description:** Package the trust flow doctrine for adjudication with supporting governance evidence.
- **Acceptance Criteria:** Trust rubric, checklist, evidence status, and submission note are bundled.
- **Linked Artifact:** [Ratification and Trust Flow](../RATIFICATION_AND_TRUST_FLOW.md)
- **Status:** `OPEN`
