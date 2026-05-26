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

## Recommended required checks

Set these as required checks in branch protection:

- `Conflict markers & workflow YAML syntax` (from `repo-hygiene-checks.yml`)
- `Analyze` / CodeQL job (from `codeql.yml`)

Path-scoped checks should remain enabled and will run when relevant files change:

- `Run GPTBrain scaffold checks` (from `gptbrain-reference-checks.yml`)
- `Artifact sync tests` (from `artifact-sync-tests.yml`)
- `Validate markdown links in canon docs` (from `docs-link-checks.yml`)

## Canon boundary reminder

GitHub is canonical for review, merge, and remediation history. Drive and Notion
remain relay layers and must not be used as merge authority.
