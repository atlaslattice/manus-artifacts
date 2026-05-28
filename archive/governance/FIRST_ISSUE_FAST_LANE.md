---
artifact_id: DX-POLICY-FIRST-ISSUE-FAST-LANE-001
title: First Issue Fast Lane
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, onboarding, first-issue, community]
---

# First Issue Fast Lane

> Defines the pipeline for identifying, labeling, and supporting first-time contributor issues.

status: candidate

---

## What Is the First Issue Fast Lane?

The Fast Lane is a curated set of GitHub issues specifically maintained for first-time contributors. These issues are:
- Well-defined with clear acceptance criteria
- Small in scope (completable in a few hours)
- Labeled `good first issue`
- Mentored (a council member is assigned to answer questions)

---

## Issue Selection Criteria

An issue qualifies for `good first issue` if:
- [ ] The fix is isolated to ≤ 3 files
- [ ] No deep context about the codebase is needed to start
- [ ] Clear "done" criteria can be written in ≤ 5 bullet points
- [ ] A more experienced contributor is willing to mentor

---

## Issue Template: Good First Issue

When creating a Fast Lane issue, use this structure:

```markdown
## Summary
[One sentence: what needs to be done]

## Background
[1-2 sentences: why this matters]

## Acceptance Criteria
- [ ] [Specific, testable criterion 1]
- [ ] [Specific, testable criterion 2]
- [ ] [Specific, testable criterion 3]

## Hints
- [Where to start looking in the codebase]
- [Relevant docs/policies to read first]

## Mentor
@[council-member-username] is available to answer questions.
```

---

## Fast Lane SLAs

| Action | SLA |
|--------|-----|
| Respond to first comment on a Fast Lane issue | 48 hours |
| Review first PR draft from a first-time contributor | 5 business days |
| Provide actionable feedback on a stalled Fast Lane PR | 7 days |

---

## Fast Lane Metrics

Track monthly in the quality report:
- Number of active Fast Lane issues
- Number of Fast Lane PRs opened
- Number of Fast Lane PRs merged
- Average time from first PR to merge

**Target:** ≥ 2 Fast Lane merges per month when contribution velocity allows.

---

## Fast Lane Maintenance

The Fast Lane is reviewed monthly:
- Issues that have been open > 90 days without a PR are reassigned or closed
- New Fast Lane issues are added when existing ones are claimed

---

*Atlas Lattice Foundation · status: candidate*
