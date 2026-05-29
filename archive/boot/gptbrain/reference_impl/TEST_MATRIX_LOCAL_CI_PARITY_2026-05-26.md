# GPTBrain Reference Impl Test Matrix (Local/CI Parity)

```text
STATUS: TEST MATRIX — NOT CANON
DATE: 2026-05-26
CANON STATUS: candidate
AUTHORITY: validation reference
```

| Surface | Local command | CI workflow step |
|---|---|---|
| Pytest suite | `python -m pytest -q` | `.github/workflows/gptbrain-reference-checks.yml` / Run pytest suite |
| CLI smoke harness | `bash run_checks.sh` | `.github/workflows/gptbrain-reference-checks.yml` / Run local check harness |
| Atlas gate checks | `python atlasbrain_gate.py` | Included by pytest gate tests |
