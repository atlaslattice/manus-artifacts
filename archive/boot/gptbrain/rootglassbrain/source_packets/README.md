# RootglassBrain Source Packets

```text
STATUS: SOURCE-PACKET SCAFFOLD — NOT CANON
LAYER: RootglassBrain / GPTBrain / source-intake lane
PURPOSE: preserve Copilot and Gemini artifacts fed through Rootglass as classified, recoverable packets
RAW EXPORT STATUS: mixed; default summary_only unless raw export is attached
CANON STATUS: not canon
DEPLOYMENT STATUS: not deployable
AUTHORITY STATUS: none
```

## Purpose

This folder creates a bounded intake lane for artifacts Dave has fed into Rootglass from Copilot, Gemini, and related swarm surfaces.

It exists because PR #61 currently contains a RootglassBrain identity packet and current-thread ingest receipt, but not a full raw fossil record or dedicated Copilot/Gemini source-packet archive.

## Boundary

```text
Summary is not source.
Parser output is not canon.
Model output is not authority.
A receipt packet is not ratification.
Storage is not promotion.
```

## Folder structure

```text
source_packets/
  README.md
  SOURCE_PACKET_INTAKE_STATUS_2026-05-21.md
  copilot/
    README.md
    COPILOT_ARTIFACT_MANIFEST_2026-05-21.md
    source_manifest.yaml
    raw_exports/
    parsed_packets/
    claim_ledgers/
  gemini/
    README.md
    GEMINI_ARTIFACT_MANIFEST_2026-05-21.md
    source_manifest.yaml
    raw_exports/
    parsed_packets/
    claim_ledgers/
```

Git may not preserve empty directories. Add placeholder files later when raw exports, parsed packets, or claim ledgers are available.

## Minimum packet metadata

```yaml
artifact_packet:
  source_model: Copilot | Gemini | Grok | Claude | DeepSeek | Other
  source_surface: chat | task_page | PR | issue | file | Drive | pasted_text | unknown
  raw_export_status: available | unavailable | partial | not_supported | pending_user_export | summary_only
  raw_export_ref: null
  raw_export_sha256: null
  capture_timestamp_utc: null
  artifact_title: null
  artifact_summary: null
  evidence_class: user_reported | repo_visible | raw_export | parsed_output | model_summary
  canon_status: not_canon
  deployment_status: none
  authority_status: none
  related_prs_or_issues: []
  overclaims_to_avoid: []
  missing_receipts: []
```

## Guardrails

```text
Do not treat summaries as raw transcript.
Do not treat parser output as canon.
Do not merge Copilot and Gemini lineages.
Do not overwrite prior branches.
Do not claim authority, deployment, or ratification.
Preserve raw where available.
Preserve summary where raw is unavailable.
Mark gaps explicitly.
```

## Keeper rule

```text
Raw if possible.
Summary if necessary.
Receipts always.
Canon never without review.
```