# Krakoa / ORCS offline source-index validation — candidate v0.1

**STATUS: SOURCE-ONLY REFERENCE / CANON: NO / DEPLOYMENT: NO / AUTHORITY: NONE**

This is an inert reference for [#25](https://github.com/atlaslattice/manus-artifacts/issues/25), independent of the historical Krakoa MCP code. It never imports or starts the MCP server, calls provider APIs, reads shell or model-session history, opens referenced source paths, triggers device effects, or writes to the seed files.

## Input and exact source edition

- Gate source: `archive/boot/gptbrain/KRAKOA_GATE_INDEX.seed.jsonl` (Git blob `bdd29d3cd24d1a1f9e9f111104eb331ed297da06`)
- Route source: `archive/boot/gptbrain/LATTICE_ORCS_ROUTE_INDEX.seed.jsonl` (Git blob `cc3134840defb804dac731897752493cfda1b0af`)
- Strict JSONL loader: `reference_impl/krakoa_index_common.py`
- Gate validator: `reference_impl/krakoa_gate_check.py`
- Route validator: `reference_impl/orcs_route_check.py`
- Test files: `reference_impl/test_krakoa_gate_check.py`, `reference_impl/test_orcs_route_check.py`
- Candidate structural contracts: `schema/KRAKOA_GATE_SCHEMA.yaml`, `schema/LATTICE_ORCS_ROUTE_SCHEMA.yaml`
- Human review worksheets: `KRAKOA_GATE_CHECK_REPORT_TEMPLATE.md`, `ORCS_ROUTE_REPORT_TEMPLATE.md`

The YAML files are explanatory review contracts rather than a separately ratified runtime schema; the Python validators enforce their relevant candidate-field boundaries.

## Run in an ordinary cloned repository (no credentials)

```bash
cd archive/boot/gptbrain/reference_impl
python -m unittest -v test_krakoa_gate_check.py test_orcs_route_check.py
python krakoa_gate_check.py
python orcs_route_check.py
```

Local synthetic execution: **29/29 tests passed**, using the exact byte-matched GitHub branch code and test files. The actual GitHub seed bodies were separately source-fetched and structurally checked: **10/10 gate rows** and **8/8 route rows** have the expected fields, valid candidate types, unique identifiers and required human-root flags. **One gate row** (`KRAKOA-GATE-2026-0509-0010`) sets `canon_authority:true`, which must yield **REVIEW_REQUIRED**, not approval. The separate JavaScript structural preflight is not the same as actually running both Python CLIs over those full original seed files, and no hosted GitHub CI result is claimed.

## Semantics

- `CANDIDATE_POINTER_ONLY`: a row has an acceptable shape for review, but is **not** permission, authenticated identity, verified source rights, confirmed source existence or live routing.
- `REVIEW_REQUIRED`: a historical authority-flagged governance reference still requires an actual authenticated human-root decision and supporting receipts. It never ratifies itself.
- `HOLD`: invalid JSONL/fields, duplicate IDs, missing human review, unsafe paths, unknown mode or non-governance canon flags. Keep source, report needed fixes and do not execute.
- A route source path is **never dereferenced**. Relative strings may point across repositories; pointer validity does not prove the file exists or is public.
- PLAY and DREAM values on existing gate records are **labels about historical data**, not rights to read or migrate private Play, Social, Quiet, Imagine, Dream or personal Brain bodies into Work.

## Historical and production boundary

No legacy MCP behavior changes. The old `krakoa_mcp_server.py` remains blocked for hosted deployment under [#26](https://github.com/atlaslattice/manus-artifacts/issues/26), independent of these offline index checks. Do not treat `canon_authority:true` as a cryptographic signature, user verification, approved action, resident identity, CANON promotion or execution grant.

Before use in a live host: authenticated principal, explicit rights at read+return, permission revocation, source-root coverage, stable schema edition, fail-closed source fetch, independent security testing, and human release approval are required.

**Keeper:** Indexes point toward evidence. They do not confer the authority the evidence might describe.
