---
artifact_id: ARTIFACT-SECURITY-MD-2026-05-27
title: Security Policy
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---
# Security Policy

## Supported Versions

This repository contains research artifacts, documentation, and reference
implementations. Security disclosures apply primarily to any executable code,
CI workflows, and automation scripts.

| Component | Supported |
|-----------|-----------|
| CI/CD workflows | ✅ Yes |
| Reference implementations (`archive/boot/gptbrain/reference_impl/`) | ✅ Yes |
| Documentation/markdown only | ℹ️ N/A |

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Please report security issues privately via one of the following:

1. **GitHub Private Security Advisory** — [Submit here](../../security/advisories/new)
2. **Email** — atlas-lattice-foundation [at] proton.me  
   Subject line: `[SECURITY] manus-artifacts — <brief description>`

Include:
- A description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact
- Suggested remediation (optional)

## Response Timeline

| Milestone | Target |
|-----------|--------|
| Acknowledgment | Within 48 hours |
| Initial assessment | Within 7 days |
| Remediation / public disclosure | Within 90 days |

We follow coordinated disclosure. We will credit reporters in the release notes
unless they prefer to remain anonymous.

## Scope

The following are **in scope**:

- Secrets or credentials accidentally committed to this repository
- Malicious or unsafe CI workflow configurations
- Supply-chain risks in dependencies used by reference implementations

The following are **out of scope**:

- Theoretical vulnerabilities with no realistic attack vector
- Issues in third-party services referenced by documents (Notion, Drive, etc.)
