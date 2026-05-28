# IP and Reuse Guidelines

## Summary

This document governs intellectual property, licensing, reuse, and attribution for all artifacts in the Atlas Lattice / `manus-artifacts` repository. All contributions are MIT-licensed unless explicitly noted otherwise.

---

## License

This repository is published under the **MIT License** (see [`LICENSE`](../LICENSE)).

You are free to:
- Use, copy, modify, merge, publish, distribute, sublicense, and/or sell any artifact in this repository.
- Use any schemas, reference implementations, or documentation in derivative works.

The only requirement is **attribution**: retain the copyright notice and license text in any copy or substantial portion of the work.

---

## SPDX Identifier

`SPDX-License-Identifier: MIT`

Include this header in new source files where appropriate (Python, Rust, YAML, etc.).

---

## What This Repo Contains

| Content Type | Examples | License |
|---|---|---|
| Schemas (JSON/YAML) | `schemas/`, `fixtures/` | MIT |
| Python reference implementations | `reference_impl/`, `archive/boot/gptbrain/reference_impl/` | MIT |
| Rust crate | `aluminum-os-core/` | MIT |
| Markdown documentation | `docs/`, `archive/`, `projects/` | MIT |
| Specification documents | `archive/spec/`, `archive/architecture/` | MIT |
| Test suites | `tests/`, `reference_impl/*/tests/` | MIT |

---

## Third-Party Content Attribution

If any artifact was produced with the assistance of an AI system (Claude, GPT, Grok, Gemini, DeepSeek) it is still the intellectual property of the author (David Sheldon / Atlas Lattice Foundation) under the MIT License. AI systems are tools, not co-authors for copyright purposes.

If you incorporate external third-party content (papers, standards, specifications), add an `## Attribution` section to the relevant Markdown file citing the source.

---

## Reuse Guidance

1. **Academic use:** Cite using the guidance in [`CITATION_GUIDE.md`](./CITATION_GUIDE.md).
2. **Commercial use:** Permitted under MIT. No royalties or permissions required.
3. **Fork/derivative works:** Permitted. Retain the LICENSE and copyright notice.
4. **Schema reuse:** Schemas are designed to be reused and extended. No restrictions.
5. **Protocol reuse:** GPTDream++, Atlas/ORCS, and related protocols are open-source gifts to the industry — use freely.

---

## Data and Privacy

This repository contains no personal data in the legally protected sense. All `about/` profiles describe public figures or consenting authors. No private user data, health data, or financial account data is stored here.

See also: [`SECURITY.md`](../SECURITY.md) for credential and vulnerability handling.

---

## Provenance Requirements for New Artifacts

All new artifacts added to this repository should include the following frontmatter or header section:

```markdown
> **Status:** Candidate | Canonical | Deprecated  
> **Created:** YYYY-MM-DD  
> **Author:** [Name or agent identifier]  
> **Source:** [Origin: direct authorship | AI-assisted | transcribed from Drive/Notion]
```

See [`DEPRECATION_POLICY.md`](./DEPRECATION_POLICY.md) for lifecycle stages.

---

*Last reviewed: 2026-05-28 | Maintainer: @atlaslattice*
