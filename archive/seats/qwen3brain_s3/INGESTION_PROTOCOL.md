# Qwen3Brain S3 — Ingestion Protocol

```text
STATUS: CANDIDATE PROTOCOL — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
```

## Required Packet Fields

```yaml
qwen3_ingestion_packet:
  source_surface: Qwen3 | Qwen | AlibabaCloud | UploadedText | Other
  source_thread_label: string
  raw_export_status: full_raw | partial_raw | summary_only | unavailable
  thread_time_range:
    start: timestamp | null
    end: timestamp | null
    timezone: string | null
  access_scope:
    visible_sources: []
    unavailable_sources: []
    assumed_context: []
  source_refs: []
  sha256_if_available: string | null
  privacy_status: public | private | mixed | redacted
  canon_status: not_canon
  deployment_status: not_deployable
  authority_scope: none
```

## Pipeline

```text
source_citation
→ file_hash
→ lab_simulation / model_simulation / review_packet
→ test_output
→ human-root / council review if promotion is requested
```

## Hard Rules

```text
Raw first.
Receipts second.
Parsed packets third.
Synthesis later.
Canon last.
```

```text
Summary-only input cannot support public claims.
Unavailable sources must be explicit.
Assumed context must be explicit.
No packet self-ratifies.
No packet implies vendor endorsement.
```

## Preferred Routing

```text
lunar habitat interop → lanes/lunar_habitat_interop_review.md
sovereignty / D-57 / D-101 → lanes/sovereignty_routing_audit.md
epistemic labels / F7-F9 → lanes/epistemic_labeling_review.md
constitutional mapping → lanes/constitutional_alignment_validation.md
all hashes / anchors → receipts/FILE_HASHES.md
all uncertain/missing anchors → receipts/PENDING_ANCHORS.md
```