# Aluminum OS Core — Anti-Busywork Policy Engine

**The elimination of busywork is inevitable. This system ensures that when busywork dies, human flourishing rises.**

## What This Is

A real, compilable Rust implementation of the Fiduciary Duty Against Busywork. Not a manifesto. Not a concept doc. Working code with tests.

This is a **policy engine** — a system that evaluates proposed AI workflows and answers one question: *Does this automation make humans more capable, or does it just create a new layer of digital TPS reports?*

## The 10x Throughput Argument (In Plain Economics)

The 10x claim is not about doing 10x more tasks. It's about doing 10x more **valuable** tasks.

**Before automation:**
- 40 workers × 160 hrs/month = 6,400 human-hours
- 80% spent on agency-0.1 busywork (data entry, filing, routing)
- 20% spent on agency-0.8 judgment work (analysis, decisions, design)
- Effective high-value output: **1,280 hours/month**

**After automation + tier routing:**
- 40 workers × 160 hrs/month = 6,400 human-hours (same headcount)
- 0% busywork (automated away)
- 100% spent on agency-0.7+ work across three protected tiers
- Effective high-value output: **6,400 hours/month**

**That's a 5x multiplier on high-value output with zero layoffs.** Factor in the higher economic value per hour of high-agency work (3-4x based on BLS wage differentials between clerical and professional roles), and you're at **15-20x economic throughput**. Call it 10x conservatively.

## Architecture

```
aluminum-os-core/
├── src/
│   ├── lib.rs                 # AluminumEngine — the orchestrator
│   ├── classification/mod.rs  # Task taxonomy + 5-dimension agency scoring
│   ├── telemetry/mod.rs       # Net Positive Flourishing Metric (NPFM)
│   ├── routing/mod.rs         # Displaced labor → 3 protected tiers
│   ├── embodiment/mod.rs      # Simulation fidelity gating for robotics
│   └── governance/mod.rs      # Audit trail + decision logging
├── tests/
│   └── integration_test.rs    # 4 end-to-end scenarios
├── Cargo.toml
└── README.md
```

### Module Overview

**Classification** — Scores every task on 5 agency dimensions (decision depth, creative input, consequence scope, skill transfer, autonomy). Tasks scoring below 0.25 are classified as busywork.

**Telemetry (NPFM)** — Computes a single score: `(AutomationGain × AgencyUplift) - BusyworkPenalty - DisplacementRisk`. Positive = net-positive for human flourishing. Negative = reject.

**Routing** — Maps displaced workers into three protected tiers: High-Agency Oversight, Creative Genesis, or Metaverse Engineering. Each tier has defined training hours, value multipliers, and productivity timelines.

**Embodiment** — Before any AI-designed robot enters physical manufacturing, it must pass simulation fidelity thresholds across task completion, physics accuracy, failure coverage, and safety margins. No shortcuts.

**Governance** — Every evaluation is logged with full context. If you claim your AI is net-positive for humans, you need receipts.

## The NPFM Formula

```
NPFM = (AutomationGain × AgencyUplift) - BusyworkPenalty - (0.5 × DisplacementRisk)

Where:
  AutomationGain   = hours_saved / current_hours              [0.0–1.0]
  AgencyUplift     = avg_agency(retained) - avg_agency(automated)  [-1.0–1.0]
  BusyworkPenalty  = Σ(hours of AI-created busywork) / current_hours  [0.0+]
  DisplacementRisk = unrouted_displaced_hours / total_displaced       [0.0–1.0]
```

A workflow is **approved** when:
1. NPFM composite is positive
2. At least 60% of displaced workers have tier routing plans
3. If physical manufacturing is involved, embodiment gate passes

## Integration Test Scenarios

| Scenario | What Happens | Expected Verdict |
|---|---|---|
| Good Automation | 160hrs busywork automated, 8 workers routed to Tier 1 | **Approved** |
| Busywork Generator | AI creates 150hrs of new low-agency tasks | **Rejected** |
| Untested Robotics | Robot proposed with 200hrs sim (1000 required) | **Rejected** |
| 10x Transformation | 800hrs busywork automated, 40 workers across all 3 tiers | **Approved** |

## Quick Start

```bash
# Build
cargo build

# Run all tests (unit + integration)
cargo test

# Run with output visible
cargo test -- --nocapture
```

## What This Is NOT

- **Not a compiler.** It's a policy engine. Compilers process syntax; this evaluates socioeconomic impact.
- **Not a manifesto.** Every concept has a struct, a formula, and a test.
- **Not theoretical.** The four integration test scenarios model real-world automation patterns.

## License

MIT
