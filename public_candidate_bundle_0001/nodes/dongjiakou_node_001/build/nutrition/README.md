STATUS: CANDIDATE
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PUBLIC_RELEASE: candidate

# MM-135 daily nutrition extension v0.1 — 2026-10-10

Additive companion to the recovered Dongjiakou simulator at master
85f06406c724067ef917c55761ba5ff4354409ef. Original simulator, locality models,
source manifests and historical formulations are preserved.

Run from build:
```bash
python simulator_nutrition.py nutrition/examples/local_unknown.json
python simulator_nutrition.py nutrition/examples/central.json
python -m pytest -q
python simulator.py reproduce
python simulator.py validate
```

The companion composes models.current_state.run() unchanged with NUT01.
It does not change the canonical CLI, merge other draft PRs, install a service,
or add measured benefits to existing stream ledgers. All realized credit is zero.
The source evidence vocabulary is preserved in provenance; numeric projections
are SENSITIVITY, not MEASURED. A study on an ingredient is not a product trial.

## Candidate material and formulation delta

Select Fusarium compactum MM-135 as the **candidate authorized ingredient route**.
NHC's May2026 interpretation describes fermentation, RNA removal, inactivation
and filtration with >=50% dry-basis protein. Excluded users include infants/young
children, pregnant/lactating people and those allergic to edible fungi. Arbitrary
further extraction/concentration is not thereby cleared. Exact supplier identity,
lot safety/composition, operative annex and finished-product category audit remain
open. Supplier availability, local production, economics and compliance are UNKNOWN.

For 30g protein:
- 50% dry basis: 60g dry ingredient.
- 50% dry basis with assumed8% moisture:65.22g as-is powder.
- West's study concentrate:28/38.2=73.30%,40.93g study ingredient.
These are different references. Default local MM135 fraction/moisture are UNKNOWN.
The illustrative cases use50% dry only; no supplier CoA is implied.

Daily supplementation is NUT01's scope. Preserve the historical two150g-pouch
meal concept as a separate development branch; energy/macronutrients and complete
daily ration qualification are not inherited. Keep greens, superfoods, amino-acid
assays, selected functional mushrooms, broad micronutrient adequacy, smooth texture
and flavors as formulation R&D. A micronutrient target is not category permission:
subtract native nutrients, account for usual diet and upper exposures, choose exact
legal forms and intended population, then calculate an end-of-life label.

Theanine: tea-derived material0.4g/day at20% gives80mg active. This is not a universal
80mg active ceiling. A200mg active target needs >=50% potency to fit0.4g; exact
process/material authorization is unresolved. Creatine3g/day is a study dose,
not a percent performance effect; retain dry-compartment research and category
review. Lion's mane1.2g proposal is not equivalent to1.8g trial material.
Cordyceps stays gated pending the operative2014 amendment; old2g permission is not
accepted. Lingzhi's2023 inclusion is preparation-specific. Liposomal B3/C/Zn/Fe
exposure findings do not establish whole-premix encapsulation or gel performance.

## Ballpark sensitivities, not population forecasts

Illustrative denominator:10,000 eligible people, **not a Dongjiakou census**.
Adherent-equivalent people = population * adoption * adherence.
Task output change across that denominator =
adoption * adherence * joint susceptible prevalence * correction response *
subgroup task effect. One joint cohort prevents iron/zinc/D/protein double counting.
All four effect/prevalence inputs are arbitrary sensitivities, not recovered
DeepSeek coefficients or literature-derived regional estimates.

| Case | Adoption/adherence | Joint prevalence/response | Subgroup effect | Adherent equivalents | Responders (hypothetical) | Population task change |
|---|---|---|---|---:|---:|---:|
| Low |25%/60%|5%/40%|0%|1,500|30|0%|
| Central |50%/80%|15%/60%|3%|4,000|360|0.108%|
| High |75%/90%|25%/80%|8%|6,750|1,350|1.08%|
| Adverse |50%/80%|15%/60%|-2%|4,000|360|-0.072%|

These labels are not probability quantiles or a confidence interval. Scaling
the population changes counts, not percentages. The central convenience
assumption5minutes/day yields121,667 gross hours/year at365days; net usable time,
paid output and QOL are unmeasured. Convenience is not added to task change.
Creatine test effects and eligible fractions defaultUNKNOWN and remain a separate
endpoint. No numeric mushroom or liposomal enhancement multiplier is assigned.
No automatic GDP, healthy-life-year or disease-risk conversion exists.

Evidence supports conditional study endpoints, not these arbitrary coefficients:
iron-deficient Beijing workers improved energetic efficiency at the same work;
another low-ferritin trial improved fatigue without QOL improvement; a low-vitamin-D
trial had no strength benefit. Dose, population and comparator differ from this gel.
Zinc and protein adequacy require local baseline and matched outcome data; no
independent universal productivity coefficient is available here.

## Other gaps carried as structures

- **Household economics:** incremental annual spending=(daily full delivered
  price-displaced purchases)*days. Supplementation is not credited with displacing
  an entire meal. Price, affordability, income, clinical costs and lost-work savings
  remainUNKNOWN; measure time separately and report distribution, not just an average.
- **Operational skills/capacity:** min(equipment servings/day,
  staff hours/day*qualified fraction/hours per serving). Staffing competency,
  training completion, QA coverage, downtime, batch yield, cold-chain/utility
  reliability and demand all need local receipts. Capacity does not clear food safety.
  Health sensitivities assume supply; report capacity-limited coverage before use.
- **Emergency service days:** stock servings can express supplement-person-days
  only after safety, shelf-life and access qualification. Complete-ration service
  days stayUNKNOWN even if someone sets hypothetical qualification flags; a
  supplement cannot establish calories, hydration, clinical resilience or spaceflight
  suitability. Full emergency module still needs joint calorie/water/power/staff/access
  bottlenecks and validated storage. Reserved emergency_days is a planning request,
  not a credited deliverable.
- **Environment:** electricity*grid factor + substrate*substrate factor + other
  burdens per serving; subtract an explicit same-scope displaced comparator only in
  a hypothetical ledger. Net realized credit staysUNKNOWN/zero. PLENITUDE is a
  hotspot reference, not an MM135 local inventory. Track food-safe substrate,
  water, RNA-removal heat, recovery/drying, reject waste, packaging, transport,
  backup power, marginal displacement and one allocation owner. Food nutrient salts
  require separate domestic/import P/S/N origin and marginal-demand ledgers.
- **Cost:** Risner's USD3.55/kg wet (~USD29.56/kgprotein) is a modeled reference,
  not a current quote for driedMM135 or complete pouches. Extraction, drying,
  yield, contamination/rejects, labor, QA, flavor, premix, packaging and delivered
  utilities must enter a supplier/pilot TEA. Household outputs remainUNKNOWN until
  those costs and displaced purchases are evidenced.
- **Terpenes/texture:** benchmark purchased qualified flavor against food-safe
  citrus peel recovery, shared pectin/fiber/flavor processing, and a separate
  fermentation scenario. Do not grow engineered aroma organisms inside the protein
  line without a separate authorized process. Compare direct emulsion and
  encapsulation; measure retained analytes/headspace, oxidation and sensory release.
  Screen actual powder fineness x hydrocolloids in the complete mineral/liposome
  base, then assess viscosity/yield stress/squeeze force/grit/separation before and
  after preservation. TCM mushroom triterpenoids are not aroma monoterpenes.
- **Health/QOL:** prioritize safe nutrient adequacy and enjoyable daily use;
  measure GI/adverse events, fatigue, validatedQOL, affordability and time.
  Preregister a matched-calorie/protein/nutrient comparator trial before claiming
  gel efficacy. Any mushroom incremental arm must use identified trial-matched
  preparation/dose and prespecified endpoints.

## Receipt promotion sequence

1. Chinese ingredient/source/form/process/category/dose/claim audit.
2. MM135 supplierCoA: strain/process, moisture, protein and allEAAs, digestibility,
   RNA/purines, contaminants/mycotoxins, microbiology and food-grade feedstock.
3. Safe bench composition/preservation then sensory panel, repeated-use uptake.
4. Product-specific stability/pack integrity/liposome/aroma retention;5year
   shelf life remains aspirational and creatine dry packaging unvalidated.
5. Local prevalence/adherence/cost/capacity and controlled product outcomes.

The three first receipts are not interchangeable with efficacy or shelf-life.
None were created by running this software. Gypsum10kt standalone bounded-negative
result is preserved; shared-hub path remains a candidate, not proof of a unique
viable route or an actual avoided investment.

Artifact ID:NUT01-MM135-v01; source surface:public primary sources and recovered
simulator; source URI:source_register.json; raw export status:source exports/hashes
not archived in this package; receipt status:partial_content; review lane:
nutrition/regulatory/software; missing receipts:listed above.
Claims: candidate route, arithmetic, structures and tested non-crediting behavior.
Receipts: local test/validation outputs, exact base commit, source URLs and
provenance; no field, supplier, sensory, clinical, deployment or aerospace receipt.

