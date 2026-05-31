# GPTBrain Packet Schema

**Status:** public candidate  
**Canon:** no  
**Deployment:** no  
**Authority:** none  

Every GPT-side packet should preserve the same status spine.

```yaml
packet_id:
packet_type:
created_utc:
operator:
source_refs:
raw_export_status:
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
proof_status: not_a_proof
privacy_status:
rights_status:
strongest_safe_claim:
overclaims_to_avoid:
missing_receipts:
contradictions:
next_safe_action:
human_gate_required: true
```

## Rule

A packet can organize work. It cannot crown work.
