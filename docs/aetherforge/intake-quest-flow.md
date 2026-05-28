# Intake Quest Flow

> **Status:** CANDIDATE  
> **Artifact Type:** flow checklist  
> **Date:** 2026-05-28  
> **Related:** [Intake Standards](../intake/migration-standards-v0.1.md), [Import Triage Classes](../intake/import-triage-classes.md), [Import Receipt Template](../intake/import-receipt-template.md)

## Eight-Step Flow

<!-- METADATA
stable_id: AL-AF-106
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

1. **Capture source** — confirm the Notion/Drive document exists, is readable, and has a durable source URL.  
   **Acceptance:** source title, URL, and creation date are known.
2. **Assign triage class** — decide `PRESERVE`, `NORMALIZE`, `DEPRECATE`, or `REJECT`.  
   **Acceptance:** class and rationale are recorded.
3. **Choose destination path** — map the artifact into the right repo domain and kebab-case filename.  
   **Acceptance:** destination path is stable and collision-free.
4. **Preserve provenance** — copy original creation date, source system, and source URL into the artifact.  
   **Acceptance:** provenance block survives the migration.
5. **Normalize structure if needed** — add candidate notice, headers, and repo-standard link sections.  
   **Acceptance:** artifact matches current markdown conventions.
6. **Complete required metadata** — add owner, lifecycle, artifact type, and any stable ID if assigned.  
   **Acceptance:** metadata fields satisfy the intake standard.
7. **Run validation** — execute `python3 scripts/validate_metadata_completeness.py` and any relevant file-specific checks.  
   **Acceptance:** validation outcome is captured in the receipt.
8. **Register in KG** — add or queue the artifact for registry inclusion once it passes quality checks.  
   **Acceptance:** the artifact is registry-ready or explicitly queued with blockers.
