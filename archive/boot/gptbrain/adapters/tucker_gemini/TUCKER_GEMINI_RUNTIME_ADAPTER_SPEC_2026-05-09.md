---
artifact_id: ARTIFACT-ARCHIVE-BOOT-GPTBRAIN-ADAPTERS-TUCKER-GEMINI-TUCKER-GEMINI-RUNTIME-ADAPTER-SPEC-2026-05-09-MD-2026-05-29
title: Tucker / Gemini Runtime Adapter Spec
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Tucker / Gemini Runtime Adapter Spec

```text
STATUS: RUNTIME ADAPTER SPEC — NOT CANON
MODE: WORK
ISSUE: manus-artifacts#22
DATE: 2026-05-09
SEAT: S1 GPTBrain
HUMAN-ROOT GATE: required before live execution
```

## Purpose

Define a future-safe adapter boundary for Tucker / Gemini runtime work without confusing provenance visibility with executable integration.

## Current safe status

```text
Tucker is provenance-wired.
Tucker is boot-visible to GPTBrain.
Gemini is a broader council/backend context.
Tucker/Gemini are not yet hard-runtime wired.
```

## Source surfaces

```text
archive/provenance/TUCKER_PUBLIC_BUILD_PROVENANCE_NOTE_2026-05-08.md
archive/provenance/TUCKER_BUILD_CULTURE_AND_GPT_ASSISTANCE_NOTE_2026-05-08.md
archive/boot/gptbrain/TUCKER_BOOT_INTEGRATION_NOTE_2026-05-09.md
https://github.com/atlaslattice/tucker-gemini-GPT-/blob/main/ARTIFACT_PROVENANCE.md
```

## Modes

```text
REPO_TRACE_ONLY  — trace Tucker provenance/source files only
DRY_RUN_ONLY     — default; produce a receipt; no external calls
MOCK_GEMINI      — deterministic fake Gemini result for tests
LIVE_GEMINI      — disabled unless human-root + secrets policy approve
```

## Default behavior

The adapter must default to:

```text
DRY_RUN_ONLY
```

This means:

```text
- no Gemini API calls
- no Tucker code invocation
- no network dependency
- no secrets required
- output is an AdapterReceipt, not model output
```

## Minimal interface

```python
class TuckerGeminiAdapter:
    def describe_sources(self) -> SourceManifest: ...
    def validate_config(self) -> ConfigStatus: ...
    def dry_run(self, prompt: str) -> AdapterReceipt: ...
    def mock_gemini(self, prompt: str) -> AdapterReceipt: ...
    def propose_live_call(self, prompt: str) -> HumanApprovalRequest: ...
    def record_result(self, result: object) -> AuditEvent: ...
```

## Required receipts

Every adapter operation should emit a receipt containing:

```text
mode
prompt_hash
source_refs
live_call_attempted
live_call_allowed
human_root_required
human_root_status
safe_claim
forbidden_claims
next_review
```

## Guardrails

```text
Provenance visibility is not execution permission.
Boot-visible is not runtime-wired.
Readable memory is not executable memory.
Gemini configured is not Gemini authorized.
Tucker referenced is not Tucker invoked.
Live calls require explicit human-root approval and secrets policy.
```

## Acceptance criteria

```text
[ ] Adapter can describe Tucker/Gemini source surfaces.
[ ] Adapter validates missing config without failure.
[ ] Dry-run returns receipt with live_call_attempted=false.
[ ] Mock Gemini mode returns deterministic fake result.
[ ] Live Gemini mode is blocked by default.
[ ] Tests run without secrets and without network.
[ ] Claim ledger records adapter as scaffold/proposed, not live integration.
```

## Strongest safe claim

```text
The Tucker/Gemini adapter scaffold defines a future execution boundary. It does not yet execute Tucker, call Gemini, or authorize live runtime behavior.
```
