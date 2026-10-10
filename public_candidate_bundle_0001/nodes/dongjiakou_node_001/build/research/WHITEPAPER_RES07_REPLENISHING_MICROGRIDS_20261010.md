# RES07 White Paper — Networked Replenishing Microgrids for Sustained Service
NON-CANON · DESIGN RESEARCH · ZERO REALIZED CREDIT

## Thesis
Resilience should be measured as preserved human and community capability, not battery nameplate. User-reported Lahaina experience describes two networked island-capable solar+battery installations replenishing continuously and supplying limited fridges, WiFi and phone charging for weeks. The engineering question is how to provide seven days of critical service under a specified shock and conditionally longer service as generation replenishes reserves.

## Three regimes and recovery
Normal: economic grid flexibility and protected readiness. Adverse: low-solar/wind 3–10 day sequences with SOC and changing critical-load priorities. Catastrophic: combined energy, roads, communications and water failure over weeks. Repeat-event regime: quantify time required to restore designated 50/80/100% reserves before another shock.

## Energy accounting and practical limits
At each hour, direct local generation, loads, storage charge/discharge, grid imports and losses are separate. Storage cannot create energy. 10MW protected load=240MWh/day; 168h without generation requires 1680MWh before margins; solar 70.6MWp at 4 equivalent sun-hours and 0.85 net derating covers average daily energy only, NOT dark-storm endurance. PV may be damaged by wildfire/storm; wind shutdown and widespread low wind occur; hydro requires established flow, head, permissions and ecological protection.

## Topology and controls
Compare one central PV+BESS, dual shared-bus, dual isolated-island with protected intertie, and independent island microgrids. Control-only networking differs from electrical sharing. Validate inverter, anti-islanding, grid-forming, blackstart, protection, safety and N-1 prior to claiming redundancy. Physical emergency outlets must be certified, clear and accessible. Critical loads include life safety, sanitation, communications, medical refrigeration, water, essential compute and coordination; industrial shutoff must be process safe. Offline operation and human triage should not rely on cloud AI.

## Simulator interface
REGION_PROFILE/ASSET_GRAPH/ENERGY_RESOURCE/SERVICE_CLASS/FAILURE_SCENARIO/RECOVERY_PLAN with source, date, geography, units and license per measurement. RES01 duration, RES02 protected MW, RES03 restoration curve, RES04 surrounding facilities served, RES05 readiness costs, RES06 human logistics, RES07 SOC/replenishment and reserve-restoration time. Scenario test durations 24/48/96/168/336h plus 30d, 0/1/2 cluster failure and coincident weather. Track unserved essential MWh and service-hours, not fabricated risk-adjusted value.

## Scope
A seven-day target is a proposed engineering benchmark, not proven site endurance. No finite renewable/battery system can promise indefinite autonomy through arbitrarily long loss of generation. Actual Maui installation sizing and topology unknown. Follow site-specific engineering review and community requirements before any installation. Historic press documentation: https://www.washingtonpost.com/nation/interactive/2023/photos-hawaii-wildfires-recovery/ ; community testimony remains separately classified.