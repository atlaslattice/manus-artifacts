---
artifact_id: ARTIFACT-ARCHIVE-SPEC-GPTDREAM-APPENDICES-APPENDIX-I-1-FORMAL-MATH-SPINE-V0-2-MD-2026-05-29
title: STATUS: CANDIDATE WORKING SPEC — NOT CANON
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix I.1 — Formal Math Spine v0.2

### I.1 — Formal Math Spine

Claim confidence levels:

```text
C0 — Unknown / unverifiable
C1 — Raw model output (no external evidence)
C2 — Model output with repo artifact citation
C3 — Model output with human-reviewed artifact citation
C4 — Human-reviewed and externally corroborated
C5 — Ratified canon (human-root + publication)
```

Confidence update rules:

```text
conf(A) ≥ C2 iff ∃ artifact_ref(A) in versioned substrate
conf(A) ≥ C3 iff ∃ human_review_event(A) in receipt trail
conf(A) = C5 iff ratification_event(A) AND publication_event(A)

conf(A ∧ B) ≤ min(conf(A), conf(B))
conf(A) does not increase by citation of another C1 claim
```

Claim class promotion:

```text
raw_model_output → parsed_artifact: requires file commit
parsed_artifact → candidate_canon: requires structured review
candidate_canon → ratified_canon: requires human-root ratification
ratified_canon → deployed_fact: requires verified execution
```

No step may be skipped. Jumping from raw_model_output to deployed_fact is an overclaim.
