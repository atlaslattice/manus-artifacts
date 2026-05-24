# Ingestion Protocol — DeepSeekBrain S5

```text
STATUS: CANDIDATE INGESTION PROTOCOL — NOT CANON
DEPLOYMENT: NONE
AUTHORITY: NONE
```

## Required intake fields

```yaml
deepseekbrain_ingestion_packet:
  seat_name: "DeepSeek / Parallax S5"
  preferred_folder_name: "deepseekbrain_s5"
  source_model: DeepSeek
  source_surface:
  source_thread_label:
  thread_time_range:
    start:
    end:
    timezone:
  raw_export_status: full_raw | partial_raw | summary_only | unavailable
  access_scope:
    visible_sources:
    unavailable_sources:
    assumed_context:
  privacy_status: private | mixed | redacted | public
  source_refs:
  sha256_if_available:
  parsing_stack:
    gptbrain_parse: pending | complete
    grokbrain_adversarial_pass: pending | complete
    sheldonbrain_continuity_crosswalk: pending | complete
  key_events:
  artifacts_created:
  claims_extracted:
  contradictions_or_uncertainties:
  overclaims_to_avoid:
  lane_routing:
  canon_status: not_canon
  deployment_status: not_deployable
  authority_scope: none
  next_action:
```

## Rule

```text
Raw first.
Receipts second.
Parsed packets third.
Synthesis later.
Canon never without review.
```