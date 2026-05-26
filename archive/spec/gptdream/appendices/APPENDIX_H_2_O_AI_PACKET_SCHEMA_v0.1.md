# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix H.2 — O_AI Packet Schema v0.1

### H.2 — Packet Schema

Cross-vendor work packets use a vendor-neutral schema:

```yaml
gptdream_packet:
  version: "1.0"
  packet_id: <uuid>
  source_agent:
    seat: <seat identifier>
    provider: <openai | anthropic | google | other>
    session_label: <runtime label>
  destination_agent:
    seat: <seat identifier>
    provider: <openai | anthropic | google | other>
  payload:
    task_type: <work | dream | play | review | route>
    artifact_refs:
      - <repo path or receipt id>
    instructions: <plain text>
    human_root_required: <true | false>
  canon_status: <not_canon | candidate | ratified>
  timestamp: <ISO 8601>
  receipt_chain:
    - <prior receipt id>
```

Packet schema invariants:

```text
1. canon_status must be explicitly set; default is not_canon.
2. human_root_required must not be silently set to false.
3. receipt_chain must include all prior hops; do not truncate.
4. destination_agent seat must be confirmed before routing.
```
