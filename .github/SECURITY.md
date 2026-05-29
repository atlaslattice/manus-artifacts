# Security Policy

## Supported scope

Security reports are welcome for:

- CI/CD workflows under `.github/workflows/`
- Python automation in `codebases/**`
- GPTBrain reference implementation under `archive/boot/gptbrain/reference_impl/`

## Reporting a vulnerability

Please open a **private security advisory** in GitHub Security for this repository.

If private advisory flow is unavailable, open an issue with minimal public detail and
request a secure handoff channel.

## Response expectations

- Initial triage acknowledgement target: within 3 business days
- Containment/remediation target: risk-based, prioritized by impact and exploitability

## Secret scanning operations

- Enable GitHub secret scanning and push protection for this repository.
- Treat any detected secret as potentially compromised until rotated and revoked.
- Track incident remediation in GitHub with clear timelines and verification notes.

## Hard boundaries

- Do not include secrets, tokens, credentials, or private data in reports.
- GitHub remains the canonical source of truth for remediation tracking.
