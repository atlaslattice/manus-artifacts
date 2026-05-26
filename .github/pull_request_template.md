## Summary

<!-- What does this PR do? One sentence. -->

## Changes

<!-- List the key files changed and why. -->

## Risk and rollback

<!-- What could go wrong and how would we quickly roll this back? -->

## Validation evidence

<!-- Paste command outputs, workflow links, or exact evidence paths. -->

## Checklist

- [ ] `ruff check archive/boot/gptbrain/reference_impl/` passes
- [ ] `ruff format --check archive/boot/gptbrain/reference_impl/` passes
- [ ] `python -m pytest -q` passes (from `archive/boot/gptbrain/reference_impl/`)
- [ ] `bash run_checks.sh` passes (from `archive/boot/gptbrain/reference_impl/`)
- [ ] No candidate canon was promoted without human-root approval
- [ ] No C0 claims are asserted as fact
- [ ] Risk and rollback section completed
- [ ] Validation evidence section completed

## Related issues

<!-- Closes #... -->
