---
artifact_id: CICD-POLICY-DEPENDABOT-001
title: Dependabot Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, dependabot, dependencies, security, supply-chain]
---

# Dependabot Policy

> Defines how Dependabot is configured and managed for the Atlas Lattice repository.

status: candidate

---

## Dependabot Scope

Atlas Lattice uses Dependabot for:

| Ecosystem | Location | Update type |
|-----------|---------|------------|
| Python (pip) | `requirements*.txt`, `pyproject.toml` | Security + minor |
| GitHub Actions | `.github/workflows/` | Security + minor |
| npm (if any) | `package.json` | Security only |

---

## Update Policy

| Update type | Auto-merge? | Review required? |
|-------------|-----------|-----------------|
| Security patch (patch version) | Yes — if CI passes | No |
| Security update (minor version) | No | Yes — section owner |
| Feature update (minor version) | No | Yes — @atlaslattice |
| Major version bump | No | Yes — full council review |

---

## Dependabot Configuration

Current configuration is in `.github/dependabot.yml`. It should be structured as:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "automated"

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "ci-cd"
```

---

## PR Review Process for Dependabot PRs

1. Check CI passes (all quality gates green)
2. Review the changelog of the updated dependency
3. Verify no breaking changes for the version bump
4. For security patches: approve and merge immediately
5. For feature/major updates: assess impact on test suite and reference implementations

---

## Dependency Freeze Windows

During major ratification reviews or council sessions, dependency auto-merges may be paused. Freeze windows are announced in the repository's GitHub Discussions.

---

## Monitoring

Dependabot PRs are tracked in the [Public Risk Register](./PUBLIC_RISK_REGISTER.md) if they involve high-severity CVEs. All Dependabot activity is logged in the [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md) quarterly.

---

*Atlas Lattice Foundation · status: candidate*
