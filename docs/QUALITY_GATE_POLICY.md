---
title: Quality Gate Policy
artifact_id: GOVERNANCE-QUALITY-GATE-POLICY-2026-05-29
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-29
provenance: Created from 7-pillar world-class execution plan (2026-05-29). Formalizes "no merge without passing gates" policy for execution branches.
---

# Quality Gate Policy

## Purpose

Define the mandatory quality gates that must pass before any pull request targeting `main` is merged. Every major stream has automated checks. No exceptions.

---

## Policy Statement

> **No PR merges to `main` unless all required quality gates pass.**

This is not advisory — it is the minimum bar for world-class open-source repository status.

---

## Required Status Checks (PR merge gates)

All of the following CI checks must pass before merge:

| Check | Workflow File | What It Validates |
|-------|--------------|-------------------|
| Repo Hygiene | `repo-hygiene-checks.yml` | No merge-conflict markers; YAML syntax valid |
| Markdown Lint | `markdown-lint.yml` | Markdown style and format compliance |
| Docs Link Checks | `docs-link-checks.yml` | No broken relative links in docs surfaces |
| GPTBrain Reference | `gptbrain-reference-checks.yml` | GPTBrain reference implementation tests |
| Lattice KG Quality Gates | `lattice-kg-quality-gates.yml` | KG schema integrity and positron coverage |

---

## Enforcement Model

### Branch Protection (recommended settings for `main`)

```yaml
# Branch: main
required_status_checks:
  strict: true
  contexts:
    - "Check for merge conflicts and YAML syntax"
    - "Markdown lint"
    - "Check relative doc links"
    - "GPTBrain reference checks"
    - "Validate lattice indices and positron coverage"
require_pull_request_reviews:
  required_approving_review_count: 1
  dismiss_stale_reviews: true
require_signed_commits: false  # Preferred but not yet enforced
enforce_admins: false  # @atlaslattice has override for emergency
```

See GitHub → Settings → Branches → Branch protection rules to apply these settings.

---

## Gate Bypass Rules

| Situation | Bypass Allowed? | Procedure |
|-----------|----------------|-----------|
| Emergency security fix | Yes — with post-hoc review | Create follow-up issue within 24h |
| CI environment failure (not code) | Yes — with documented reason | Comment on PR with failure evidence |
| Docs-only typo fix | Yes — maintainer discretion | Label PR `docs-only` |

Bypass is never allowed for:
- Logic or schema changes
- Governance artifact updates
- New artifacts claiming `canonical` status

---

## Stream-Level Quality Gates

Each stream has additional gates beyond the repo-wide requirements:

### Knowledge Graph Stream
- `python scripts/build_lattice_global_index.py` — must complete with zero errors
- `python scripts/validate_lattice_quality_gates.py` — must pass all checks
- `python -m pytest -q tests/test_lattice_kg_hypercube_program.py` — must pass

### GPTDream++ Stream
- Full adversarial test suite: `python -m pytest -q tests/adversarial/`
- Schema validation: all 15 Atlas/ORCS YAML schemas must validate

### Governance / Docs Stream
- `python scripts/validate_artifact_metadata.py` — frontmatter completeness check
- `python scripts/check_markdown_links.py` — full link integrity pass

---

## Adding a New Gate

When a new stream is added:

1. Create a workflow file in `.github/workflows/`
2. Run it on `push` + `pull_request` to `main`
3. Add it to the Required Status Checks in branch protection
4. Document it in this table
5. Add a validation runbook in `CONTRIBUTING.md`

---

## Running Gates Locally

```bash
# Repo hygiene
grep -rn --include="*.md" --include="*.yml" -e "^<<<<<<< " -e "^=======$" -e "^>>>>>>> " .
yamllint -d "{extends: default, rules: {line-length: {max: 200}}}" .github/workflows/

# Metadata + links
python scripts/validate_artifact_metadata.py
python scripts/check_markdown_links.py

# Lattice KG
python scripts/build_lattice_global_index.py
python scripts/validate_lattice_quality_gates.py
python -m pytest -q tests/test_lattice_kg_hypercube_program.py

# GPTBrain
bash archive/boot/gptbrain/reference_impl/run_checks.sh
```

---

## Cross-References

- [CONTRIBUTING.md](../.github/CONTRIBUTING.md)
- [Swarm Operations Spec](./SWARM_OPERATIONS_SPEC.md)
- [Swarm Health Scorecard](../health/SWARM_HEALTH_SCORECARD.md)

---

*Last updated: 2026-05-29 · Status: Candidate · License: MIT*
