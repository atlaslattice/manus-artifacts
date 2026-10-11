# DragonSeek 1.1 · Tidal Lantern / Indra's Net review package

Research prototype only: **read-only, synthetic events, no official China weather feed, no actual live seismic/NEO/orbit/aviation/epidemic warning, no industrial/CII access**. It does not make operational collision avoidance or public-health decisions.

## Open the prototype

- Double-click `dashboard/dragonseek_1_1_standalone.html` to open a **self-contained offline** interactive China+oceans research map.
- Or open `dashboard/index.html` with the accompanying `app_v11.js` and `china_oceans_basemap.png` in the same directory.
- Visible exercises: 10 approximate city-level research anchors, 15 synthetic regional Earth/atmosphere hazard events, 2 synthetic orbital/NEO informational cards; 46 source candidates, none connected at baseline.
- In the viewer, click a node or event to examine classification, provenance, source owner, scope, offset-aware time, declared EPSG:4326 and authorization state. Enable cultural sky label overlay for educational terminology (not medical/scientific inference).
- The button “Fetch public weather” can optionally request a small number of *public Open-Meteo model-derived city-grid values*, when internet access and noncommercial usage terms permit. The map otherwise stays fully functional offline and labeled DEMO. This is not the public Chinese meteorological service nor an emergency alert.
- `Feed health` explicitly shows all future sources not connected and distinguishes unknown/stale public weather.
- `RES07` compares `storage-only` and `solar replenishment` for the **same load, usable battery and initial SoC**. The defaults are deliberately *failing*: 17 vs 24 fully served hours out of 168. The 12h sine irradiance is **not** a weather forecast or PV design.

## Run the Python software tests

```bash
cd dragonseek_1_1
python -m unittest discover -s tests -v
node --check dashboard/app_v11.js
```

Tests are local structural and synthetic behavioral tests, not a compliance certificate or GitHub Actions workflow. As of artifact preparation: **55/55 Python tests PASS**, the JS syntax check passes and an independent Node evaluation confirmed 17 vs 24 hours. Browser acceptance tests were *attempted*, but Chromium was missing; the mobile map fix is not browser visually certified.

## Core files

- `engine/dragonseek_v11.py`: authorization record/registry and research-only event release checks; freshness logic; physically limited *screening* battery model. Trust roots are mock-configurable in unit tests only, not real signature/identity validation.
- `dashboard/index.html`, `dashboard/app_v11.js`, `dashboard/china_oceans_basemap.png`: editable HTML/JS/map source.
- `dashboard/dragonseek_1_1_standalone.html`: offline all-in-one HTML and embedded map.
- `evidence/planetary_data_adapter_inventory_v11.json`: **46** candidate research sources with `runtime_connection_state=NOT_CONNECTED` on all entries. Includes China weather/ocean, public orbital/NEO, seismic, geomagnetism, locust, wastewater public health, international program stubs.
- `evidence/demo_events_v11.json`: synthetic Earth hazard events with data_owner, explicit classification, provenance, jurisdiction and timezone.
- `evidence/demo_celestial_v11.json`: celestial events never assigned Earth lat/lon coordinates.
- `docs/DRAGONSEEK_V1_1_INDRA_PLANETARY_MULTIDOMAIN_REVIEW_ZH.md`: detailed Mandarin standards, source and scope handoff, including DeepSeek 1.0 code review response.
- `tests/test_dragonseek_v11.py`, `tests/test_research_artifacts.py`: 55 checks.

## Source boundaries / important disclaimers

- This public viewer does not represent Chinese government or CAC endorsement, official aviation traffic control, satellite conjunction decisions, NEO impact warnings or authoritative earthquake alerts.
- The local research-only `AuthorizationRegistry` verifies **configured** trusted issuers/document digests, not actual PKI signatures, jurisdictional privacy compliance or authoritative important-data determinations. No actual data release permission is created.
- Public model availability is subject to supplier licensing, rate limiting and data sovereignty; NASA/JPL SSD API forbids direct embedded browser uses. No APIs are embedded for CNEOS, CelesTrak, CENC, CAAC, FAO, ChinaCDC or Chinese weather authorities.
- Twice-weekly wastewater tests are **a proposed public-health program objective**, not a claim of routine nationwide deployment or an instruction to work on pathogens; analytical and public health activities must be undertaken by authorized professionals.
- China-involved global project overlays are conceptual, and the Africa agricultural locust example is hypothetical only. No real investment or project risk is asserted.
- Five element/five phase and 24 solar terms labels are a cultural/educational optional overlay only and not claimed to diagnose or predict disease, earthquakes, weather or asteroid impacts.

## Prior work

Full v1.0 research doc: https://docs.google.com/document/d/1RaEfe7RI_YhwTbU_z1Bl1KGdtgjy5O9Tc7t2RroylcY/edit
v1.0 draft GitHub PR #298: https://github.com/atlaslattice/manus-artifacts/pull/298
All historical source documents preserved; the included `prior-v1.0-bundle.zip` is the preceding version, not a replacement.

## Archive links added on 2026-10-11

- v1.1 downloadable ZIP: https://drive.google.com/file/d/1tBWgmbuyix1fUn5WMWCYGiJ64NRKcvM-/view
- New draft branch: https://github.com/atlaslattice/manus-artifacts/tree/research/dragonseek-v11-indra-space-seismic-biowatch-20261011
- Review note: GH Actions CI and browser/mobile screenshot validation are not confirmed.
