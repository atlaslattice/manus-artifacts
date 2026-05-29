# Documentation Style Guide

> **Status:** Candidate
> **Last reviewed:** 2026-05-28
> **Provenance:** Repository-level standard for writing and updating markdown documentation.

## Purpose

Keep documentation clear, consistent, and easy to navigate across the entire repository.

## Required top block (for key docs)

Use this metadata block on major docs pages:

> **Status:** Candidate/Ratified  
> **Last reviewed:** YYYY-MM-DD  
> **Provenance:** short maintenance/source note  
> **Start here:** relative link to entry page (when applicable)

## Structure rules

1. Use exactly one H1 title per file.
2. Keep heading levels sequential (H2 under H1, H3 under H2).
3. Keep sections short and scannable.
4. End major docs with a **Read next** section.

## Link rules

1. Prefer relative links for in-repo references.
2. Add a descriptive label; avoid raw URL-only labels.
3. Keep at least one back-link to a hub page (`README.md`, docs index, or project index).

## Language rules

1. Prefer concrete, direct language.
2. Define specialized terms in [GLOSSARY.md](./GLOSSARY.md).
3. Avoid ambiguous terms when a precise governance term exists (see
   [ANTI_CONFUSION_TERMINOLOGY_NOTES.md](./ANTI_CONFUSION_TERMINOLOGY_NOTES.md)).

## Code blocks

1. Always include code-fence language tags when using fenced blocks.
2. Keep command examples copy/paste ready.

## Read next

- [Docs Index](./README.md)
- [Documentation FAQ](./FAQ.md)
- [Anti-Confusion Terminology Notes](./ANTI_CONFUSION_TERMINOLOGY_NOTES.md)
