---
artifact_id: A11Y-POLICY-PLAIN-LANGUAGE-001
title: Plain Language Policy
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, plain-language, readability, a11y]
---

# Plain Language Policy

> Defines plain-language standards for Atlas Lattice documentation to maximize comprehension for all readers.

status: candidate

---

## What Is Plain Language?

Plain language means writing that readers can understand the first time they read it. It does not mean "dumbed down" — it means efficient and clear. Technical concepts can be expressed plainly; jargon and needlessly complex structure cannot.

---

## Plain Language Principles

### 1. Write for the Reader

Before writing a document, identify:
- **Who is the reader?** (contributor, researcher, consumer, newcomer)
- **What do they need to do after reading?** (understand a concept, follow a procedure, make a decision)

Structure the document to answer those questions directly.

---

### 2. Use Active Voice

| Passive (avoid) | Active (prefer) |
|----------------|----------------|
| "The policy is enforced by CI" | "CI enforces the policy" |
| "Documents must be tagged by contributors" | "Contributors must tag documents" |
| "Errors are reported when validation fails" | "Validation reports errors when it fails" |

Exception: passive voice is acceptable when the actor is genuinely unknown or irrelevant.

---

### 3. Prefer Short Sentences

- Target: average sentence length ≤ 20 words
- Each sentence should express one idea
- Break compound sentences at conjunctions when clarity improves

---

### 4. Use Familiar Words

| Complex (avoid) | Plain (prefer) |
|----------------|---------------|
| Utilize | Use |
| Facilitate | Help, enable |
| Commence | Start, begin |
| Subsequently | Then, next |
| Endeavor | Try |
| Aforementioned | The above, this |

---

### 5. Define Technical Terms

On first use, define every term that a newcomer might not know. Link to the [GLOSSARY.md](../../docs/GLOSSARY.md) after the first definition:

> "The **Knowledge Graph (KG)** is a structured network of all documents and their relationships. See [GLOSSARY.md](../../docs/GLOSSARY.md) for full definitions."

---

### 6. Use Parallel Structure

Lists must use parallel grammatical form:

```
# Good (all gerunds)
- Installing dependencies
- Running tests
- Deploying to production

# Bad (mixed forms)
- Installing dependencies
- Run tests
- The deployment to production
```

---

## Plain Language Audit

The plain language audit is part of the annual accessibility audit. It samples 10% of documents and applies the Flesch-Kincaid readability score:

- **Target for conceptual docs:** Grade 8 or below
- **Target for technical reference docs:** Grade 12 or below (technical precision may raise grade level)

---

*Atlas Lattice Foundation · status: candidate*
