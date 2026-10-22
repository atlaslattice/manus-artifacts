# Shell-calcium and brine sulfate v0.4 — executed sensitivity 2026-10-09
**Status:** computational screening, SYNTHETIC / NON-CANON / ZERO REALIZED. Base scenario was run with the exact committed v0.4 Python source and JSON fixture copied into local execution; companion low/base/high sweep calculated by importing that module; no GitHub Actions CI claim.
## Stoichiometric outputs from exact base run
Input: 150,000 m³/day brine, Ca 680 mg/L, sulfate 4,500 mg/L, 365 days, 60% direct recovery; 96,000 t/year hypothetical shell feed at 95% dry carbonate and 70% activation, 65% shell-gypsum capture.
- Direct brine-derived gypsum: **95,961.77 t/y**
- Additional gypsum from shell + brine sulfate: **71,381.98 t/y**; total **167,343.75 t/y**, +74.4% vs brine-only
- Additional **brine-origin sulfate** captured: **39,826.41 t/y**, nominal resulting acid at 0.40 t per dry gypsum t: **28,552.79 t/y** pure H2SO4, **9,334.77 t/y elemental sulfur equivalent**. ALL THEORETICAL, not qualified, not import displaced.
- Pure HCl reagent nominal stoichiometric requirement **46,512.94 t/y**; shell activation reaction CO2 **28,071.56 t/y** before handling/capture. Actual acid dosing including side reactions may be greater.
- HCl at hypothetical **¥500, ¥1,000, ¥2,000, ¥3,000/t** = ¥23.26m, ¥46.51m, ¥93.03m, ¥139.54m annual pure-acid feed **cost only**, before storage, separation, brine and industrial acid conversion.
- If **pure acid sells/offsets at an illustrative ¥1,500/t**, the hypothetical additional acid production is valued at **¥42.83m/year**. HCl-only break-even price ceiling **~¥921/t pure acid equivalent** ignoring ALL other costs. This is neither a market price quotation nor actual plant profitability.
- Purchased vs reclaimed HCl routes are IDENTICAL physically and have **no cost data** in v0.4, so their economics cannot be ranked. Thermal activation gives same ideal material output at imposed same recovery but no heat, kiln CAPEX, CO2, calcination quality or operating costs. Not a proven better solution.

## Low/base/high activation + shell availability screen
| case | clean shell wet t/y | active CaCO3 fraction | gypsum capture | extra gypsum t/y | extra H2SO4 t/y (0.4 t/t) | pure HCl t/y | HCl-only break-even @¥1500/t H2SO4 |
| LOW | 24,000 | 40% | 40% | 6,275.34 | 2,510.14 | 6,644.71 | ¥566.6/t HCl |
| BASE | 96,000 | 70% | 65% | 71,381.98 | 28,552.79 | 46,512.94 | ¥920.8/t HCl |
| HIGH | 96,000 | 95% | 90% | 134,135.36 | 53,654.14 | 63,124.70 | ¥1,275.0/t HCl |
These are sensitivity options, NOT plausible probabilities. Shell feed is unverified 2017-era hypothesis; actual availability, moisture/contaminants, other users and site logistics unknown.

## Identified issue in exact v0.4 code
`sulfuric_acid_control` computed nominal H2SO4 input as **recovered gypsum ×0.5697**, reporting **40,663.48 t/y** in base. The **activated shell carbonate requires ~62,559.21 t/y H2SO4** for 1:1 acid-carbonate stoichiometry, independent of downstream precipitate recovery; acid undercount **~21,895.73 t/y**. This report corrects interpretation; code must be patched before further economic uses. Sulfur-source accounting also requires explicit mass flow and coproducts. Sulfuric-acid control adds **no new brine-origin sulfur**; it is an acid recycling route, not sulfur import replacement.

## Major unresolved chemical feasibility gate
The 0.65 'gypsum capture' coefficient is assumed, NOT an equilibrium/kinetic prediction. High-salinity CaCl2 + brine sulfate may remain below gypsum precipitation threshold; requires brine speciation, supersaturation, antiscalant, crystal separation and remaining high-chloride mother-liquor measurements. HCl reacts with shell carbonate to make soluble Ca and CO2; potential brine sulfate precipitation is not proof of industrial feasibility. 0.40 t/t downstream acid recovery is hypothesized from different solid feed process. Actual acid demand, recovered-acid available tonnage and whole-system net cash = UNKNOWN.
Realized sulfur import displacement 0; cash receipts 0; environmental outcome unknown. Next steps: site Ca/sulfate brine assays, shell offtake assays, thermodynamic modeling, bench precipitation trials by licensed operators, acid suppliers and regional acid hub's specifications.
