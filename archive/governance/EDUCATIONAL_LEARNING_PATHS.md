---
artifact_id: COMM-POLICY-LEARNING-PATHS-001
title: Educational Learning Paths
status: candidate
created: 2026-05-28
owner: council
tags: [community, education, learning, onboarding, documentation]
---

# Educational Learning Paths

> Defines curated learning paths for different types of contributors and learners engaging with Atlas Lattice.

status: candidate

---

## Learning Path 1: The New Contributor

**Goal:** Go from zero to first merged PR.
**Time estimate:** 2–4 hours

1. Read `README.md` — understand the mission
2. Read `docs/NEWCOMER_FAQ.md` — answer your first questions
3. Read `docs/GLOSSARY.md` — learn the vocabulary
4. Run the bootstrap: `python -m venv venv && pip install -r requirements.txt && python -m pytest -q`
5. Browse `good first issue` labels
6. Open a PR, get it merged 🎉

---

## Learning Path 2: The Knowledge Graph Enthusiast

**Goal:** Understand and contribute to the Lattice KG.
**Time estimate:** 4–6 hours

1. Read `archive/governance/ONTOLOGY_RELATION_TYPES.md` — the 14 KG relations
2. Read `archive/governance/PERSISTENT_ARTIFACT_ID_STANDARD.md` — ID format
3. Read `archive/governance/MACHINE_READABLE_CITATION_BLOCKS.md` — how edges are built
4. Run `python scripts/build_lattice_global_index.py` — build the KG locally
5. Read `scripts/kg_query.py` — explore the query interface
6. Read `archive/governance/KG_PUBLIC_API_ROADMAP.md` — what's coming
7. Contribute: add `cite` blocks to an existing document

---

## Learning Path 3: The Governance & Policy Designer

**Goal:** Understand and contribute to policy documents.
**Time estimate:** 3–5 hours

1. Read `docs/GOVERNANCE_ONBOARDING_GUIDE.md` — governance overview
2. Read `archive/governance/EXECUTIVE_SUMMARIES_STANDARD.md` — document standards
3. Read `archive/governance/METADATA_HEADERS_STANDARD.md` — frontmatter format
4. Read `archive/governance/CHANGELOG_DISCIPLINE_POLICY.md` — how to update CHANGELOG
5. Contribute: improve an existing policy or propose a new one via RFC

---

## Learning Path 4: The GPTDream++ Protocol Researcher

**Goal:** Understand the GPTDream++ AI protocol stack.
**Time estimate:** 4–6 hours

1. Read `archive/boot/gptbrain/REM8_DREAM_PROTOCOL.md`
2. Read `archive/boot/gptbrain/WAKE_REPORT_TEMPLATE.md`
3. Read `archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md`
4. Browse the 10 appendix docs in `archive/spec/gptdream/appendices/`
5. Run the reference implementation: `cd archive/boot/gptbrain/reference_impl && python -m pytest -q`

---

## Learning Path 5: The Aetherforge Player

**Goal:** Play the Aetherforge archive game.
**Time estimate:** 1–2 hours (starter)

1. Read `README.md` — the mission statement
2. Read `projects/aetherforge-144-task-campaign-2026-05-27.md` — the game board
3. Find an unchecked task on the board
4. Complete the task and open a PR with the deliverable
5. The council scores the contribution — every wave is a new game level!

---

*Atlas Lattice Foundation · status: candidate*
