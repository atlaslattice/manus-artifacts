# Pull Request

```text
STATUS: PR REVIEW PACKET
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
```

## Summary

Describe the change in plain language.

## Files changed

- [ ] List files added or modified
- [ ] Note any generated files
- [ ] Note any templates or schemas added

## Source / receipt scope

```yaml
source_surface:
source_uri_or_path:
raw_export_status:
receipt_status:
linked_claims:
missing_receipts:
```

## Receipt status checklist

- [ ] Search hit is not being treated as verification
- [ ] Partial content is marked as partial
- [ ] Full exports are identified when present
- [ ] Hashes are included when available
- [ ] Missing receipts are documented instead of hidden
- [ ] Private / sensitive / rights-unclear material is not exposed as public-safe

## Claim safety checklist

- [ ] No canon claim
- [ ] No deployment claim
- [ ] No proof claim
- [ ] No vendor endorsement claim
- [ ] No “tests passing” claim without test receipt
- [ ] No coverage/count claim without report receipt
- [ ] No public-release claim without review status

## Tests / checks run

```text
Commands run:
Results:
Known failures:
Skipped checks and reason:
```

## Blockers / missing receipts

List unresolved gaps.

```yaml
missing_receipts:
  - id:
    claim_or_artifact:
    why_needed:
    next_action:
```

## Safe claim

Write the strongest safe claim this PR supports.

```text
...
```

## Forbidden claims avoided

List any tempting but unsupported claims this PR avoids.

```text
...
```

## Human review needed

- [ ] Rights/license review
- [ ] Public release review
- [ ] Canon/governance review
- [ ] Technical verification
- [ ] Privacy/safety review
- [ ] Not applicable

## Keeper

```text
A PR moves work. It does not crown work.
```
