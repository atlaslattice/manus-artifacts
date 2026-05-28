# Contributor Decision Tree

> **Status:** CANDIDATE  
> **Artifact Type:** guide  
> **Date:** 2026-05-28  
> **Related:** [Contributing](../.github/CONTRIBUTING.md), [Evidence standards](./evidence-standards.md), [Ratification and Trust Flow](./RATIFICATION_AND_TRUST_FLOW.md)

## What am I trying to do?

Choose the branch that best matches your task.

### 1. Add a new artifact

- read [Contributing](../.github/CONTRIBUTING.md)
- add candidate status and provenance details near the top
- choose a stable path and versioned name
- link related docs and update any required registry metadata
- open a PR with the [PR template](../.github/pull_request_template.md)

### 2. Fix an existing artifact

- confirm whether the artifact is candidate, deprecated, or ratified
- make the smallest complete fix that preserves provenance
- update links, metadata, or receipts if the fix changes trust-relevant facts
- run the existing relevant validation checks before opening the PR
- explain the fix scope in the PR

### 3. Add evidence

- read [Evidence ledger index](./evidence/README.md)
- follow [Evidence standards](./evidence-standards.md)
- create or update the matching `docs/evidence/*.json` entry
- include source paths, AI systems involved, and verification method
- if the evidence is technical, include or reference a validation receipt

### 4. Request ratification

- verify the artifact is still marked candidate
- gather evidence references, review links, and any validation receipts
- read [Ratification and Trust Flow](./RATIFICATION_AND_TRUST_FLOW.md)
- open a review request using the [PR template](../.github/pull_request_template.md) and link supporting evidence
- wait for adjudication by `@atlaslattice`

### 5. Deprecate an artifact

- read [Deprecation and Supersession Policy](./deprecation-policy.md)
- add the required deprecation notice and replacement link
- preserve the old file so inbound links continue to work
- update nearby indexes, registries, or evidence references
- explain the supersession path in the PR

## Quick links

- [Artifact quality rubric](./artifact-quality-rubric.md)
- [Evidence coverage dashboard](./evidence-coverage-dashboard.md)
- [Issue templates](../.github/ISSUE_TEMPLATE/)
