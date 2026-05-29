# OpenAI-Relevant Source Packet Inventory (2026-05-26)

STATUS: CANDIDATE WORKING SPEC — NOT CANON  
DEPLOYMENT: NOT DEPLOYABLE  
AUTHORITY: NONE

## Inventory table

| packet_id | packet_type | raw_export_status | public_use_status | blocked_reason | notes |
|---|---|---|---|---|---|
| oai_pkt_001 | o-ai-packet | full_raw | source_complete | none | direct raw export ingestion |
| oai_pkt_002 | o-ai-packet | summary_only | source_incomplete | summary_only | cannot be promoted to public claim |
| oai_pkt_003 | o-ai-packet | partial_raw | source_incomplete | partial_raw | requires additional source material |
| oai_pkt_004 | o-ai-packet | unavailable | none | unavailable_sources | blocked until source recovery |

## Integration notes
- Packet schema source: `schemas/o_ai/v0_1/o-ai-packet.schema.yaml`
- Inventory packets map to `raw_source` nodes in Source Graph Engine.
- Claims derived from summary-only or incomplete sources are review-gated.
