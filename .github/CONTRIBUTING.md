# Contributing

## Canon boundary

- GitHub repository artifacts are canonical.
- External vaults/notes can be drafting inputs, not canon authority.
- Promote claims only with lineage and human-root review where required.

## Local validation (GPTBrain reference_impl)

From:
`/home/runner/work/manus-artifacts/manus-artifacts/archive/boot/gptbrain/reference_impl`

Run:

```bash
python -m pytest -q
bash run_checks.sh
```

Optional formatting/lint (if `ruff` is available):

```bash
ruff check .
ruff format --check .
```
