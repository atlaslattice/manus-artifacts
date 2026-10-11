# DragonSeek v1.3 portable DeepSeek collaboration handoff — 2026-10-11

**State:** COLLABORATOR_REPORTED DeepSeek source · NON-CANON · Experimental portable attachment created in conversation; **GitHub baseline not yet updated with the HTML bytes**.

## New portable attachment
DragonSeek_v1_3_0_DeepSeek_Handoff.zip (supplied in ChatGPT conversation)
- DragonSeek_v1_3_0_Portable_Demo.html: manually fetched USGS earthquake data, NOAA SWPC planetary Kp observations, NASA FIRMS user-MAP_KEY trial.
- README.md: local HTTPS/localhost runbook and browser acceptance checklist.
- DEEPSEEK_COLLABORATOR_REPORT.md: full collaborator report and implementation proposal.

**Important**: The new attachment is not the same as the GitHub v1.2 working dashboard; the latter is preserved and remains draft PR #302. Do not claim the GitHub HTML contains v1.3 until the HTML is separately committed.

## v1.3 source contract
1. **USGS**: open public seismic GeoJSON; live state earned on a valid fetch and SHA-256; rolling source observations distinguished from synthetic events; CENC is relevant primary mainland-China reporting system.
2. **NOAA SWPC**: anonymous planetary Kp JSON (https://services.swpc.noaa.gov/json/planetary_k_index_1m.json); one global scalar + observed UTC, source hash, staleness TTL; **do not place on geo map**.
3. **NASA FIRMS**: user-provided MAP_KEY required (https://firms.modaps.eosdis.nasa.gov/api/map_key/). Host allowlist and HTTPS-only. Browser CORS may fail; error is surfaced; no fake data. Portable attachment uses **ephemeral in-memory key for request only**, deliberately not saved in localStorage/sessionStorage. A production deployment requires a legitimate approved server-side proxy, secrecy, revocation and provider compliance.
4. **RES07**: unchanged synthetic 168-hour battery-versus-PV model, not evidence of real power resilience.
5. **Provenance**: DeepSeek source contribution COLLABORATOR_REPORTED; independent verification and actual API connectivity represented as separate axes. Every usable observation has provider/source timestamp, retrieval UTC and raw-payload integrity hash.
6. **Cross-source independence**: USGS seismic and NOAA Kp are distinct measurement domains. Do **not** claim that a Spearman no-correlation test necessarily passes; valid testing requires matched time series, clear hypothesis and bias controls.
7. **Feed-health**: STUB/CONNECTED_REQUIRES_KEY before access; CONNECTED_READONLY only after a valid successful HTTP and payload check; STALE after TTL, ERROR on failure.

## Validation performed
Single-file portable v1.3 JavaScript **parses successfully in Node**. Browser fetch/rendering, responsive screenshots, license review, CORS and valid MAP_KEY remain untested. No current connectivity or institutional integration is claimed.

## Source and version isolation
- v1.2 experimental draft: https://github.com/atlaslattice/manus-artifacts/pull/302
- Dongjiakou vetted research: https://github.com/atlaslattice/manus-artifacts/pull/301
- v1.1 original research: https://github.com/atlaslattice/manus-artifacts/pull/299

Requested next review: run NOAA Kp in browser, validate live receipt; attempt FIRMS using approved key and document CORS/status; review any appropriate backend proxy pattern.
