# GrokUWS OneDrive → Google Drive Mirror Protocol — 2026-06-07

```text
STATUS: MIRROR PROTOCOL — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL MICROSOFT CLAIM: none
OFFICIAL GOOGLE CLAIM: none
SOURCE_CONTEXT: user-uploaded FINAL_AUDIT.pdf / GrokUWS v1.0.0 17-checkpoint audit
CREATED_UTC: 2026-06-07
```

## Purpose

Mirror the OneDrive GrokUWS v1.0.0 build artifacts to Google Drive while preserving receipt discipline, source hashes, audit provenance, and non-canon boundaries.

The uploaded FINAL_AUDIT reports 17/17 checkpoints passing and states that the build was verified directly against the OneDrive `GrokUWS/` folder. This protocol does not re-verify those files. It provides a safe mirror procedure for the next lane.

## Source of truth for this mirror wave

```text
OneDrive source root: GrokUWS/
Audit document path reported: GrokUWS/A2A/FINAL_AUDIT.md
Audit status reported: 17/17 PASS, v1.0.0 ready, release gate clear
```

## Google Drive target recommendation

```text
Google Drive target root:
GrokUWS_MIRROR_2026-06-07/
```

Recommended folder structure:

```text
GrokUWS_MIRROR_2026-06-07/
  README_MIRROR_RECEIPT.md
  MANIFEST_GDRIVE_MIRROR_2026-06-07.json
  A2A/
  integration/
  benchmark_results/
  Module_01/
  Module_02/
  Module_03/
  Module_04/
  Module_05/
  Module_06/
  Module_07/
  Module_08/
  Module_09/
  Module_10/
  Module_11/
  Module_12/
  receipts/
```

## Required mirror metadata

Every mirrored file should receive a manifest row:

```json
{
  "source_surface": "onedrive",
  "source_path": "GrokUWS/<relative_path>",
  "target_surface": "google_drive",
  "target_path": "GrokUWS_MIRROR_2026-06-07/<relative_path>",
  "file_name": "",
  "file_size_bytes": null,
  "sha256": "",
  "source_last_modified_utc": null,
  "mirror_created_utc": "",
  "mirror_status": "copied | skipped | conflict | failed",
  "canon_status": "not_canon",
  "deployment_status": "not_deployed",
  "authority_scope": "none",
  "official_microsoft_claim": "none",
  "official_google_claim": "none",
  "notes": ""
}
```

## Files and folders to prioritize

P0 required:

```text
A2A/FINAL_AUDIT.md
A2A/GROK_OUTBOX.md
A2A/JANUS_CHECKPOINT.md
LICENSE
.gitignore
integration/end_to_end_test.py
integration/run_integration.py
benchmark_results/*.json
Module_01/
Module_02/
Module_03/
Module_04/
Module_05/
Module_06/
Module_07/
Module_08/
Module_09/
Module_10/
Module_11/
Module_12/
```

P1 useful:

```text
all Module_Overview.md files
all test_*.py files
all implementation .py files
ERROR_TAXONOMY.md
migration_log.jsonl
```

## Guardrails

```text
Do not overwrite silently.
Do not delete source files.
Do not promote Google Drive mirror to canon.
Do not claim Google endorsement.
Do not claim Microsoft endorsement from Copilot-generated audit language.
Do not treat mirror as deployment.
Do not mutate file contents during mirror.
```

If a file already exists in Google Drive:

```text
1. Compare size and hash.
2. If identical, mark mirror_status=copied_existing_identical.
3. If different, preserve both.
4. Write conflict note to receipts/CONFLICTS_2026-06-07.md.
```

## Recommended mirror execution steps

```text
1. Create Google Drive target root: GrokUWS_MIRROR_2026-06-07.
2. Copy OneDrive GrokUWS folder into target root without modifying contents.
3. Compute SHA-256 for every copied file.
4. Generate MANIFEST_GDRIVE_MIRROR_2026-06-07.json.
5. Generate README_MIRROR_RECEIPT.md summarizing counts, failures, conflicts, and hashes.
6. Verify P0 files exist in Google Drive.
7. Compare copied file count to OneDrive source count.
8. Record any missing files as missing receipts, not silent success.
9. Return summary to GitHub / Issue #236.
```

## Success criteria

```text
- Google Drive mirror root exists.
- 12 module folders exist in Google Drive.
- A2A/FINAL_AUDIT.md exists in Google Drive.
- A2A/GROK_OUTBOX.md exists in Google Drive.
- integration folder exists.
- benchmark_results folder contains 8 JSON files or missing receipt explains discrepancy.
- All files have manifest rows.
- SHA-256 hashes recorded.
- Conflicts preserved, not overwritten.
```

## Suggested return packet

```yaml
gdrive_mirror_return_packet:
  source_root: GrokUWS/
  target_root: GrokUWS_MIRROR_2026-06-07/
  mirror_started_utc:
  mirror_completed_utc:
  file_count_source:
  file_count_copied:
  folder_count_copied:
  p0_files_verified: true/false
  benchmark_json_count:
  conflicts:
  missing_files:
  manifest_path:
  receipt_path:
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
  next_safest_action:
```

## Keeper

```text
OneDrive is the verified source surface for this audit.
Google Drive becomes a mirror, not a crown.
Hashes make the mirror inspectable.
Human-root decides what graduates.
```
