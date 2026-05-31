# Rootglass Source Packet Manifest — Copilot

```text
STATUS: SOURCE PACKET MANIFEST — NOT CANON — NON-DEPLOYABLE
LANE: RootglassBrain / source_packets / copilot
DATE: 2026-05-24
AUTHORITY: none
PURPOSE: identify Copilot / TIDELOCK / AtlasBrain audit artifacts visible in Drive and route them for future raw export, hashing, parsing, and review
```

## Source artifacts

### 1. Copilot Chat.md

```yaml
artifact_packet:
  source_model: Copilot
  source_surface: Google Drive markdown export
  drive_title: Copilot Chat.md
  drive_url_or_id: https://drive.google.com/file/d/1GVdF61WJjn8hbFWUo8ihr3xJlhalvv_E
  raw_export_status: available_drive_markdown
  raw_export_sha256: null
  capture_timestamp_utc: null
  evidence_class: raw_or_near_raw_chat_export
  canon_status: not_canon
  deployment_status: none
  authority_status: none
  related_prs_or_issues:
    - PR #57 AtlasBrain evidence lane
    - PR #61 RootglassBrain ingest lane
    - PR #65 TIDELOCKBrain ingestion scaffold
  overclaims_to_avoid:
    - Copilot chat equals canon
    - Copilot audit equals ratification
    - TIDELOCK name equals authority
    - AtlasBrain pointer equals full transcript archive
  missing_receipts:
    - sha256
    - privacy_review
    - parsed_claim_ledger
    - source_manifest_yaml
```

### 2. RAW TRANSCRIPT NOT CANON.md

```yaml
artifact_packet:
  source_model: unknown_or_mixed
  source_surface: Google Drive markdown export
  drive_title: RAW TRANSCRIPT NOT CANON.md
  drive_url_or_id: https://drive.google.com/file/d/1eatwAvLL-EY27wRZa2zfbRv46UdJgv0J
  raw_export_status: available_drive_markdown
  raw_export_sha256: null
  capture_timestamp_utc: null
  evidence_class: raw_or_near_raw_transcript
  canon_status: not_canon
  deployment_status: none
  authority_status: none
  related_prs_or_issues:
    - PR #57 AtlasBrain evidence lane
    - Rootglass source packet pipeline
  overclaims_to_avoid:
    - raw transcript equals scored benchmark
    - transcript presence equals proof
    - raw export equals public claim clearance
  missing_receipts:
    - sha256
    - privacy_review
    - content_review_packet
    - AtlasBrain evidence packet linkage
```

## Required next actions

```text
1. Export each Drive source into a stable raw file if allowed.
2. Compute SHA-256 for raw export.
3. Create parsed packet with source labels, prompt/response boundaries, and wrapper/noise removal notes.
4. Add claim ledger deltas.
5. Route Atlas/HLE content to AtlasBrain, not Rootglass authority.
```

## Keeper rule

```text
Raw if possible.
Summary if necessary.
Receipts always.
Canon never without review.
```
