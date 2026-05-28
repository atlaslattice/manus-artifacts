---
artifact_id: DOC-BRANCH-PROTECTION-RECOMMENDATION-v0-1-2026-05-28
title: Branch Protection Recommendation
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Branch Protection Recommendation

## Recommended Settings for `main`

- Require a pull request before merging
- Require at least 1 approval
- Dismiss stale approvals when new commits are pushed
- Require conversation resolution before merge
- Require status checks to pass before merging
- Require linear history only if it does not disrupt evidence preservation workflows
- Restrict force pushes
- Restrict branch deletion

## Recommended Required Checks

See [Required Check Policy Proposal](./REQUIRED_CHECK_POLICY_PROPOSAL_v0_1.md).

## Notes

Because this repository contains archival and governance evidence, protection settings should prioritize auditability and review traceability over raw speed.
