---
artifact_id: ARTIFACT-ARCHIVE-BOOT-GPTBRAIN-S1-TOPOLOGY-ALIAS-DECISION-NOTE-2026-05-09-MD-2026-05-29
title: S1 GPTBrain — Topology / Alias Decision Note
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# S1 GPTBrain — Topology / Alias Decision Note

```text
STATUS: HARDENING DECISION NOTE — NOT CANON
PURPOSE: resolve alias drift between dated snapshots and bare convenience paths
DATE: 2026-05-09
ISSUE: manus-artifacts#19
```

## Finding

The S1 GPTBrain corpus contains both dated snapshot paths and bare convenience paths.

Examples:

```text
archive/boot/gptbrain/CURRENT_STATE.md
archive/boot/gptbrain/CURRENT_STATE_2026-05-09.md
archive/boot/gptbrain/NEXT_ACTIONS.md
archive/boot/gptbrain/NEXT_ACTIONS_2026-05-09.md
```

This creates boot ambiguity if different files drift.

## Decision

Use **dated snapshot files** as the durable source of truth.

Use bare files only as convenience aliases or generated pointers.

```text
Dated snapshot = authoritative fossil record
Bare alias     = latest pointer / convenience surface
```

## Canonical current paths

For 2026-05-09, the authoritative paths are:

```text
archive/boot/gptbrain/CURRENT_STATE_2026-05-09.md
archive/boot/gptbrain/NEXT_ACTIONS_2026-05-09.md
```

If bare aliases exist, they should either:

```text
1. duplicate the latest dated snapshot with a clear pointer header; or
2. contain only a redirect/pointer to the latest dated snapshot.
```

## Boot packet rule

Boot packets should load dated snapshots first.

Recommended load order:

```text
archive/boot/gptbrain/CURRENT_STATE_2026-05-09.md
archive/boot/gptbrain/NEXT_ACTIONS_2026-05-09.md
archive/boot/gptbrain/CURRENT_STATE.md        # optional alias check only
archive/boot/gptbrain/NEXT_ACTIONS.md         # optional alias check only
```

## Seed provenance rule

Seed ledgers should reference dated snapshots when preserving evidence.

Bare aliases may be referenced only as convenience surfaces and should not be the sole provenance path.

## Required follow-up

```text
[ ] Update BOOT_PACKET_TEMPLATE.md to prefer dated snapshots.
[ ] Update MEMORY_OBJECTS.seed.jsonl to include dated snapshot refs.
[ ] Add alias verification note to issue #19.
[ ] If aliases exist, mark them explicitly as latest pointers.
```

## Guardrail

```text
Do not silently delete aliases.
Do not silently rewrite dated snapshots.
Do not allow aliases to become untracked canon.
```
