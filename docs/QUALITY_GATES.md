# Quality Gates
Status: Candidate
Date: 2026-05-26

This document defines measurable gates for archive readiness at three levels: candidate promotion, public release, and canon promotion.
Gates should be strict enough to protect trust and simple enough to use consistently.

## Gate summary

| Gate | Purpose | Typical owner |
| --- | --- | --- |
| Candidate-ready | Make an artifact safely reviewable in public | Domain steward |
| Public-release-ready | Make an artifact suitable for broad external consumption | Domain steward + communications review |
| Canon-ready | Make an artifact eligible for ratified authority | Full council + @atlaslattice adjudication |

## Candidate-ready gate

An artifact passes the candidate-ready gate when all of the following are true:

- title, status, and date are visible
- structure is coherent and non-fragmentary
- domain and steward are known
- key links resolve
- obvious contradictions are resolved or flagged
- provenance is adequate for the claims being made

## Public-release-ready gate

An artifact passes the public-release-ready gate when candidate-ready requirements are met and:

- a clear summary exists for non-expert readers
- terminology is defined or linked
- sensitive claims have been reviewed for public framing risk
- website publication checklist passes if the artifact is website-bound
- companion materials such as primers, summaries, or FAQs exist where needed

## Canon-ready gate

An artifact passes the canon-ready gate only when all of the following are true:

- candidate-ready and public-release-ready gates already pass
- canon promotion checklist is complete
- lineage and supersession are correct
- vote record is captured
- adjudication path is complete
- canon decision log entry is ready for publication

## Quantitative targets

Use these default thresholds unless a steward documents an exception:

- metadata coverage: 100% for new governance-critical artifacts
- broken links: 0 unresolved internal links
- stale unresolved review comments: 0 for canon-ready artifacts
- blocking provenance gaps: 0 for high-impact claims
- status ambiguity: 0 files presented without visible state label in a release batch

## Gate failure rules

- Failing candidate-ready means the artifact should remain Draft or be revised before broad linking.
- Failing public-release-ready means the artifact may remain in-repo but should not be amplified externally.
- Failing canon-ready means the artifact remains Candidate even if highly polished.

## Related documents

- [CANON_PROMOTION_CHECKLIST.md](./CANON_PROMOTION_CHECKLIST.md)
- [VALIDATION_PLAYBOOK.md](./VALIDATION_PLAYBOOK.md)
- [../governance/WEBSITE_PUBLICATION_GATE.md](../governance/WEBSITE_PUBLICATION_GATE.md)
