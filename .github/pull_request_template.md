<!--
  STATUS: PR TEMPLATE — NOT CANON
  SEAT: S7 CopilotBrain / Code Integrator
  PURPOSE: Standardize pull request format across the Council Brain / manus-artifacts repo.
  PROMOTION: Template artifact. Does not ratify canon; human-root review required for any promoted artifact.

  Fill out all sections that apply. Remove sections that do not.
  Keep status labels honest. Do not mark RATIFIED CANON without explicit human-root approval.
-->

## Summary

<!-- One-sentence description of what this PR changes and why. -->

## Status

```text
RUNTIME_LABEL: WORK_OUTPUT | DREAM_OUTPUT | PLAY_OUTPUT | MODEL_ASSESSMENT
CANON_STATUS:  VARIANT_NOT_CANON | CANDIDATE_CANON | CANONICAL_CANDIDATE | RATIFIED_CANON | SCAFFOLD
SEAT:          S1 | S2 | S3 | S4 | S5 | S6 | S7 | MULTI | HUMAN_ROOT
```

## What changed

<!-- List new or modified files with a one-line description each. -->

- `path/to/file.md` — _description_

## Evidence boundary

<!-- Which claim-confidence tier best describes the contents of this PR? -->

- [ ] **C0** — Unsupported or unverified; do not treat as fact.
- [ ] **C1** — User-reported or model-stated; preserve as such.
- [ ] **C2** — Source artifact(s) exist to support the content.
- [ ] **C3** — Multiple converging source artifacts.
- [ ] **C4** — Internally reviewed or scored.
- [ ] **C5** — Independently verified or operationally demonstrated.

## Canon / non-canon checklist

- [ ] Artifacts are correctly labeled (`STATUS: ...` header present in each new file)
- [ ] Play/dream outputs are marked `PLAY OUTPUT — CULTURE LAYER — NOT CANON` or equivalent
- [ ] Variants are preserved, not overwritten
- [ ] No file is silently deleted; supersession or aliasing is documented if applicable
- [ ] No artifact is marked `RATIFIED CANON` without explicit human-root approval
- [ ] Candidate canon is clearly distinguished from ratified canon

## Repo hygiene

- [ ] New paths are added to the relevant index or registry (if applicable)
- [ ] Duplicate artifact risk checked (no unintentional path aliasing)
- [ ] Tests pass (if touching `reference_impl/`)
- [ ] PR adds no credentials, secrets, or private personal data

## Human-root decisions required

<!-- List any decisions that require Dave / human-root sign-off before merging. -->

- [ ] _Decision needed:_ …

## Related issues / artifacts

<!-- Link issues, spec files, or related PRs. -->

- Issue: #
- Artifact: `archive/boot/...`

## Notes for reviewers

<!-- Anything unusual, incomplete, or needing focused review. -->
