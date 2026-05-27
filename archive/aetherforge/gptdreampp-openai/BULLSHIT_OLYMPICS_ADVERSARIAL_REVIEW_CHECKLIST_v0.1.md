# Bullshit Olympics Adversarial Review Checklist v0.1

```text
STATUS: REVIEW CHECKLIST — CANDIDATE — NOT CANON
PURPOSE: detect authority drift, canon drift, deployment overclaim, and provenance gaps
```

## A. Authority drift checks

- [ ] Any wording that implies model output has governance authority.
- [ ] Any wording that bypasses human-root review.
- [ ] Any role confusion between staging tools and adjudication authority.

## B. Canon drift checks

- [ ] Any artifact marked/phrased as canon without ratification metadata.
- [ ] Any candidate artifact promoted by implication only.
- [ ] Any missing `canon_status` field.

## C. Deployment-claim drift checks

- [ ] Any deployment/runtime claim without executable receipt evidence.
- [ ] Any benchmark/performance claim without reproducible fixture references.
- [ ] Any “done” status without linked implementation artifact.

## D. Provenance gap checks

- [ ] Missing source path.
- [ ] Missing source hash.
- [ ] Missing attribution.
- [ ] Missing contamination flags and review status.

## E. Disposition

- `retain` — language and receipts pass checks.
- `quarantine` — unresolved risk; keep as candidate.
- `escalate` — send to adjudication lane with explicit issues.
