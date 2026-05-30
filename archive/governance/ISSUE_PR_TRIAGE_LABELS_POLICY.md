---
artifact_id: DX-POLICY-ISSUE-TRIAGE-LABELS-001
title: Issue and PR Triage Labeling Policy
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, triage, labels, github, automation]
---

# Issue and PR Triage Labeling Policy

> Defines the label taxonomy and triage automation for GitHub issues and pull requests.

status: candidate

---

## Label Taxonomy

### Type Labels (what is it?)

| Label | Color | Use |
|-------|-------|-----|
| `bug` | `#d73a4a` (red) | Something is broken |
| `enhancement` | `#a2eeef` (teal) | New feature or improvement |
| `documentation` | `#0075ca` (blue) | Documentation-only change |
| `governance` | `#6f42c1` (purple) | Policy or governance change |
| `question` | `#d876e3` (pink) | Question; no code change needed |
| `duplicate` | `#cfd3d7` (grey) | Duplicate of another issue |
| `invalid` | `#e4e669` (yellow) | Not applicable or misreported |
| `wontfix` | `#ffffff` (white) | Won't address this |

---

### Effort Labels (how big is it?)

| Label | Use |
|-------|-----|
| `size/xs` | ≤ 1 hour |
| `size/s` | 1–4 hours |
| `size/m` | 4–8 hours (one work session) |
| `size/l` | 1–3 days |
| `size/xl` | > 3 days |

---

### Domain Labels (which area?)

| Label | Use |
|-------|-----|
| `domain/governance` | archive/governance/ changes |
| `domain/kg` | Knowledge graph, scripts/, kg/ changes |
| `domain/docs` | docs/ changes |
| `domain/ci` | .github/workflows/ changes |
| `domain/security` | Security-related changes |
| `domain/testing` | Test suite changes |
| `domain/spec` | archive/spec/ changes |
| `domain/product` | archive/product/ changes |

---

### Status Labels (where is it?)

| Label | Use |
|-------|-----|
| `status/triage` | Needs initial review |
| `status/in-progress` | Actively being worked |
| `status/needs-review` | PR ready for review |
| `status/blocked` | Blocked on external factor |
| `status/stale` | No activity in 60 days |

---

### Special Labels

| Label | Use |
|-------|-----|
| `good first issue` | Fast Lane entry point |
| `help wanted` | Looking for any contributor |
| `accessibility` | Accessibility issue |
| `flaky-test` | Flaky test report |
| `translation-needed` | Translation gap |

---

## Triage Automation (Planned)

A GitHub Actions workflow (`triage.yml`) will:
1. Auto-apply `status/triage` to all new issues
2. Auto-apply `status/stale` to issues with no activity in 60 days
3. Close issues with `status/stale` after 90 days with a polite message
4. Apply domain labels based on PR file paths (using `actions/labeler`)

---

*Atlas Lattice Foundation · status: candidate*
