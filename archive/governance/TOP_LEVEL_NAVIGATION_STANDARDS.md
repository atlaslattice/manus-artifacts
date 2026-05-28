# Top-Level Navigation Standards

*Atlas Lattice Foundation · Aetherforge Mission #25 · 2026-05-28*

status: candidate

> Defines the normalized navigation structure for the Atlas Lattice repository root, establishing clear purposes for each top-level directory and guiding contributors on where to find and place content.

---

## Repository Navigation Map

### Primary Entry Points (Always Visible in README)

| Path | Purpose | Audience |
|------|---------|----------|
| `README.md` | Public entry point — mission, overview, links | Everyone |
| `docs/` | User-facing documentation, indexes, models | Contributors, researchers |
| `projects/` | Taskboards, roadmaps, campaign briefs | Core team, contributors |
| `archive/` | All canonical artifact archive (specs, governance, KG) | Deep researchers |

### Core System Directories

| Path | Purpose |
|------|---------|
| `aluminum-os/` | Aluminum OS constitutional substrate (docs) |
| `aluminum-os-core/` | Aluminum OS Rust implementation source |
| `bazinga/` | Constitutional middleware and launch protocols |
| `sheldonbrain/` | SheldonBrain system architecture artifacts |

### Governance & Community

| Path | Purpose |
|------|---------|
| `council/` | Council session records |
| `council-reviews/` | External council reviews |
| `CODE_OF_CONDUCT.md` | Community standards |
| `SECURITY.md` | Security policy |
| `LICENSE` | MIT License |

### Technical Infrastructure

| Path | Purpose |
|------|---------|
| `reference_impl/` | Python reference implementations |
| `schemas/` | YAML/JSON schema registry |
| `scripts/` | Automation and validation scripts |
| `tests/` | Test suite (pytest) |
| `.github/` | CI/CD workflows, templates, contributing guide |

### Research & Archives

| Path | Purpose |
|------|---------|
| `research/` | Intelligence sweeps and convergence reports |
| `archives/` | Janus session checkpoints and resurrection logs |
| `codebases/` | Implementation sandboxes and application snapshots |
| `manus-vault/` | Internal session summaries and Noah's Ark protocols |
| `health/` | Patient rights and wellness facility research |
| `about/` | Founder and project leadership context |

---

## Navigation Conventions

### 1. Every Directory Must Have a README

All top-level directories must contain a `README.md` with:
- One-paragraph purpose statement
- List of key files or subdirectories
- Link back to the root README

### 2. README Must Have a Table of Contents Section

The root `README.md` Table of Contents must mirror this navigation map, with one entry per top-level directory. Sections are grouped by the categories above.

### 3. No Orphan Directories

Directories created without a README are not permitted on the main branch. Use the file placement decision tree ([Mission #31](./FILE_PLACEMENT_DECISION_TREE.md)) to determine where new content belongs.

### 4. Redundancy Reduction

Where similar directories exist (e.g., `archive/` and `archives/`), their scopes are:
- `archive/` → Operational artifacts, specs, governance, KG — the primary archive
- `archives/` → Session state snapshots (Janus checkpoints) — a historical record

These are intentionally separate; do not merge without a council decision.

---

## Navigation Health Metrics

Tracked in CI (Mission #61) and monthly wave review:
- ✅ All top-level directories have README files
- ✅ README Table of Contents covers all top-level dirs
- 🔄 Breadcrumb standards applied throughout (Mission #27)
- 🔄 Canonical path map published (Mission #35)

---

## Related Documents

- [Breadcrumb Standards](./BREADCRUMB_STANDARDS.md)
- [File Placement Decision Tree](./FILE_PLACEMENT_DECISION_TREE.md)
- [Canonical Path Map](./CANONICAL_PATH_MAP.md)
- [Archive Taxonomy Map](./ARCHIVE_TAXONOMY_MAP.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
