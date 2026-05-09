# S1 Alias Topology Policy

```text
STATUS: ALIAS TOPOLOGY POLICY — NOT CANON
DATE: 2026-05-09
ISSUE: manus-artifacts#17
PURPOSE: Resolve ambiguity between stable alias paths and dated snapshot paths for GPTBrain / S1 boot/runtime files.
```

## Decision

Use **both** stable aliases and dated snapshots, with strict roles.

```text
Stable aliases = current pointers for boot convenience.
Dated snapshots = immutable/fossilized historical records.
```

## Stable Alias Paths

Stable aliases may be referenced by boot packets and live onboarding docs:

```text
archive/boot/gptbrain/CURRENT_STATE.md
archive/boot/gptbrain/NEXT_ACTIONS.md
archive/boot/gptbrain/BOOT_PACKET.md
```

Each alias must point to or duplicate the latest dated snapshot and include a pointer to the source dated file.

## Dated Snapshot Paths

Dated snapshots remain the fossil record:

```text
archive/boot/gptbrain/CURRENT_STATE_2026-05-09.md
archive/boot/gptbrain/NEXT_ACTIONS_2026-05-09.md
archive/boot/gptbrain/BOOT_PACKET_TEMPLATE.md
archive/boot/gptbrain/GPT_INSTANCE_STATE_LOG_2026-05-09.md
```

These should not be silently overwritten.

## Referencing Rule

For human/boot convenience:

```text
Use stable aliases.
```

For provenance/audit/seed ledgers:

```text
Use dated snapshot paths plus commit_sha when available.
```

## Seed Ledger Rule

Machine-readable seed objects should prefer:

```yaml
source_ref:
  path: archive/boot/gptbrain/CURRENT_STATE_2026-05-09.md
  alias: archive/boot/gptbrain/CURRENT_STATE.md
  commit_sha: null
```

Do not use only a bare alias in provenance-critical records.

## Required Action

```text
[ ] Create CURRENT_STATE.md alias if missing.
[ ] Create NEXT_ACTIONS.md alias if missing.
[ ] Create BOOT_PACKET.md alias if missing or define BOOT_PACKET_TEMPLATE.md as template only.
[ ] Update seed ledgers to include dated paths and commit_sha fields.
[ ] Update boot docs to explain alias vs snapshot roles.
```

## Guardrail

```text
An alias is a convenience pointer, not source lineage by itself.
A dated snapshot is source lineage.
A commit SHA makes source lineage auditable.
```

## Strongest Safe Claim

> S1 should use stable alias paths for boot convenience and dated snapshot paths for provenance, with seed ledgers carrying both alias and dated path plus commit SHA where available.
