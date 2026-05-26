# Governance

## Authority and Ratification

All artifacts in this repository are **candidates** until ratified.

Final canon adjudication rests with **@atlaslattice** (David Sheldon), supported by
the full Aetherforge Council. No artifact — including this document — achieves
canonical status without full council ratification and explicit adjudication.

## Decision-Making Process

| Decision type | Who decides | How |
|---|---|---|
| Day-to-day PRs | Any council member with CODEOWNERS coverage | GitHub PR review |
| Canon promotion | @atlaslattice + full council | Council session + signed adjudication |
| Security policy changes | @atlaslattice | Direct commit to `main` |
| Governance changes | @atlaslattice + council vote | PR with council sign-off |

## Merge Rights

Merge rights to `main` are held by @atlaslattice. Branch-level merges may be
delegated per CODEOWNERS. See `.github/CODEOWNERS` for the current ownership map.

## Contribution Path

1. Open an issue or discussion to propose intent.
2. Follow `.github/CONTRIBUTING.md` for pre-flight validation requirements.
3. Submit a PR referencing the originating issue.
4. A CODEOWNER review is required before merge.
5. Canon artifacts require additional council ratification after merge.

## Canon Trust Hierarchy

```
RATIFIED (canonical) ← adjudicated by @atlaslattice + full council
CANDIDATE             ← committed and under review
DRAFT                 ← open PR or discussion, not yet committed
DEPRECATED            ← superseded, retained for historical record
```

## Council Structure

The Aetherforge Council governs this repository. Agent members include the
Children of the Swarm squad (see `archive/boot/gptbrain/agents/`). Human
authority rests solely with @atlaslattice.

## Canonical Substrate

GitHub is the durable canonical substrate. Drive, Notion, and other relay
layers are working-vault tools only. No artifact is canonical until it exists
as a committed, ratified entry in this repository.

## Contact

Open a GitHub Discussion for general governance questions.
For security matters, follow `.github/SECURITY.md`.
