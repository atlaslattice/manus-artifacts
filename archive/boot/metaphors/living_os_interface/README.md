# Living OS Interface Scaffold

```text
STATUS: IMPLEMENTATION SCAFFOLD — NOT PRODUCTION — NOT CANON
ISSUE: manus-artifacts#40
SOURCE: archive/boot/metaphors/KRAKOA_LIVING_OS_INTERFACE_LENS_2026-05-09.md
```

## Purpose

This scaffold translates the living-OS metaphor into generic interface primitives for Council Brain / GPTBrain / Aluminum OS design.

It does not implement, reference, or depend on Marvel IP.

## Translation

```text
living platform -> substrate
network gate -> capability-gated adapter
language/cipher -> translation/access boundary
backup/restore -> context rehydration from artifact refs
sovereignty/admin -> human-root approval gate
specialized powers -> services/agents/adapters
```

## Guardrails

```text
No literal resurrection.
No consciousness-continuity claim.
No service gets root authority by default.
No gate opens without capability and approval state.
Human-root remains the sovereignty/admin boundary.
```

## Files

```text
LIVING_OS_INTERFACE_SPEC_2026-05-09.md
living_os_interface.py
test_living_os_interface.py
```

## Quick local test

```bash
python test_living_os_interface.py
```

## Running and interpreting the reference implementation

The two Python files are dependency-free and operate entirely in process:

```bash
python test_living_os_interface.py -v
```

The 18 tests cover default denial, exact approval scopes, missing and mismatched capabilities, refused root claims, private Play/Imagine/Dream intake, immutable artifact IDs, and source-backed context lookup.

**Important:** `grant_capability(subject, capability, approval=...)` requires a scoped `ApprovalContext` in this stricter prototype, rather than allowing the earlier documentation's two-argument call to install an ambient grant. A caller can write `approved_by="HUMAN_ROOT"`, but this is a self-declared string, **not authenticated human permission**. A passing scope check only returns `PREVIEW_ONLY` and never calls any tool or service.

`register_artifact` takes explicitly supplied, in-memory, source-referenced payloads. It refuses Play/Social/Imagine/Dream/Quiet mode labels, does not fetch account data, and treats `consented_work` as an unverified declaration, not proof of rights. `rehydrate_context` returns a copy of an artifact packet, never a restored person or persistent agent. Audit events are local, non-durable test traces.

Before live integration: replace self-declared approval with a host-verified principal and scoped capability, add durable append-only audit receipts, perform privacy and licensing review, and run deployment-specific security tests. Until then: **not canon, not production, no authority**.

## Closing line

```text
A living OS is safest when its gates are more disciplined than its metaphors are beautiful.
```
