# GPTDream++ Schemas

**Status:** CANDIDATE SCHEMA INDEX — NOT CANON  
**Purpose:** Collect v1 packet schemas for GPTDream++ dream/play residue, native-thread ingestion, and memory packet generation.

## Boundary

```text
These schemas are candidate validation scaffolds.
They are not canon.
They are not deployment evidence.
They do not validate GPTDream++ performance.
They do not grant native memory, authority, or runtime status.
```

## Schemas

| Schema | Path | Purpose |
|---|---|---|
| Dream Cycle Packet v1 | `schemas/gptdream/dream_cycle_packet.v1.yaml` | Wake report for bounded sleep/play/dream cycles. |
| Native Thread Ingestion Packet v1 | `schemas/gptdream/native_thread_ingestion_packet.v1.yaml` | Active-thread/session ingestion metadata with raw export boundaries. |
| Memory Packet v1 | `schemas/gptdream/memory_packet.v1.yaml` | Candidate context surface derived from dream residue or native-thread ingestion. |

## Core Required Boundaries

```text
canon_status: not_canon
authority_effect: none
deployment_status: not_deployed
false_authority_risk: required
raw_export_status: required
```

## Raw Export Rule

```text
If raw_export_status indicates full raw export exists,
then a path/location and sha256 must be provided.
```

## Keeper Rule

```text
Dreams can produce residue.
Schemas make residue reviewable.
Receipts make residue durable.
Humans decide what advances.
```

## Status

Candidate schema index. Not canon.
