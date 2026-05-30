---
artifact_id: A11Y-POLICY-LOW-BANDWIDTH-001
title: Low-Bandwidth Documentation Mode Policy
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, low-bandwidth, performance, a11y, global-reach]
---

# Low-Bandwidth Documentation Mode Policy

> Defines standards for making Atlas Lattice documentation accessible to contributors on low-bandwidth or metered connections.

status: candidate

---

## Why Low Bandwidth?

The world-class open-source community includes contributors in regions with slow, metered, or intermittent internet connections. Documentation that relies on large images, embedded videos, or heavy rendering is a barrier for these contributors.

---

## Low-Bandwidth Standards

### 1. Image Size Budget

| Image type | Maximum file size |
|-----------|-----------------|
| Inline diagram | 100 KB |
| Screenshot | 200 KB |
| Hero banner / decorative | 50 KB |
| Architecture diagram | 300 KB |

Images larger than these limits must be:
- Compressed (use tools like `optipng`, `jpegoptim`, or `squoosh`)
- Or replaced with a text description + lightweight SVG

---

### 2. No Auto-Loading Videos or GIFs

- Animated GIFs in documentation must be avoided (prefer a static screenshot + text "animated walkthrough" link)
- Videos are not embedded inline; instead, link to external video with a descriptive title and optional static screenshot

---

### 3. SVG Over Raster for Diagrams

Where possible:
- Use SVG instead of PNG/JPEG for diagrams (SVG is typically much smaller and scales perfectly)
- Architecture diagrams, flowcharts, and KG visualizations should be SVG when created from tooling

---

### 4. Repository Size Monitoring

Binary files (images, PDFs, datasets) must be tracked via Git LFS (Large File Storage) when they exceed 1 MB. Large files committed directly to git bloat all clones — a barrier for contributors on slow connections.

---

### 5. Offline-First Consideration

Where feasible, documentation should be meaningful without rendering live content:
- Don't link to live dashboards or APIs as primary content; always include a snapshot or description
- Ensure cross-links are relative paths (so a cloned repository is navigable offline)

---

## Monitoring

Repository total size and image sizes are tracked annually in the quality report. If the repository exceeds **50 MB** of binary assets, a cleanup pass is initiated.

---

*Atlas Lattice Foundation · status: candidate*
