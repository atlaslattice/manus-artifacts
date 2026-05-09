# Tucker / Gemini Adapter Scaffold

```text
STATUS: ADAPTER SCAFFOLD — NOT CANON
MODE: WORK
ISSUE: manus-artifacts#22
PURPOSE: define a safe boundary between Tucker/Gemini provenance visibility and future runtime execution
```

## Summary

This directory contains a non-canon scaffold for a future Tucker / Gemini runtime adapter.

The adapter starts in dry-run / repo-trace mode only. It does not make live Gemini API calls by default, does not invoke Tucker code, and does not grant execution authority based on provenance visibility.

## Boundary

```text
Provenance visibility is not execution permission.
Boot-visible is not runtime-wired.
Readable memory is not executable memory.
Gemini configured is not Gemini authorized.
Tucker referenced is not Tucker invoked.
```

## Files

```text
TUCKER_GEMINI_RUNTIME_ADAPTER_SPEC_2026-05-09.md
tucker_gemini_adapter.py
test_tucker_gemini_adapter.py
```

## Intended default mode

```text
DRY_RUN_ONLY
```

No external calls. No secrets required. Tests must pass without network or API credentials.
