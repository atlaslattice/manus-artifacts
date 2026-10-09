# Simulator implementation contract — v0.7 proposal

**Not implemented in this publication.** This contract informs a later, separate reviewed PR.

## Compatibility boundary
- Keep the recovered Dongjiakou simulator, original source hashes and all historical CLI outputs unchanged.
- Preserve all 23 outstanding DARs, six ecological vetoes and zero realized credits until individually closed by qualifying receipts and review.
- Add new outcome/resource operations as a namespaced adapter; no real plant control interface, credentials or proprietary telemetry.
- Maintain separate v0.1 contracts. Migrate only through an explicit versioned converter with reproducible tests.

## Proposed commands
- outcomes validate: structural schema validation plus provenance, unit, uniqueness and credit-gate checks.
- allocate validate: waste-only eligibility, source rights, competing uses, dry-mass and constituent balances, no double allocation.
- resilience scenario: probability basis/horizon, severity, duration, dependencies, deliverability, protected service and avoided-loss ceiling.
- agronomy stack: factor/population IDs, site-season, interventions, overlap groups, comparator, adoption and interaction effects.
- outcomes current: display a separate null-first ledger; do not mutate existing locality output.
- GRV register: stage-gate evidence for independently reproducible or operating adaptation.

## Core invariants
1. Unknown stays null; zero is a known measured value only when supported.
2. Waste-only eligibility rejects dedicated energy crops in the base case.
3. Physical allocations conserve dry mass and declared constituents within explicit tolerance.
4. No repeated credit for shared feedstock, energy, tax transfers, gate fees, QOL or avoided loss.
5. Natural-gas mass and normalized gas volumes are not mixed.
6. Evidence classes cannot be upgraded from policy, capacity, press release or model output alone.
7. Ecological vetoes are non-compensable.

## Tests and acceptance
Run schema, positive and negative tests in CI; demonstrate a successful full workflow; verify historical outputs against pinned baseline; independent reviewer checks citations and formulas. No merge until v0.6 CI is resolved, new CI passes, the claim register is complete for promoted numbers, and no data acquisition request has been silently closed. Field deployment remains subject to operator/regulatory authority and consent.
