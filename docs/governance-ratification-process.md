# Governance and Ratification Process

```text
STATUS: CANDIDATE GOVERNANCE SPEC — NOT CANON
```

This document defines the repository-wide governance flow for artifact status,
ratification, and adjudication.

## 1) Artifact status state machine

```text
candidate -> reviewed -> ratified
ratified -> superseded (when replaced by newer ratified artifact)
candidate/reviewed/ratified -> deprecated (kept for lineage; not deleted)
```

### Status definitions

- **candidate**: submitted artifact with no canon authority yet.
- **reviewed**: reviewed artifact that passed scoped checks and review lanes.
- **ratified**: artifact explicitly ratified by full council and adjudicated by
  @atlaslattice.
- **superseded**: ratified artifact replaced by a newer ratified artifact.
- **deprecated**: retained legacy artifact no longer preferred for active use.

## 2) Candidate vs canon boundary

- No artifact is canon by default.
- Ratification requires:
  - explicit ratification event identifier,
  - adjudication decision,
  - trust/provenance evidence references.
- Publication surface alone does not grant canon status.

## 3) Roles and decision rights matrix

| Role | Submit candidate | Review candidate | Ratify canon | Adjudicate canon disputes | Deprecate/supersede |
|---|---|---|---|---|---|
| Contributors | ✅ | ❌ | ❌ | ❌ | ❌ |
| Reviewers/Maintainers | ✅ | ✅ | ❌ | ❌ | ✅ (proposal) |
| Full Council | ✅ | ✅ | ✅ | ✅ (recommendation) | ✅ |
| @atlaslattice | ✅ | ✅ | ✅ (final adjudication gate) | ✅ (final) | ✅ |

## 4) Ratification process (standalone flow)

1. Create or update candidate artifact with explicit candidate labeling.
2. Attach provenance and trust evidence (links, receipts, tests as applicable).
3. Open pull request with governance/trust/provenance checklist.
4. Complete review and validation gates.
5. Record decision in `RATIFICATION_LOG.md` with
   `ratification_event_id`, artifact path, adjudicator, and decision.
6. If ratified, update status references in index documents.

## 5) Governance checklist for PR reviewers

- [ ] Artifact status declared (candidate/reviewed/ratified/deprecated).
- [ ] Canon claim absent unless explicit ratification evidence is present.
- [ ] Provenance header present for major artifacts.
- [ ] Ratification log entry added/updated for canon-impacting decisions.
- [ ] Supersession/deprecation path recorded when replacing prior artifacts.

## 6) Mandatory governance + provenance header for major artifacts

Use the template in:

- `docs/artifact-provenance-header-template.md`

All major new governance, policy, and release artifacts should include this
header block near the top of the file.
