# Provenance Evidence Tiering Model
Status: Candidate
Date: 2026-05-28

This model defines evidence tiers so reviewers can quickly judge claim strength.
It standardizes provenance quality language across governance and public surfaces.

## Tier definitions

| Tier | Label | Evidence quality | Typical use |
| --- | --- | --- | --- |
| T0 | Unverified assertion | No source attached | Draft ideation only (not publishable claims) |
| T1 | Single-source claim | One source, limited corroboration | Internal note with explicit uncertainty |
| T2 | Multi-source corroborated | Two or more aligned sources | Candidate artifacts and routine public summaries |
| T3 | Review-backed evidence | Corroborated sources + reviewer sign-off | High-impact candidate and governance packets |
| T4 | Decision-grade evidence | T3 + council review/adjudication record | Canon promotion and high-stakes publication |

## Minimum tier by claim class

| Claim class | Minimum required tier |
| --- | --- |
| General archive orientation | T1 |
| Operational/process claim | T2 |
| High-impact institutional claim | T3 |
| Canon authority/lifecycle claim | T4 |
| Sensitive health/public-risk claim | T3 (T4 if canon-bound) |

## Promotion path

1. Start at observed tier based on attached sources.
2. Add corroboration and context notes to raise T1 to T2.
3. Add review records to raise T2 to T3.
4. Add ratification/adjudication artifacts to raise T3 to T4.

## Failure handling

- Claims below required tier must be downgraded, relabeled, or withheld.
- If a claim tier regresses after publication, issue a correction note and review risk impact.
- Tier disputes route through `governance/COUNCIL_REVIEW_WORKFLOW.md`.

## Citations

- Source: [PROVENANCE_REQUIREMENTS.md](./PROVENANCE_REQUIREMENTS.md)
- Source: [CANON_AUDIT_PROTOCOL.md](./CANON_AUDIT_PROTOCOL.md)
- Source: [COUNCIL_REVIEW_WORKFLOW.md](./COUNCIL_REVIEW_WORKFLOW.md)
