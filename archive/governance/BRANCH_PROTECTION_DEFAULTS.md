---
artifact_id: SEC-POLICY-BRANCH-PROTECTION-001
title: Branch Protection Defaults
status: candidate
created: 2026-05-28
owner: council
tags: [security, governance, branch-protection, ci-cd]
---

# Branch Protection Defaults

> Defines the required branch protection settings for the Atlas Lattice repository.

status: candidate

---

## Protected Branches

| Branch | Protection level | Notes |
|--------|----------------|-------|
| `main` | Strict (see below) | Default branch; all production artifacts |
| `release/*` | Strict | Release branches when created |
| `copilot/*` | Basic | Agent work branches |

---

## Main Branch Protection Requirements

The following settings must be enabled on the `main` branch:

| Setting | Required value | Rationale |
|---------|--------------|----------|
| Require pull request reviews | 1 approval minimum | No direct push |
| Dismiss stale reviews on new commits | Enabled | Prevents stale approvals |
| Require status checks to pass | All CI gates (see below) | Gates must pass before merge |
| Require branches to be up to date | Enabled | Prevents integration failures |
| Require linear history | Optional (recommended) | Cleaner git log |
| Include administrators | Enabled | Admins follow the same rules |
| Allow force pushes | Disabled | Prevent history rewriting |
| Allow deletions | Disabled | Prevent branch deletion |

---

## Required Status Checks (main)

These CI jobs must pass before merge to `main`:

| Status check | Workflow |
|-------------|---------|
| `boring-machine-validation` | `boring-machine-validation.yml` |
| `gptbrain-reference-checks` | `gptbrain-reference-checks.yml` |
| `lattice-kg-quality-gates` | `lattice-kg-quality-gates.yml` |

---

## Review Authority

| Scenario | Who can approve |
|----------|----------------|
| Documentation-only PR | Any council member |
| Schema or code change | @atlaslattice or designated technical reviewer |
| Security-sensitive change | @atlaslattice required |
| Governance policy change | @atlaslattice required |

---

## Emergency Override

In a critical incident, @atlaslattice may merge directly to `main` using admin override. This must be:
1. Documented in the [INCIDENT_RESPONSE_RUNBOOK.md](./INCIDENT_RESPONSE_RUNBOOK.md)
2. Followed by a post-incident PR within 24 hours that restores proper process
3. Logged in [COMPLIANCE_EVIDENCE_INDEX.md](./COMPLIANCE_EVIDENCE_INDEX.md)

---

## Audit

Branch protection settings are reviewed quarterly. Settings are verified by inspecting the GitHub repository Settings > Branches > `main` protection rules.

---

*Atlas Lattice Foundation · status: candidate*
