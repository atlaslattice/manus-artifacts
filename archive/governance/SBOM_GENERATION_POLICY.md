---
artifact_id: SEC-POLICY-SBOM-001
title: SBOM Generation Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, sbom, supply-chain, dependencies]
---

# SBOM Generation Policy

> Defines how Software Bill of Materials (SBOMs) are generated, maintained, and published for the Atlas Lattice repository.

status: candidate

---

## What Is an SBOM?

A Software Bill of Materials (SBOM) is a machine-readable inventory of all software components, dependencies, and their versions used in a project. SBOMs enable:
- Supply chain transparency
- Vulnerability tracking (compare SBOM against CVE databases)
- Compliance reporting
- Dependency auditing

---

## SBOM Scope

| Component | Included? | Notes |
|-----------|---------|-------|
| Python runtime dependencies | Yes | `requirements*.txt`, `pyproject.toml` |
| Python dev/test dependencies | Yes (separate SBOM) | `requirements-dev.txt` |
| GitHub Actions (CI deps) | Yes | Workflow action versions |
| Markdown/documentation only files | No | Not software components |
| JavaScript/npm (if any) | Yes | `package.json` |

---

## SBOM Format

Primary format: **SPDX 2.3** (JSON)
Secondary format: **CycloneDX 1.4** (JSON)

Both are widely supported by vulnerability scanners and compliance tools.

---

## Generation Process

### Automated (Planned: Q3 2026)

A GitHub Actions workflow will generate and commit the SBOM on every push to main:

```yaml
# .github/workflows/sbom-generation.yml (planned)
- name: Generate SBOM
  uses: anchore/sbom-action@...  # pinned SHA
  with:
    format: spdx-json
    output-file: sbom/atlas-lattice-sbom.spdx.json
```

**Output location:** `sbom/atlas-lattice-sbom.spdx.json`

### Manual (Current)

Until the workflow is live, generate the SBOM manually using `syft`:

```bash
pip install syft  # or install via https://github.com/anchore/syft
syft . -o spdx-json=sbom/atlas-lattice-sbom.spdx.json
```

Regenerate and commit the SBOM whenever `requirements*.txt` or `pyproject.toml` changes.

---

## SBOM Distribution

| Location | Audience | Update frequency |
|----------|---------|-----------------|
| `sbom/atlas-lattice-sbom.spdx.json` | Machine consumers, auditors | Every push to main (planned) |
| GitHub Release assets | External users of tagged releases | Every release |

---

## SBOM-to-CVE Scanning

The SBOM is scanned against the NVD (National Vulnerability Database) using `grype`:

```bash
grype sbom:sbom/atlas-lattice-sbom.spdx.json
```

Results feed into the [Vulnerability Triage SLAs](./VULNERABILITY_TRIAGE_SLAS.md) process.

---

## Compliance

SBOM generation is tracked as evidence in the [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md). Quarterly SBOM reviews are part of the [Quarterly Legal Trust Audit Template](./QUARTERLY_LEGAL_TRUST_AUDIT_TEMPLATE.md).

---

*Atlas Lattice Foundation · status: candidate*
