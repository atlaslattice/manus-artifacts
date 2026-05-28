# Contributing to manus-artifacts

Thank you for your interest in contributing. This repository is the canonical
public archive of David Sheldon's research, system design, and Aetherforge
council artifacts. All contributions are welcome and subject to the governance
rules below.

## Quick Start

```bash
git clone https://github.com/atlaslattice/manus-artifacts.git
cd manus-artifacts
```

No build step is required — this is primarily a document archive. For code
paths under `archive/boot/gptbrain/reference_impl/`, see the local validation
section below.

## Governance

- **Nothing is canon until ratified** by full council and adjudicated by
  @atlaslattice. All current artifacts are candidates.
- **GitHub is the durable canonical substrate.** Drive and Notion are
  relay/working-vault layers, not canon authorities.
- Follow the repository governance flow in
  [`docs/governance-ratification-process.md`](../docs/governance-ratification-process.md).
- Candidate artifacts are welcome via pull request. Label your PR clearly
  with the domain (e.g., `aluminum-os`, `gptbrain`, `council`).

## Issue Intake Paths

- Use the **Artifact proposal** issue form for new archive artifacts, docs, and
  public candidate additions.
- Use the **Governance / review request** form for provenance review, canon-state
  routing, archive ingestion, and release-readiness requests.
- Use the **Community onboarding / help request** form for first-quest routing,
  navigation help, and newcomer support.
- Use the **GPTDream / Atlas-ORCS task** form for lane-routed GPTDream work.

## Pull Request Guidelines

1. One logical change per PR.
2. Use a clear, present-tense commit message (`add`, `fix`, `update`, `remove`).
3. Reference the relevant domain folder and artifact status in the PR description.
4. Run local validation before opening a PR (see below).
5. All PRs require at least one review before merge.
6. Complete the governance/provenance checklist in
   [`.github/pull_request_template.md`](./pull_request_template.md).

## Local Validation (GPTBrain reference_impl)

```bash
# Lint and format check
ruff check archive/boot/gptbrain/reference_impl/
ruff format --check archive/boot/gptbrain/reference_impl/

# Run tests
python -m pytest archive/boot/gptbrain/reference_impl/ -q

# Run full check suite
bash archive/boot/gptbrain/reference_impl/run_checks.sh
```

## Code of Conduct

All contributors are expected to follow our
[Code of Conduct](./CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the
[MIT License](../LICENSE).
