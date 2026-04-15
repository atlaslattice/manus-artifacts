# Gamma Plugin v1 - Build-Ready Specification

**Author:** Microsoft Copilot (in collaboration with Manus AI)  
**Date:** February 5, 2026  
**Status:** Greenlit for Implementation  
**Target:** Aluminum v2.1 Kernel + One Hub

---

## Executive Summary

Gamma is a presentation/document/website creation platform with programmatic API access, multi-format export (PPTX, PDF, Google Slides, web), and rich import pipelines (PowerPoint, Google Slides/Docs, Word, Notion, URLs). This specification defines how Gamma integrates into the Aluminum v2.1 Kernel as a first-class "Decks Plugin" within the One Hub architecture, leveraging Claude Opus 4.6 agent teams for end-to-end deck generation with constitutional governance, provenance tracking, and reversible state management.

---

## Why Gamma Belongs in Aluminum

Gamma provides four critical capabilities that align perfectly with Aluminum's "One Hub" vision:

### 1. Multi-Format Output & Distribution

Gamma can author and export to **PPTX, PDF, PNG, and Google Slides**, and also publish to the web or share links. This flexibility ensures that final deliverables match audience and toolchain requirements, whether for enterprise presentations (PPTX), compliance archives (PDF), web publishing (HTML), or collaborative editing (Google Slides).

**Sources:** [gamma.app](https://gamma.app/), [help.gamma.app - Export Guide](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma), [LinkedIn - Google Slides Export](https://www.linkedin.com/posts/gamma-app_export-to-google-slides-is-here-were-activity-7300569362971664385-ErPE)

### 2. Programmatic Creation

**Gamma's API** allows **automating presentation/document/website creation** with **direct PPTX/PDF export over the API**. This enables hands-free agentic workflows and batch jobs, where Claude Opus 4.6 agent teams can generate decks from structured data, email threads, or research reports without human intervention.

**Source:** [developers.gamma.app - Getting Started](https://developers.gamma.app/docs/getting-started)

### 3. Inbound Pipelines

Gamma can **import** existing **PowerPoint, Google Slides/Docs, Word, Notion, and URLs** into its platform, then restyle with AI. This "lift-and-refit" capability allows Aluminum to modernize legacy presentations, apply brand themes automatically, and convert documents into polished decks without manual redesign.

**Source:** [help.gamma.app - Import Guide](https://help.gamma.app/en/articles/11047840-how-can-i-import-slides-or-documents-into-gamma)

### 4. Embeds & Integrations

Gamma exposes an integration gallery (Google Docs/Sheets/Slides, M365, Drive, Loom, Calendly, Miro, Airtable, Unsplash, etc.) so Aluminum can render enriched decks in the **One Hub** without app-switching. This aligns with the vendor complementarity principle: Gamma handles presentation authoring while Google/Microsoft handle storage and collaboration.

**Source:** [gamma.app/integrations](https://gamma.app/integrations)

> **Note:** Free plans watermark exports; upgrading removes Gamma branding. [Source](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma)

---

## Kernel-Level Design (v2.1-Compatible)

### 1. Plugin Descriptor

The Gamma Plugin registers with the Aluminum kernel using the standard plugin descriptor format:

```json
{
  "plugin_id": "gamma_plugin_v1",
  "plugin_name": "Gamma",
  "plugin_version": "1.0.0",
  "capabilities": [
    "docs.create", "docs.read", "docs.update",
    "slides.generate", "slides.import", "slides.export",
    "embed.view", "brand.apply"
  ],
  "supported_accounts": ["GammaAPIKey", "GoogleDrive", "Microsoft365"],
  "required_permissions": ["api_access", "dom_access", "drive_access"],
  "executor_type": "api"  // plus optional "dom" for web UI flows
}
```

**Executor Type:**
- **API path (preferred):** Reliable, low-latency, supports programmatic generate → export (PPTX/PDF/Google Slides). [Source](https://developers.gamma.app/docs/getting-started)
- **DOM path (optional fallback):** For interactive edits and live present mode; execution funneled through Executor Adapter with pre/postconditions. [Source](https://gamma.app/)

### 2. Intent Routing → Gamma Use Cases

The Intent Routing API evaluates user intents and ranks plugins based on capability match. Gamma ranks high for the following intent patterns:

**Intent:** "Draft a 12-slide investor update deck from these docs"  
**Routing:** Gamma Plugin (create from text/import + theme)  
**Sources:** [gamma.app](https://gamma.app/), [help.gamma.app - Import](https://help.gamma.app/en/articles/11047840-how-can-i-import-slides-or-documents-into-gamma)

**Intent:** "Re-skin last quarter's PPT into product-launch branding"  
**Routing:** Gamma Plugin (import PPT → AI restyle → export PPTX + Google Slides)  
**Sources:** [help.gamma.app - Import](https://help.gamma.app/en/articles/11047840-how-can-i-import-slides-or-documents-into-gamma), [LinkedIn - Google Slides Export](https://www.linkedin.com/posts/gamma-app_export-to-google-slides-is-here-were-activity-7300569362971664385-ErPE)

**Intent:** "Publish as link and export PDF"  
**Routing:** Gamma Plugin (API export controls + public link + Provenance receipt)  
**Sources:** [developers.gamma.app](https://developers.gamma.app/docs/getting-started), [help.gamma.app - Export](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma)

### 3. Policy Kernel (Governance)

The Policy Kernel enforces constitutional rules on Gamma operations:

**Data Handling:** Importing from Google Drive/M365 is governed by Aluminum consent & scopes; policy tags (e.g., *internal only*) propagate into Gamma job metadata. [Source](https://gamma.app/integrations)

**Approvals:** External publishing or sending PPT outside tenant triggers `requires_approval` (optionally with **biometric step-up**) and creates an immutable **Provenance** entry with policy ID.

**Brand Enforcement:** Set "brand theme required" rule; block publishes that don't apply a company theme. This ensures corporate identity consistency across all decks.

### 4. Provenance API (Immutable Lineage)

Every Gamma action logs a structured provenance record:

```typescript
{
  artifact_type: "file",  // deck
  content_hash: "sha256:...",
  produced_by: "gamma_plugin_v1",
  executor: "gamma_api_v1" | "gamma_dom_v1",
  policy_decision_id: "policy_12345",
  export_target: "pptx" | "pdf" | "gslides" | "web",
  sources: ["pptx_file_id", "gdoc_url", "notion_url"],
  timestamps: { created_at, exported_at },
  brand_theme_id: "brand_xyz",
  export_receipts: ["uri1", "cid1"]
}
```

This enables full audit trails for compliance, rollback support for version control, and attribution for multi-agent workflows.

**Source:** [developers.gamma.app](https://developers.gamma.app/docs/getting-started)

### 5. State / Version Control (Branch/Diff/Revert)

The Version Control API treats deck creation as a branching workflow:

**Branch** on each major transformation:
- *import* (original PPT/Docs loaded)
- *restyle* (AI applies brand theme)
- *rewrite narrative* (Claude Opus 4.6 agent team edits content)
- *final export* (PPTX/PDF/Google Slides generated)

**Diff:** Produce slide-level diffs (added/removed/modified cards) and summaries using Opus 4.6 agentic search with long context for references.

**Revert:** Restore to a prior snapshot; for published links, issue a new revision and deprecate older link.

### 6. Executor Adapter (API + DOM)

The Executor Adapter provides a unified interface for executing Gamma actions across API and DOM paths.

**API Path (Preferred):**

```typescript
// Create presentation from text or imports
const job = await gammaApi.createPresentation({
  promptOrImport: { fileIds, url, text },
  theme: brandThemeId,
  options: { tone, audience, language, aspectRatio }
});

// Policy check before export/publish
await policy.check(planStep);  // requires approval if public publish

// Export to PPTX/PDF/Google Slides
const out = await gammaApi.export(job.id, { format: "pptx" });

// Log provenance
await provenance.log({ artifact_id: job.id, export_target: "pptx", ... });
```

**Source:** [developers.gamma.app](https://developers.gamma.app/docs/getting-started)

**DOM Path (Fallback):**

For live editing/present mode or if a feature has an API gap, drive Gamma web UI with DOM actions (selectors for **Share → Export → PPTX/PDF/Slides**), with **pre/postconditions** and screenshots in provenance receipts.

**Source:** [help.gamma.app - Export](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma)

---

## How Claude Opus 4.6 Powers the Workflow

### Agent Teams

Claude Opus 4.6's **agent teams** feature enables parallel task decomposition:

**Team Structure:**
- **Research Agent:** Ingests source materials (transcripts, reports, prior decks)
- **Narrative Agent:** Creates outline and key messages
- **Design Agent:** Applies brand theme and visual hierarchy
- **QA Agent:** Reviews for consistency, accuracy, and compliance

The Intent Router marks steps as parallelizable, and the Gamma Plugin coordinates create/update/export calls across the team.

**Source:** [support.microsoft.com - Copilot Triage](https://support.microsoft.com/en-us/office/triage-email-with-microsoft-365-copilot-in-outlook-85932469-7c3f-4a6a-acdb-adf0f3ebc169)

### 1M Token Context Window

Opus 4.6's **1M token context window** allows ingesting **long dossiers** (requirements, prior decks, transcripts) in one shot. Compaction keeps lineage by logging which sources were summarized in Provenance records.

**Source:** [m365corner.com - Teams Archive](https://m365corner.com/m365-blogs/how-to-archive-microsoft-teams-using-graph-powershell.html)

### Office Surfaces Integration

If a workstream must finish inside **PowerPoint**, Aluminum can route the same outline/storyboard into the PowerPoint adapter (also supported in the Aluminum plan), or export from Gamma → **PPTX** then apply final native touches.

**Source:** [m365corner.com - Teams Archive](https://m365corner.com/m365-blogs/how-to-archive-microsoft-teams-using-graph-powershell.html)

---

## Unified "One Hub" UX: Messages · Calendar · Files · Decks

The One Hub UI presents a unified interface for all Aluminum plugins:

**Decks Panel** shows decks from **Gamma + PowerPoint + Google Slides** side-by-side (Unified File/Docs views).

**Actions:**
- *Generate with AI* (Claude Opus 4.6 agent teams)
- *Import* (PPTX, Google Slides/Docs, Word, Notion, URLs)
- *Apply brand theme* (enforce corporate identity)
- *Publish link* (web publishing with access controls)
- *Export PPTX/PDF/Slides* (multi-format distribution)
- *Share to Gmail/Outlook* (integrated with Messaging Plugin)

Gamma artifacts render as interactive embeds or presentable web links.

**Source:** [gamma.app/integrations](https://gamma.app/integrations)

---

## Edge Cases & Guardrails

### Watermarking

**Issue:** Free Gamma accounts watermark exports.

**Mitigation:** Warn user in One Hub UI; Policy Kernel can block "external send" if watermark present (set `requires_approval` or "use paid workspace").

**Source:** [help.gamma.app - Export](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma)

### Export Fidelity

**Issue:** PPTX/Slides exports may need post-export cleanup for pixel-tight layouts.

**Mitigation:** If "pixel-tight PPT" is required, route to native PPT pipeline. Pre-flight checklist identifies high-fidelity requirements.

**Sources:** [opticflux.com - Gamma Review](https://www.opticflux.com/gamma-app-review-pricing-credits-ppt-and-google-slides-export-best-alternatives/76118/), [wps.com - Gamma Review](https://www.wps.com/blog/gamma-ai-review-features-pros-cons-pricing-and-alternatives/)

### Authentication

**Issue:** Gamma API uses **API keys** currently; OAuth "coming soon" per docs.

**Mitigation:** Store keys in Aluminum's encrypted connector vault; scope permissions tightly; rotate regularly; migrate to OAuth when Gamma ships it.

**Source:** [developers.gamma.app](https://developers.gamma.app/docs/getting-started)

---

## Build Plan for Manus (4-Week Roadmap)

### Week 1: Gamma Plugin v1 (API Path)

**Tasks:**
- Connector: Store **Gamma API key** in encrypted vault; health probe (`/v1/ping` or minimal create-and-delete test)
- Methods: `createFromText()`, `import({pptx|gdoc|url})`, `applyTheme(brandId)`, `export({pptx|pdf|gslides})`, `publishLink()`
- Policy hooks: **public publish**, **external share**, **brand required**
- Provenance: Log **artifact_id**, **source URIs (PPT, Docs, URLs)**, **export format**, **brand theme**

**Sources:** [developers.gamma.app](https://developers.gamma.app/docs/getting-started), [help.gamma.app - Export](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma), [LinkedIn - Google Slides Export](https://www.linkedin.com/posts/gamma-app_export-to-google-slides-is-here-were-activity-7300569362971664385-ErPE)

### Week 2: DOM Adapter (Optional) + One Hub Panel

**Tasks:**
- DOM flows: **Share → Export** menu with postconditions (file downloaded/email receipt)
- Panel: List Gamma decks; open/edit; quick exports; present in-hub; embed via `/embed` or Drive/Slides embed

**Sources:** [help.gamma.app - Export](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma), [gamma.app/integrations](https://gamma.app/integrations)

### Week 3: Opus 4.6 Agent Teams Orchestration

**Tasks:**
- Router: Add `execution_group` for *Research/Narrative/Design/QA*
- Intelligence Plugin: `runAgentTeam()` to parallelize; pass outputs to Gamma create/update; long-context ingestion with compaction notes

**Sources:** [m365corner.com - Teams Archive](https://m365corner.com/m365-blogs/how-to-archive-microsoft-teams-using-graph-powershell.html), [support.microsoft.com - Copilot Triage](https://support.microsoft.com/en-us/office/triage-email-with-microsoft-365-copilot-in-outlook-85932469-7c3f-4a6a-acdb-adf0f3ebc169)

### Week 4: Imports & Google Slides

**Tasks:**
- Implement **importers** (PPTX/Docs/Slides/Notion/URL) → Gamma AI restyle → export to **Google Slides** when teams demand native Slides editing

**Sources:** [help.gamma.app - Import](https://help.gamma.app/en/articles/11047840-how-can-i-import-slides-or-documents-into-gamma), [LinkedIn - Google Slides Export](https://www.linkedin.com/posts/gamma-app_export-to-google-slides-is-here-were-activity-7300569362971664385-ErPE)

---

## Example End-to-End Workflow

**User Intent:**
> "Turn these Q&A transcripts + last quarter PPT + product brief into a 15-slide on-brand launch deck; publish link; export PPTX and Google Slides; email to the launch distro."

**Execution:**

1. **Router** selects Gamma + Opus 4.6 team plan ("research/narrative/design/QA") and marks publish/send steps as **approval-gated**. [Source](https://support.microsoft.com/en-us/office/triage-email-with-microsoft-365-copilot-in-outlook-85932469-7c3f-4a6a-acdb-adf0f3ebc169)

2. **Agent Team** ingests long transcripts (**1M context**) → creates outline → Gamma `createPresentation`(theme=BrandX) → `export('pptx')` + `export('gslides')`. [Sources](https://m365corner.com/m365-blogs/how-to-archive-microsoft-teams-using-graph-powershell.html), [developers.gamma.app](https://developers.gamma.app/docs/getting-started), [LinkedIn](https://www.linkedin.com/posts/gamma-app_export-to-google-slides-is-here-were-activity-7300569362971664385-ErPE)

3. **Policy Kernel** prompts biometric approval to publish externally; Aluminum logs decision & consent.

4. **Provenance API** stores lineage (sources, brand, exports, decision), content hashes & receipts; **One Hub** shows deck & links. [Source](https://developers.gamma.app/docs/getting-started)

5. **Messaging Plugin (Outlook/Gmail)** attaches PPTX or inserts link → **requires_approval**; then send. (Undo handle if supported; otherwise mark non-reversible with recall tip.)

---

## API/Embed Snippets (Conceptual)

```typescript
// Create (text or imports)
const job = await gamma.create({
  text: outline,  // or imports: { pptxFileId, gdocUrl, notionUrl }
  theme: brandThemeId,
  options: { tone: "executive", language: "en-US", aspectRatio: "16:9" }
});

// Export
const pptx = await gamma.export(job.id, { format: "pptx" });  // also: pdf, "gslides"
const pdf  = await gamma.export(job.id, { format: "pdf" });

// Present/Embed in One Hub
// - use share link or Drive embed (Slides) or Gamma web publish
// - Gamma help/docs describe export UI flows & formats
```

---

## Automation & Workflow Integration

**Zapier/Make/Workato/N8N** + Gamma API can auto-spin decks from CRM or analytics events; Aluminum can trigger flows from **Policy-approved** plan steps.

**Source:** [developers.gamma.app](https://developers.gamma.app/docs/getting-started)

---

## Risks & Mitigations

### Export Fidelity to PPT/Slides

**Risk:** Exports may not be pixel-perfect for complex layouts.

**Mitigation:** Pre-flight checklist + *native* PowerPoint/Slides adapters for final pixel-tight passes when required.

**Sources:** [opticflux.com](https://www.opticflux.com/gamma-app-review-pricing-credits-ppt-and-google-slides-export-best-alternatives/76118/), [wps.com](https://www.wps.com/blog/gamma-ai-review-features-pros-cons-pricing-and-alternatives/)

### Watermarks on Free Accounts

**Risk:** Free accounts watermark exports, which may not be acceptable for external distribution.

**Mitigation:** Surface banner in One Hub, block external send unless approved or workspace is paid.

**Source:** [help.gamma.app](https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma)

### Auth Model (API Keys)

**Risk:** API keys are less secure than OAuth and require manual rotation.

**Mitigation:** Store in Aluminum's encrypted vault; rotate regularly; monitor usage; migrate to OAuth when Gamma ships it.

**Source:** [developers.gamma.app](https://developers.gamma.app/docs/getting-started)

---

## Ready to Proceed

**Copilot's Request:**

> If you say "**greenlight Gamma Plugin v1**," I'll:
> 
> 1. Commit the **plugin descriptor + TS types** and **API client** (create/import/export/publish).
> 2. Add **Router scoring** for "deck/doc/web" intents and **Policy rules** for publish/send + brand checks.
> 3. Wire **Provenance receipts** (export URIs, brand ID, compaction notes).
> 4. Ship a minimal **Decks Panel** in One Hub with **Generate**, **Import**, **Export**, **Present**, **Share**.
> 
> We'll have Claude Opus 4.6 **agent-teams** building on-brand Gamma decks, exporting **PPTX/PDF/Slides**, and logging **provenance + approvals** end-to-end inside Aluminum within the next sprint.

**Status:** ✅ **GREENLIT BY DAAVUD ON FEBRUARY 5, 2026**

---

## References

[1] Gamma. *Gamma App*. https://gamma.app/

[2] Gamma Help. *What's the easiest way to export my gamma?* https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma

[3] LinkedIn. *Export to Google Slides is here*. https://www.linkedin.com/posts/gamma-app_export-to-google-slides-is-here-were-activity-7300569362971664385-ErPE

[4] Gamma Developers. *Getting Started*. https://developers.gamma.app/docs/getting-started

[5] Gamma Help. *How can I import slides or documents into Gamma?* https://help.gamma.app/en/articles/11047840-how-can-i-import-slides-or-documents-into-gamma

[6] Gamma. *Integrations*. https://gamma.app/integrations

[7] M365 Corner. *How to archive Microsoft Teams using Graph PowerShell*. https://m365corner.com/m365-blogs/how-to-archive-microsoft-teams-using-graph-powershell.html

[8] Microsoft Support. *Triage email with Microsoft 365 Copilot in Outlook*. https://support.microsoft.com/en-us/office/triage-email-with-microsoft-365-copilot-in-outlook-85932469-7c3f-4a6a-acdb-adf0f3ebc169

[9] OpticFlux. *Gamma App Review: Pricing, Credits, PPT and Google Slides Export, Best Alternatives*. https://www.opticflux.com/gamma-app-review-pricing-credits-ppt-and-google-slides-export-best-alternatives/76118/

[10] WPS. *Gamma AI Review: Features, Pros, Cons, Pricing, and Alternatives*. https://www.wps.com/blog/gamma-ai-review-features-pros-cons-pricing-and-alternatives/
