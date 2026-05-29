## Summary

<!-- What does this PR do? One paragraph. -->

## Type of Change

- [ ] Bug fix
- [ ] New artifact / documentation
- [ ] Code / tooling improvement
- [ ] CI / infrastructure
- [ ] Refactor
- [ ] Other: ___

## Checklist

- [ ] PR title follows Conventional Commits format (`feat:`, `fix:`, `docs:`, `chore:`, etc.)
- [ ] No secrets, credentials, or PII committed
- [ ] Markdown is well-formed; relative links verified
- [ ] New Python code passes `ruff check` and `ruff format --check`
- [ ] GPTBrain checks pass if `archive/boot/gptbrain/` was touched:
  ```bash
  cd archive/boot/gptbrain/reference_impl && python -m pytest -q && bash run_checks.sh
  ```
- [ ] No artifact is marked "canonical" without @atlaslattice ratification

## Related Issues

Closes #<!-- issue number -->

## Notes for Reviewers

<!-- Anything that would help a reviewer understand the change. -->
