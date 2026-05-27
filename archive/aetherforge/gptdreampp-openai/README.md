# GPTDream++ OpenAI Staging Package (CANDIDATE)

Status: NON-CANON candidate staging package for Drive→GitHub promotion.

## Scope

This package implements:
- A single promotion gate contract with required provenance fields.
- Artifact-class validation mapping for `dream`, `play`, and `work` artifacts.
- Non-canon-by-default enforcement checks.
- A lightweight "Bullshit Olympics" overclaim/authority-drift review lane.
- Synced high-priority Drive-side artifact receipts.

## Structure

- `schemas/` — JSON schema contracts for promotion-gate records.
- `ruleset/` — promotion and review lane rules.
- `eval_fixtures/` — valid/invalid fixtures for contract checks.
- `delta_templates/` — dream/play/work delta templates.
- `receipts/` — attached receipt records for staged artifacts.
- `manifests/` — high-priority Drive→GitHub sync manifests.

## Validation

- Local enforcement script: `python3 scripts/validate_gptdreampp_promotion_gate.py`
- CI review lane: `.github/workflows/bullshit-olympics-review.yml`
