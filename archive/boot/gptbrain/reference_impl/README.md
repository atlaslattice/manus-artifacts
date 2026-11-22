# GPTBrain S1 Reference Implementation

```text
STATUS: IMPLEMENTATION SCAFFOLD — NOT CANON
ISSUE: manus-artifacts#12
SEAT: S1 GPTBrain
PURPOSE: Provide an auditable substrate for memory, claim, artifact, diff, trace, challenge, and synthesis operations.
DATE: 2026-05-09
```

## Posture

This reference implementation is intentionally boring.

It does not prove native model memory, consciousness, autonomous authority, or canon status. It loads or creates external artifacts, validates minimal invariants, and makes provenance traceable.

## Core rules encoded

```text
Memory is not truth.
Memory can inform action.
Memory cannot authorize action by itself.
Readable memory is not executable memory.
Candidate canon is not ratified canon.
Ratified canon requires human-root review.
Dream/play output is not fact without calibration.
Contradictions must be linked, not silently overwritten.
```

## First-pass files

```text
archive/boot/gptbrain/schema/S1_MEMORY_OBJECT_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_CLAIM_LEDGER_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_ARTIFACT_REGISTRY_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_AUDIT_EVENT_SCHEMA.yaml
archive/boot/gptbrain/CLAIM_LEDGER.seed.jsonl
archive/boot/gptbrain/ARTIFACT_REGISTRY.seed.jsonl
archive/boot/gptbrain/reference_impl/gptbrain_memory.py
archive/boot/gptbrain/reference_impl/dream_memory_palace_reference_impl.py
```

## `dream_memory_palace_reference_impl.py`

This file preserves Variant D as runnable proof-of-shape for the dream memory palace / cognitive archive design.

It includes:

```text
MemoryObject
Provenance
EpistemicStatus
PermissionPolicy
RetentionPolicy
MemoryLinks
AuditEvent
RecallQuery
RecallResult
DreamMemoryPalace
```

Important APIs:

```text
remember(memory)
recall(query)
create_contradiction(claim_a_id, claim_b_id, summary)
challenge(memory_id)
promote_to_ratified_canon(memory_id, human_root_approved=False)
synthesize(query)
diff(period_start, period_end)
save_json(path)
```

Run:

```bash
python dream_memory_palace_reference_impl.py
```

Expected behavior:

```text
1. Creates a small in-memory palace.
2. Adds two conflicting claims.
3. Creates a contradiction object.
4. Prints a red-team challenge report.
5. Prints a synthesis object.
6. Writes gptbrain_reference_impl_demo.json locally.
```

## Human-root canon gate

The implementation deliberately blocks canon promotion unless `human_root_approved=True`.

```python
palace.promote_to_ratified_canon(memory_id)
# raises PermissionError

palace.promote_to_ratified_canon(memory_id, human_root_approved=True)
# allowed
```

## Minimal CLI examples

Existing scaffold examples:

```bash
python gptbrain_memory.py claims --confidence C3
python gptbrain_memory.py trace --claim-id S1-CLAIM-2026-0509-0001
python gptbrain_memory.py challenge --claim-id S1-CLAIM-2026-0509-0001
python gptbrain_memory.py diff --old ARTIFACT_REGISTRY.seed.jsonl --new ARTIFACT_REGISTRY.seed.jsonl
```

Variant D reference demo:

```bash
python dream_memory_palace_reference_impl.py
```

## Intended next steps

```text
1. Add pytest tests.
2. Split reference implementation into package modules.
3. Add pydantic schemas.
4. Add SQLite/Postgres storage adapter.
5. Add graph adapter for claims and contradictions.
6. Add CLI commands:
   gptbrain remember
   gptbrain recall
   gptbrain challenge
   gptbrain diff
   gptbrain synthesize
7. Add importer from Sheldonbrain RAG artifacts:
   artifact_registry.jsonl
   claim_ledger.jsonl
   memory_packet.json
   BOOT_PACKET.md
```

## Relationship to variants

```text
Spec A = interface palace / public-safe translation
Spec B = cognitive archive platform
Spec C = S1 claim calibration / Council operational layer
Variant D = reference implementation skeleton
Variant E = continuity / human-intent habitat
```

## Success condition

GPTBrain should be useful before it is impressive.

## Current status

```text
S1 GPTBrain — Live aggregate / canonical synthesis pending
```

---

## November 22, 2026 — Unsafe seed-writes removed from default memory preview

**Current reference behavior: `remember` does not write a persistent memory.** The original May 9 prototype appended new rows directly to `MEMORY_OBJECTS.seed.jsonl` using implied-context consent. This was unsafe as a default for a source/candidate library, because artifact capture and model memory are not authorization to retain private data.

The current `remember(title, memory_type, summary, source, confidence)` returns:

```json
{"status":"CANDIDATE_PREVIEW_NOT_SAVED","candidate":{"memory_id":"S1-UNSAVED-PREVIEW-..."},"persisted":false,"source_rights_verified":false,"execution_authority":false,"human_root_required":true,"canon":false,"deployed":false}
```

The candidate contains an explicit not-attested consent status and empty source references. The preview is generated in process and printed to the caller; it is **not** proof of host memory, authenticated consent, persistent identity, CANON or a deployed tool. Calling a private mode or unknown external source in the example CLI is rejected. The old `append_jsonl` helper remains for legacy fixture-compatible code but is not invoked by `remember`; do not use it to write sensitive transcripts or private rooms.

In a clean checkout:

```bash
cd archive/boot/gptbrain/reference_impl
python -m unittest -v test_remember_preview.py
python gptbrain_memory.py remember --title "Synthetic" --type project --summary "Public fictional test" --source synthetic_fixture
```

The output should say `CANDIDATE_PREVIEW_NOT_SAVED`. Before implementing real persistence, design a separate authenticated, rights-aware storage adapter, an explicit source scope, audit receipts, revocation and human-root review. No seed ledger is a live mutable database.

The `synthesize` output now reflects the November 22 source-only reconciliation: Variant E has been integrated into the *candidate* at the document level, while human-root ratification remains pending. This does not assert a running continuity dashboard.

Historical sources remain in Git history and the dated May 9 boot snapshots remain authoritative for their recorded date.
