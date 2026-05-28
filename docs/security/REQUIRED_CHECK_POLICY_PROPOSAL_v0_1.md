---
artifact_id: DOC-REQUIRED-CHECK-POLICY-PROPOSAL-v0-1-2026-05-28
title: Required Check Policy Proposal
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Required Check Policy Proposal

## Proposed Required Checks for Protected Branches

| Check | Require? | Rationale |
|---|---|---|
| `Secret Scan / Gitleaks scan` | Yes | Prevent secret leakage |
| `Repo Hygiene Checks / Hygiene` | Yes | Prevent broken workflow syntax and merge markers |
| `Lattice KG Quality Gates / Build and validate lattice gates` | Yes | Protect metadata and lattice integrity |
| `Docs Link Checks / Relative Link Validation` | Yes | Protect public navigation and evidence paths |
| `GPTBrain reference checks / Run GPTBrain scaffold checks` | Conditional | Required for PRs touching GPTBrain reference surfaces |
| `Markdown Lint / markdownlint` | Advisory | Keep non-blocking until corpus is normalized |

## Merge Policy

- Require pull requests before merge.
- Require at least 1 approving review.
- Dismiss stale approvals after new commits.
- Require branches to be up to date before merge where feasible.
