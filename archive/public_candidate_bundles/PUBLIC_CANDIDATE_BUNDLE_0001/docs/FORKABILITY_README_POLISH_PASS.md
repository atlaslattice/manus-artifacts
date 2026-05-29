# Forkability / README Polish Pass — PUBLIC_CANDIDATE_BUNDLE_0001

```text
STATUS: CANDIDATE STAGING MATERIAL
CANON: no
DEPLOYMENT: no
AUTHORITY: none
MODULE: 11 — Public GitHub / Forkability Excellence
```

## Purpose

This pass defines how the public GitHub surface should read to a new contributor in the first 30 seconds.

The goal is clarity, forkability, safety, and contribution readiness — without claiming canon, deployment, proof, or endorsement.

## 30-second hook

```text
Atlas Lattice is a provenance-first public knowledge graph project.
It maps sources, claims, evidence, review states, contradictions, deltas, and next actions.
It begins with a large archive of human-AI creative and technical work.
The graph shows review pressure. It does not decide truth.
```

## README top section candidate

```markdown
# Atlas Lattice Public Knowledge Graph

Atlas Lattice is a candidate public, open-source, provenance-first knowledge graph and archive substrate.

It is designed to make a large body of human-AI creative and technical work inspectable through sources, receipts, claims, review states, contradictions, and next actions.

**Important:** this repository is not canon, not deployment proof, and not authority. Public GitHub makes artifacts inspectable; it does not make them true.

## Start here

- Read `docs/GRAPH_IS_NOT_CANON_FAQ.md`
- Read `docs/SENSITIVE_TERM_RELEASE_GATE.md`
- Read `docs/ARCHIVIST_TRUST_FAILURE_PROTOCOL.md`
- Review `examples/toy_graph_demo/README.md`
- Use `PR_CHECKLIST.md` before proposing changes
```

## Forkability checklist

- [ ] Clear project purpose in first paragraph.
- [ ] Boundary statement above the fold.
- [ ] Start-here links.
- [ ] Toy example with fake data.
- [ ] Contribution path.
- [ ] Public-release gate before raw cargo.
- [ ] License status visible.
- [ ] Issue templates for inspection routes.
- [ ] Schema files readable without special tooling.
- [ ] No private data in examples.
- [ ] No unsupported endorsement or deployment claims.
- [ ] No canon claims without human-root decision.

## Contributor path

```text
1. Pick one module.
2. Return one bounded module packet.
3. Mark receipts and blockers.
4. Do not claim canon.
5. Do not publish raw cargo without release review.
6. Preserve gaps as graph objects.
```

## Safe language guide

```yaml
use:
  - candidate
  - source-root
  - receipt
  - review route
  - public-safe summary
  - missing receipt
  - not canon
  - not deployed
  - advisory only

avoid_without_receipts:
  - official
  - ratified
  - deployed
  - production-ready
  - single source of truth
  - proven
  - endorsed
  - complete
```

## Keeper

```text
Make it readable.
Make it forkable.
Make it safe.
Make it honest.
No crowns.
```
