# DragonSeek 1.2 — Runnable USGS Connector and Feed Health Demo
Date: 2026-10-11 · Status: EXPERIMENTAL / NON-CANON / READ-ONLY
DeepSeek contribution: COLLABORATOR_REPORTED. Public-data fetch concept adapted from collaborator-supplied code; no claimed state/government sponsorship.

## Launch
In the repository checkout, from `research/dragonseek_1_1/dashboard`:
```bash
python3 -m http.server 8765
```
Open `http://localhost:8765/index.html` in a modern browser. The existing China/Oceans dashboard loads and the extension adds a USGS seismic experiment at the bottom of the page.

Press **Fetch last 24 hours (M≥2.5)** to retrieve live USGS GeoJSON. No request runs automatically. The current public feed is `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson`. This endpoint uses no login and returns magnitude-2.5+ GeoJSON. It was deliberately chosen instead of all-day because 2.5+ filtering at the source is smaller.

Network request requires an internet-connected browser with USGS reachable. The UI shows STUB before fetch, CONNECTED_READONLY only after HTTP success and JSON validation. If inaccessible, it displays ERROR and does not invent data. A rolling payload SHA-256 receipt, fetch time and provider event-origin timestamp are displayed. No claims about access to CMA, NSMC, Ocean Cloud, FIRMS or CelesTrak.

Markers use the existing EPSG:4326 regional map envelope (72–151 E; 0–56 N) rather than falsely plotting global longitudes on a China-region map. The observations outside that envelope appear in the event list but not geographically plotted. The synthetic scenario events remain visibly distinct.

Click an event for USGS-sourced details and the original USGS event URL. For mainland China, CENC is the primary national seismic reporting system; network times and magnitudes can differ.

## RES07
Below the new feed-health cards is the **Run 168h side-by-side** button. It uses the existing RES07 load, PV, battery and solar inputs plus added regime and round-trip efficiency. Solar is off for storage-only, enabled for replenishment. Both simulations start with a full battery and use 0.25C limit, 12h sine daylight, symmetric sqrt(round-trip) conversion. Synthetic screening only; no real powerflow or certified resilience model.

## Quality and authorization requirements
- DeepSeek report: COLLABORATOR_REPORTED origin distinct from INDEPENDENT_VERIFICATION. Public USGS event: source-verified at fetch, not blanket validation of earthquake impacts.
- PUBLIC natural-hazard point coordinates are permitted. This does **not** authorize any sensitive facility point coordinates.
- Numeric inspector values use `UNKNOWN` for absent uncertainty; detection-limit rendering helper preserves left/right censoring.
- Only HTTPS USGS event links are accepted from feed.
- No secret tokens, logins, institutional endorsements, unattended feed polling, external command execution, operational warnings, or fresh CMA permissions.

## Test checklist to execute in a browser
1. Serve with Python; verify page loads without JS errors.
2. Before click: no observed earthquake icons and USGS status is STUB.
3. Click fetch; verify CONNECTED_READONLY *only* on valid HTTP payload, event details, hash receipt and origin timestamp.
4. Choose Seismic layer; only in-bounds public seismic points display; simulated icons retain their labels.
5. Turn off network and retry. Error/stale status must be visible and older results must not silently claim freshness.
6. Run RES07 comparison with same model inputs. Check nonnegative SOC and unmet load.
7. Test 390px and desktop viewports; ensure no horizontal overflow and markers align with source map.
8. Run existing repository Python CI tests. These checks have **not** been executed by the repo write action; do not claim pass.

## Current limitations
This branch includes a browser-runnable draft, **not a browser-executed acceptance receipt**, because the connector-write operation alone cannot guarantee runtime reachability. The standalone all-in-one v1.1 HTML remains the older snapshot; use index.html served with app_v11.js + dragonseek_v12_extension.js for v1.2. Other modules and feed categories are stubs.
