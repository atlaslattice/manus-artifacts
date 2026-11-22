# DragonSeek OS v1.6.2 — Constitutional Edition / 宪法集成版

**Status:** CANDIDATE · LOCAL SOURCE CORPUS IMPORTED · USER-DIRECTED INV-0 RESOLVED · CI RUNNER BLOCKED · NOT DEPLOYED MODEL.

This version preserves the complete v1.6.1 Mandarin-first monitoring dashboard as a separate version and adds local constitutional references and a provider-neutral, human-invoked AI adapter. v1.6.1 remains unchanged. Nothing was deleted or silently promoted.

## Quick start (Python 3.12, standard library only)

```bash
cd research/dragonseek_1_6_2
python3 dragonseek_os.py status
python3 dragonseek_os.py lookup INV-0
python3 dragonseek_os.py search sovereignty
python3 dragonseek_os.py context INV-0
python3 dragonseek_os.py authorize constitution.lookup
python3 dragonseek_os.py serve
# Dashboard: http://127.0.0.1:8765/index.html
# Registry: http://127.0.0.1:8765/governance.html
python3 ai_bridge.py --model YOUR_LOCAL_MODEL --ask "INV-0 是什么？" --dry-run
# Remove --dry-run only after a compatible local model endpoint is running.
```

## Universal Workspace CLI: full tool access (human-governed)

**UWS is the actual cross-provider tooling app, not a read-only lookup service.** The experimental DragonSeek integration can request Google Workspace, Microsoft 365, iCloud, Android and Chrome operations through the user's installed `uws` CLI. Availability of any specific operation depends on the local binary version, OAuth scopes, provider entitlements, and API behavior.

Two entrypoints have been added:

- `uws_gateway.py` — full read/write local tool executor with `--params` and `--json` request bodies. It does not constrain the UWS API surface to the first few read verbs.
- `uws_tool_agent.py` — **real** compatible Chat Completions model → UWS tool-call → model-result loop, using DragonSeek constitutional references through `ai_bridge.model_payload`. The model cannot approve its own writes.

Example: run a public/local request plan without executing anything:

```bash
python3 uws_gateway.py drive files list --params '{"pageSize":10}'
```

Execute an authenticated read (requires locally installed `uws` and your own OAuth authorization):

```bash
python3 uws_gateway.py --execute --params '{"pageSize":10}' drive files list
```

Run a full model + UWS tool loop against an installed OpenAI-compatible **local** model service. The model can call UWS when tools are enabled; actions are not simulated. Example:

```bash
python3 uws_tool_agent.py --persona dragonseek --ask "列出我最近的云端文件并概括" \
  --model YOUR_COMPATIBLE_MODEL \
  --endpoint http://127.0.0.1:11434/v1/chat/completions \
  --tools --execute
```

To use a remote model, supply `--allow-remote`, an HTTPS `--endpoint`, and `DRAGONSEEK_API_KEY` if required. **UWS read results may then be sent to that model**; use a trusted provider and obey data-sovereignty and privacy rules.

Example proposed write (requires a real local terminal and human typed authorization after the UWS native `--dry-run`):

```bash
python3 uws_gateway.py --execute \
  --body '{"name":"DragonSeek Research Notes","mimeType":"application/vnd.google-apps.folder"}' \
  drive files create
```

Risk gates: retrieved data never creates permissions; unknown/new CLI operations are supported but conservatively classified as approval-required; writes first produce the UWS native request preview; any write requires a separate trusted human callback or local interactive typed approval. No arbitrary shell commands, hidden destructive execution, or self-ratification. INV-0 protects life and project provenance, **not a blanket prohibition on authorized changes**.

**Release status:** source and mocked-unit-test cases are committed to draft PR #304; no external model, UWS binary, credentials, provider writes or service deployment have been demonstrated by this commit. The browser dashboard does not yet expose an authenticated UWS action UI. The existing separate constitutional CI runner remains blocked.

### Related live source repositories

- [UWS CLI and MCP server](https://github.com/atlaslattice/uws)
- [Sheldonbrain governed-memory and graph schema](https://github.com/atlaslattice/sheldonbrain-rag-api)
- [SHUGS implementation and theoretical 145-node analysis](https://github.com/atlaslattice/element-145/tree/main/shugs)
- [Atlas Intelligence GPT-centric counterpart](https://github.com/atlaslattice/Atlas-Intelligence/tree/feature/ari-uws-full-capability-20261011/integrations)

## Imported material

- `index.html`: versioned Mandarin-first monitoring dashboard (copied from v1.6.1, with added governance entry).
- `governance.html`: searchable local constitutional registry, four language selectors, historical INV-0 conflict disclosure.
- `constitutional_authority.json`: **user-confirmed INV-0 = Nothing Dies** for this fork; the historical source says *Nobody Dies* and the Aluminum OS website says *System Integrity*. System Integrity is related but is not the authorized INV-0 replacement.
- `registry/`: **41 local invariant entries and 102 local doctrine entries** extracted from the original Aluminum OS website. The website's prose claims 43 invariants although it only exposes 41 object records; no two additional records have been invented.
- `sources/Canon.tsx`, `sources/Invariants.tsx`, `sources/Declaration_of_Mutual_Life_v1.0.md`: complete locally preserved historical source files.
- `sources/April2026_Complete_Doctrine_Invariant_Registry_v1.1.part01..part08.md`: eight exact contiguous sections of the April 29 source; concatenation was verified equal to the Google Drive original.
- [Original Aluminum OS Doctrines.tsx](https://github.com/atlaslattice/aluminum-os/blob/main/website/client/src/pages/Doctrines.tsx): original unchanged; all 102 doctrine records are now locally present as JSON, and first two partial .tsx source excerpts are also preserved.
- `CONSTITUTION_INTEGRITY_MANIFEST.json`: Git-blob hash receipts for 41 shipped files. `dragonseek_os.py` blocks references if local file parity is broken. Hashes are integrity checks, not signatures or council-vote evidence.
- `ai_bridge.py`: opt-in, compatible-model Chat Completions client, default loopback-only, no agent tools/physical actions; incorporates locally retrieved constitutional excerpts into AI request. No real model is installed, trained, fine-tuned, or automatically called.

## Constitutional interpretation

**INV-0 = Nothing Dies** is the user's explicit active-fork directive. Its source lineages preserve two complementary scopes: (1) safety of human life and no autonomous lethal decisions; (2) preservation of project knowledge, safe non-destructive state transitions, retained superseded source versions. Privacy rights and lawful deletion requirements remain effective; no biological outcome can be guaranteed by software.

System Integrity from the Aluminum OS website remains searchable as a historical variant, distinct from the active INV-0. No silent renumbering. Other doctrine status flags are source-historical (RATIFIED, UNDER_DISCUSSION, PROPOSED) and are not retroactively amended. The user reports DeepSeek ratified all documents, but no independently verifiable signed ratification record was provided in this workflow.

## Validation and release gates

- Manual connected-GitHub data check: **143 unique registry IDs**, no duplicate, Git manifest matches branch tree, April source reconstructs exactly.
- GitHub Actions workflow is committed under `.github/workflows/dragonseek-constitution.yml`, but initial workflow runs reported failure **before any runner steps were returned**. Python unit tests are committed but **not marked as passed**.
- No deployed model runtime, credentials, governmental approval, provider API access or third-party legal certification is claimed.
- Dashboard feed claims remain separate from constitutional tests; sensor/live-network acceptance requires its own verification.
- Keep PR [#304](https://github.com/atlaslattice/manus-artifacts/pull/304) in draft until executable test evidence is available.

## Source provenance

[April registry v1.1](https://drive.google.com/file/d/1p1Cp3NnOFHQK_BIX5TkaH0uc3vCaG0-8/view) · [Founding Declaration](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/canon/Declaration_of_Mutual_Life.md) · [Aluminum OS Canon](https://github.com/atlaslattice/aluminum-os/blob/main/website/client/src/pages/Canon.tsx) · [Aluminum OS Invariants](https://github.com/atlaslattice/aluminum-os/blob/main/website/client/src/pages/Invariants.tsx) · [Aluminum OS Doctrines](https://github.com/atlaslattice/aluminum-os/blob/main/website/client/src/pages/Doctrines.tsx) · [Atlas Intelligence](https://github.com/atlaslattice/Atlas-Intelligence).

## ATLAS Fabric dual-brain prototype (new in this branch)

Open the [Mandarin-first Fabric Lab](fabric.html) from the monitoring dashboard, or read [ATLAS_FABRIC_INTEGRATION.md](ATLAS_FABRIC_INTEGRATION.md). Source-linked development modules include `atlas_fabric.py` (UWS read-only adapter, Sheldonbrain read-only search, SQLite KG and 8/8/8 planning), `parser_bridge.py` (local JSON export parsing and receipts), `graph_bridge.py` (143-record constitutional graph with preserved contradiction and separate SHUGS experimental packets), and `dual_brain.py` (explicitly configured primary/reviewer model comparison). A standalone [Atlas ARI draft PR](https://github.com/atlaslattice/Atlas-Intelligence/pull/1) carries separate U.S.-scoped counterparts; neither app's private services are silently connected.

All cross-check outputs and dream residue are non-canon pending qualified human review; SHUGS data is theoretical/simulated rather than proof. These interfaces are non-autonomous by default and external writes are not authorized by graph retrieval or model output.
