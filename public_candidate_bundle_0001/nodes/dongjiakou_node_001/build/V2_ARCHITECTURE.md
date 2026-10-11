# Dongjiakou Simulator v2.0-alpha: v1 baseline + first-class QOL / ECO / FUND
DATE: 2026-10-10
STATUS: PROPOSED · NON-CANON · NON-DEPLOYED · ZERO REALIZED CREDIT

## Core correction
QOL cannot be a mere external reporting appendix. QOL01 must join WATER/ENERGY/RESOURCES/FINANCE/ECO/GOV as a first-class *decision* module. This is not the same as booking speculative life satisfaction as revenue. Human-relevant physical outcomes and ecological outcomes receive independent ledgers with direct vetoes, benefit goals, opportunity costs and funding decisions. QOL projects may be valid despite negative narrow commercial cash flows if real public funding covers the remainder and independent evidence supports the benefit.

The first v2 alpha mirrors v1 in-process by **calling its original locality and resource run functions**, not copying/recalculating the physical baseline. It adds three modules to one returned JSON object: QOL01 (programs/indicators), ECO01 (outfall load and ecological unknowns), FUND01 (cost gap and funding status). The accepted schema/companion from preceding PR #288 are inherited on this branch, but the new `simulator_v2.py` is the unified command, rather than a disconnected sidecar. It leaves original `simulator.py` unchanged.

## Run
`python3 simulator_v2.py` — emits unified full JSON (large).
`python3 -m pytest tests/test_simulator_v2.py -q`
`python3 -m pytest tests -q` — full regression suite.

## Funding pathway (first class, not automatic)
A candidate environmental closure project with scenario-total cost C and comparable modeled resource-recovery value R gives a *sensitivity* funding gap G=C−R. QOL01 can register non-commercial reason to consider G. ECO01 can establish physical objectives, veto harmful alternatives and measure real improvement. FUND01 must still check who bears G, currency/time basis, binding authority, financing instruments, intergenerational liabilities, maintenance reserves, and ecological outcome verification. **No QOL points create money; no automatic 'funded' verdict.** Present candidate cash and non-cash outcomes separately; do not force biodiversity/childhood into financial units.

## Evidence and portability boundaries
- `UNKNOWN` stays null; never zero; missing funding != authorized.
- 40% recovered / 60% residual is a user-reported illustrative fraction only.
- Locality transport requires its own physical flows and permits before any Dongjiakou output can be reused. This alpha refuses locality relabeling.
- Modular extension to full national dashboard: generic source/edge registries; multi-site schema; QOL indicators per population/household, ecological outfall IDs; validated cross-sector funding contracts, independent outcomes, sensitivity analysis.
- **Outstanding v2 work:** integrate other v1 models (solar/hydro/compute/biometabolic/BESS), transport every validator gate and evidence ledger into one output; add complete QOL measures and social funding cases; reconcile competing v1 physical register versions; implement real longitudinal QOL and natural-capital observations; site baseline; CI results. This is an alpha vertical slice, not the finished full v2 mirror.

Sources:
- https://app.notion.com/p/3f20c1de73d98132893ae61d44225d38
- https://app.notion.com/p/3f40c1de73d98130a203fa148fd32d18
- https://app.notion.com/p/3f50c1de73d981c0bfdac34f11c0e373
- https://github.com/atlaslattice/manus-artifacts/pull/288
