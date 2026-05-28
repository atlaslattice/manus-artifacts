# Ingestion Sources Registry

```
STATUS: CANDIDATE — not canon
PURPOSE: Pre-synthesis inventory of all external sources (GitHub repos, Notion, Drive)
         that must be indexed/ingested before knowledge-graph synthesis can proceed.
OWNER: @atlaslattice
UPDATED: 2026-05-28
```

This registry is the **pre-flight manifest** for the synthesis goal:
> *"Merge fragmented GitHub repos, Notion workspaces, and Google Drive into one
> cohesive knowledge graph."*

Ingestion happens before synthesis. No source is merged until it is listed,
triaged, and marked `status: ingested` here.

---

## Legend

| Field | Meaning |
|---|---|
| `source_id` | Short unique identifier used in `source_system` metadata field |
| `type` | `github-repo`, `notion-db`, `drive-folder`, `raw-export` |
| `visibility` | `public`, `private`, `unknown` |
| `status` | `pending` / `partial` / `ingested` / `quarantine` |
| `target_path` | Where ingested content lands in this repo |
| `priority` | `P0` (blockers), `P1` (high), `P2` (medium), `P3` (low) |

---

## GitHub Repositories

### Primary Public Repos

| source_id | Repo URL | Visibility | Status | Target Path | Priority | Notes |
|---|---|---|---|---|---|---|
| `github:manus-artifacts` | https://github.com/atlaslattice/manus-artifacts | public | **hub** | `.` (this repo) | — | Canonical synthesis target |
| `github:aluminum-os` | https://github.com/atlaslattice/aluminum-os | public | partial | `codebases/aluminum-os/` | P1 | Core architecture; partial mirror in codebases |
| `github:uws` | https://github.com/atlaslattice/uws | public (archived) | partial | `codebases/uws/` | P1 | Command-surface CLI; archived, needs full index |
| `github:sheldonbrain-rag-api` | https://github.com/atlaslattice/sheldonbrain-rag-api | public | partial | `codebases/sheldonbrain/` | P1 | Parser/RAG tooling; omega-v1 partially mirrored |
| `github:atlas-lattice-foundation` | https://github.com/atlaslattice/atlas-lattice-foundation | public | partial | `codebases/atlas-lattice/` | P1 | Foundation docs; 2 files partially mirrored |
| `github:element-145` | https://github.com/atlaslattice/element-145 | public | pending | `codebases/element-145/` | P1 | Meta-orchestrator; not yet mirrored |
| `github:open-regenerative-compute-standard` | https://github.com/atlaslattice/open-regenerative-compute-standard | public | pending | `codebases/orcs/` | P2 | Regenerative compute standard |
| `github:snrs` | https://github.com/atlaslattice/snrs | public | partial | `codebases/snrs/` | P1 | SNRS ontology; ~10 files mirrored |
| `github:free-bank` | https://github.com/atlaslattice/free-bank | public | partial | `codebases/free-bank/` | P2 | Free bank blueprint |
| `github:atlas-vault` | https://github.com/atlaslattice/atlas-vault | unknown | pending | `codebases/atlas-vault/` | P2 | Vault — needs visibility check |
| `github:colab-notebooks` | https://github.com/atlaslattice/colab-notebooks | unknown | pending | `codebases/colab-notebooks/` | P3 | Notebooks |
| `github:sovereign-oracle` | https://github.com/atlaslattice/sovereign-oracle | unknown | pending | `codebases/sovereign-oracle/` | P2 | Sovereign oracle codebase |
| `github:project-symbiote` | https://github.com/atlaslattice/project-symbiote | unknown | pending | `codebases/project-symbiote/` | P2 | Symbiote project |

### Private Repos (Restricted — Review Before Ingestion)

| source_id | Repo URL | Visibility | Status | Notes |
|---|---|---|---|---|
| `github:noosphere-archive` | https://github.com/atlaslattice/noosphere-archive | **private** | pending | Shenmu/DragonSeek governance; do not cite publicly until mirrored/public-safe |
| `github:noosphere-defense` | https://github.com/atlaslattice/noosphere-defense | **private** | pending | Defense materials; private-only |
| `github:aluminum-os-v3` | https://github.com/atlaslattice/aluminum-os-v3 | **private** | pending | Prior architecture branch; requires reconciliation |

---

## Notion Databases / Pages

| source_id | Notion ID / Description | Status | Target Path | Priority | Notes |
|---|---|---|---|---|---|
| `notion-export` | Organism research pages (Ganoderma, Tsamma Melon, etc.) | partial | `codebases/other/` | P3 | 5 files already exported; pattern shows Notion page export format (hash suffix in filename) |
| `notion:workspace-main` | Primary Notion workspace | pending | `docs/notion-archive/` | P1 | Full workspace not yet inventoried; needs @atlaslattice Notion export |
| `notion:sheldonbrain-vault` | SheldonBrain Notion vault | pending | `archive/boot/gptbrain/` | P1 | Key memory palace docs; unknown page count |
| `notion:council-sessions` | Council session notes | pending | `council/` | P1 | Cross-reference with `council/council-session-master-archive.md` |
| `notion:project-plans` | Project planning boards | pending | `projects/` | P2 | Task boards that may predate Aetherforge boards |
| `notion:research-notes` | Research/intelligence sweep notes | pending | `research/` | P2 | May overlap with `research/intelligence-sweeps/` |

---

## Google Drive Folders

| source_id | Drive Folder / Description | Status | Target Path | Priority | Notes |
|---|---|---|---|---|---|
| `drive:main-vault` | Primary Drive vault (all IP) | pending | `docs/drive-archive/` | P0 | 500+ IP archives; @atlaslattice action required to export |
| `drive:aluminum-os-docs` | Aluminum OS working docs | pending | `aluminum-os/` | P1 | May contain pre-GitHub Aluminum iterations |
| `drive:health-records` | Health/PT/facility research | partial | `health/` | P2 | 4 files already in repo; privacy-reviewed |
| `drive:financial` | Financial sovereignty research | pending | `quarantine/` | **QUARANTINE** | Contains bank-related content → private repo only |
| `drive:research-sweeps` | Intelligence sweep raw notes | pending | `research/intelligence-sweeps/` | P1 | Raw versions of the 4 published sweeps |
| `drive:council-sessions` | Council session audio/notes | pending | `council/` | P1 | Source material for council-session-master-archive.md |

---

## Raw Exports / Other

| source_id | Description | Status | Target Path | Priority | Notes |
|---|---|---|---|---|---|
| `chatlog-export` | Geopolitical chokepoint canon boot chatlogs | partial | `archive/chatlogs/` | P3 | 1 chatlog directory indexed |
| `manus-agent` | Manus AI agent session outputs | partial | `manus-vault/` | P2 | 12 files; agent session summaries |
| `research-sweep` | Intelligence sweep exports | partial | `research/intelligence-sweeps/` | P2 | 4 sweeps indexed |

---

## Ingestion Pipeline Summary

```
Phase 0 — Index (NOW)
  - [x] Expand LATTICE_GLOBAL_INDEX to full repo (367 files)
  - [ ] Inventory all known GitHub repos (this document)
  - [ ] Confirm visibility of unknown repos

Phase 1 — GitHub Synthesis (P0/P1)
  Priority order: aluminum-os → uws → sheldonbrain-rag-api → snrs →
                  element-145 → atlas-lattice-foundation → orcs

  For each repo:
    1. Clone/fetch into /tmp
    2. Run check_markdown_links.py equivalent on target
    3. Copy key docs into codebases/<repo>/ or merge into canonical paths
    4. Add source_system: github:<repo> frontmatter
    5. Update this registry to status: ingested

Phase 2 — Notion Export
  Priority order: workspace-main → sheldonbrain-vault → council-sessions
  Requires: @atlaslattice to run Notion → Markdown export

Phase 3 — Drive Ingestion
  Priority order: main-vault → aluminum-os-docs → research-sweeps
  Requires: @atlaslattice to run Drive export; PII/bank-content quarantine review

Phase 4 — Synthesis
  Only after Phase 0-3 complete. Run graph build against full corpus.
```

---

## Quarantine Rules

Anything matching these criteria → `quarantine/` directory → private repo only:
- Contains the word "hacker"
- Primarily refers to banking/financial institutions
- Contains PII (personal data, health records outside already-public health/)

Reference: `quarantine/README.md` and `ATLASLATTICE_PRIVATE_REPO_ROUTING_NOTE.md §6`

---

## Action Items for @atlaslattice

These tasks require manual owner action (cannot be automated):

1. **Confirm GitHub repo list**: Verify the list above is complete. Missing repos?
2. **Notion export**: Export Notion workspace to Markdown and drop in `docs/notion-archive/`
3. **Drive export**: Export key Drive folders to Markdown/PDF and stage for ingestion
4. **Private repo decisions**: Decide which private repo content can go public
5. **Bank/hacker content**: Route to private repo per quarantine policy

---

*Source: derived from `archive/integrations/lattice/LATTICE_REPO_SOURCE_MAP_2026-05-09.md` and full-repo audit.*
*Cross-reference: `docs/LATTICE_GLOBAL_INDEX.md` (auto-generated), `docs/data-provenance-map.md`*
