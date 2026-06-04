# Contributing to the Atlas Lattice Archive

Welcome to the **Aetherforge**. This is a living public archive — a canon-anchored knowledge substrate for the Atlas Lattice Foundation's work on constitutional AI governance, multi-agent architecture, and regenerative infrastructure.

---

## Canon Boundary — Read First

> **Nothing is canon until ratified by full council and adjudicated by @atlaslattice.**
> Storage is not ratification. Review is not ratification. No agent self-ratifies.

All artifacts in this repository are **candidates** unless explicitly marked `canon: true` and ratified. When contributing:

- Do not claim canon status for new artifacts
- Do not modify existing ratified artifacts without opening an issue first
- Preserve provenance: keep source links, dates, and authorship intact
- Never delete historical artifacts — deprecate and archive instead

**GitHub is the canonical substrate.** Drive and Notion are relay/working-vault layers. The `main` branch is the source of truth.

---

## How to Contribute

### For Documentation / Archive Artifacts

1. Fork the repository and create a branch: `your-username/brief-description`
2. Add or edit markdown files following the existing conventions
3. Include provenance frontmatter where appropriate (see below)
4. Open a PR using the [PR template](./pull_request_template.md)
5. Wait for review — canon changes require @atlaslattice adjudication

### For Code (Rust, Python)

1. Fork, branch, and make targeted changes
2. Run existing validation before opening a PR:
   ```bash
   # GPTBrain scaffold checks
   cd archive/boot/gptbrain/reference_impl
   python -m pytest -q
   bash run_checks.sh

   # Python linting
   ruff check archive/boot/gptbrain/reference_impl/
   ruff format --check archive/boot/gptbrain/reference_impl/

   # Rust (if touching aluminum-os-core)
   cd aluminum-os-core
   cargo test
   cargo clippy
   ```
3. Ensure CI passes before requesting review

---

## Artifact Conventions

### Naming
- Use `SCREAMING_SNAKE_CASE` for major archive documents (e.g., `AGENT_DNA_SCHEMA_DRAFT.yaml`)
- Use `kebab-case` for versioned documents (e.g., `v4.0-unified-field.md`)
- Include ISO dates where relevant: `ARTIFACT_NAME_2026-05-26.md`

### Artifact Types
| Type | Description |
|---|---|
| `doctrine` | Immutable constitutional principles |
| `spec` | Technical specifications |
| `log` | Session and audit logs |
| `dream` | Compressed simulation outputs |
| `seed` | Structured JSONL seed data |
| `schema` | YAML/JSON schemas |
| `registry` | Machine-readable artifact index and relationships |
| `agent-dna` | Agent identity declarations |
| `synthesis` | Cross-model synthesis outputs |
| `blueprint` | Project architecture docs |
| `guide` | Contributor or implementation guidance |

### Lifecycle States
New artifacts should indicate their status:
- `STATUS: DRAFT` — work in progress
- `STATUS: CANDIDATE` — ready for review
- `STATUS: RATIFIED` — canon (requires @atlaslattice adjudication)
- `STATUS: ARCHIVED` — historical, no longer active
- `STATUS: DEPRECATED` — superseded by a newer artifact

### Provenance Block
Major new artifacts should include a provenance block:
```markdown
> **Author:** [Name or Agent]
> **Date:** YYYY-MM-DD
> **Source:** [original location if migrated]
> **Status:** CANDIDATE
> **Review:** Pending @atlaslattice
```

### Machine-Readable Graph Metadata

For mission-critical net-new artifacts, update:

- `docs/knowledge-graph/artifact_taxonomy.v0_1.json` (if adding a new type/state pattern)
- `docs/knowledge-graph/artifact_registry.v0_1.json` (stable ID, path, and required cross-links)

Registry entries must include:

- `id`, `title`, `artifact_type`, `status`, `path`, `links`
- at least one outbound link with `relation` and `target_id`

---

## Issue and PR Guidelines

- Use the provided issue templates for new ideas, curation tasks, or bug reports
- Use the **Ratification Candidate** template for `candidate` → `canon-pending` trust transitions
- Use the PR template for all pull requests
- Reference the [Aetherforge Taskboard](../projects/aetherforge-top50-taskboard-2026-05-26.md) for open work items
- Keep PRs focused — one logical change per PR
- Prefer labeling newcomer-friendly tasks with `good first issue` and `help wanted`
- Route onboarding and architecture questions to Discussions (`discussion:q-and-a`)

---

## CI Checks

All PRs must pass:
- **Repo Hygiene** (`repo-hygiene-checks.yml`): merge-conflict markers, workflow syntax
- **Docs Link Checks** (`docs-link-checks.yml`): internal markdown link validation
- **GPTBrain Reference Checks** (`gptbrain-reference-checks.yml`): pytest suite for Python scaffold
- **Artifact Graph Checks** (`artifact-graph-checks.yml`): taxonomy/registry structure and cross-link integrity
- **KG Surface Autobuild** (`kg-surface-autobuild.yml`): validates generated ingestion/search/live graph payloads

---

## Questions

Open an issue or start a discussion. The archive welcomes thoughtful questions, corrections, and additions.

---

*Maintained by TIDELOCKBRAIN on behalf of the Atlas Lattice Foundation*
