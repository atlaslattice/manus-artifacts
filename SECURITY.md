# Security Policy

## Supported Versions

This repository is a public knowledge archive. Security considerations primarily apply
to any runnable code (Python scripts, CI tooling) and credential handling.

| Area | Supported |
|---|---|
| Python scripts in `codebases/` and `archive/` | ✅ |
| CI workflow files in `.github/workflows/` | ✅ |
| Documentation / Markdown files | N/A |

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Please report security issues privately by emailing the maintainer or using
[GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)
for this repository.

Include:
1. A clear description of the vulnerability
2. Steps to reproduce (proof of concept if applicable)
3. Potential impact assessment
4. Suggested remediation if known

**Response SLA:** We aim to acknowledge reports within 72 hours and provide a remediation
timeline within 7 days.

## Scope

- Exposed secrets or credentials accidentally committed
- Code execution vulnerabilities in Python scripts
- CI pipeline injection vulnerabilities
- Dependency vulnerabilities in `requirements*.txt` or `pyproject.toml` files

## Out of Scope

- Markdown content inaccuracies (use a regular issue instead)
- Broken links (use a regular issue instead)
