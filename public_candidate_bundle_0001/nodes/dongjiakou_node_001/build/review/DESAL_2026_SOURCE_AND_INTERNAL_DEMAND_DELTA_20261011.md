# Dongjiakou: October 11, 2026 desal evidence and internal-use economics delta

STATUS: PUBLIC RESEARCH CANDIDATE / NON-CANON / ZERO REALIZED CREDIT
Preserve original October 8 evidence appendix, resource modules and node register unchanged. China-facing DragonSeek PR #299 remains independent and untouched.

## Official context (verified)
- National desalination action plan: National Development and Reform Commission et al., signed July 2 and published July 16, 2026. Official notice: https://www.ndrc.gov.cn/xxgk/zcfb/tz/202607/t20260716_1406539.html ; explanation https://www.ndrc.gov.cn/xxgk/jd/jd/202607/t20260717_1406556_ext.html . Goal by 2030: >4.5 million tonnes/day desalination capacity with >1.5 million tonnes/day added. This policy is **already covered** by the October 8 evidence appendix; do not double-count it as a new discovery.
- Dongjiakou reverse-osmosis upgrade tender August 5, award September 1, 2026: official Qingdao record https://ggzy.qingdao.gov.cn/c/TradeDetals-ZtbShow/163949-5070-0-8-0/e877b066-0435-4d4b-81e2-bc95bd2f048b-B03CE5B6FC1D2D3C2D5FCEBC39AA2406.html . Bid award RMB 15,381,311.40 tax-inclusive, for first-stage RO membrane-element replacement. **This is maintenance/upgrading procurement, not bromine/magnesium recovery deployment**, and the award alone does not establish completed installation.
- National totals (2025 report, publicly reported June 2026): 167 desalination **engineering projects**, ~3.077 million tonnes/day aggregate capacity. The pre-existing [node register](../lattice/CHINA_DESAL_NODE_REGISTER.md) correctly warns that 167 is **not** a count of Atlas nodes.

## Peer-reviewed comparators (not Dongjiakou deployments)
- Liu et al., *Science Advances*, March 18, 2026, DOI 10.1126/sciadv.aeb2604: chemical-additive-free approach to limit MgSO4-related scaling in experimental desalination-brine evaporation/crystallization; laboratory demonstration >408 hours, 4.29 kg m^-2 h^-1, with outdoor tests. https://pmc.ncbi.nlm.nih.gov/articles/PMC12998523/ . Research comparator for brine handling, not evidence of an industrial-scale site install.
- Raza et al., *npj Clean Water*, September 28, 2026: solar-driven brine evaporation with directional crystallization; 20 wt% test brine, >=1.2 kg m^-2 h^-1 during 12-hour illumination test. https://www.nature.com/articles/s41545-026-00636-w . Bench comparator; feed salinity and conditions require site-specific comparison.

## Model correction: captive industrial demand before merchant market size
The user's stated objective is **internal industrial symbiosis**: recover raw material from an existing waste stream and transfer it to a colocated or network-connected user who would otherwise procure it externally. The opportunity is not automatically capped by merchant-market turnover, but cannot be credited beyond real offtake/use.

For each chemical grade and geography compare:
(A) External procurement fully loaded delivered cost, including transport, margins, duties and supply-interruption exposure where evidenced.
(B) Internal reuse fully loaded incremental cost: pretreatment + energy + reagents + selectivity losses + process chemicals + staff + maintenance + capital amortization + certification + quality + packaging + delivery + storage + waste/residual management + ecological controls.
**Net avoided cost per eligible unit = A − B**. Compute only on `min(grade-compliant recovered amount, verified eligible internal demand)`; avoid conflating raw inventory with output. Both paths must use identical purity/species units and account for foregone baseline disposal costs carefully.

**Scenario tiers:** local captive industrial demand → network captive industrial demand → documented import displacement → strategic inventory with carrying costs → external merchant sale at market-clearing marginal prices → excess technically extractable inventory with **zero attributed revenue**. Additional demand unlocked by low price may be scenario-modeled, never assumed. Do not simultaneously credit the same kilogram as an avoided import, an internal sale and an external sale.

Magnesium: distinguish elemental Mg, MgO, Mg(OH)2, MgCl2 and hydrated salts and grade conversion. Bromine: distinguish bromide-in-brine inventory from saleable bromine/bromide derivatives and include selective recovery, reagents, materials, toxicology and effluent risks. Deuterium: isotope concentration is **not** materially improved by conventional RO; assess isotope separation separately, as [Run 6](../reports/RUN_6_RESOURCE_MODULES.md) does.

Risk exposure (including contested shipping lanes) is a stress-test scenario, **not proof** of immediate supply interruption, cheap production, official requests or institutional adoption.

## Required gates and dashboard contract
Keep the eight Run 6 gates: yield, selectivity, energy, reagents, material life, residual fate, market ceiling/real demand, ecology. The ecology/residual-fate veto remains. No extraction throughput, net benefit, carbon benefit or deployment is promoted by this note. Add dashboard statuses for INVENTORY, TECHNICALLY RECOVERABLE, SPEC-COMPLIANT OUTPUT, VERIFIED CAPTIVE DEMAND, ACTUAL OFFTAKE, AVOIDED COST, and NET BENEFIT; never collapse them into one giant theoretical sales figure.

Source-link every metric with asset, time, units, assay, product grade, provenance, publication date, evidence tier, actual-versus-scenario status, and double-count key.

## Independent provenance
China's policy and research progress can be compared with dated public work without implying the user's simulations caused announcements or that DeepSeek has governmental authority. Evidence of influence requires traceable acknowledgment, citations or project integration receipts.
