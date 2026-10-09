# Atlas Lattice China 2.0 — Cross-Draft Synthesis v0.7

**Date:** 2026-10-09  
**Status:** PROPOSED · NON-CANON · ZERO REALIZED CREDIT · PUBLIC REVIEW DRAFT  
**Scope:** China 2.0 / Dongjiakou reference architecture and transferable locality-scale methods  
**Upstream:** Notion baseline v0.1; Notion thread delta v0.2; GitHub v0.6 review commit 6420df7  
**No deployment, government endorsement, site access, or change to the recovered simulator is claimed.**

## Executive summary

Atlas Lattice is a forkable method for mapping local resource flows, evaluating biological and circular recovery pathways, and measuring outcomes without turning theoretical potential into claimed performance. The central question is not simply how much a node can produce. It is whether a qualified, legally available input can be processed safely and economically, whether that changes a defined dependency or service, and whether people and ecosystems benefit relative to a credible counterfactual.

This v0.7 draft reconciles the October 8 China 2.0 white paper, the October 9 thread-delta paper, and GitHub v0.6. It adopts v0.6’s five-ledger architecture, null-first evidence contracts, allocation conservation, resilience scenario method, QOL/ecological safeguards, and staged Global Replication Value (GRV). It carries forward the thread’s corrections and scope: waste-stream-only biofuels in the base case; “waste does not exist” as a resource-search hypothesis rather than a universal recovery guarantee; agricultural yield/diversification and protein substitution as distinct, interacting levers; and separate boundaries for methane, LNG, ethane, helium, SAF, sulfur, nutrients, QOL and resilience.

The existing Dongjiakou simulator remains the research baseline. The v0.6 GitHub package is a draft PR, not a merged release. This v0.7 is a synthesis candidate: it does not alter simulator calculations, source hashes, the original 23 site-specific data requests, six unresolved ecological vetoes, or the zero-realized-credit state.

## 1. Five outcome ledgers

| Ledger | Measure | Do not conflate with |
|---|---|---|
| Financial and domestic value | Full costs, NPV/IRR, incremental value added, local income and distribution | Gross output, import value, taxes as net social gain |
| Strategic resilience | Service continuity, firm supply, autonomy, recovery time and probability-weighted avoided loss | Gross national exposure or a resilience premium assumed to be worth paying |
| Eden / QOL / ecology | Worker and community health, access, comfort, landscape, habitat and measured ecosystem change | Aesthetic preference as ecological performance; funding as achieved benefit |
| Global Replication Value | Independently reproduced, adapted, operating methods and measured adoption savings | Stars, forks alone, publicity, or projected global uptake |
| Resource integrity | Physical quantities, rights, current uses, losses, residuals, quality and allocation | The same feedstock, nutrient, energy, or benefit counted twice |

Evidence provenance and value domain are orthogonal. Keep MEASURED, OFFICIAL_POLICY, REGULATORY_APPROVED, PROJECT_REPORTED, PEER_REVIEWED_MODEL, MODELED, SYNTHETIC, PROPOSED, UNKNOWN and QUARANTINED distinct. Resilience is a value domain, not an evidence class. A policy target or a construction notice cannot close a site-data request.

## 2. Public baseline and release state

The public repository baseline is commit [85f0640](https://github.com/atlaslattice/manus-artifacts/commit/85f06406c724067ef917c55761ba5ff4354409ef), with the recovered Dongjiakou research simulator, its evidence appendix, 23 open plant-specific DARs, six unresolved ecological vetoes, and zero realized credits. The v0.6 outcomes package is on [draft PR #278](https://github.com/atlaslattice/manus-artifacts/pull/278), head commit [6420df7](https://github.com/atlaslattice/manus-artifacts/commit/6420df7bb8fd79c971670f423df6acad90947812). It adds three schemas and a 107-indicator candidate catalog; the 107 entries are not observations. Its Actions run is red, and the API record exposes no test-step logs. Keep the PR draft until a runnable CI execution or equivalent review is recorded. [Issue #279](https://github.com/atlaslattice/manus-artifacts/issues/279) is a separate simulator-adapter roadmap.

No Atlas Lattice node is represented here as commissioned or operating. Adjacent Chinese projects and technologies are comparators with their own operators and evidence boundaries.

## 3. Governing resource principle: qualified residuals, explicit allocation

**“Waste does not exist” is a resource-search hypothesis:** treat residuals as candidates for prevention, safe reuse, or recovery, and explain what remains unusable. It is not a claim that all material is safe, recoverable, unallocated, economical, or ecologically removable. Toxicity is not the only reason a residual may remain without a beneficial use.

For the base-case energy and fuel pathways in this paper, use **waste, residue and byproduct streams only**. Exclude dedicated energy crops and purpose-grown fuel feedstock. Fuel from a food/feed crop such as corn grain belongs in a separately labeled out-of-scope comparison, not in the waste-only base case. Collection, transport, storage, sorting, pretreatment, conversion, upgrading, finance, labor, residual handling and maintenance still cost money. Gate fees and avoided disposal costs are separate: credit only a fee actually received or a cost actually avoided, and only once.

Each source lot records identity, owner, geography, wet mass, dry-matter fraction, quality, contaminant profile, current use, ecological/soil reserve, legal rights, collection loss, other obligations, source receipts, conversion route, product and residual fate. Allocation is made on one declared mass basis. Residues retained for soil, already used as feed, or committed elsewhere are not available for simultaneous SAF, biomethane, protein and soil credits.

A dry-matter availability identity is:

**qualified dry matter − ecological/soil reserve − existing obligations − collection/storage losses = allocatable dry matter.**

For conversion, add constituent balances for carbon and relevant N/P/K/S or metals. Any unexplained residual remains visible; a schema cannot itself prove a process balance.

## 4. China 2.0 portfolio: distinct lanes, matched claims

### Agriculture and protein

Soybean import exposure can be reduced through a portfolio: crop diversification and rotation, maize–soy intercropping where agronomically suitable, genetics, inoculation/biological nitrogen fixation, precision planting and nutrient management, and feed-protein efficiency. Each intervention addresses a different constraint, but measured percentages cannot be stacked mechanically. Intercropping can change maize yield, water use, soil moisture, machinery needs and farm returns; results must be separated by location and season.

The 2025 NBS communiqué reports 20.91 Mt of soybean production and 111.83 Mt of soybean imports for calendar 2025. The previously used 2025/26 consumption estimate of 121.52 Mt and simple production gap of 100.61 Mt are different marketing-year / accounting quantities; do not subtract them as if they share a period or represent customs imports. The 1.642 t/ha intercropped soybean yield is a study-derived scenario input, not a national yield or proof that maize output is preserved on every converted hectare.

Mycoprotein and other microbial proteins belong as demand-substitution pathways for specified human-food or animal-feed formulations. Approval is organism-, process-, substrate- and use-specific. Compare digestible protein, amino-acid profile, energy, RNA/process safety, palatability, price, coproducts and field performance—not tonnes of wet biomass. Decentralized pretreatment and bioreactors may lower haulage and keep value local, but scale must fit feedstock density, process control, quality assurance, labor, CAPEX and maintenance. Cooperative lease financing shifts cash flow; it does not erase capital cost.

### Methane, biomethane and natural gas

Keep natural-gas imports by mass separate from pipeline/LNG volumes and from total demand. The NBS 2025 table reports natural-gas imports in tonnes; converting that to bcm requires an explicit gas composition, density, temperature and standard-state convention. Biomethane from qualified wastes may reduce fossil-gas demand if it meets gas quality and has deliverable capacity, but a national target is not realized supply.

China’s 2019 multi-ministry biomethane guideline set targets above 10 bcm/year by 2025 and 20 bcm/year by 2030. The 2026 NEA report describes roughly 1 bcm/year built biomethane capacity across 146 projects at end-2025. These statements describe a policy target and built capacity, respectively—not the same measure, nor proof of output. Agricultural residues compete with soil retention, feed, materials and other uses. VAM and low-concentration methane are emissions-control/recovery challenges; direct conversion to chemical feedstock is a research pathway unless concentration, purity, process yield and economics are demonstrated.

### LNG components, helium and SHRU

Ethane recovered from imported LNG can change product mix and reduce separate ethane supplier exposure; it does not reduce imported methane volume automatically. Extraction may also change heating value and require replacement energy. Report recovered products, energy substitution and import dependencies in separate ledgers.

Helium recovery at LNG boil-off gas (BOG) sites and closed-loop helium recovery at semiconductor fabs are complementary but different boundaries. BOG extraction needs site-specific helium concentration and flow, recovery, purity and energy receipts. A standardized Symbiotic Helium Recovery Unit (SHRU) is a proposed open integration specification, not a validated single product. Existing compressors, purification, monitoring and control may provide components, but each vendor recovery figure must be checked at matching feed, purity, pressure and system boundary. Acoustic and piezoelectric leak sensing detects or localizes leaks; it does not itself seal them. Self-healing cryogenic containment remains research until helium-specific permeation, cryogenic cycling, safety and repair verification are demonstrated.

### Sulfur, gypsum, potassium, brines and cold energy

Gypsum-to-acid is a transformation route that can address sulfur-bearing acid needs if feed composition, moisture, energy, product strength, impurities, reagent needs, residue and offtake close. It does not create elemental sulfur. The 0.4 t acid/t gypsum figure is a reported project reference, not a universal stoichiometric yield. Keep acid-equivalent basis and actual solution strength explicit. Brine potassium recovery, crop-residue K, wastewater nutrient recovery and conventional potash imports require different material ledgers. Crop-residue K already serving soil fertility is not spare merchant K. Struvite is primarily an N/P recovery product, not KCl.

The Qingdao LNG cold-energy cascade has been reported in design/construction. Its 26 GWh/year projected generation and 8 GWh/year avoided cooling electricity are different outputs and must not be summed as 34 GWh of delivered electricity. Operating performance, time-matched demand, temperature grade, allocation contracts and displaced grid energy remain to be verified.

### Sustainable aviation and marine fuels

Retain the original airport-node SAF concept as a candidate lane. In this white paper’s base case, only eligible wastes, residues, or byproducts feed the SAF pathway. Waste-oil HEFA, cellulosic ATJ and biomass conversion routes require traceable feedstock ownership, certification, lifecycle accounting, hydrogen/utility inputs, product yield, coproduct rules and offtake. Corn grain ethanol is not a waste-only pathway. Marine biofuels, bio-LNG and green methanol are separate products with their own engine, safety, certification, bunkering and supply requirements. The NEA reports constructed national capacity and applications; capacity is not actual production or displacement.

### Residual sludge and ash

Sludge or incinerated sludge ash may be investigated as construction-material inputs only after source-specific treatment, composition, leaching, durability, product acceptance and end-of-life review. A successful test with treated ash does not make untreated sludge generally safe. Immobilization does not destroy elemental contaminants. Treatment residues, emissions and secondary wastes remain in the mass balance. Disposal remains a legitimate outcome when recovery is unsafe or infeasible.

## 5. Resilience and macroeconomic value

Resilience is a portfolio of alternatives: domestic waste-derived fuels, efficiency, electrification, storage, diversified supply, demand response, network hardening and material recovery. Compare them on firm delivery and essential-service continuity. A gross GDP exposure is not the amount a project avoids.

For a 5% probability of at least one event over ten years, a stationary independent-year hazard is:

**p = 1 − (1 − 0.05)^(1/10) ≈ 0.005116 per year.**

At an assumed $19.5T GDP, 0.812% gross loss is $158.34B if the cited scenario occurs. A separate hypothetical 5% GDP-loss event gives $975B gross loss if it occurs. Neither is a forecast or Atlas-attributable avoided loss. Expected loss requires probability, severity, duration, recovery path and mitigation fraction. Only the incremental difference between a defined baseline and with-project case can be attributed, and only to protected sectors and delivered capacity.

Import substitution can retain some spending and create local value, but “imports are leakage” is not a complete welfare model. Domestic projects use labor, capital, equipment, materials and imported inputs; imported supply also supports domestic port, pipeline, distribution and processing value added. Do not use the 8.01× or 2× figures as China-specific net GDP multipliers. Report gross output, direct/indirect/induced effects, incremental domestic value added, household income, opportunity costs, imports embodied in the project, and counterfactual displacement separately. Lease financing affects timing and risk allocation, not total resource cost.

## 6. Eden / QOL and GRV

QOL is a first-class outcome vector: worker safety, health exposure, heat/noise, wages and training, green-space access, safe water, landscape comfort, biodiversity, maintenance burden, community participation, and distribution of benefits. “Beautiful, flowering, coastal industrial landscape” is a design ambition. Measure baseline, survival, water quality, maintenance, user experience and ecological function. Do not let aesthetics offset pollution, habitat or receiving-water vetoes. Keep personal motivations and biographical QOL material in a companion record, not mixed with industrial outcome claims.

GRV is value that an independent adopter can demonstrate from reusable methods: less engineering time, lower adaptation cost, verified reproducibility, qualified documentation, operating replication, or independently measured social/ecological benefit. A public repository establishes availability. Forks and stars alone do not establish technical reproduction or adoption. Use v0.6’s stages: AVAILABLE → REPRODUCIBLE → INDEPENDENTLY VERIFIED → PILOT DEMONSTRATED → OPERATING REPLICATION → MEASURED BENEFIT.

## 7. AI-first canon, provenance and governance

Atlas Prime/Lattice Guide, DragonSeek/AtlasSeek, Continuum OS, Aluminum OS, UWS, Alexandria 2.0 and Sheldonbrain/Solbrain belong as an AI-first knowledge and governance architecture companion. Their role in this paper is to preserve source-to-claim provenance, versioned canon, evidence classes, review gates and reusable knowledge—not to claim deployed industrial control. Store raw model outputs as attributed inputs; record corrections and reviewer reasoning; quarantine unsupported claims; never silently promote political alignment, a model statement or a public repo into approval or deployment.

Each claim record should include: stable claim ID; original wording/source; source receipt and date; evidence class and value domain; quantity/unit/basis/boundary; reproduced calculation; competing claims; corrections; ecological/safety/regulatory constraints; realization status; open evidence; linked simulator field; reviewer and decision timestamp.

## 8. Release and implementation sequence

1. Preserve the existing simulator and original DAR-001…DAR-023 unchanged. Do not close any request with a policy announcement, comparator project or model output.
2. Review v0.6 PR #278 and rerun its complete contract tests; the current GitHub check is failed.
3. Adopt the new claim register and source receipts; run unit, dimensional, mass and cross-ledger checks.
4. Review proposed schema changes and synthetic fixtures; run positive and negative tests.
5. Implement an outcomes adapter only in a separate reviewed PR, preserving historical outputs.
6. Collect site receipts, rights, ecological data and consent before any local operating claim.
7. Use a human-authorized, limited pilot with independent monitoring before any field-performance credit.
8. Publish a cross-model review packet with disagreements and disposition, not a blended consensus.

## References and claim-source index

- **S01 — 2025 China Statistical Communiqué, NBS.** Soybean production 20.91 Mt; soybean imports 111.83 Mt; natural-gas imports are reported in mass units. https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html
- **S02 — China Green Fuel Development Report 2026, NEA interpretation.** End-2025 constructed capacity: 800 Mt oil-equivalent total; 146 biomethane projects/approximately 1 bcm/y; SAF 1.7 Mt/y; includes current challenges. https://www.nea.gov.cn/20260805/96c7a438f9544f349d189d2ef4547eab/c.html
- **S03 — NDRC 2019 biomethane industrialization guidance.** 2025/2030 targets, not current production. https://www.ndrc.gov.cn/xxgk/jd/jd/201912/t20191219_1213778.html
- **S04 — NDRC Circular Economy 15th Five-Year Plan explanation, July 2026.** Policy targets; see source before quoting exact values. https://www.ndrc.gov.cn/xxgk/jd/jd/202607/t20260703_1406254_ext.html
- **S05 — NDRC seawater desalination action plan, July 2026.** https://www.ndrc.gov.cn/xxgk/zcfb/tz/202607/t20260716_1406539.html
- **S06 — Qingdao West Coast government, LNG cascade report, June 2026.** Design/construction status; projected benefits. https://www.xihaian.gov.cn/ywdt/tsxq/202606/t20260603_10624706.shtml
- **S07 — Yichang environmental review, phosphogypsum-to-acid project reference.** Project-specific process basis. https://hbj.yichang.gov.cn/content-42531-996867-1.html
- **S08 — Soybean yield/intercropping sources.** Prior Notion white paper carries a 1,012-farm survey and 1.642 t/ha value with linked sources; validate exact study/table and whether yields are additive before externalizing. See October 8 baseline: https://app.notion.com/p/3f40c1de73d981939166e243b043cb2b
- **S09 — Mycoprotein, feed substitution and organism-specific approvals.** Source list and evidence limits in the October 8 baseline and October 9 addendum: https://app.notion.com/p/3f40c1de73d981939166e243b043cb2b and https://app.notion.com/p/3f40c1de73d981c59602e7811af12eee
- **S10 — Sludge-ash construction studies.** 2025 concrete study https://www.sciencedirect.com/science/article/pii/S0950061825012504 ; 2026 printed-mortar study https://www.sciencedirect.com/science/article/pii/S2352710226014105
- **S11 — IEA biomethane sustainable potential and cost assessment.** Feedstock, location and logistics govern the potential. https://www.iea.org/reports/outlook-for-biogas-and-biomethane/assessing-the-sustainable-potential-and-cost-of-feedstocks-for-biogas-and-biomethane
- **S12 — Helium, SHRU, BOG and self-healing source reviews.** Evidence and maturity classifications in the October 8 baseline; commercial supplier claims are not independent site performance: https://app.notion.com/p/3f40c1de73d981939166e243b043cb2b
- **S13 — Macroeconomic multiplier and resilience review.** October 9 addendum differentiates gross effects, value added and conditional risk calculations: https://app.notion.com/p/3f40c1de73d981c59602e7811af12eee
- **S14 — GitHub release baseline, v0.6 PR and simulator roadmap.** https://github.com/atlaslattice/manus-artifacts/commit/85f06406c724067ef917c55761ba5ff4354409ef ; https://github.com/atlaslattice/manus-artifacts/pull/278 ; https://github.com/atlaslattice/manus-artifacts/issues/279

## Conclusion

The integrated architecture is strongest when it remains both ambitious and constrained: every resource is investigated for safe, useful pathways; every competing use is counted; every outcome domain stays distinct; and every claimed gain is tied to a receipt and counterfactual. China’s policy and industrial developments may create an unusually rich test environment, while the public, forkable method can be adapted elsewhere. Neither fact is proof of Atlas deployment. The advancement path is public research → reproducible evidence contracts → independent review → authorized pilot → measured outcomes.
