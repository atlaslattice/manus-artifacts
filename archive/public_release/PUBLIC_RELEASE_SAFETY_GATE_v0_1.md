# PUBLIC_RELEASE_SAFETY_GATE_v0.1

```text
STATUS: CANDIDATE SAFETY GATE
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PURPOSE: prevent public-facing mistakes before artifacts leave private/review space
```

## Rule

Public visibility is not public release. Public release is a reviewed state.

```text
A repo can be visible before an artifact is reusable.
A source can be useful before it is publishable.
A graph can be public-facing before every node is public-safe.
```

## Required fields

```yaml
public_release_status: private_raw | private_review | public_candidate | public_reviewed | blocked | deprecated | unknown
rights_status: dave_created | rights_cleared | third_party | mixed | unknown | blocked
license_status: licensed | license_pending | no_license | not_reusable | unknown
sensitive_content: yes | no | unknown
private_data: yes | no | unknown
third_party_content: yes | no | unknown
screenshot_or_chat_log: yes | no | unknown
redaction_status: not_needed | needed | complete | incomplete | unknown
release_blockers: []
safe_public_summary:
reviewer:
review_date:
```

## Release blockers

```yaml
release_blockers:
  - private personal data present
  - medical/legal/financial sensitive content present
  - third-party copyrighted content unclear
  - license missing or ambiguous
  - screenshots/chat logs not reviewed
  - source receipt missing
  - public claim stronger than evidence
  - vendor endorsement implied
  - canon/deployment/proof language present
```

## Release-ready checklist

- [ ] Status strip present.
- [ ] Raw export status visible.
- [ ] Receipt status visible.
- [ ] Missing receipts listed.
- [ ] Rights status reviewed.
- [ ] License status reviewed.
- [ ] Sensitive content reviewed.
- [ ] Third-party content reviewed.
- [ ] Redactions complete or not needed.
- [ ] Safe public summary written.
- [ ] Forbidden claims removed.
- [ ] Human reviewer recorded.

## Safe public summary template

```text
This artifact is a public candidate summary of [artifact]. It is not canon, not deployed, not proof, and carries no external endorsement claim. Source and receipt status are shown below; unresolved gaps are listed as MissingReceipts.
```

## Public release states

```yaml
private_raw:
  meaning: raw material; not public-ready

private_review:
  meaning: available for internal review only

public_candidate:
  meaning: visible or prepared for public review; not reusable by default

public_reviewed:
  meaning: reviewed for public safety, rights, and wording; still not canon unless separately adjudicated

blocked:
  meaning: cannot be public-released until blockers resolve

deprecated:
  meaning: preserved for lineage but not recommended as current public surface
```

## Keeper

```text
Release is a threshold, not a vibe.
```
