# Intake Checklist

> **Status:** CANDIDATE  
> **Artifact Type:** checklist  
> **Date:** 2026-05-28  
> **Related:** [Migration Standards](./migration-standards-v0.1.md), [Import Triage Classes](./import-triage-classes.md), [Import Receipt Template](./import-receipt-template.md)

<!-- METADATA
stable_id: AL-SYS-204
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

- [ ] Confirm source title, source system, and source URL. **Acceptance:** source lineage is explicitly known. **Link:** [Migration Standards](./migration-standards-v0.1.md)
- [ ] Capture original creation date. **Acceptance:** original date or best-known estimate is preserved. **Link:** [Migration Standards](./migration-standards-v0.1.md)
- [ ] Assign a triage class. **Acceptance:** `PRESERVE`, `NORMALIZE`, `DEPRECATE`, or `REJECT` is recorded with rationale. **Link:** [Import Triage Classes](./import-triage-classes.md)
- [ ] Choose a destination path and filename. **Acceptance:** path is stable and filename is kebab-case for new imports. **Link:** [Migration Standards](./migration-standards-v0.1.md)
- [ ] Add candidate status notice. **Acceptance:** imported artifact opens with explicit candidate posture. **Link:** [Contributor Decision Tree](../contributor-decision-tree.md)
- [ ] Preserve provenance in the body or metadata block. **Acceptance:** source URL and original date remain visible. **Link:** [Migration Standards](./migration-standards-v0.1.md)
- [ ] Normalize headings and navigation. **Acceptance:** ATX headers and related-doc links are present. **Link:** [Import Triage Classes](./import-triage-classes.md)
- [ ] Add required metadata fields. **Acceptance:** owner, artifact type, lifecycle, and import date are present. **Link:** [Migration Standards](./migration-standards-v0.1.md)
- [ ] Fill the import receipt. **Acceptance:** all required receipt fields are complete. **Link:** [Import Receipt Template](./import-receipt-template.md)
- [ ] Run metadata validation. **Acceptance:** `python3 scripts/validate_metadata_completeness.py` outcome is recorded. **Link:** [Migration Standards](./migration-standards-v0.1.md)
- [ ] Decide registry readiness. **Acceptance:** artifact is either queued for KG registration or blocked with a reason. **Link:** [Knowledge Graph Topic](../topics/knowledge-graph.md)
- [ ] Update the IP tracker or backlog. **Acceptance:** intake queue reflects the new state. **Link:** [IP-500 Tracker](./ip-500-tracker.md)
