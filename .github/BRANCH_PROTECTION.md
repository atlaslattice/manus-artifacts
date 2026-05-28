# Branch Protection Guidance

This repository should use branch protection on the default branch to ensure all
canon and automation safeguards execute before merge.

## Recommended protections

1. Require pull request before merging
2. Require at least one approval
3. Dismiss stale approvals when new commits are pushed
4. Require conversation resolution before merge
5. Require status checks to pass before merge
6. Restrict force-pushes and deletions on the default branch

## Required checks baseline (minimum)

Set these as required checks in branch protection:

- `Conflict markers & workflow YAML syntax` (from `repo-hygiene-checks.yml`)
- `Analyze` (from `codeql.yml`)

## Path-scoped checks (recommended)

Keep these enabled so relevant paths cannot merge without validation:

- `Run GPTBrain scaffold checks` (from `gptbrain-reference-checks.yml`)
- `Artifact sync tests` (from `artifact-sync-tests.yml`)
- `Validate markdown links in canon docs` (from `docs-link-checks.yml`)

## Verification procedure

After enabling branch protection in repository settings:

1. Open a PR to `main` from a temporary branch.
2. Confirm required checks block merge until green.
3. Confirm direct push to `main` is blocked for non-admin flows.
4. Confirm force-push and branch deletion are blocked.
5. Capture final rule configuration in release/readiness notes.

## Canon boundary reminder

GitHub is canonical for review, merge, and remediation history. Drive and Notion
remain relay layers and must not be used as merge authority.
