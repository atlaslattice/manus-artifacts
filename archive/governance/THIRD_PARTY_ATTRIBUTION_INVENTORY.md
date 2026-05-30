# Third-Party Attribution Inventory

*Atlas Lattice Foundation · Aetherforge Mission #14 · 2026-05-28*

status: candidate

> Catalog of all third-party libraries, tools, data sources, and content used in the Atlas Lattice repository, with their licenses and attribution requirements.

---

## Overview

Atlas Lattice is an MIT-licensed open-source repository. We are committed to honoring all third-party licenses and providing accurate attribution. This inventory is updated with each significant dependency addition.

---

## Python Dependencies

| Package | Version | License | Used In | Attribution Required |
|---------|---------|---------|---------|---------------------|
| `pytest` | ≥7.0 | MIT | `tests/`, `reference_impl/` | No (dev dependency) |
| `jsonschema` | ≥4.0 | MIT | `reference_impl/`, schema validation | No |
| `pyyaml` | ≥6.0 | MIT | Schema parsing, scripts | No |

> Note: Pinned versions are maintained in individual `requirements.txt` or `pyproject.toml` files where present.

---

## GitHub Actions

| Action | Publisher | License | Used In |
|--------|-----------|---------|---------|
| `actions/checkout` | GitHub | MIT | All CI workflows |
| `actions/setup-python` | GitHub | MIT | Python CI workflows |
| `actions/cache` | GitHub | MIT | CI caching |
| `DavidAnson/markdownlint-cli2-action` | David Anson | MIT | Markdown lint workflow |

---

## Content & Standards References

| Resource | Source | License / Terms | Usage |
|----------|--------|-----------------|-------|
| JSON Schema specification | json-schema.org | MIT/Apache | Schema authoring |
| OpenAI API message format | OpenAI | Public reference | GPTDream++ packet schema |
| SPDX License List | Linux Foundation | CC-BY-3.0 | License identification |

---

## Fonts, Icons, Media

No third-party fonts, icons, or media assets are currently included in this repository.

---

## Attribution Statements

Where third-party content has specific attribution requirements, they are noted here:

- **SPDX License List** (Linux Foundation): Licensed under Creative Commons Attribution 3.0. Used for license identification shortcodes only; no redistribution of the list itself.

---

## Maintenance

- This inventory is reviewed quarterly during the [Council Review Cadence](./COUNCIL_REVIEW_CADENCE.md).
- Any contributor adding a new third-party dependency must update this file in the same PR.
- Incompatible licenses (GPL, AGPL, proprietary) require council review before inclusion.

---

## Related Documents

- [License Header Audit Report](./LICENSE_AUDIT_REPORT.md)
- [Trademark Usage Guide](./TRADEMARK_USAGE_GUIDE.md)
- [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
