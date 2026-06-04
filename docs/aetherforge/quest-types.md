# Aetherforge Quest Types

> **Status:** CANDIDATE  
> **Artifact Type:** quest contract  
> **Date:** 2026-05-28  
> **Related:** [Aetherforge README](./README.md), [Quest-to-Task Map](./quest-to-task-map.md), [Validation Receipt Format](../validation-receipt-format-v0.1.md)

## Quest Type Matrix

<!-- METADATA
stable_id: AL-AF-102
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

| Quest Type | Description | Required Inputs | Output Artifact / Receipt | XP |
| --- | --- | --- | --- | ---: |
| `BACKFILL` | Add missing metadata to an existing artifact without changing its core meaning. | Target path, required field checklist, provenance source, stable ID plan. | Updated artifact plus metadata/validation receipt. | 2 |
| `CROSSLINK` | Repair broken, missing, or one-way cross-links between related artifacts. | Source artifact, target artifact, relation rationale, link locations. | Updated links in docs and/or registry plus validation receipt. | 2 |
| `INTAKE` | Migrate a net-new artifact from Notion, Drive, or another working vault into the repo. | Source document, provenance URL, triage class, destination path, import receipt template. | Imported artifact, intake receipt, and registry-ready record. | 4 |
| `EVIDENCE` | Add a machine-readable evidence entry for an AI-built or AI-assisted artifact. | Target artifact ID/path, claim summary, source paths, validation evidence. | New or updated evidence entry linked to the artifact. | 3 |
| `POLISH` | Improve public discoverability, readability, or navigation for an existing artifact. | Target artifact, audience, readability goal, related-doc links. | Improved README/guide/index plus optional validation note. | 2 |
| `DEPRECATE` | Mark a superseded artifact deprecated while preserving its addressability. | Target artifact, replacement artifact, supersession rationale, deprecation notice. | Deprecated artifact with replacement link and audit note. | 1 |
| `VALIDATE` | Run an existing validator or test suite and capture the outcome as a receipt. | Validator command, target scope, prior artifact links, receipt format. | Validation receipt with pass/fail status and notes. | 2 |
| `RATIFY` | Assemble a candidate artifact packet for human-root review. | Artifact path, evidence links, checklist, validation receipts, adjudication request. | Ratification packet and queue update. | 5 |

## Reward Logic

XP measures leverage, not difficulty alone. `RATIFY` and `INTAKE` are highest because they combine curation, provenance, and governance risk. `DEPRECATE` is low XP because the operation is intentionally small and reversible.
