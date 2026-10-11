# DragonSeek OS v1.6.2 — ATLAS Fabric Integration

**Status:** EXPERIMENTAL · DEVELOPMENT BRANCH · USER-DIRECTED LOCAL CONFIGURATION · NO VENDOR/STATE DEPLOYMENT  
**Date:** 2026-10-11. **Sources remain in their original repositories.** The working UWS, memory, SHUGS and Dream interfaces are opted in by the user, never autonomous by default.

## Architecture

```text
                        Human approval / INV-0 Nothing Dies
                                     |
          DragonSeek local constitutional registry (41 INV, 102 DOC)
                                     |
                  Read-only source and identity contracts
          ___________|_______________|_______________
         |                   |                       |
    UWS (read-only)    Sheldonbrain / parser     Local ReceiptGraph
   Explicit commands   Opt-in HTTP / local JSON    SQLite receipts
         |                   |                       |
         +-------------------+-----------------------+
                                     |
                        Independent primary / reviewer
                      (provider models configured by user)
                                     |
                       DISSENT / VERIFY SOURCES / HUMAN REVIEW
                                     |
                  Dream / Play / optional Work 8/8/8 candidates
                                     |
                         SHUGS research in quarantine
```

The OS and AI are not their own authority. Context is evidence, not permission. Model generation receives NO tool-calling schema or executor.

## Local reproducible commands

Run in `research/dragonseek_1_6_2/` using Python 3.11+.

```bash
python dragonseek_os.py status
python dragonseek_os.py lookup INV-0
python graph_bridge.py --search INV-0
python graph_bridge.py --shugs-json experimental/shugs_lattice_optimum_original.json --shugs-receipt 'element-145:shugs/canonical_lattice_optimum_results.json@2ae08de' --search Nothing
python ai_bridge.py --ask '解释 INV-0 的意义' --model local-model --dry-run
python dual_brain.py --ask 'Check the source provenance of INV-0' --primary-model model-a --primary-lineage model-family-a --review-model model-b --review-lineage model-family-b
python -m unittest discover -s tests -v
```

`atlas_fabric.py` is importable from a local Python REPL:

```python
from atlas_fabric import run_uws_readonly, query_sheldonbrain, cycle_plan, dream_packet
print(run_uws_readonly(["drive","files","list"]))   # dry-run by default
print(query_sheldonbrain("source receipts"))          # dry-run by default
print(cycle_plan())                                  # 8 Dream, 8 Play, 8 optional Work
print(dream_packet(["source:receipt"],"New cross-domain idea"))
```

UWS must be installed and authenticated by the user. `run_uws_readonly(..., execute=True)` runs only exact allowed read commands. Other UWS functionality, including writes, needs a separately reviewed permission system and is NOT exposed to the model.

Sheldonbrain's `/query` integration is a read-only, explicit option and is private by default, with remote HTTPS opt-in. It cannot execute memory content or use /store, /lifecycle, or /delete. The parser handles two JSON shapes: Grok nested `conversations/responses` and a generic `messages` list. Local input is preserved and parsed output is created only on explicit `--out` and never overwrites a file.

Dual-brain `--execute` calls two OpenAI-compatible endpoints configured by the user. Loopback is default; nonlocal endpoints require `--allow-remote` with HTTPS. Distinct declared model lineages are recommended. Agreement does not verify claims, and lexical source-ID extraction is not independent verification. No tool-calling, automatic actions, weights training, or institutional endorsements.

## SHUGS boundary

The file `experimental/shugs_lattice_optimum_original.json` is a byte-preserving snapshot of [Element 145's numerical research](https://github.com/atlaslattice/element-145/blob/main/shugs/canonical_lattice_optimum_results.json). The numerical results are **reported simulation outputs**; the importer labels them research pending review. Neither GUE-KS comparisons nor N=145 design selection prove physical unified-field dynamics, production routing efficiency, or the Riemann hypothesis. The full `shugs_core.py` and tests remain in [element-145](https://github.com/atlaslattice/element-145/tree/main/shugs). The [ORC-036 bridge](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/ORC-036_SHUGS_SNRS_Bridge_Stub_v0.1.md) is a stub, not a complete operational bridge.

## Dream boundary

[GPTDream++ schema](https://github.com/atlaslattice/manus-artifacts/blob/master/archive/boot/gptbrain/gptdream_best_in_world_packet_v0_1/GPTDREAM_PLUS_SCHEMA_v0.3.yaml) · [GrokDream sweep](https://github.com/atlaslattice/manus-artifacts/blob/master/archive/reports/GROKDREAM_GPTDREAM_SWEEP_12x12_EXECUTION_PACKET_2026-05-30.md) · [Dream-spec index](https://github.com/atlaslattice/dream-specs/blob/main/MASTER_DREAM_INDEX.json).

The 8/8/8 schedule is an exploratory *simulation of work modes*, not biological sleep, actual subjective centuries, measured productivity gains, or an active daemon. Dream exploration is deliberately **not limited to memory replay**: it supports hypothetical association and unbounded references within finite compute/time limits, but all wake artifacts remain non-canon until independently evaluated.

## Source interfaces

- [UWS](https://github.com/atlaslattice/uws/tree/uws-universal) CLI, [MCP source](https://github.com/atlaslattice/uws/blob/uws-universal/mcp_server/server.py). Broad `alum_execute` exists upstream, but this integration does **not** expose it: no blanket external write grants.
- [Sheldonbrain RAG API OpenAPI v2.1](https://github.com/atlaslattice/sheldonbrain-rag-api/blob/master/docs/openapi.yaml) and [Grok parser](https://github.com/atlaslattice/sheldonbrain-rag-api/blob/master/grokbrain_parser/grok_parser.py).
- [KG schema](https://github.com/atlaslattice/sheldonbrain-rag-api/blob/master/archive/knowledge_graph/KG_NODE_EDGE_SCHEMA_v0.1.yaml): graph != memory != canon != permission.
- [Atlas ARI](https://github.com/atlaslattice/Atlas-Intelligence) receives separate source-linked, US-scoped config and independent provider preferences; no joint sovereign data-pool implied.

## Release gate

The draft PR remains unmerged. GitHub Actions previously reported failed jobs **without runner steps/logs**; a successful local `compileall`, unit tests, invalid UWS action checks, privacy tests and provider endpoint dry-run are required before stable release. Do not claim these checks passed until they run.

INV-0 is **Nothing Dies**, a user-directed active configuration; historical “Nobody Dies” and “System Integrity” source versions remain source-addressable rather than overwritten. Human safety, data privacy and valid erasure requirements are part of its implementation scope.
