# Editorial Style Guide

*Atlas Lattice Foundation · Aetherforge Mission #42 · 2026-05-28*

status: candidate

> The Atlas Lattice editorial standard for writing clear, consistent, and world-class documentation across the knowledge graph.

---

## Voice and Tone

| Attribute | Guidance |
|-----------|---------|
| **Voice** | Direct, confident, non-hostile. Speak as an authoritative peer, not a bureaucrat. |
| **Tone** | Warm, inclusive, aspirational. This is a gift to the world — the writing should feel like one. |
| **Person** | Second person ("you") for guides; third person ("contributors", "the council") for policies. |
| **Formality** | Professional but not stiff. Emoji are welcome in headings and callouts; not in body text. |

---

## Language Rules

### 1. Plain Language First

Write for a reader encountering this content for the first time. Define jargon on first use. Link to the [Glossary](../../docs/GLOSSARY.md) for technical terms.

### 2. Active Voice

✅ "The council ratifies artifacts."  
❌ "Artifacts are ratified by the council."

### 3. Inclusive Language

- Use gender-neutral pronouns ("they", not "he/she")
- Avoid ableist metaphors
- Use "allowlist/denylist" not "whitelist/blacklist"
- Refer to hostile actors as "adversaries" or "bad actors", not slurs

### 4. Positive Framing

✅ "Submit a PR to contribute."  
❌ "Don't forget to submit a PR."

### 5. Present Tense for Docs

Write documentation in the present tense: "This document defines…" not "This document will define…"

---

## Formatting Standards

### Headings

- H1 (`#`): Document title only — one per file
- H2 (`##`): Major sections
- H3 (`###`): Subsections
- H4 (`####`): Rare; only for dense technical content

### Lists

- Use unordered lists (`-`) for non-sequential items
- Use ordered lists (`1.`) for sequential steps or ranked items
- Max 2 levels of nesting; restructure if more needed

### Tables

- Use tables for structured comparisons, not flowing prose
- Always include a header row
- Keep table cells concise (< 80 chars)

### Code Blocks

- Always specify the language for syntax highlighting: ` ```python `, ` ```yaml `, ` ```bash `
- Use inline code (`` `code` ``) for file paths, commands, field names

### Links

- Use descriptive link text: ✅ [Governance Onboarding Guide](link) ❌ [click here](link)
- Relative links for internal documents
- Absolute URLs for external resources

---

## Document Structure

Every governance/spec/docs artifact should follow:

```
1. Title (H1)
2. Byline (Foundation · Mission # · Date)
3. status: candidate
4. One-sentence description (blockquote)
5. --- (divider)
6. Body sections (H2/H3)
7. --- (divider)
8. Related Documents
9. --- (divider)
10. Footer line
```

---

## Terminology Consistency

Always use the canonical form of key terms:

| Use This | Not This |
|----------|----------|
| Atlas Lattice Foundation | "the foundation", "ALF" (except in abbreviation tables) |
| knowledge graph | "KG", "knowledge-graph" (except in code/tags) |
| candidate | "draft", "WIP" (use lifecycle_state for those) |
| @atlaslattice | "David", "the founder" |
| TIDELOCK | "TideLock", "tidelock" |
| GPTDream++ | "gptdream++", "GPT Dream" |
| Aetherforge | "aetherforge", "AetherForge" |

---

## File Naming

Per the [Naming Conventions](../../docs/NAMING_CONVENTIONS.md):
- `SCREAMING_SNAKE_CASE.md` for governance, spec, and policy documents
- `kebab-case.md` for user-facing docs
- Date suffix: `_YYYY-MM-DD` for time-stamped artifacts

---

## Related Documents

- [Glossary](../../docs/GLOSSARY.md)
- [Naming Conventions](../../docs/NAMING_CONVENTIONS.md)
- [Breadcrumb Standards](./BREADCRUMB_STANDARDS.md)
- [Metadata Headers Standard](./METADATA_HEADERS_STANDARD.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
