# Merge Readiness Checklist

## Purpose

Use this checklist when reviewing TIDELOCK-related PRs or habitat changes before merge recommendation.

This checklist supports review discipline. It does not grant merge authority.

## Status

Candidate review artifact.  
Not canon.  
No authority effect.  
No deployment effect.

## Checklist

### Scope and target

- [ ] PR or change target is explicitly identified
- [ ] Files changed are known and relevant to stated scope
- [ ] No unexplained scope expansion is present

### Evidence and parsing

- [ ] Raw evidence is distinguished from parsed or summarized output
- [ ] Claims are traceable to repo-visible artifacts
- [ ] No implementation proof is asserted without receipts

### Boundary safety

- [ ] No hidden memory claims
- [ ] No canon claims
- [ ] No merge-authority claims
- [ ] No deployment-authority claims
- [ ] No runtime-authority claims

### Review hygiene

- [ ] Blockers are listed explicitly
- [ ] Patch items are minimal and concrete
- [ ] Open questions are stated where uncertainty remains
- [ ] Next safest action is provided

### Routing

- [ ] Interactive review work is routed to GitHub Copilot where appropriate
- [ ] Narrow async work is routed to Copilot Tasks where appropriate
- [ ] Human/root approval is preserved for merge, canon, and deployment decisions

## Recommendation output

Suggested final output shape:

```yaml
verdict: ready | needs_patch | blocked
blockers: []
patch_items: []
open_questions: []
next_safest_action: ""
boundary_note: ""
```

## Keeper

```text
Review is not authority.
A checklist is not a merge.
Receipts before approval.
```
