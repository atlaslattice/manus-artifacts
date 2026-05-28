---
artifact_id: A11Y-POLICY-ALT-TEXT-001
title: Alt Text and Caption Policy
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, alt-text, images, a11y]
---

# Alt Text and Caption Policy

> Defines requirements for alternative text and captions on all images and media in Atlas Lattice documentation.

status: candidate

---

## Policy

Every image embedded in any Atlas Lattice document must have descriptive alt text. Images without alt text are an accessibility blocker and a CI lint failure.

---

## Alt Text Rules

### Decorative Images

Images that add no information (e.g., decorative banners) should use empty alt text:

```markdown
![](path/to/image.png)
```

or in HTML:
```html
<img src="path/to/image.png" alt="">
```

**Note:** Most images in a knowledge archive are informational, not decorative. When in doubt, write descriptive text.

---

### Informational Images

For all diagrams, screenshots, charts, and graphs:

```markdown
![A flowchart showing the three-stage ratification process: proposal, council review, and adjudication by @atlaslattice](path/to/ratification-flow.png)
```

**Alt text must:**
- Describe what the image shows, not what it is ("A bar chart showing increasing node counts" not "A graph")
- Be concise (ideally ≤ 125 characters); use a caption for longer descriptions
- Not start with "Image of..." or "Picture of..." (screen readers announce the image type)
- Not repeat the surrounding text verbatim

---

### Complex Diagrams (Maps, Architecture Diagrams)

For diagrams too complex to describe in alt text:
1. Use brief alt text summarizing the diagram's purpose
2. Add a `<details>` block with a full text description

```markdown
![Architecture diagram of the Lattice KG pipeline](pipeline.png)

<details>
<summary>Text description of pipeline diagram</summary>
The pipeline has three stages: (1) ingestion from markdown files via scripts/build_lattice_global_index.py, (2) KG graph construction stored in kg/global_index.json, and (3) quality gate validation via scripts/validate_lattice_quality_gates.py.
</details>
```

---

## Caption Policy

For images that benefit from a visible caption (e.g., figures with labels), use GitHub-flavored Markdown's italics convention below the image:

```markdown
![Alt text describing the image](path/to/image.png)
*Figure 1: Brief caption visible to all readers.*
```

---

## Audit Pass

The "alt text/caption pass" (#98 on the campaign board) is a one-time sweep of all existing documents to add missing alt text. All documents created after this policy is published must comply on creation.

---

*Atlas Lattice Foundation · status: candidate*
