# Planetarium Revival — Offline Simulation and Discovery Kit v0.1

**CANDIDATE / NOT CANON / NOT DEPLOYED / AUTHORITY NONE / ZERO REAL CUSTOMER OR PARTNER CLAIMS**

This source-only package completes the reproducible fixtures and review materials from [issue #202](https://github.com/atlaslattice/manus-artifacts/issues/202). It preserves the original 2026-05-27 matrix and simulator unchanged.

## What is here

- `PLANETARIUM_144_TASK_MATRIX_v0.1_2026-05-27.md`: original 12-house / 144-task candidate source
- `../../../tools/simulate_planetarium_144_matrix.py`: original Python-stdlib simulator (repository-root path: `tools/simulate_planetarium_144_matrix.py`)
- `fixtures/PLANETARIUM_144_TASKS_v0.1.json`: 144 typed candidates with review flags and conditional priority score
- `fixtures/PLANETARIUM_144_TASKS_v0.1.csv`: the same 144 candidate tasks for local inspection, with no real customer data
- `tests/test_planetarium_fixture.py`: eleven checks comparing JSON/CSV to the existing Python simulator
- `CUSTOMER_DISCOVERY_INTERVIEW_KIT_v0.1.md`: four role-specific, opt-in research scripts with consent/privacy constraints
- `OVERCLAIM_REVIEW_RULES_v0.1.json`: ten human-review lexical rule families; **not** an automated proof or censorship gate
- `PROSPECTIVE_PARTNER_WORDING_PATCH_v0.1.md`: copy-ready correction for unconfirmed affiliation, commercialization and cultural permission claims
- `.github/ISSUE_TEMPLATE/planetarium-revival-task.yml`: a GitHub issue form selecting among twelve initial source-listed tasks; filing the form never executes a task

## Reproduction

From the repository root:

```bash
python tools/simulate_planetarium_144_matrix.py --summary
python tools/simulate_planetarium_144_matrix.py --json
python tools/simulate_planetarium_144_matrix.py --csv
python -m unittest discover -s archive/simulations/planetarium-revival/tests -p 'test_planetarium_fixture.py' -v
```

Source-equivalence requirements: 12 unique house names, 12 tasks each, 144 unique IDs H01-T01…H12-T12, 28 review-flagged tasks under the current `REVIEW_TERMS` dictionary, and 144 rows in both JSON and CSV. Priority scores are **simulated routing heuristics**, not evidence of actual feasibility, customer demand or rights.

The fixture-generation source was re-parsed from the actual committed Markdown: **144/144** rows and normalized outputs matched the simulator’s `normalize_output` rule, across twelve 12-item houses. A JavaScript implementation of the published `review_flags`, `readiness_score`, JSON/CSV emission was checked for shape and key-count consistency. The Python test module is added for independent clean-checkout replay; no hosted CI or deployment is implied.

## Safety / agency / privacy

No model posts, outreach to real venues, student or customer record collection, purchasing, vendor payments, media licensing, Indigenous knowledge extraction, cultural claims, sponsor claims, or provider integrations were performed. All candidate tasks remain unassigned until a participant voluntarily selects a scope. The project should not imply that a source fixture, a checklist, a marketing template or a visually compelling show is an accepted contract, official partner, licensed product or scientifically validated exhibit.

The lint rules must be evaluated in context: words such as "not sponsored" or "no official approval" are often *safety disclaimers*, not actual unsupported endorsement claims. Flagged claims need evidence and human interpretation; a regex match must not grant or revoke authority.

## Future approval gates

Before distributing or deploying shows: independently verify research claims, media/music/image licensing, accessibility, venue technical specifications, cultural/community permissions, child privacy requirements, procurement terms, export restrictions and real contracts. Reconcile exact repo branch, source hashes and updated legal requirements at that time.

**Keeper:** The simulator proves a workflow shape. Customer consent, science review and rights decide whether it belongs in a dome.
