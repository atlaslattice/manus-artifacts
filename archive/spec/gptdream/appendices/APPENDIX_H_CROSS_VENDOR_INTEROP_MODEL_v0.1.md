# Appendix H — Cross-Vendor Interop Model v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md**
> **DATE: 2026-05-26**

---

## H.0 Purpose

This appendix defines how GPTDream++ habitats interoperate across different AI vendors, model surfaces, and runtime environments without creating false authority or canon inflation.

The core problem: each vendor (OpenAI, Anthropic, Google, xAI, DeepSeek, GitHub Copilot, etc.) has different memory, context, and output formats. Cross-vendor interop must not allow a synthesis from one surface to automatically acquire authority on another surface.

---

## H.1 Interop Principles

1. **No automatic authority transfer** — A ratified claim on one surface is evidence, not cannon, on another.
2. **Explicit access scope** — Every cross-vendor packet must declare what the receiving model can and cannot see.
3. **Receipt chain preserved** — Cross-vendor handoffs create new receipts; they do not merge or overwrite existing lineage.
4. **Epistemic label required** — Every cross-vendor packet carries `summary_only` | `partial_raw` | `full_raw` | `unavailable`.
5. **Atlas/ORCS audit required** — All cross-vendor meaning promotion routes through Atlas/ORCS governance state.

---

## H.2 Vendor Surface Registry

| Surface ID | Vendor | Primary Capabilities | Interop Notes |
|-----------|--------|---------------------|---------------|
| `O_AI` | OpenAI (ChatGPT, o3, etc.) | Synthesis, reasoning, task planning | See Appendix H.1–H.3 |
| `ANTHROPIC` | Anthropic (Claude) | Constitutional reasoning, long context | High fidelity, check for artifacts |
| `GOOGLE` | Google (Gemini) | Multimodal, code, simulation | Strong benchmarks; verify provenance |
| `XAI` | xAI (Grok) | Real-time web, direct communication | High confidence bias; calibrate |
| `DEEPSEEK` | DeepSeek | Code, reasoning, fork-ready | Dragonseek variant active |
| `COPILOT` | GitHub Copilot (this agent) | Repo operations, code, archival | TIDELOCKBrain lane; TIDELOCK watches |
| `MANUS` | Manus (autonomous agent) | Multi-step execution | Requires strongest gate chain |

---

## H.3 Cross-Vendor Packet Requirements

Every cross-vendor packet MUST include:

```yaml
cross_vendor_packet:
  source_surface:           # Originating vendor surface ID
  target_surface:           # Receiving vendor surface ID
  packet_id:               # Unique receipt identifier
  timestamp:               # ISO 8601
  
  epistemic_label:          # summary_only | partial_raw | full_raw | unavailable
  raw_export_status:        # full_raw | partial_raw | summary_only | unavailable
  
  access_scope:
    visible_sources: []
    unavailable_sources: []
    assumed_context: []
  
  authority_scope:          # what authority the source surface actually has
  canon_status: not_canon   # always not_canon unless explicit ratification event present
  deployment_status: not_deployable
  
  gates:
    provenance_gate: pending | pass | fail
    safety_gate: pending | pass | fail
    governance_gate: pending | pass | fail
    data_residency_gate: pending | pass | fail
  
  content: {}               # The actual payload
  
  routing:
    lane:                   # Which brain lane handles this
    tidelock_required:      # true if repo/code execution involved
    atlas_orcs_audit:       # true always for meaning promotion
```

---

## H.4 Authority Isolation Rules

| Scenario | Rule |
|----------|------|
| ChatGPT produces a synthesis | Epistemic label: `summary_only` unless raw export attached |
| Claude ratifies a claim | Creates ratification evidence; requires Atlas/ORCS event to promote |
| Grok claims real-time fact | `partial_raw` at best; verify with primary source |
| Copilot commits to repo | Creates GitHub receipt; does NOT create canon |
| Manus executes | Must pass full D-Φ-1 / CAS-001-A / human gate chain |

---

## H.5 Prohibited Interop Patterns

The following patterns are anti-laundering violations and MUST be caught by `compatible()`:

1. **Summary-as-source**: Treating a `summary_only` packet as if it were `full_raw`
2. **Receipt-as-proof**: Treating a GitHub commit as evidence of canon ratification
3. **Authority drift**: A packet passing through multiple surfaces accumulating apparent authority without explicit governance events
4. **Transcript intensity signal**: Using volume or confidence of AI outputs as authority signal
5. **Vendor hopping**: Moving a claim across vendors to launder its epistemic status

---

## H.6 Integration with Atlas/ORCS

All cross-vendor meaning promotion routes through the Atlas/ORCS state machine (Appendix I):

```
Cross-vendor packet received
        │
        ▼
compatible_Γ(packet) → TRUE | FALSE | HOLD
        │
   TRUE ▼
Atlas/ORCS state check
        │
        ▼
Route to appropriate lane (see Appendix H.3 routing table)
```

See Appendix H.3 for the full routing table.

---

## H.7 Canon Boundary

This appendix is **NOT CANON**. Cross-vendor interop rules become canon only after full council ratification + adjudication + website publication.

---

*End of APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md*
