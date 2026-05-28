# Export Control Screening Checklist

*Atlas Lattice Foundation · Aetherforge Mission #18 · 2026-05-28*

status: candidate

> Checklist for screening Atlas Lattice contributions against applicable export control regulations (EAR, ITAR, and equivalent), ensuring the open-source repository remains compliant with US and international law.

---

## Context

Atlas Lattice is a publicly available open-source repository. Most open-source software and research documentation is exempt from export control under the **EAR § 734.3(b)(3)** "publicly available" exception. However, certain categories of technical data retain export control requirements even when published publicly.

---

## Pre-Submission Screening Checklist

Complete this checklist before committing content that may contain technical data:

### Category 1 — Cryptography

- [ ] Does the content include encryption source code, algorithms, or key material?
  - If YES: Confirm this is published open-source cryptography already in the public domain (e.g., AES, RSA, SHA). Standard published algorithms are generally EAR-exempt.
  - If the cryptography is novel or unpublished: **STOP — seek legal review before committing.**

### Category 2 — Defense / Dual-Use Technology

- [ ] Does the content describe weapons systems, military equipment, or surveillance technology?
  - If YES: **STOP — this is outside scope for Atlas Lattice. Do not include.**

### Category 3 — Nuclear, Biological, Chemical

- [ ] Does the content include technical data for nuclear, biological, or chemical applications?
  - If YES: **STOP — this is prohibited content. Do not include.**

### Category 4 — Controlled Technical Data

- [ ] Was this content received under an NDA, government contract, or other agreement restricting publication?
  - If YES: **STOP — do not commit without clearance from the originating organization.**

### Category 5 — AI Systems with Export Implications

- [ ] Does the content describe AI systems designed for autonomous weapons, mass surveillance, or social scoring?
  - If YES: **STOP — seek legal and governance review.**

---

## Standard Cases (Generally Permitted)

The following are generally **not** subject to export controls in this repository context:

- Open-source software under MIT/Apache/GPL
- Published research papers and academic references
- Standard software documentation and governance documents
- AI protocols designed for transparency, archival, and public benefit (GPTDream++)
- Knowledge graph schemas and ontologies

---

## What to Do If Uncertain

1. Do not commit the content yet.
2. Open a GitHub Discussion with the `export-control-question` tag.
3. Consult @atlaslattice or the designated legal advisor.
4. Await clearance before proceeding.

---

## Annual Review

This checklist is reviewed annually to reflect changes in EAR/ITAR regulations and emerging technology classifications.

---

## Related Documents

- [Sensitive Content Review Process](./SENSITIVE_CONTENT_REVIEW_PROCESS.md)
- [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md)
- [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
