# Incident Response Runbook
Status: Candidate
Date: 2026-05-26

This runbook defines response steps for governance failures and public trust incidents.
The goal is rapid stabilization, accurate public signaling, and durable remediation.

## Incident types

- canon breach
- unauthorized edit to trust-critical material
- stewardship gap on a critical domain
- public trust incident caused by misleading status, provenance, or publication

## Universal response steps

1. identify the affected artifact or surface
2. classify severity and trust impact
3. pause further promotion or publication if needed
4. assign incident lead and domain owner
5. document actions and findings
6. publish corrections or warnings when appropriate

## Scenario: canon breach

Example: a candidate artifact is represented as canon without ratification and adjudication.

Response:

- correct the label immediately
- review where the misstatement propagated
- create a governance incident note
- assess whether public correction is required

## Scenario: unauthorized edits

Response:

- inspect git history and scope of change
- restore accurate state if required
- review access, review process, and oversight gaps
- log preventive actions

## Scenario: stewardship gap

Response:

- activate backup steward
- freeze trust-sensitive actions if necessary
- record continuity risk in the register
- schedule succession handoff actions

## Scenario: public trust incident

Response:

- identify the misleading claim or framing
- verify provenance and lifecycle state
- publish corrective context in the repository or public channel as appropriate
- review whether website publication gate or external review should change

## Post-incident review

Every non-trivial incident should result in:

- root cause analysis
- owner-assigned remediation actions
- cadence follow-up to confirm closure
- risk register update if the issue is systemic
