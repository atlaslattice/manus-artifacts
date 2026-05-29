# Aetherforge Wave 2 Implementation Pack — Information Architecture & Navigation (2026-05-27)

Status: `active implementation artifact` (candidate)

This pack implements Wave 2 tasks (13–24).

## 13) Audit top-level folder structure

Audit result (README index presence before Wave 2 implementation):

- Indexed: `README.md` (root only)
- Missing indexes in major domains: `about/`, `aluminum-os/`, `archive/`, `archives/`, `bazinga/`, `council/`, `council-reviews/`, `docs/`, `health/`, `manus-vault/`, `projects/`, `research/`, `sheldonbrain/`

## 14) Normalize naming conventions

Navigation artifacts in this wave use:

- Prefix: `REPO_` for repository-level maps
- Date suffix: `YYYY-MM-DD`
- Stable version suffix where needed: `v0_1`, `v1`

## 15) Create consistent README pattern

Pattern is defined at:

- `/tmp/workspace/atlaslattice/manus-artifacts/docs/navigation/README_PATTERN_v0_1.md`

## 16) Add index file per major domain

Indexes added:

- `about/README.md`
- `aluminum-os/README.md`
- `archive/README.md`
- `archives/README.md`
- `bazinga/README.md`
- `council/README.md`
- `council-reviews/README.md`
- `docs/README.md`
- `health/README.md`
- `manus-vault/README.md`
- `projects/README.md`
- `research/README.md`
- `sheldonbrain/README.md`

## 17) Add cross-links between major domains

Each new domain README includes cross-links to START_HERE and related domain indexes.

## 18) Remove dead/legacy navigation paths

Legacy/no-target links are avoided in new indexes and Wave 2 navigation uses only existing files/folders.

## 19) Add start-here onboarding path

Added onboarding entrypoint:

- `/tmp/workspace/atlaslattice/manus-artifacts/START_HERE.md`

## 20) Add role-based navigation

Role paths (Reader/Builder/Reviewer) are defined in `START_HERE.md`.

## 21) Add machine-readable site map

Added:

- `/tmp/workspace/atlaslattice/manus-artifacts/docs/navigation/REPO_SITE_MAP_v1.json`

## 22) Add architecture map for repo domains

Added:

- `/tmp/workspace/atlaslattice/manus-artifacts/docs/navigation/REPO_ARCHITECTURE_MAP_2026-05-27.md`

## 23) Add ownership map by folder

Added:

- `/tmp/workspace/atlaslattice/manus-artifacts/docs/navigation/REPO_OWNERSHIP_MAP_2026-05-27.md`

## 24) Add dependency map for key artifacts

Added:

- `/tmp/workspace/atlaslattice/manus-artifacts/docs/navigation/REPO_DEPENDENCY_MAP_2026-05-27.md`

## Linked campaign source

- `/tmp/workspace/atlaslattice/manus-artifacts/projects/aetherforge-144-task-campaign-2026-05-27.md`
