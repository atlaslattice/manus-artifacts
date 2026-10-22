# Shandong 2026 Acid Balance — DeepSeek Dataset Handoff v1.4

## Objective
Fill the regional 2026 sulfuric-acid supply/reliability balance and industrial-sulfur input ledger with *observed* public data. **PROPOSED / NON-CANON / ZERO REALIZED BENEFITS / NOT A VERIFIED NET SHORTAGE.**
## Verified dataset rows for independent ingestion
**NBS China monthly 100%-equivalent H2SO4 production (national, enterprises above designated size):**
| Month | Monthly Mt | YTD Mt | YoY | Official source |
| --- | ---: | ---: | ---: | --- |
| 2026-05 | 8.37 | 44.29 | -1.6% | [NBS May](https://www.stats.gov.cn/english/PressRelease/202606/t20260617_1963964.html) |
| 2026-06 | 7.92 | 52.22 | -10.0% | [NBS June](https://www.stats.gov.cn/english/PressRelease/202607/t20260717_1964159.html) |
| 2026-07 | 7.68 | 60.24 | -14.0% | [NBS July](https://www.stats.gov.cn/english/PressRelease/202608/t20260818_1965071.html) |
| 2026-08 | 7.98 | 68.14 | -15.5% | [NBS August](https://www.stats.gov.cn/english/PressRelease/202609/t20260917_1965348.html) |
Caveat: above-designated-size industrial national output differs from the sulfuric acid industry association census; do not splice with 127.8Mt 2025 total without a coverage bridge. Monthly and YTD values are each rounded by NBS; don't infer missing months simply by subtracting adjacent rounded YTD records.
**Shandong weekly Longzhong/Mysteel acid production utilization SAMPLE by process:**
| Week end | All acids | Sulfur-burning acid | Smelter acid | Ore/pyrite acid | Other acid | Sample count |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-05-08 | 78.30% | 64.05% | 92.60% | 93.40% | 71.37% | 47 |
| 2026-06-25 | 57.03% | 32.33% | 67.25% | 96.07% | 53.43% | 50 |
Links: [May 8](https://www.mysteel.com/oilchem/a/26050817/6A72C81562BD1948.html), [June 25](https://www.mysteel.com/oilchem/a/26062414/995C7C6F7D27D4A8.html). These demonstrate a **sampled utilization decline**, not a production drop or shortage unless capacities and sampling frames are bridged. Sample counts differ (47 and 50).
**Shandong elemental sulfur downstream factory sample:** June 19–25 report ~20,400 t sulfur/week consumed and 29.94% operating rate; source [Longzhong June25](https://nenghua.mysteel.com/a/26062511/1122768F929A4742.html). Sample of sulfur-consuming facilities, NOT representative of all acid producers or identical to the utilization sample.
**Temporary disruption:** Shandong May–early July acid plant turnaround projection ~426kt potential losses; **forecast not certified unmet orders**. [Mysteel May12](https://www.mysteel.net/analysis/5123368-shandong-sulfuric-acid-market-strengthens-despite-seasonal-off-peak-season).
## Existing source directories (NOT downloaded national monthly datasets)
- [Longzhong/Mysteel Chinese provincial weekly sulfuric acid production and customs tables](https://www.mysteel.com/oilchem/article/4kscop/) indexes Shandong, Jiangsu, Zhejiang and Anhui weekly production, 2026 monthly national production, customs acid imports/exports. Licensing/individual row coverage must be assessed.
- [Longzhong sulfur consumption directory](https://www.mysteel.com/oilchem/article/atntkc/) indexes Shandong weekly consumption, central China and Southwest samples.
- [Longzhong monthly apparent sulfuric acid consumption directory](https://nenghua.mysteel.com/list/article/pa11433a04%2C1402aaaaa1.html) indexes Jan–Jul national monthly apparent consumption; do not equate apparent with province-specific unmet fertilizer demand.
- [China GACC Customs Monthly Bulletin](https://english.customs.gov.cn/statics/report/monthly.html) and corresponding interactive trade interfaces. Query sulfur **HS 2503** and sulfuric acid/oleum **HS 2807** with edition and customs nomenclature verified; do not mistake customs destination province for final consumption.
## Required DeepSeek work / precise ask
Construct 2026 Jan–Sep monthly SHANDONG and neighboring provincial series for sulfuric acid by **100% H2SO4 equivalent**, separation of sulfur-burning/smelter/ore/spent-acid routes, actual utilization and production, domestic elemental sulfur production/import inputs, inventories, qualified fertilizer vs other offtake, exports and interprovincial arrivals/departures; track sampled versus census coverage, capacity weights, price grade/delivered logistics. Fill each field as OBSERVED with row-wise URL/timeframe/license, REPORTED, MODELED or UNKNOWN; do not extrapolate a week into a year. Add sensitivity to maintenance outages (avoid double count of redirected exports). Return interval for SHANDONG_NET_UNMET_DEMAND by month, or explicitly UNKNOWN if transactions and demand not observed.
## Unit/source safeguards
Molecular sulfur mass fraction of pure H2SO4: 32.065/98.079=0.32692. The prior 0.87Mt acid hypothesis is ~0.284Mt contained S; never claim 12% of 7.48Mt S. 109.3-107.55=1.75Mt acid, not 1.87. Domestic acid demand, acid imports and sulfur feedstock imports are independent. The chemical process recovery, cost/energy/CO2 and national export permission remain unverified. No dataset here establishes an Atlas operational node or permit.
