---
artifact_id: ARTIFACT-GITHUB-CONTRIBUTING-MD-2026-05-27
title: Contributing to Manus Artifacts
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---
# Contributing to Manus Artifacts

Thank you for your interest in contributing to the **Atlas Lattice Foundation**
artifact archive. This guide covers everything you need to know to participate
effectively and keep the archive world-class.

---

## Table of Contents

1. [Guiding Principles](#guiding-principles)
2. [Canon vs. Candidate](#canon-vs-candidate)
3. [Branch Naming](#branch-naming)
4. [Commit Conventions](#commit-conventions)
5. [Pull Request Process](#pull-request-process)
6. [Local Validation](#local-validation)
7. [Code of Conduct](#code-of-conduct)
8. [Support](#support)

---

## Guiding Principles

- **Public by default** — all work is intended to be public, open-source, and
  world-class. If something isn't ready to be public, mark it `[CANDIDATE]`.
- **GitHub is canon** — Drive and Notion are working-vault layers. GitHub is
  the durable, authoritative substrate.
- **No artifact is canon** until full council ratification and final
  adjudication by @atlaslattice. All current artifacts are candidates.
- **Quality over quantity** — world-class means reviewed, sourced, and versioned.

---

## Canon vs. Candidate

Every artifact has a status:

| Status | Meaning |
|--------|---------|
| `CANONICAL` | Ratified by full council + adjudicated by @atlaslattice |
| `CANDIDATE` | Submitted, under review — may be promoted or rejected |
| `ARCHIVED` | Superseded; retained for historical reference |
| `DRAFT` | Work in progress, not yet submitted for review |

Place the status prominently at the top of any new document.

---

## Branch Naming

```
<type>/<short-description>
```

Types: `feat`, `fix`, `docs`, `chore`, `archive`, `ci`

Examples:
- `docs/start-here-guide`
- `archive/council-session-2026-06`
- `feat/pinecone-sync-v2`

---

## Commit Conventions

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>
```

Examples:
- `docs(archive): add Aluminum OS v4.1 candidate`
- `fix(ci): correct YAML lint path glob`
- `feat(sync): add Pinecone upsert retry logic`

---

## Pull Request Process

1. Fork or branch from `main`.
2. Follow the PR template — fill in every section.
3. Ensure local validation passes (see below).
4. Request review from @atlaslattice or a designated council member.
5. Do not merge your own PR without approval.

---

## Local Validation

### GPTBrain Reference Checks

```bash
cd archive/boot/gptbrain/reference_impl
ruff check .
ruff format --check .
python -m pytest -q
bash run_checks.sh
```

### Repo Hygiene (run from repo root)

```bash
# Check for merge-conflict markers
grep -rn "<<<<<<" . --include="*.md" --include="*.yml" --include="*.py" && echo "CONFLICT MARKERS FOUND" || echo "Clean"

# YAML syntax check (requires yamllint)
yamllint .github/workflows/
```

---

## Code of Conduct

All contributors must follow the [Code of Conduct](../CODE_OF_CONDUCT.md).
Violations can be reported to atlas-lattice-foundation [at] proton.me.

---

## Support

For support expectations and help channels, see [SUPPORT.md](../SUPPORT.md).
