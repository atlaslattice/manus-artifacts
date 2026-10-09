# Calculation and dimensional-analysis appendix — Atlas Lattice v0.7

**Status:** NON-CANON · scenario arithmetic only. Use alongside the claim matrix and source receipts. All unresolved values remain unknown.

## A. Calendar-year soybean baseline

NBS 2025 communiqué reports output 20.91 Mt and imports 111.83 Mt. These sum to 132.74 Mt before exports, inventory changes, crush, seed, loss and other flows; they do not directly equal consumption.

Simple gross import share of output-plus-import supply:
111.83 / (111.83 + 20.91) = 84.25%.

This is not a complete self-sufficiency ratio because stocks, exports and use are omitted. The 2025/26 marketing-year estimate of 121.52 Mt consumption and 108 Mt imports has a different period. Do not combine it with calendar-year NBS data.

## B. Intercropping arithmetic (conditional)

Using the reported study input 1.642 t soybean/ha:
- 30 Mha × 1.642 t/ha = 49.26 Mt gross soybean in the modeled intercropped area.
- 44.96 Mha maize area × 1.642 t/ha = 73.82 Mt gross soybean scenario.
- 100.61 Mt simple production gap ÷ 1.642 t/ha = 61.30 Mha.

These are dimensional calculations, not incremental national production. Whether soybean is additional to baseline, what maize yield changes, where the method fits, and the adoption ceiling must be established. The 97% stacked scenario from the DeepSeek note is not accepted as a forecast: it applies overlapping gains without an adoption/interaction model.

## C. Nutritional substitution

For feed, use:
soybean-equivalent avoided = verified soybean-meal reduction × species/feed adoption × protein/energy equivalence ÷ soybean-meal yield per tonne of beans.

A tonne of mycoprotein does not replace a tonne of soybean meal by default. Keep soybean oil co-product demand separate; do not infer seed imports avoided from meal substitution without crush-market and stock accounting. Farm trials and product approvals are species/process specific.

## D. Gas and LNG normalization

NBS 2025 reports natural-gas imports as 127.87 million tonnes. This mass figure cannot be directly divided into biomethane bcm. First establish pipeline/LNG split, gas composition, density, temperature and pressure basis, and lower/heating value. Then compare on both:
1. standardized gas volume (e.g., Nm³ at an explicitly stated reference);
2. energy content (GJ or MWh LHV/HHV).
For like-for-like volume, replacement fraction = delivered qualifying biomethane volume ÷ comparable fossil-gas import volume. For energy, replace numerator/denominator with energy quantities. Capacity, target and output must be distinct.
The official 2019 guideline target >20 bcm/y by 2030 is not current production; NEA reports ~1 bcm/y built biomethane capacity at end-2025. Neither figure establishes utilization or residue availability.

## E. Waste-only allocation and recovery

For a 1,000 dry-tonne synthetic straw lot with 400 t ecological/soil reserve, 200 t current feed obligation, 100 t collection/storage loss:
allocatable = 1,000 − 400 − 200 − 100 = 300 dry t.
Example allocations BIO01 150 t + eligible waste-derived SAF 100 t + other route 50 t = 300 dry t. This is a synthetic conservation fixture only; it does not establish local availability, rights, sustainability, conversion yield, or credits.
Net usable dry matter must be measured after competing uses. Dedicated crop feedstock is excluded from the base case. Do not claim a disposal fee unless contracted and received.

## F. 5% decadal event probability

If probability of at least one event during ten years is 0.05 under a stationary independent-year hazard p:
1 − (1 − p)^10 = 0.05
p = 1 − 0.95^(1/10) = 0.0051162 = 0.51162% per year.

This is not an empirical hazard estimate. It only translates the stated assumption.

## G. GDP stress-scenario arithmetic

At GDP reference $19.5 trillion:
- 0.812% × $19.5T = $158.34B gross loss if that scenario occurs.
- 5% × $19.5T = $975B gross loss if a separate hypothetical scenario occurs.
- If a $975B loss scenario has 5% decadal probability, annualized gross expected loss under the hazard above = $975B × 0.0051162 = about $4.99B/year.
- At 5% annual event probability, expectation = $975B × 0.05 = $48.75B/year.

These do not estimate Atlas-avoided loss. The avoided fraction is null until a sectoral supply-and-recovery model identifies physical coverage, counterfactual and attribution. If the 0.812% modeled result already includes linked sectors, do not add each sector loss again.

## H. Value-added and multiplier arithmetic

Do not report “2x” or “8.01x” as the China net GDP impact of import substitution. Input-output multipliers often measure gross output including intermediate transactions. For an actual project calculate:
- imported expenditure displaced under a stated counterfactual;
- domestic intermediate and imported inputs used by the replacement;
- direct, indirect and induced gross output separately;
- domestic value added net of intermediate purchases;
- opportunity cost of labor, capital and land;
- local household income and distribution;
- transfers/taxes distinctly from social welfare.
Import payments are not all a GDP leakage: domestic shipping, terminals, distribution, taxes and services remain domestic activity.

## I. Sulfur, potassium, sludge ash and cold-energy units

- For gypsum-to-acid, state feed as dry CaSO4-equivalent, conversion and acid output as solution mass and H2SO4-equivalent concentration. The reported 0.4 t/t is a project reference; do not universalize it.
- For potassium, distinguish elemental K, K2O, KCl and brine mass/volume basis. Struvite is not KCl. Crop-residue K returned to soil remains a competing use.
- For sludge/ash, constituent input = qualified product + captured residual + emissions + documented unaccounted fraction, each on an agreed basis. Leaching and durability gates are required; immobilization is not destruction.
- Qingdao cold-energy project: 26 GWh/y projected power generation; 8 GWh/y avoided cooling electricity. They are not both generation.

## Source receipts

NBS: https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html  
NDRC biomethane guideline: https://www.ndrc.gov.cn/xxgk/jd/jd/201912/t20191219_1213778.html  
NEA 2026 green-fuel report: https://www.nea.gov.cn/20260805/96c7a438f9544f349d189d2ef4547eab/c.html  
IEA biomethane cost/feedstock assessment: https://www.iea.org/reports/outlook-for-biogas-and-biomethane/assessing-the-sustainable-potential-and-cost-of-feedstocks-for-biogas-and-biomethane  
Cold-energy source: https://www.xihaian.gov.cn/ywdt/tsxq/202606/t20260603_10624706.shtml  
Sludge studies: https://www.sciencedirect.com/science/article/pii/S0950061825012504 ; https://www.sciencedirect.com/science/article/pii/S2352710226014105
