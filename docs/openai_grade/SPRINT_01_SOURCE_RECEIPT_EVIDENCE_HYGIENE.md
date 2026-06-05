# OpenAI Grade Sprint 01 — Source, Receipt, and Evidence Hygiene

```text
STATUS: ACTIVE SPRINT PLAN — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
PARENT: docs/OPENAI_GRADE_12x12_TASK_LATTICE.md / Module 01
CREATED_UTC: 2026-06-03
LANE: GPTBrain / Octaveglass / Lucerna / Hashlight
```

## Purpose

Start the OpenAI Grade work lattice with the highest-leverage foundation: source, receipt, and evidence hygiene.

Everything downstream depends on this:

```text
retrieval quality
evals
claim calibration
public-safe language
Codex patches
KG nodes and edges
website canon crosswalks
OneDrive mirror integrity
```

## Sprint doctrine

```text
Raw before parsed.
Parsed before claim.
Claim before synthesis.
Synthesis before public wording.
Public wording before canon.
Human-root before authority.
```

## Module 01 scope

This sprint covers the first twelve tasks from the OpenAI Grade task lattice.

```text
01.01 Create a single source-status enum used across GitHub, OneDrive, Notion, uploads, and website refs.
01.02 Add raw_export_status to every ingestion packet.
01.03 Add source_surface and source_locator to every claim packet.
01.04 Require SHA-256 or explicit hash_missing_reason for every raw file.
01.05 Create missing_receipts.seed.jsonl for all known gaps.
01.06 Create a receipt-health dashboard grouped by source surface.
01.07 Add a validator proving summary-only material cannot become evidence-complete.
01.08 Add a validator proving a GitHub commit is not website canon.
01.09 Add a validator proving a coordinate is not proof.
01.10 Create a public-safe explanation of receipt classes.
01.11 Create a red/yellow/green evidence quality rubric.
01.12 Emit first EVIDENCE_HEALTH_REPORT.md.
```

## Deliverables

```text
schemas/openai_grade/source-status.enum.yaml
schemas/openai_grade/evidence-anchor.schema.yaml
archive/knowledge_graph/openai_grade/missing_receipts.seed.jsonl
docs/openai_grade/RECEIPT_CLASSES_EXPLAINER.md
docs/openai_grade/EVIDENCE_QUALITY_RUBRIC.md
docs/openai_grade/EVIDENCE_HEALTH_REPORT.md
scripts/validate_openai_grade_evidence.py
```

## Source-status enum draft

```yaml
source_status_enum:
  raw_available:
    meaning: full raw source is available and preservable
  raw_hashed:
    meaning: full raw source is available with SHA-256 hash
  partial_raw:
    meaning: partial raw source available; completeness not claimed
  pointer_only:
    meaning: source pointer exists but raw content not attached
  summary_only:
    meaning: only a summary exists; cannot support high-confidence claims
  mirror_reported:
    meaning: mirror has been reported but not independently verified
  mirror_verified:
    meaning: mirror path and source receipt have been verified
  confidential_quarantine:
    meaning: raw source exists but must not be publicly mirrored
  missing:
    meaning: source is referenced but not located
  unknown:
    meaning: status has not yet been inspected
```

## Evidence quality rubric draft

```text
GREEN: source is public/allowed, raw or hashed, locator stable, claim scope narrow, no authority/deployment overclaim.
YELLOW: partial source, pointer-only source, stale mirror, or model-generated summary that needs review.
RED: confidential/quarantined source, missing raw, unsupported officiality, deployment claim without receipt, or summary-only used as proof.
```

## Validator requirements

Validator should fail or warn when:

```text
- claim has no source_surface
- claim has no source_locator
- claim cites summary_only as evidence_complete
- claim has canon_status=website_canon without website URL
- claim has deployment_status=deployed_with_receipt without deployment evidence
- coordinate assignment changes canon_status
- confidential_quarantine is mirrored publicly
- hash_missing_reason is absent when SHA-256 is missing
```

## Initial missing-receipt classes

```text
website_canon_url_missing
raw_transcript_hash_missing
onedrive_mirror_hash_missing
notion_child_export_missing
github_workflow_logs_missing
runtime_count_clean_clone_missing
confidential_source_public_derivative_review_missing
company_participation_receipt_missing
```

## Definition of Done

```text
A reviewer can pick any claim and see source status.
A reviewer can tell raw, partial, pointer-only, summary-only, quarantined, and missing apart.
A reviewer can see why a claim is green/yellow/red.
Validators prevent summary-only, coordinate-only, or GitHub-only evidence from becoming canon by accident.
```

## Keeper

```text
Receipts first.
Evidence has state.
State prevents overclaim.
OpenAI Grade starts with knowing what we actually know.
```