# Solbrain Hydration — 2026-10-10
NON-CANON · DRAFT · ZERO REALIZED CREDIT

## Essential context
The arbitrary 1.21 GW Back to the Future joke prompted hypothetical four-hour BESS study (4.84 GWh output) but no actual plant sizing. The project evolved toward a 168-hour essential-service islanded resilience target, with conditional longer sustained supply through replenishing solar, wind and qualified hydro, plus restoration of emergency reserve between disasters.

Lahaina user testimony: TWO networked solar-battery installations powered selected emergency fridges, Wi-Fi, phones and coordination during the 2023 fire response. Solar replenished batteries continuously for several weeks while user was present; user says operation continued until external grid restoration. The equipment was operationally grid-independent then, but shared electrical intertie/topology and exact outputs unknown. Washington Post confirmed separate Paul Romero and Kasidee Rose emergency fuel and shelter relief; photographs did not verify electrical design. https://www.washingtonpost.com/nation/2023/08/12/maui-fire-death-toll-lahaina-hawaii-damage/ .

## Numbers and guardrails
1.21GW x 4h=4.84GWh; 365 full daily cycles=1.7666TWh/year discharge; 90% roundtrip =>1.9629TWh charge and 196.3GWh losses. E02 is 26GWh/y projected generation PLUS 8GWh/y avoided cooling electricity: 34GWh/y combined projected benefit, NOT 34GW cooling. Compute baseline 40MW IT/PUE1.25=50MW facility; 50MW x96h=4.8GWh before margins. For protected 10MW, 168h battery-only =1.68GWh; 4 full-sun hours and 0.85 derating imply 70.6MWp nominal PV average-day equivalence, NOT seven-day firm supply.

Shandong Oct 2026 applicable eligible-component TOU: deep valley 11–14 0.1x, other valley 09–11 and 14–15 0.3x, critical peak 17–20 2x, ordinary peak 16–17 and 20–22 1.7x. 5.378GWh charging at 1.21GW takes 4.44h; three deep valley hours insufficient. Gross arbitrage = discharge electricity times peak price MINUS charging electricity times charging price, once. Illustrative $0.13 and $0.045/kWh imply $0.085 spread and ~$141.3m annual gross before costs, NOT profit. Reference https://fgw.weihai.gov.cn/art/2026/9/16/art_53887_6617746.html .

China MEM survey covers six groups/23 disaster types, >1.7 billion risk records and 2846 counties; precise GIS publication/rights differ. https://www.mem.gov.cn/xw/xwfbh/2024n05y08rxwfbh/wzsl_4260/202405/t20240508_487313.shtml . Dongjiakou EIA extreme DESIGN water level 5.91m is referenced to local THEORETICAL LOWEST TIDAL DATUM, not mean sea level nor measured surge: https://www.mee.gov.cn/ywdt/gsgg/gongshi/wqgs_1/201808/W020180824572868425776.pdf . Qingdao published 0.98 coastal risk index refers to Dagu River estuary, NOT necessarily Dongjiakou. DeepSeek site seismic 0.10g/VII/0.45s, geology and hazard counts require original site citations.

## Durable pointers
GitHub draft PR https://github.com/atlaslattice/manus-artifacts/pull/285 ; Maui companion https://app.notion.com/p/3f50c1de73d981c69ee2f4ab2a395497 ; Maui wastewater/reef https://app.notion.com/p/3f40c1de73d98134b47cf2e2a7b74018 ; Maui parent https://app.notion.com/p/3f40c1de73d98122b22bc46b43f8bdb2 .

## Handoff
RES01–RES06 capability and human coordination, RES07 replenishing islanded energy/SoC, RES08 hazards and common-cause failures. Compare 1-site, 2 shared-bus, two intertie and independent nodes; 96/168/336h plus 30d synthetic scenarios, recovery under repeated disruptions. Preserve exact source and scope, don't fabricate local generation or save realized credit. PR remains draft/unmerged; do not overwrite.