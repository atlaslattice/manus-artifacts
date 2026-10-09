# 2026-10-09 — DeepSeek HCl spot-price discovery: corrected 31%-solution unit basis
**Status: researched price observations plus non-canon synthetic economics. ZERO REALIZED CREDIT.** This is an additive correction to existing [DJK draft PR #282](https://github.com/atlaslattice/manus-artifacts/pull/282). No delivered offer or Dongjiakou operating baseline verified.
## Quote checks
- [Tonghuashun iFind Oct 9](https://goodsfu.10jqka.com.cn/20261009/c680530339.shtml): national HCl spot **¥195/metric tonne**, but the short item does NOT clearly specify delivered concentration/grade, so match specifications before treating as 31%.
- [Shengyishe Oct 8](https://www.jh1958.com/qb/list-819-1.html): Dongming Petrochemical **31% HCl ¥250/t** in Shandong; more reliable 31% same-unit comparator.
- [Longzhong Oct 8 excerpts](https://m.mysteel.com/hot/1645018.html): Shandong Jinling high-purity ¥240/t, some byproduct HCl ¥40–50/t; composition, availability, transport and contaminant load differ.
- [China government commodity statistics June 2026](https://www.chinaprice.cn/jsdzqk/60873.jhtml): HCl defined as **31% synthetic acid**; distinguishes solution grade.
**Error in DeepSeek's apparent uplift:** prior model required **46,512.94 t/y pure HCl stoichiometric equivalent**, whereas HCl Chinese spot quotes are usually aqueous product **31% concentration by mass**, thus **150,041.74 tonnes of 31% commercial solution** is needed before side reactions. Charging 46,513 tonnes at ¥195/t commercial solution underprices reagent by **3.2258×**.
## Corrected base sensitivity; illustrative acid value 28,552.79 t/y × ¥1,500/t = ¥42.829m/y
| HCl price ¥/t commercial 31% solution | Annual HCl solution cost ¥m | Gross contribution acid value minus HCl cost ¥m |
|---:|---:|---:|
| 110 | 16.505 | +26.325 |
| 135 | 20.256 | +22.574 |
| 160 | 24.007 | +18.823 |
| 195 | 29.258 | +13.571 |
| 250 | 37.510 | +5.319 |
| 400 | 60.017 | −17.188 |
Pure-HCl stoichiometric 46.513kt/y; aqueous 31% = **150.042kt/y**. **Upper bound pre-other-cost break-even 31% HCl at ~¥285.45/t**, with every yuan/t of delivery or other variable handling lowering threshold. Full value chain CAPEX/processing/transport/conversion/emissions/dilution/salts mother liquor may eliminate positive operating contribution.
## Key physical and commercial uncertainties
- Chemical speciation and supersaturation: soluble CaCl2 (from acid-dissolved shells) mixed with sulfate-rich brine must actually precipitate recoverable CaSO4 at scale. Published shell-driven *flue-gas desulfurization* precedent does not validate CaCl2+SWRO-brine gypsum precipitation.
- 150kt/year dilute acid solution carries approximately **103.5kt/y water**, important for tankers, pumping, storage, brine-volume and ZLD duties; chemical purity and handling are critical. HCl is NOT automatically cost-free if called a byproduct; qualified supply chain and delivered at-cost invoices needed. Unqualified raw waste acids may carry solvent, organics, metals and other impurities.
- Shell annual volume assumption 96kt from older Qingdao oyster figures is unverified as accessible waste in 2026. Verify real operators, seasonal supply and present offtake. Acid conversion 0.40t/t dry gypsum is not confirmed for this product. Sulfur equivalent is not recognized import displacement.
- **Previous v0.4 sulfuric-acid-control undercounts purchased H2SO4** because it charges only captured gypsum rather than activated CaCO3; fix before using this comparator financially; the sulfur source is acid, NOT brine in this control.
- No internal at-cost invoice, physical receipt, agriculture diversion, asset commissioning or national self-sufficiency credit verified. Proposed status `TESTABLE_PENDING_ASSAYS_AND_CONTRACTS`, not financially positive or deployed.
