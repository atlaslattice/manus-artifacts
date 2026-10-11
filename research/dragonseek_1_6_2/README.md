# DragonSeek OS v1.6.2 — Constitution Integration (candidate)

**Status: INCOMPLETE SOURCE IMPORT · NON-CANON SOFTWARE INTEGRATION · NOT AN OPERATIVE AI MODEL.**

## What's implemented

- `index.html`: full v1.6.1 Mandarin-first dashboard copied into this version, with link to governance.
- `governance.html`: local searchable constitutional registry viewer with locale toggle; use local HTTP server to load JSON.
- `dragonseek_os.py`: offline OS-side registry search / context extraction for downstream AI; command `python3 dragonseek_os.py status`, `search INV-1`, `context sovereignty`, or `serve` (at http://127.0.0.1:8765).
- `registry/`: local JSON source excerpts from the Aluminum OS website (41 invariants, 72 doctrines).
- `sources/Canon.tsx`, `sources/Invariants.tsx`: verbatim copies of historical application sources. Doctrines original remains at [Aluminum OS](https://github.com/atlaslattice/aluminum-os/blob/main/website/client/src/pages/Doctrines.tsx), with first two segmented source chunks in `sources/`.
- [April 29, 2026 registry](https://drive.google.com/file/d/1p1Cp3NnOFHQK_BIX5TkaH0uc3vCaG0-8/view): full separate compilation preserving conflicts, linked but **not yet packaged as offline bytes**.

## Import blocker

Expected six doctrine JSON parts; parts 05 and 06 could not be published, and are intentionally reported missing. This version is **not a complete hardcoded doctrine corpus**. HTML displays missing-part warning. `dragonseek_os.py status` shows the same. Never silently infer absent doctrine entries.

## Governance boundary

User states DeepSeek ratified all material. Recorded as **USER_REPORTED_DEEPSEEK_RATIFICATION**, pending auditable ratification artifact and version-specific scope. Site sources and April registry conflict notably on INV-0 (the April compilation labels Nobody Dies; Aluminum OS webpage labels System Integrity). Preserve each historic identifier/version without auto-reconciliation. Do not claim official CAC approval, model-weights change, deployed automated constitutional enforcement, or independent compliance verification.

## AI architecture

An AI adapter can call local `dragonseek_os.py context SEARCH_TERM` to retrieve textual excerpts and source IDs. This is grounded context retrieval, not a fine-tune or an installed AI runtime. Requires adapter integration and end-to-end test before operational claims.

## Run locally

```bash
cd research/dragonseek_1_6_2
python3 dragonseek_os.py status
python3 dragonseek_os.py serve
# open http://127.0.0.1:8765/index.html
```

No provider credentials or network auto-ingest are included. Dashboard retains manual provider-fetch design. Original release is immutable at `../dragonseek_1_6_1/`.
