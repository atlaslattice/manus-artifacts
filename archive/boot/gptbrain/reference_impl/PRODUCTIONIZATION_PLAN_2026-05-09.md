# GPTBrain Reference Implementation — Productionization Plan

```text
STATUS: ROADMAP — NOT CANON
SEAT: S1 GPTBrain
PURPOSE: convert the reference implementation into a testable package without losing governance boundaries
DATE: 2026-05-09
```

## Current state

The current implementation is a runnable single-file reference skeleton:

```text
archive/boot/gptbrain/reference_impl/dream_memory_palace_reference_impl.py
```

It now has a first-pass test scaffold:

```text
archive/boot/gptbrain/reference_impl/test_dream_memory_palace_reference_impl.py
```

## Design goal

GPTBrain should be useful before it is impressive.

The system should first become:

```text
testable
boring
auditable
source-grounded
permission-aware
canon-safe
```

Only then should it become:

```text
distributed
agentic
multi-backend
automated
UI-rich
```

## Phase 0 — Freeze invariants

Required invariants:

```text
[ ] Memory is not truth.
[ ] Readable memory is not executable memory.
[ ] Canon promotion requires human-root approval.
[ ] Contradictions are linked, not overwritten.
[ ] Dream/play outputs are not facts by default.
[ ] All public claims require confidence level and provenance.
[ ] C0 claims are never externally asserted as fact.
[ ] Audit log records memory reads/writes/updates/deletes/promotions/blocks.
```

## Phase 1 — Package split

Split `dream_memory_palace_reference_impl.py` into:

```text
gptbrain/
  __init__.py
  models.py          # dataclasses / enums
  engine.py          # DreamMemoryPalace
  retrieval.py       # scoring / indexes
  governance.py      # canon gate / permission checks
  serialization.py   # JSON encoders / loaders
  cli.py             # command interface

tests/
  test_memory.py
  test_contradictions.py
  test_canon_gate.py
  test_permissions.py
  test_serialization.py
```

## Phase 2 — Schemas

Add schemas for:

```text
MemoryObject
ClaimLedgerEntry
ArtifactRegistryEntry
AuditEvent
MemoryPacket
BootPacket
Contradiction
PromotionReceipt
```

Preferred options:

```text
pydantic for runtime validation
YAML/JSON Schema for repo-readable contracts
```

## Phase 3 — Storage adapters

Start with:

```text
SQLite adapter for local dev
JSONL adapter for repo fossil record
```

Then add:

```text
Postgres adapter for canonical records
pgvector adapter for semantic retrieval
Kuzu / Neo4j adapter for claim graph
Object storage adapter for raw artifacts
Git adapter for variant/canon paths
```

## Phase 4 — CLI

Minimum commands:

```bash
gptbrain remember --file artifact.md --type artifact --confidence C2
gptbrain recall "memory palace provenance" --project GPTBrain
gptbrain challenge --memory-id MEM-...
gptbrain contradiction --claim-a MEM-... --claim-b MEM-...
gptbrain diff --from 2026-05-08 --to 2026-05-09
gptbrain synthesize --project GPTBrain --status candidate
gptbrain promote --memory-id MEM-... --human-root-approved
```

Guardrail:

```text
The promote command must require an explicit human-root approval flag and produce an audit receipt.
```

## Phase 5 — Sheldonbrain importer

Import from existing S1 pipeline artifacts:

```text
metadata.json
turns.jsonl
events.jsonl
artifact_registry.jsonl
claim_ledger.jsonl
memory_packet.json
BOOT_PACKET.md
ASSESSMENT.md
```

Importer should map:

```text
raw log -> source artifact
artifact registry row -> artifact memory
claim ledger row -> claim memory
memory packet -> boot memory bundle
assessment -> model assessment memory
candidate action item -> task memory
candidate canon ref -> candidate canon memory
```

## Phase 6 — CI / quality gate

Add:

```text
python -m pytest
ruff check
mypy or pyright
schema validation tests
sample import fixture
sample boot packet fixture
```

Minimum CI success:

```text
[ ] tests pass
[ ] schema examples validate
[ ] C0 claim cannot be promoted without review
[ ] sealed-sensitive memory cannot be recalled
[ ] contradiction creates links both ways
[ ] JSONL roundtrip does not lose provenance
```

## Phase 7 — Human-facing dashboard

Build a minimal dashboard over:

```text
active threads
unresolved contradictions
C0/C1 risky claims
candidate canon
ratified canon
S10 decision queue
recent diffs
missing provenance
```

Variant E contributes heavily here.

## Phase 8 — Council integration

Connect to:

```text
S1 GPTBrain — calibration / evidence architect
S2 ClaudeBrain — constitutional scribe
S3 Grokbrain — adversarial play/dream
S4 GeminiBrain — engineering simulation
S5 DeepSeek — sovereign synthesis
S6 ManusBrain — continuity/execution
S7 CopilotBrain — code integrator
```

Each seat should produce:

```text
seat memory packet
candidate action items
candidate canon refs
claim ledger updates
artifact registry updates
assessment notes
```

## Non-goals for early implementation

Do not implement yet:

```text
autonomous tool execution from memory
private data ingestion without explicit scoping
auto-ratification
hidden model-to-model backchannel
unreviewed public artifact publication
sensitive data storage without encryption
```

## Open risks

```text
1. Variant terminology drift.
2. S1 path duplication.
3. Claims losing provenance during compression.
4. Tests proving behavior but not governance intent.
5. Public-safe translation being skipped in external docs.
6. Reference code mistaken for production service.
```

## Immediate next tasks

```text
[ ] Run tests locally.
[ ] Fix any import/path problems.
[ ] Add pyproject.toml for pytest/ruff.
[ ] Add package split branch.
[ ] Add sample fixture from issue #11.
[ ] Create issue for storage adapter.
[ ] Create issue for CLI.
[ ] Create issue for COUNCIL_BRAIN_INDEX update after human-root review.
```

## Success phrase

```text
The implementation is allowed to be small.
It is not allowed to be vague about authority, provenance, or canon.
```
