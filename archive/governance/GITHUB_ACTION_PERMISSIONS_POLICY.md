---
artifact_id: SEC-POLICY-GITHUB-ACTION-PERMISSIONS-001
title: GitHub Action Permissions Minimization Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, github-actions, permissions, supply-chain]
---

# GitHub Action Permissions Minimization Policy

> Defines how GitHub Actions workflow permissions are minimized to reduce attack surface.

status: candidate

---

## The Risk

GitHub Actions workflows run with a `GITHUB_TOKEN` that can have broad repository permissions. If a malicious action or compromised dependency gains code execution in a workflow, over-permissioned tokens enable significant damage: deleting branches, creating releases, modifying issues, or accessing secrets.

---

## Required Settings

### Repository-Level Default Permissions

In GitHub repository Settings > Actions > General:
- **Workflow permissions:** Set to `Read repository contents and packages permissions` (read-only default)
- **Allow GitHub Actions to create and approve pull requests:** Disabled (unless a specific workflow requires it)

### Workflow-Level Permissions

Every workflow file must declare explicit permissions:

```yaml
name: Example Workflow
on: [push]

permissions:
  contents: read   # minimum default

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read   # per-job override if needed
    steps:
      - uses: actions/checkout@...
```

---

## Permission Inventory

Current workflows and their required permissions:

| Workflow | Required permissions | Reason |
|----------|--------------------|----|
| `boring-machine-validation.yml` | `contents: read` | Read source only |
| `gptbrain-reference-checks.yml` | `contents: read` | Read source only |
| `lattice-kg-quality-gates.yml` | `contents: read` | Read + run scripts |
| Drift detection (planned) | `contents: read`, `issues: write` | Opens drift issues |
| SBOM generation (planned) | `contents: read`, `id-token: write` | Sigstore OIDC signing |

---

## Third-Party Action Risk

Third-party actions run in the workflow context and may have access to the `GITHUB_TOKEN`. Mitigations:

1. **Pin to SHA** (per [GITHUB_ACTIONS_VERSION_PINNING_POLICY.md](./GITHUB_ACTIONS_VERSION_PINNING_POLICY.md))
2. **Scope permissions minimally** — jobs using third-party actions have only the minimum required permissions
3. **Prefer GitHub's verified actions** (`actions/*`, `github/*`) over unverified community actions
4. **Review action source** before first use

---

## Audit

Workflow permissions are audited quarterly as part of the security review. Changes to workflow permissions require @atlaslattice approval.

---

*Atlas Lattice Foundation · status: candidate*
