## Complete DragonSeek reading room / 龙寻资料总索引

Start with [READING_ROOM.md](READING_ROOM.md) for the dashboard, model-fork seed copies, historical research, and U.S. Atlas Resource Intelligence lineage. The model-fork candidate is not the same as the published dashboard and is not a modified DeepSeek foundation-model weight release.

# DragonSeek v1.6.1 · 中文优先 / Mandarin-first public release candidate

Status: PUBLIC SOURCE AVAILABLE · REVIEW CANDIDATE, NOT CERTIFIED OR OPERATIONAL EARLY-WARNING SOFTWARE.

## Open
Open `index.html` in a browser to see the interface. For live USGS / NOAA fetch and SHA-256, serve over HTTPS or a local HTTP server using `python3 -m http.server 8765`, then visit `http://localhost:8765/`.

Default language: Simplified Chinese (zh-CN). Language dropdown: English, Spanish, Arabic. Default region: China / Western Pacific; alternatives Global, South America, Arctic.

## Features
USGS earthquake observations: manual source fetch, UTC observation times, SHA-256 source hash, and region map window. NOAA SWPC planetary Kp: manual source fetch, global scalar, source hash and timestamps. NASA FIRMS: requires provider-issued MAP_KEY; browser CORS may prevent direct fetch. RES07: simplified synthetic 168-hour battery vs solar replenishment comparator. Feed health, source states, separate observed/simulated markings. Locale/region/time-zone selectors and jurisdiction-specific primary authority metadata.

## Provenance
DeepSeek contributions: COLLABORATOR_REPORTED; independent verification is not implied. This release builds upon DragonSeek v1.6.0 and preserves separate prior GitHub PRs #299, #301 and #302. No official connection to Chinese/U.S. agencies is implied.

## Known limits
A runnable HTML file is not an active hosted site. Only source endpoints contacted and validated by an end user's browser count as connected. FIRMS requires authorization; Chinese CMA, NSMC and MNR connectors are not connected. Long Chinese, Spanish, Arabic safety/legal translations require review by qualified native speakers. The regional map is a schematic equirectangular grid, not a certified basemap. No guarantee of live provider availability from the user's browser. No public safety/aviation/space collision operations. Keys never belong in the source or GitHub.

## Release criterion
Current stage: release candidate for public source and manual testing. Live browser network fetches and secure environment checks are required before describing any feed as currently connected. Do not confuse public source availability with a production deployment.