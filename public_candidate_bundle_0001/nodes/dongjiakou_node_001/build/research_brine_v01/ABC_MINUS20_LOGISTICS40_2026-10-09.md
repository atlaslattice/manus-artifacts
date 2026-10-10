# 2026-10-09 — Executed A/B/C: −¥20/t byproduct HCl and ¥40/t logistics
**Status:** COMPUTED_SYNTHETIC / NON_CANON / ZERO_REALIZED_CREDIT. A local standalone Python script executed the same base numerical constants as earlier S01 v0.4/Route C estimates. This is a commercial-rate **sensitivity**; it is NOT a supplier quote, actual production, operational model, GitHub CI, or proof of chemistry.
**Agreed inputs:** A brine-only; B shell with 31% commercial HCl at ¥195/t solution; C shell with byproduct 31% HCl at **−¥20/t solution** (historical 2025 Shandong observed price) plus **¥40/t solution estimated freight/logistics**. Extra conditioning surcharge set to ¥0 for the explicit requested run, which is NOT evidence none is required. Also assume 46,512.94 tonnes/y 100%-HCl equivalent, 150,041.74t/y 31% solution, base brine gypsum 95,961.77 t/y, additional shell gypsum 71,381.98t/y, acid yield 0.40t H2SO4/t dry gypsum, hypothetical acid value ¥1,500/t. Other costs absent, including additional shell procurement/washing, acid dissolution, precipitation, mother liquor salt/water, downstream gypsum→H2SO4 hub, environmental controls, utilities, CO2, capital and financing.
| Annual metric | A brine-only | B purchased HCl | C byproduct HCl |
|---|---:|---:|---:|
| Total gypsum theoretical t/y | 95,961.77 | 167,343.75 | 167,343.75 |
| Total acid potential t/y | 38,384.71 | 66,937.50 | 66,937.50 |
| Extra acid potential vs A t/y | 0 | 28,552.79 | 28,552.79 |
| HCl solution t/y | 0 | 150,041.74 | 150,041.74 |
| HCl source purchase / receiver payment ¥m/y | 0 | +29.258 | −3.001 |
| Logistics ¥m/y | 0 | +6.002 | +6.002 |
| Net reagent + freight outlay ¥m/y | 0 | 35.260 | 3.001 |
| Extra acid nominal value ¥m/y | 0 | 42.829 | 42.829 |
| **Incremental contribution before omitted costs ¥m/y** | 0 | **7.569** | **39.828** |
**Accounting:** the negative source price implies receiving party gets ¥3.001m if this historic price existed for all 150kt and no grade/quantity discount, which has NOT been established. If both supplier and receiver join Atlas, the transfer cancels in consolidated accounts: group result cannot include a fictitious transfer receipt. Real avoided disposal treatment may be an independent benefit **only** with supplier records and clear counterfactual, not double counted.
**Break-even logistics for Route C** at these assumptions is up to about ¥305/t solution ignoring all other costs; this threshold is not a project feasibility estimate. Need actual logistics quotes inclusive of road/ship, distance, hazardous material licensing, equipment, return loads, temporary storage, and insurance. True delivered cost = −20 + 40 + conditioning and other real fees per t.
**Material caveat:** hard calcium/sulfate inputs remain SYNTHETIC; salt/brine activity may prevent assumed gypsum recovery even when stoichiometry balances. Industrial conversion to acid unverified. Internal S-atom, water, chlorine and carbon boundary requires certified process flows. Realized imported-S substitution, industrial deployment and profit remain zero.
**Run files:** Python reproducible script `run_abc_minus20_logistics40.py`, output `abc_minus20_logistics40.csv`, both committed to draft research branch as standalone synthetic analysis.
