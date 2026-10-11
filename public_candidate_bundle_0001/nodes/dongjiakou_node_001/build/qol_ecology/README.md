# QOL01 + ECO01 portable companion — candidate v0.1

STATUS: PROPOSED / NON-CANON / NOT DEPLOYED / ZERO REALIZED CREDIT
DATE: 2026-10-10
SCOPE: additive and independently executable, **not integrated** with the main simulator's `current` command. No changes to existing numerical baselines, scripts, or resource-gap schema.

This companion records the user's approval of five candidate additions: right to disconnect; free café/community commons; coastal stewardship commons; full-lifespan accessibility, care and mobility; independent ecological observatory. It also carries proposed older provisions (8/8/8, events/festivals, backup, HVAC/HEPA) as candidate service identifiers. Nothing here implies installations or realized outcomes.

Read [scenario.schema.json](scenario.schema.json), [dongjiakou_candidate.json](dongjiakou_candidate.json), [companion.py](companion.py) and [tests/test_companion.py](tests/test_companion.py). Dependencies: Python standard library; jsonschema optional for JSON Schema validation. Run `python3 qol_ecology/companion.py qol_ecology/dongjiakou_candidate.json` from build root; `python3 -m unittest discover -s qol_ecology/tests`.

## Principles
1. Model **measured** conditions first, not the attractive design target. Any unknown values remain null; null does not mean zero.
2. Provenance for every input: source URL/identifier, observation date, measurement/report/sensitivity/proposed state, geography, denominator, unit.
3. Keep **finance**, **people**, and **ecology** outcomes distinct. Never assume ecological benefits are cash flows or add them into an undifferentiated score.
4. Discharges tracked by outfall and contaminant; no disappearing pollutants via sludge, brine, groundwater or other watersheds. Necessary environmental freshwater flows are not waste discharges.
5. Treat 40% cost recovery and 60% social financing as a **user-reported scenario needing original receipt**, not verified Dongjiakou CAPEX/OPEX or a net-present-value calculation.
6. Comparisons across localities depend on location-specific denominators, energy mix, units, climate, regulation, accessibility and pollution pathways; never just multiply a single-site benefit by a national node count.
7. A 1,000-year stewardship horizon requires maintenance/replacement scenarios, uncertainty and physical ecology endpoints; no naïve annual benefit × 1,000.
8. No assumption of direct near-term North Pacific/Hawaii pH response. Global ocean acidification and local effluent chemistry are separate domains.

## Original source anchors
- https://app.notion.com/p/3f50c1de73d981ccb63affc1a2fc89ac (Culture, backup, HEPA, Oct 9)
- https://app.notion.com/p/3f50c1de73d981c0bfdac34f11c0e373 (8/8/8, movement, urban design, Oct 9)
- https://app.notion.com/p/3f20c1de73d98132893ae61d44225d38 (Living Well evidence review)
- https://app.notion.com/p/3f40c1de73d98130a203fa148fd32d18 (Outfall protection invariant)
- https://app.notion.com/p/3f40c1de73d98148b74ed6bcc24aac1c (Illustrative Hawaii sensitivity only)
- https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md (source-review boundaries)

Evidence labels are not proof; a REALIZED claim additionally needs authenticated operating evidence, independent validation and affected-party approval. Baseline uses nulls for missing observations.
