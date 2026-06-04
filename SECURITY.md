# Security Policy — Atlas Lattice Foundation

## Overview

The Atlas Lattice Foundation is committed to building and maintaining transparent, trustworthy, and secure systems. This document describes our security policy and how to report vulnerabilities or concerns.

---

## Scope

This policy applies to:

- All code in this repository (`atlaslattice/manus-artifacts`)
- The Aluminum OS microkernel (`aluminum-os-core/`)
- Python tooling in `codebases/` and `archive/boot/gptbrain/reference_impl/`
- CI/CD workflows in `.github/workflows/`

This policy **does not** apply to:
- External services linked from documentation (Notion, Google Drive, Pinecone cloud)
- Third-party repositories referenced in integration plans

---

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please **do not** open a public GitHub Issue.

### Responsible Disclosure

1. **Email:** Contact the repository owner through GitHub's private vulnerability reporting feature.
   - Navigate to the [Security tab](https://github.com/atlaslattice/manus-artifacts/security) → *Report a vulnerability*
2. **Include:**
   - Description of the vulnerability
   - Steps to reproduce
   - Affected file(s) and line number(s)
   - Potential impact assessment
3. **Response time:** We aim to acknowledge reports within 72 hours and provide a resolution timeline within 7 days.

---

## Security Principles

The Atlas Lattice Foundation's security philosophy is grounded in Aluminum OS constitutional principles:

1. **Health Data Sovereignty (INV-26):** Patient health data belongs to the patient, cryptographically signed, IPFS-backed, and portable. No institution may hold it hostage.
2. **Post-Quantum Cryptography:** All cryptographic implementations target PQC standards (see `aluminum-os-core/`).
3. **Full Transparency:** Security incidents are disclosed publicly after remediation. See [Full Transparency Policy](./archive/boot/governance/FULL_TRANSPARENCY_POLICY_2026-05-09.md).
4. **Zero Trust by Default:** No agent, system, or contributor inherits elevated trust without explicit ratification.

---

## Supported Versions

| Component | Supported | Notes |
|---|---|---|
| `aluminum-os-core/` (Rust) | ✅ Yes | Active development |
| `archive/boot/gptbrain/reference_impl/` (Python) | ✅ Yes | Active checks |
| `codebases/` (Python) | ✅ Yes | Active tooling |
| Documentation (`.md` files) | ⚠️ Informational | No code execution |
| Legacy `aluminum-os/` specs (v1–v3) | ⚠️ Historical | Not actively maintained |

---

## Known Limitations

- This is a research and archival repository. Not all code artifacts are production-hardened.
- Artifact sync tooling (`codebases/*/artifact_sync.py`) requires API keys; never commit secrets.
- CI workflows use `permissions: contents: read` where possible to minimize blast radius.

---

## Credential Safety

**Never commit secrets to this repository.** This includes:
- API keys (Pinecone, OpenAI, Gemini, GitHub)
- Personal access tokens
- Private keys or certificates
- Passwords

If you accidentally commit a secret, immediately:
1. Rotate the credential at the provider
2. Open a private vulnerability report
3. The exposed credential should be considered fully compromised

---

*Security policy maintained by the Atlas Lattice Foundation · Last updated: 2026-05-26*
