# Contributing to Manus Artifacts

Thank you for helping build the Atlas Lattice public knowledge archive. 🌐

## Governance First

> **Nothing is canon until ratified by full council and adjudicated by @atlaslattice.**
> All current artifacts are *candidates*. GitHub is the durable canonical substrate;
> Drive and Notion are relay/working-vault layers, not canon authorities.

## Ways to Contribute

| Contribution type | How |
|---|---|
| Bug / broken link in a doc | Open an Issue → Bug Report |
| New artifact or research | Open an Issue → Artifact Proposal |
| Feature request for tooling | Open an Issue → Feature Request |
| Code fix | Fork → branch → PR |
| Documentation improvement | Fork → branch → PR |

## Branch Naming

```text
<github-username>/<short-description>
```

Example: `atlaslattice/fix-aluminum-os-links`

## Commit Messages

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

```text
<type>: <short summary>

Types: feat | fix | docs | chore | refactor | test | ci
```

## Pull Request Checklist

Before opening a PR:

- [ ] Title follows Conventional Commits format
- [ ] No secrets, credentials, or PII committed
- [ ] Markdown files are well-formed (`python scripts/check_markdown_docs.py`)
- [ ] New Python code passes `ruff check` and `ruff format --check`
- [ ] GPTBrain scaffold checks pass (if touching `archive/boot/gptbrain/`):
  ```bash
  cd archive/boot/gptbrain/reference_impl
  python -m pytest -q
  bash run_checks.sh
  ```

## Canon Boundary Rules

1. Do **not** mark any artifact as "canonical" without explicit ratification by @atlaslattice.
2. Prefix candidate artifacts with a clear status badge: `> **Status:** Candidate`
3. Archive paths follow the pattern `archive/<subsystem>/<artifact-name>.md`
4. All dates use ISO-8601 (`YYYY-MM-DD`).

## Code Style

- Python: formatted with [ruff](https://docs.astral.sh/ruff/) (`ruff format`)
- Markdown: ATX headings (`#`), fenced code blocks, no trailing whitespace
- YAML: 2-space indent

## Docs Quality Check

Run this before opening a PR that changes repository documentation surfaces:

```bash
python scripts/check_markdown_docs.py
```

## Community

Please read our [Code of Conduct](../CODE_OF_CONDUCT.md) before participating.
Questions? Open a [GitHub Discussion](https://github.com/atlaslattice/manus-artifacts/discussions).
