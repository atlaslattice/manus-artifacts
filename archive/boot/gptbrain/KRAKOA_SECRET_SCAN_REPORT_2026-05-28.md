# Krakoa Secret Scan Report — 2026-05-28

```text
STATUS: SECRET SCAN REPORT — NOT CANON
DATE: 2026-05-28
CANON STATUS: candidate
AUTHORITY: safety audit report
METHOD: grep heuristic pattern scan
```

## Scope

- Repository root: `atlaslattice/manus-artifacts`
- Command pattern classes: API keys, private keys, token/password assignment patterns
- Excluded path: `.git/`

## Result summary

- Total hits: **9**
- Confirmed active credential leaks: **0**
- High-priority remediation: **1** (token-like string in notebook content; redact placeholder)
- Medium-priority hardening: **2** (`token` variable names in extension code; not credentials)
- Low-priority/doc examples: **6**

## Notable findings

1. `codebases/colab-notebooks/sheldongeminiHLE.ipynb`
   - Contains a string literal shaped like a Hugging Face token in a login call.
   - Action: replace with environment-secret placeholder and ensure no real token material remains in notebooks.

2. `aluminum-os/ALUMINUM_PROTOCOL_SPECIFICATION.md`
   - Contains example line `token = ...` in protocol docs.
   - Action: acceptable as documentation; keep non-secret examples explicitly marked as mock values.

3. `codebases/other/` and `codebases/project-symbiote/`
   - Token variable names in code paths (`auth token` flows) without hardcoded credential values.
   - Action: no immediate leak; retain as implementation identifiers.

## Recommendation

- Perform a focused redaction pass for notebook token-like placeholders before public launch.
- Add pre-commit secret scanning in future hardening phase.
