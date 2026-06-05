# GPTBrain Packet Schema

```text
STATUS: CANDIDATE SCHEMA — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
OFFICIALITY: not an official OpenAI statement
PURPOSE: standardize GPT-side packets for native-thread ingestion, review routing, and OpenAI-first operability
```

## Rule

```text
A packet can organize work.
It cannot crown work.
```

## Required packet spine

```yaml
packet_id: required
packet_type: required
created_utc: required
operator: required
source_refs: required
raw_export_status: required
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
proof_status: not_a_proof
privacy_status: required
rights_status: required
strongest_safe_claim: required
overclaims_to_avoid: required
missing_receipts: required
contradictions: []
next_safe_action: required
human_gate_required: true
```

## raw_export_status

Allowed values:

```text
full_raw
partial_raw
summary_only
unavailable
unknown
```

No packet may imply raw lineage preservation unless:

```text
raw_export_status = full_raw
```

## Packet types

```text
native_thread_ingestion
source_record
claim_packet
artifact_packet
review_packet
public_release_packet
codex_patch_packet
external_signal_packet
math_sandbox_packet
```

## Authority boundary

```text
packet_status != canon_status
review_status != ratification
repo_visible != canon
model_output != proof
```

## Keeper lines

```text
Receipts preserve.
Packets route.
Humans ratify.
```

```text
Raw thread first.
Parsed packet second.
Fresh synthesis later.
Canon last.
```
