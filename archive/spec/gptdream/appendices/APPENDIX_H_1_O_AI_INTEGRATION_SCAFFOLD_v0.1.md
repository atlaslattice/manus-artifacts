# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix H.1 — O_AI Integration Scaffold v0.1

### H.1 — O_AI Scaffold

The O_AI scaffold is the OpenAI-side task surface for cross-vendor GPTDream++ coordination.

```text
O_AI scaffold purpose:
  Accept incoming work packets from vendor-neutral coordinator
  Route tasks to appropriate model thread
  Return outputs with canonical runtime labels
  Preserve receipt lineage across provider boundary
```

O_AI scaffold minimum interface:

```yaml
o_ai_task_surface:
  accept_packet: true
  packet_schema_version: "1.0"
  runtime_label_required: true
  canon_status_required: true
  receipt_required: true
  human_root_flag_passthrough: true
```

O_AI scaffold invariants:

```text
1. O_AI scaffold accepts packets; it does not generate canon.
2. O_AI outputs must carry runtime label from originating scaffold.
3. O_AI scaffold does not resolve cross-vendor authority conflicts unilaterally.
4. Receipt lineage must be preserved through all scaffold hops.
```
