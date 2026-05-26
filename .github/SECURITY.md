# Security Policy

## Supported Versions

This repository is a public archive of research artifacts, design documents, and
system specifications. It does not ship production software with version release
cycles. Security considerations apply to:

| Area | Status |
|---|---|
| CI / GitHub Actions workflows | Actively maintained |
| Python scripts (`codebases/`, `scripts/`) | Best-effort review |
| Configuration files | Actively reviewed |

## Reporting a Vulnerability

If you discover a security vulnerability in this repository (e.g., a leaked
secret, an unsafe CI step, or a script with a remote-code-execution risk),
please **do not** open a public issue.

Instead:

1. Open a [GitHub Security Advisory](https://github.com/atlaslattice/manus-artifacts/security/advisories/new)
   via the **Security** tab of this repository, **or**
2. Email the maintainer directly (contact information is in the `about/` directory).

Please include:
- A description of the vulnerability
- Steps to reproduce or a proof-of-concept
- The potential impact

You can expect an acknowledgement within **72 hours** and a resolution or
mitigation plan within **14 days** of confirmed impact.

## Out of Scope

- Design documents, markdown prose, or speculative architecture described in
  artifacts — these are research-grade and not deployed systems.
- Third-party links or references within documents.
