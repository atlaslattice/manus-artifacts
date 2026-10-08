STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Run 6 — Resource Modules (one at a time)

**Artifact ID:** `DJK-NODE-001-RUN-6-RESOURCES-v0.1`
**Status:** EXECUTED_PARAMETRIC_TRANSFER_FUNCTION_NON_CANON
**Study classification:** TECHNICAL_FEASIBILITY_PLUS_CONDITIONAL_ECONOMICS

> Every resource module needs yield, selectivity, energy, reagents, material life, residual fate, market ceiling and ecology before earning value.

## Summary

| Field | Value |
| --- | --- |
| Modules instantiated | 4 |
| Modules eligible for value | **0** |
| Total value credit | **0** |
| Reason | No module has a receipt for any of the eight required questions. |

## The eight required questions

| Question | Requirement | Veto-bearing |
| --- | --- | --- |
| `yield` | Measured recovered quantity per unit of brine processed, at this site. | no |
| `selectivity` | Measured separation factor against the dominant competing ions (Na, Mg, Ca, K, Cl, sulfate). | no |
| `energy` | Measured net energy per unit of recovered product, including pumping, regeneration and thermal duty. | no |
| `reagents` | Measured reagent consumption and its own supply chain, cost and residuals. | no |
| `material_life` | Measured sorbent, membrane or electrode cycle life and replacement interval. | no |
| `residual_fate` | Where the spent brine, eluate, reagent and exhausted material actually go, with a receipt. | **YES** |
| `market_ceiling` | Contracted or exchange-published offtake for the actual product grade, not a commodity headline price. | no |
| `ecology` | Receiving-water and ecological status under INV-19. This one is a veto, not a score. | **YES** |

## Modules

### R01-Li@0.45

_RESOURCE_INVENTORY_NOT_RECOVERY_YIELD_

| Quantity | Value |
| --- | --- |
| `concentration_factor_brine_to_feed` | 1.8181818181818181 |
| `brine_volume_m3_year` | 21914444.444444444 |
| `brine_li_mg_l` | 0.3090909090909091 |
| `li_in_feed_t_year` | 6.773555555555555 |
| `li_in_brine_t_year` | 6.773555555555555 |
| `li_in_product_t_year` | 0.0 |
| `fraction_li_to_product_assumed` | 0.0 |
| `nf_brine_enrichment_reference` | 10.0 |
| `brine_li_mg_l_after_nf_reference` | 1.7000000000000002 |

- Receipted: **0 / 8**
- Eligible for value: **False**
- Value credit: **0**

**Finding.** Lithium is genuinely concentrated by the desalination step, by the brine concentration factor. The inventory is therefore larger in the brine than in the feed, and a downstream nanofiltration step is reported to enrich it roughly tenfold further. This makes lithium a concentration-and-selectivity problem, which is the favourable case.

**Not claimed:**

- No recovered lithium quantity.
- No revenue, because no offtake grade or price is contracted.
- No reduction in terrestrial lithium mining. That remains a POTENTIAL_DISPLACEMENT_HYPOTHESIS until yield, selectivity, energy, reagents, material life, markets, economics and ecology all close.

### R01-D@0.45

_RESOURCE_INVENTORY_NOT_RECOVERY_YIELD_

| Quantity | Value |
| --- | --- |
| `deuterium_mass_fraction_in_water` | 3.4881932190227415e-05 |
| `deuterium_ppm_by_mass_of_water` | 34.88193219022742 |
| `isotopic_enrichment_factor_by_RO` | 1.0 |
| `d_in_feed_t_year` | 1389.8512092683943 |
| `d_in_brine_t_year` | 764.418165097617 |
| `brine_volume_m3_year` | 21914444.444444444 |
| `d_in_product_t_year` | 625.4330441707773 |
| `note_d_is_not_lost` | Deuterium leaving with the product water is not a loss; it is a different stream. The point is that no stream is enriched. |

- Receipted: **0 / 8**
- Eligible for value: **False**
- Value credit: **0**

**Finding.** Deuterium is abundant in mass and essentially absent as a concentration gradient. Every tonne of water at this site carries roughly the same deuterium fraction as the ocean, and the desalination step does not change it. The constraint is therefore isotopic separation energy, not resource availability and not brine concentration. This lane is architecturally unlike the lithium lane and must not be modelled as though a brine stream were an ore body.

**Architecture consequence.** A deuterium lane should not be sited to exploit brine concentration, because there is none to exploit. If pursued, it is a heavy-water separation plant that happens to be co-located with a desalination plant, and it must be justified on separation energy and heat integration, not on feed enrichment.

**Not claimed:**

- No heavy-water production rate.
- No separation energy figure, because no process route is selected or measured.
- No linkage to the deuteron spin ergotropy question, which is a separate and independent baseline test with its own result: thermal ergotropy is zero at 1 T / 300 K.

### R01-Li@0.50

_RESOURCE_INVENTORY_NOT_RECOVERY_YIELD_

| Quantity | Value |
| --- | --- |
| `concentration_factor_brine_to_feed` | 2.0 |
| `brine_volume_m3_year` | 17930000.0 |
| `brine_li_mg_l` | 0.34 |
| `li_in_feed_t_year` | 6.0962 |
| `li_in_brine_t_year` | 6.0962 |
| `li_in_product_t_year` | 0.0 |
| `fraction_li_to_product_assumed` | 0.0 |
| `nf_brine_enrichment_reference` | 10.0 |
| `brine_li_mg_l_after_nf_reference` | 1.7000000000000002 |

- Receipted: **0 / 8**
- Eligible for value: **False**
- Value credit: **0**

**Finding.** Lithium is genuinely concentrated by the desalination step, by the brine concentration factor. The inventory is therefore larger in the brine than in the feed, and a downstream nanofiltration step is reported to enrich it roughly tenfold further. This makes lithium a concentration-and-selectivity problem, which is the favourable case.

**Not claimed:**

- No recovered lithium quantity.
- No revenue, because no offtake grade or price is contracted.
- No reduction in terrestrial lithium mining. That remains a POTENTIAL_DISPLACEMENT_HYPOTHESIS until yield, selectivity, energy, reagents, material life, markets, economics and ecology all close.

### R01-D@0.50

_RESOURCE_INVENTORY_NOT_RECOVERY_YIELD_

| Quantity | Value |
| --- | --- |
| `deuterium_mass_fraction_in_water` | 3.4881932190227415e-05 |
| `deuterium_ppm_by_mass_of_water` | 34.88193219022742 |
| `isotopic_enrichment_factor_by_RO` | 1.0 |
| `d_in_feed_t_year` | 1250.866088341555 |
| `d_in_brine_t_year` | 625.4330441707775 |
| `brine_volume_m3_year` | 17930000.0 |
| `d_in_product_t_year` | 625.4330441707775 |
| `note_d_is_not_lost` | Deuterium leaving with the product water is not a loss; it is a different stream. The point is that no stream is enriched. |

- Receipted: **0 / 8**
- Eligible for value: **False**
- Value credit: **0**

**Finding.** Deuterium is abundant in mass and essentially absent as a concentration gradient. Every tonne of water at this site carries roughly the same deuterium fraction as the ocean, and the desalination step does not change it. The constraint is therefore isotopic separation energy, not resource availability and not brine concentration. This lane is architecturally unlike the lithium lane and must not be modelled as though a brine stream were an ore body.

**Architecture consequence.** A deuterium lane should not be sited to exploit brine concentration, because there is none to exploit. If pursued, it is a heavy-water separation plant that happens to be co-located with a desalination plant, and it must be justified on separation energy and heat integration, not on feed enrichment.

**Not claimed:**

- No heavy-water production rate.
- No separation energy figure, because no process route is selected or measured.
- No linkage to the deuteron spin ergotropy question, which is a separate and independent baseline test with its own result: thermal ergotropy is zero at 1 T / 300 K.

## Sequencing

Modules are evaluated one at a time. Stacking survivors is Run 7 and requires sequence-dependent interference edges, which cannot exist before individual modules have measured receipts.

## Unresolved

- Site lithium assay in feed, product and brine.
- Site deuterium assay in feed, product and brine, to test the no-enrichment assumption rather than assert it.
- Any sorbent, membrane or electrode performance at this brine chemistry.
- Receiving-water and ecological status under INV-19.
