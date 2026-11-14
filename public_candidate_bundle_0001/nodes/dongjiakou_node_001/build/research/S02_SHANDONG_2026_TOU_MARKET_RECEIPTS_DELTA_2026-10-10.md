# Dongjiakou S02 — 2026 Shandong tariff and storage-market receipt delta

**Date:** 2026-10-10  
**Status:** EXTERNAL_POLICY_RECEIPTS · MODEL CORRECTIONS · NON-CANON · ZERO REALIZED CREDIT  
**Related:** S02/C01 circular BESS white paper v0.1 in draft PR #285. This note is additive; it does not modify the existing baseline, dispatch solver, source manifest, or cost ledger.

## Newly located primary government receipts

1. **Shandong revised 2026 time-of-use bands, effective October 1, 2026** — Weihai Municipal DRC September 16, 2026, citing Shandong DRC letter 鲁发改价格函〔2026〕68号: https://fgw.weihai.gov.cn/art/2026/9/16/art_53887_6617746.html
2. **Official scope and rationale** — Weihai DRC June 22, 2026: https://fgw.weihai.gov.cn/art/2026/6/22/art_53888_6433489.html . Older June explainer predates the October 1 period changes; prefer newer bands.
3. **2026 Shandong Electricity Market Rules, April revision, regulator explanation** — National Energy Administration Shandong Regional Office: https://sdb.nea.gov.cn/xxgk/zcjd/202605/t20260508_300825.html

## Verified tariff band POLICY (not a delivered Dongjiakou tariff)

Eligible components (including procurement for grid-agent customers and specified system/loss/capacity components) apply time multipliers:
- sharp peak / 尖峰: **+100%**, multiplier **2.0**;
- peak / 高峰: **+70%**, multiplier **1.7**;
- valley / 低谷: **−70%**, multiplier **0.3**;
- deep valley / 深谷: **−90%**, multiplier **0.1**;
- normal / 平段: **1.0**.

Not every tariff component is TOU-adjusted and direct-market participants face different procurement/settlement arrangements. These multipliers must not be applied to a universal retail bill or presented as guaranteed market price spreads.

**September–November revised schedule effective 2026-10-01:** valley 09:00–15:00 including deep valley 11:00–14:00; peak 16:00–22:00 including sharp peak 17:00–20:00. Detailed nonoverlapping periods:
- ordinary valley 09:00–11:00 and 14:00–15:00;
- deep valley 11:00–14:00;
- ordinary peak 16:00–17:00 and 20:00–22:00;
- sharp peak 17:00–20:00.
Hour 15:00–16:00 normal. Market prices, transmission/settlement, exact meter tariff, BESS eligibility, availability, interconnection, and daily power remain unknown.

**A four-hour 1.21 GW discharge requires four hours at output rating; three hours of the critical peak band alone cannot exhaust all energy at the critical-peak price.** **Recharging 4.84 GWh delivered at 90% round-trip efficiency requires ~5.378 GWh input, or >4.44 h at a 1.21 GW charge limit**; the 11:00–14:00 deep valley lasts only **3 hours**. Thus full-cycle charging at the deep-valley rate alone is **infeasible** for that symmetric-rate case; a mixed valley/normal tariff schedule is necessary or larger charging power with engineering checks. Grid connection/inverter rating remains unverified.

## Storage market access — meaningful partial answer

The NEA Shandong regulator's April-2026 revision commentary reports:
- qualifying **new-type storage** must have at least **2 hours continuous charge/discharge capability** for the energy market;
- at least **15 minutes** for ancillary services;
- simultaneous energy/ancillary participation, or daily selection of either, is supported under specified operating/SoC rules.

Thus a hypothetical four-hour battery passes the *duration* thresholds but has **no established facility-specific registration, technical clearance, bidding permissions, or revenues**. Mark regulatory framework **REPORTED**, project eligibility **UNKNOWN**.

## Arithmetic correction: arbitrage value

Do not subtract charging cost twice. Correct gross monetary dispatch contribution (same price/energy units):

`GROSS = E_out * P_sell_or_avoided_peak - E_in * P_buy_valley`

`E_in = E_out / eta`.

For 1.7666 TWh/year of discharge and 90% efficiency, E_in=1.96289 TWh/year. A strictly **illustrative**, not Shandong-verified tariff assumption `P_peak=$0.13/kWh`, `P_valley=$0.045/kWh` produces **$229.658m** peak value minus **$88.330m** charging purchases = **$141.328m/year gross contribution**. If one *also* invents `$20m/year` incremental O&M/other cost not already embedded in a levelized benchmark, result is ~$121.3m/year before capital recovery and other omitted costs: **not net profit**.

These two prices imply a peak–valley **spread of $0.085/kWh**, not $0.13/kWh. They do not directly demonstrate a **¥0.9/kWh** spread. Currency conversion assumptions were not verified, and a stated currency spread must be converted consistently.

The Wood Mackenzie **$58/MWh modeled storage LCOE** is an **annualized lifecycle service benchmark with its own system boundary**, not an incremental expense automatically subtractable in addition to unspecified full lifecycle costs. Compare price scenarios under transparent LCOS inclusion assumptions to avoid duplicate charging/degradation/O&M/financing. If `P_peak-P_valley` is already used, losses must be accounted explicitly: gross per delivered kWh = `spread - P_valley*(1/eta-1)`.

## Grid and carbon distinctions

Tianwan (Jiangsu) and Dongjiakou (Shandong) do not share an established direct supply contract, grid allocation, delivery route, marginal carbon factor or hourly interprovincial dispatch data. Avoid claiming Tianwan **necessarily lowers Dongjiakou marginal carbon intensity**; induced dispatch may depend on regional/cross-regional transfers, constraints and the hour. Local node benefit remains UNKNOWN.

Interconnection of **1.21 GW** charging and discharging at a specific Dongjiakou point of connection remains UNKNOWN even though local high-voltage transmission infrastructure may exist. Such a plant would require dedicated engineering, grid impact study, protection and market approval.

## Four prospective modeled use cases

A. Direct grid supply, baseline compute and water schedules.  
B. Flexibly scheduled compute/water loads without battery.  
C. Battery with fixed loads, bounded 2026 tariff eligibility.  
D. Battery + deferrable compute + water/thermal flexibility, while maintaining independent electrical and cooling flows.

Never assume electrolysis installed if unverified. Model individual constraints and water service priority. Add *physical benefit* only under measured node resource/time constraints. Keep **S02 baseline energy, carbon and revenue credits at zero**.

**KEEPER:** Shandong TOU **hours and component multipliers are now policy-known**, not entirely unknown. The **actual bankable tariff and 1.21 GW interconnection** are still unknown. The April 2026 Shandong market rules establish energy/ancillary duration thresholds without confirming facility admission. Corrected price arithmetic prevents double counting and turns the 1.21 GW DeLorean scenario into a disciplined external sensitivity.
