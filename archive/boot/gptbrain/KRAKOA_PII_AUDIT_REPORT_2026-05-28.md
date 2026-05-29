# Krakoa PII Audit Report — 2026-05-28

```text
STATUS: PII AUDIT REPORT — NOT CANON
DATE: 2026-05-28
CANON STATUS: candidate
AUTHORITY: privacy audit report
METHOD: regex heuristic scan (emails, phone, SSN patterns)
```

## Scope

- Repository root: `atlaslattice/manus-artifacts`
- Pattern classes: email-like strings, phone-like strings, SSN-like strings
- Excluded path: `.git/`

## Result summary

- Total hits: **46**
- SSN-like hits: **0**
- Email-like hits: mostly documentation examples + a small set of real-world account references
- Phone-like hits: concentrated in public health-rights contact resources

## Notable findings

1. `health/texas-neuro-rehab-patient-rights.md`
   - Contains multiple public hotline and regulatory contact numbers/emails.
   - Classification: expected public contact references, not private personal PII.

2. `codebases/uws/UWS_ALUMINUM.md` and `codebases/uws/UWS_ALUMINUM_OS_V1_ARCHITECTURE.md`
   - Contains explicit account email references.
   - Recommendation: decide whether these should remain for provenance or be converted to redacted placeholders for open-source publication.

3. Other email hits
   - Mostly example addresses (`example.com`, mock docs).
   - Low risk.

## Recommendation

- Keep public hotline/regulator references as-is.
- Redact or alias non-essential personal account addresses before public mirror/release.
