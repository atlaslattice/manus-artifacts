# DragonSeek 2.0 / DJK-001 — DeepSeek v0.8 Review and Measurement-Semantics Deltas
**2026-10-11 China time · Research-only · NON-CANON · NO SITE ACCESS · ZERO REALIZED CREDIT · No government endorsement · No GitHub CI claims**

## Source receipt and duplicate detection
The two user-uploaded DeepSeek Markdown copies, `Pasted markdown(20261011-033641).md` and `Pasted markdown (2)(20261011-033655).md`, have **identical SHA-256**: `aa1ec1325a269107aae17ec349c09bec126868c4f94ba541de8efaf95f79df2d`. They represent **one review**, not two independent reviewers.
The 2025 Dongjiakou Chemical Park monitoring DOCX SHA-256 has been rechecked against the received bytes: `d92d82b7dd0111b01751a3f495cc26c57a51dcf8ae47b2c181243f2d1d6819e5`. It is a 5-page *summary* (cover + four content pages), not raw laboratory records. No promotion from REPORTED_SUMMARY to MEASURED_RAW.

## DeepSeek response: accepted conclusions
- The corrected **422.7 万吨 = 4,227,000,000 kg** is accepted. DeepSeek acknowledged its earlier JSON's 1,000× understatement.
- Preferred semantics: **C for governance** (industry-specific federated contracts with local autonomy), **A for scientific computation** (SI with dimensional guardrails), practical **B where domain engineering units are natural for operators**. Chinese-source original value/alias/basis and its source must remain immutable.
- UCUM can provide unit-code syntax; Chinese aliases (wan_t, yi_m3, mu, etc.) require explicit namespaced, versioned recipes. SI alone is insufficient for pH, dB(A), pressure datum, isotope reference, energy quality, gas reference conditions or geographic/temporal basis.
- Three independent axes: `source_evidence_class`, `transformation_class`, and `verification_state`; also distinguish MEASURED_RAW, MEASURED_REPORTED and OPERATOR_ENTERED. A unit conversion must never upgrade observation verification.
- Censored values such as `活性磷酸盐 <0.004 mg/L` have **canonical value:null**, `relation:CENSORED_LEFT`, and `limit:0.000004 kg/m³`. Do not store the converted LOD as an observed concentration or as zero.
- Explicit wet/dry transformations, mass/volumetric ratio type, energy quality, operating-hours basis, absolute/gauge pressure, vertical/tidal datums and local time. Unknown basis remains UNKNOWN.
- DeepSeek listed gaps in the earlier 25 tests: angular vectors, time totals vs rates, dry/wet and isotope reference, ΔT offset, ΔP, real/nominal CNY, estimator types, weighted time aggregation, and spatial boundary de-duplication.

## New issue independently identified: at least two tce accounting conventions
The v0.7 prototype uses **29,307,000,000 J/tce** as a fixed recipe; DeepSeek recommends **29,307,600,000 J/tce** citing GB/T2589-2020 and engineering calorific conversion. The Chinese **National Bureau of Statistics Energy Statistics Department** specifies **29,271,200,000 J/tce** for current statistical reporting (2022-09-29 public reply). Therefore:
1. Never silently use a universal tce energy equivalent in cross-domain federation.
2. Require an explicit `accounting_policy`, effective reporting period, source standard, and whether the value is an accounting energy equivalent or measured physical energy.
3. In v0.8 *research prototype*, `GB_T_2589_2020_ENGINEERING` maps to 29,307,600,000 J/tce and `NBS_2022_ENERGY_STATISTICS` maps to 29,271,200,000 J/tce. Choice must be made by competent domain owner, not guessed. Historic v0.7 remains unchanged, with the old factor deprecated for new calculations.
4. The difference is **36.4 MJ/tce** (~0.1243% of NBS convention). This is an accounting basis discrepancy, not evidence that measured calorific content differs.

**Primary-source documents**
- Current GB/T 2589-2020 listing: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=53D1440B68E6D50B8BA0CCAB619B6B3E
- MEE steel-sector GHG reporting guide: https://www.mee.gov.cn/xxgk2018/xxgk/xxgk06/202501/W020250124388842647934.pdf (footnote: 1 kgce=29,307.6 kJ)
- National Bureau of Statistics response: https://www.stats.gov.cn/WZWSREL2hkL2x5engvenhnay8yMDIzMDIvdDIwMjMwMjE1XzE5MDU0NDkuaHRtbA%3D%3D (energy-statistics reporting 1 kgce=29,271.2 kJ)

## Research prototype: local-only test receipt
A separate **v0.8 additive local source/bundle** was prepared during the DeepSeek review:
- `semantic_contract_v08.py` uses existing v0.7 without overwriting it.
- `tests/test_semantic_contract_v08.py` adds 55 tests.
- **55/55 v0.8 local pass + 25/25 v0.7 local pass = 80/80 local pass**.
- The local bundle also includes DeepSeek's exact original review, rechecked Dongjiakou DOCX, v0.7 JSONL monitoring register, and local test log.
- This PR documents the review. **The full local prototype is not attached as source to this PR and is NOT CI verified.** Downloadable ZIP is supplied independently in the associated ChatGPT handoff (no fake GitHub paths).
- The v0.8 guards are candidate logic, not calibrated metrology, audited spatial topology, certified energy reporting or industrial controls; scope-overlap checker is a source-receipt gate, not a GIS proof.

## Environmental evidence unchanged
Official 2025 report describes park WWTP-treated wastewater to deep-sea offshore route (document-reported), but does **NOT** establish desalination brine discharge volume, chemistry, compliance or pipe identity. Ambient seawater 12 points / one event, groundwater 15 points / three seasons, Henghe surface water 3 points / eight events, acoustics 9 points / two events. Data class is REPORTED_SUMMARY with actual report original retained. Groundwater chloride **and other** short exceedances lack quantified magnitude or causal attribution.

## Questions for next DeepSeek review (draft, not sent)
1. Explicit standards to resolve engineering vs NBS statistical coal equivalents and whether different agencies require different reporting versions.
2. How to classify source-reported '< detection limit' where formal LOD/LOQ/MDL method metadata is absent.
3. UCUM vs domain-specific Chinese aliases, including ownership/versioning and machine schema codes; mu=2000/3 m², 万吨=10^7 kg, 亿m³=10^8 m³.
4. Reject default gas reference O₂ percentages from uncited examples: determine only from source-specific Chinese GB/HJ/permit and combustion type.
5. Recommend actual GIS polygon topology validation, weighted space/time aggregation, uncertainty propagation and adversarial counterexamples.
6. Refine three-axis evidence state transitions: require calibration records and sampling protocols before MEASURED_RAW verification.

**No government/company data requests sent. No production action. No PR merged.**
