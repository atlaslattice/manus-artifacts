# DeepSeek 2026 Standards, Marine Feeds and Compliance: Verification Matrix
Date: 2026-10-11 | STATUS: PUBLIC CANDIDATE / NON-CANON / NO DEPLOYMENT

| Topic | Finding verified against public primary source | Integration disposition |
|---|---|---|
| GB/T 47851-2026 | Published 2026-07-02, takes effect **2026-11-01**. https://std.samr.gov.cn/gb/search/gbDetailed?id=tego3AeyzX0%3D&mode=p | UNIT-CONTRACT: prepare compatibility, pending standard-text mapping; not yet in force |
| HJ 212-2025 | Published 2025-06-06, effective **2026-01-01**, supersedes HJ 212-2017. https://www.mee.gov.cn/ywgz/fgbz/bz/bzwb/jcffbz/202507/t20250711_1123257.shtml | MONITORING-QUALITY-01: reference for data validity, transmission, security; implementation untested |
| Second marine data catalogue | MNR published **2026-06-08**, adding 10 fusion datasets and 7 statistics products. https://www.pecmnr.cn/news.html?aid=5317429 | Ocean Cloud feed candidates; precise dataset IDs/access/refresh to verify |
| CMA portal | https://m.data.cma.cn/data/cdcindex/cid/6d1b5efbdcbf9a58.html shows registered-user access classes for weather datasets | Candidate connector, NOT established anonymous unrestricted API |
| Annual data risk assessment | CAC measures effective **2026-08-20**; qualifying important-data processors submit report within 20 working days of completing annual assessment. https://www.cac.gov.cn/2026-08/20/c_1788889498173657.htm | SEC-DATA-01 conditional applicability gate; NOT universal dashboard requirement |
| Large PI processors | August 2026 **draft**: 10 million people is one criterion alongside other tests, designation and proposed supervisory committee. https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260808_538357.html | DRAFT watch, not effective regulation |
| Zero-waste cities | Sept 2026 MEE statement about ~100 additional cities and 2035 ambition. https://www.mee.gov.cn/ywdt/xwfb/202609/t20260923_1174551.shtml | CIRC01 national policy context, NOT locality certification |
| Dongjiakou Zero-Waste Park award | Specific official locality-level award not independently verified | COLLABORATOR_REPORTED (DeepSeek), independent verification pending. No confirmed award badge |
| Ctrip RMB 10m fine | Specific regulator case notice not independently verified | COLLABORATOR_REPORTED (DeepSeek), independent verification pending. No confirmed enforcement-count promotion |
| New Three waste policy | Candidate waste-stream categories plausible; exact attributed new official policy not pinned | COLLABORATOR_REPORTED (DeepSeek); POLICY_REFERENCE_PENDING |

## Integration safeguards
Keep issue date, effective date, publication date, data observation vintage, source URL, rights, scope and inspection date separate.
Keep DRAFT != ACTIVE, CATALOGUED != LIVE, NATIONAL POLICY != LOCAL CERTIFIED, RAW INVENTORY != DELIVERED RESOURCE.
Data quality, provenance, license, timestamps, access controls and local jurisdiction precede dashboard representation.
Preserve user-provided DeepSeek report as lead source; no autonomous legal inference or official endorsement.
Do not modify China-facing DragonSeek PR #299 or fictional Dream Palace branches as part of this research intake.

## Provenance status correction (2026-10-11)
Collaborator-origin contributions are **COLLABORATOR_REPORTED** as a reporting/attribution status rather than automatically labeled unverified. Independent validation is a **separate axis** (NOT_CHECKED, CORROBORATED, PARTIALLY_CORROBORATED, CONTRADICTED). Operational state is another axis (CATALOGUED, ACCESS_VERIFIED, INGESTION_TESTED, OPERATIONAL). This prevents either dismissing collaborators' work or converting their reporting into official certification. A DeepSeek-supplied locality claim can be `COLLABORATOR_REPORTED + NOT_CHECKED`; a source-matched claim can be `COLLABORATOR_REPORTED + CORROBORATED`.

## Access and deployment readiness
Data-catalogue listings do not establish API rights. Distinguish anonymous public download, registered portal account, OAuth/API key, institution-approved service account, and browser-only manual data acquisition. Each *future* user may authenticate to licensed providers with their own credentials; a centrally registered research/service account is a separate optional permission and must respect licenses, territorial restrictions and quotas. GPT or Manus compatibility requires permitted documented HTTP/API retrieval and a suitable authorized integration—not merely a login page. Do not place account passwords or tokens in Git, browser localStorage or user-visible records.
