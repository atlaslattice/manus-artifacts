---
artifact_id: DOC-MASTER-SOURCE-REGISTRY-2026-05-28
title: Master Source Registry — Multi-Source KG Synthesis Intake Ledger
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---

# Master Source Registry — Multi-Source KG Synthesis Intake Ledger

> **Purpose:** Pre-synthesis index of every source repository, Notion workspace, Google Drive folder, and external archive that will be ingested into the Atlas Lattice Knowledge Graph.
> GitHub is the canonical substrate. All other sources are relay/working-vault layers pending ingestion.

---

## Source Schema

Each source entry follows this schema:

| Field | Description |
|---|---|
| `source_id` | Unique identifier for this source (e.g. `GIT-001`) |
| `source_type` | `git` · `notion` · `drive` · `local` · `other` |
| `name` | Human-readable name |
| `url` / `location` | Access path or URL |
| `owner` | Responsible owner / steward |
| `status` | `INDEXED` · `PENDING` · `BLOCKED` · `PARTIAL` |
| `artifact_count_est` | Estimated number of artifacts / documents |
| `priority` | `P0` (now) · `P1` (next) · `P2` (later) |
| `notes` | Routing, privacy, or ingestion notes |
| `last_synced` | Date of last sync / snapshot |

---

## Source Registry

### 🔵 Git Repositories

| source_id | name | url / location | status | priority | artifact_count_est | notes |
|---|---|---|---|---|---|---|
| `GIT-001` | manus-artifacts (this repo) | https://github.com/atlaslattice/manus-artifacts | `INDEXED` | P0 | 374 | **Canonical substrate.** Full index in `docs/LATTICE_GLOBAL_INDEX.md` |
| `GIT-002` | *(register next git)* | — | `PENDING` | P1 | — | Add URL, description, and estimated artifact count |
| `GIT-003` | *(register next git)* | — | `PENDING` | P1 | — | Add URL, description, and estimated artifact count |

### 🟡 Notion Workspaces

| source_id | name | url / location | status | priority | artifact_count_est | notes |
|---|---|---|---|---|---|---|
| `NOTION-001` | *(primary Notion workspace)* | — | `PENDING` | P1 | — | Export via Notion API or bulk HTML/MD export. Map page IDs to artifact_ids. |
| `NOTION-002` | *(secondary workspace / shared space)* | — | `PENDING` | P2 | — | Identify owner and access scope before ingest |

### 🟠 Google Drive

| source_id | name | url / location | status | priority | artifact_count_est | notes |
|---|---|---|---|---|---|---|
| `DRIVE-001` | *(primary Drive folder)* | — | `PENDING` | P1 | — | Export as MD via Google Takeout or Drive API. Map folder structure to repo taxonomy. |
| `DRIVE-002` | *(secondary Drive archive)* | — | `PENDING` | P2 | — | Review for PII / sensitive content before ingestion |

### ⚫ Local / Offline Archives

| source_id | name | location | status | priority | artifact_count_est | notes |
|---|---|---|---|---|---|---|
| `LOCAL-001` | *(local machine archive)* | — | `PENDING` | P2 | — | Scan, deduplicate, then upload to manus-artifacts under `archive/` |

---

## Ingestion Pipeline (Planned)

```
[Source] → Export/Clone → Normalize to MD + frontmatter → Dedup → Classify → KG link → manus-artifacts
```

### Step-by-step

1. **Register** — add source to this registry with all schema fields filled
2. **Export / clone** — pull raw content (git clone, Notion export, Drive Takeout)
3. **Normalize** — convert to Markdown with YAML frontmatter (artifact_id, title, status, source_of_truth, created)
4. **Quarantine check** — apply privacy/sensitivity policy (see `quarantine/README.md`)
5. **Dedup** — identify near-duplicates against existing corpus (Wave 4 orphan/dup sweep)
6. **Classify** — assign domain folder per `docs/FOLDER_TAXONOMY_AUDIT_2026-05-27.md`
7. **Graph-link** — add `related_artifacts` frontmatter fields per `docs/ARTIFACT_RELATIONSHIP_TYPES.md`
8. **Ingest** — commit to `manus-artifacts` under appropriate domain path
9. **Update registry** — mark source `INDEXED`, record artifact_count and last_synced date

---

## Intake Priority Queue

Current work order for multi-source synthesis (update as sources are registered):

| Priority | source_id | Action | Owner | Target Date |
|---|---|---|---|---|
| P0 | GIT-001 | ✅ Full deep index complete | agent | 2026-05-28 |
| P1 | GIT-002 | Register + export + normalize | @atlaslattice | TBD |
| P1 | NOTION-001 | Export workspace, map structure | @atlaslattice | TBD |
| P1 | DRIVE-001 | Export primary folder | @atlaslattice | TBD |
| P2 | GIT-003 | Register + export + normalize | @atlaslattice | TBD |
| P2 | NOTION-002 | Scope + access check | @atlaslattice | TBD |
| P2 | DRIVE-002 | PII/sensitivity review first | @atlaslattice | TBD |
| P2 | LOCAL-001 | Scan + dedup + upload | @atlaslattice | TBD |

---

## Registry Statistics

| Metric | Value |
|---|---|
| Total sources registered | 8 (1 indexed, 7 pending) |
| Total artifacts indexed (this repo) | 374 |
| Total artifacts pending ingestion (est.) | TBD — fill as sources are registered |
| Last registry update | 2026-05-28 |

---

## Related Artifacts

- [`docs/LATTICE_GLOBAL_INDEX.md`](./LATTICE_GLOBAL_INDEX.md) — full deep index of GIT-001
- [`docs/FOLDER_TAXONOMY_AUDIT_2026-05-27.md`](./FOLDER_TAXONOMY_AUDIT_2026-05-27.md) — domain taxonomy for classifying ingested artifacts
- [`docs/ARTIFACT_RELATIONSHIP_TYPES.md`](./ARTIFACT_RELATIONSHIP_TYPES.md) — relationship vocabulary for graph-linking
- [`docs/METADATA_BACKFILL_SCOPE_2026-05-27.md`](./METADATA_BACKFILL_SCOPE_2026-05-27.md) — metadata backfill queue
- [`projects/aetherforge-next144-taskboard-2026-05-28.md`](../projects/aetherforge-next144-taskboard-2026-05-28.md) — Wave 12 tasks 133–144 cover 500+ IP scale ingestion

---

*To add a new source: follow the schema above and open a PR or Artifact Proposal issue.*
