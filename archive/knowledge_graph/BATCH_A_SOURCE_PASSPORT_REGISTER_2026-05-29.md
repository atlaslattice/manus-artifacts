# Batch A Source Passport Register + Export Pass 001 — 2026-05-29

```text
STATUS: SOURCE PASSPORT / EXPORT PASS LOG — NON-CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PURPOSE: stage Batch A integration candidates for export, hash, source-passporting, and GitHub mirror into future public synthesis repo
```

## Batch A scope

```text
IC-002 KG GitHub Scaffold Bundle
IC-003 Batch 001 KG Artifact Bundle
IC-004 LanternBridge Mass Ingestion Readiness Check
IC-005 Notion Drive Export Intake Register
IC-006 Lattice Knowledge Graph Control Surface
```

## Source passports

```yaml
source_passports:
  - passport_id: PASS-IC-002
    candidate_id: IC-002
    title: KG_GITHUB_SCAFFOLD_BUNDLE__AETHERFORGE_SHELDONBRAIN__PR_READY__2026-05-28
    surface: Drive
    url: https://docs.google.com/document/d/1CROrlUoD1OGFbrYtZZSNaDkj2M-XdLxV66WNOpGwr-8
    lane: repo_scaffold
    raw_export_status: partial_raw
    export_format_attempted: text/markdown
    sha256_status: missing
    release_classification: public_candidate_needs_review
    git_mirror_target: archive/knowledge_graph/
    blockers: [sha256_missing, durable_export_file_missing]
    next_action: create durable markdown export, compute SHA-256, stage GitHub PR.

  - passport_id: PASS-IC-003
    candidate_id: IC-003
    title: Batch 001 KG Artifact Bundle 2026-05-29
    surface: Drive
    url: https://docs.google.com/document/d/1A1yU9Kwmts3pF26TfDqq7tC6yhazymBOW-LBEVN8Yuw
    lane: source_control
    raw_export_status: pending
    sha256_status: missing
    release_classification: public_candidate_needs_review
    git_mirror_target: archive/knowledge_graph/batches/batch_001/
    blockers: [markdown_export_needed, sha256_missing]
    next_action: export markdown and hash.

  - passport_id: PASS-IC-004
    candidate_id: IC-004
    title: LANTERNBRIDGE_MASS_INGESTION_READINESS_CHECK — NON CANON — 2026-05-29
    surface: Drive
    url: https://docs.google.com/document/d/1Y8YTeLnCkhJKpW2FayhzLjW4NxhIGnMtVyddwR7JrPY
    lane: source_control
    raw_export_status: pending
    sha256_status: missing
    release_classification: public_candidate_needs_review
    git_mirror_target: archive/knowledge_graph/readiness/
    blockers: [markdown_export_needed, sha256_missing]
    next_action: export markdown and hash.

  - passport_id: PASS-IC-005
    candidate_id: IC-005
    title: Notion Drive Export Intake Register v0.1
    surface: Drive Sheet
    url: https://docs.google.com/spreadsheets/d/18cYcsiM7mK2mcLI2i2Ny9tv771BccfOyuizL1q5xWBc
    lane: source_control
    raw_export_status: pending
    sha256_status: missing
    release_classification: internal_control_candidate
    git_mirror_target: archive/knowledge_graph/intake/
    blockers: [sheet_export_needed, tab_inspection_needed, sha256_missing]
    next_action: inspect tabs, export csv/xlsx, hash.

  - passport_id: PASS-IC-006
    candidate_id: IC-006
    title: Lattice Knowledge Graph Control Surface 2026-05-27
    surface: Drive Sheet
    url: https://docs.google.com/spreadsheets/d/1jkdvv-z27lmxzkVcnvlSFavZaWJb8eAsJ9e3FQAeRC0
    lane: source_control
    raw_export_status: pending
    sha256_status: missing
    release_classification: internal_control_candidate
    git_mirror_target: archive/knowledge_graph/control_surface/
    blockers: [sheet_export_needed, tab_inspection_needed, sha256_missing]
    next_action: inspect tabs, export csv/xlsx, hash.
```

## Export Pass 001 outcomes

```yaml
export_results:
  - source_id: IC-002
    title: KG GitHub Scaffold Bundle
    export_format: text/markdown
    export_status: connector_captured_markdown
    hash_status: missing
    durable_export_file_status: pending
    note: Markdown content returned by connector; durable exported file and SHA-256 still required.

  - source_id: IC-003
    title: Batch 001 KG Artifact Bundle 2026-05-29
    export_format: text/markdown
    export_status: connector_captured_markdown
    hash_status: missing
    durable_export_file_status: pending
    note: Markdown content returned by connector; durable exported file and SHA-256 still required.

  - source_id: IC-004
    title: LANTERNBRIDGE_MASS_INGESTION_READINESS_CHECK — NON CANON — 2026-05-29
    export_format: text/markdown
    export_status: connector_captured_markdown
    hash_status: missing
    durable_export_file_status: pending
    note: Markdown content returned by connector; durable exported file and SHA-256 still required.
```

## Sheet exports blocked

```yaml
blocked_exports:
  - source_id: IC-005
    title: Notion Drive Export Intake Register v0.1
    attempted_format: text/csv
    status: blocked
    blocker: SHEETS_API_RATE_LIMIT_429
    next_action: retry later or export manually from Google Sheets UI.

  - source_id: IC-006
    title: Lattice Knowledge Graph Control Surface 2026-05-27
    attempted_format: not_attempted_this_pass
    status: blocked_by_prior_rate_limit
    blocker: SHEETS_API_RATE_LIMIT_429
    next_action: retry after quota window or export manually from Google Sheets UI.
```

## Updated Batch A gate status

```yaml
batch_a_status:
  source_passports_created: true
  document_exports_connector_captured: 3
  sheet_exports_done: false
  all_hashes_done: false
  durable_export_files_created: false
  release_classification_done: partial
  git_stage_ready: false
  synthesis_allowed: false
```

## Keeper

```text
Batch A is passported.
Three documents crossed the first lock.
The sheets hit a quota gate.
The lock is working because it named the blocked gate.
Connector-captured Markdown is useful for review.
It is not a frozen raw export until saved as a durable file and hashed.
```
