# Atlas Lattice executable RES07/RES09/RES10 synthetic simulator v0.1

**PROPOSED · NON-CANON · ZERO REALIZED CREDIT.** Study-only Python prototype. No live control/actuation.

Run `python resilience_sim.py` or `python -m unittest -v test_resilience_sim.py`.

Features: Tarjan SCC cycles, capacity-based minimum service thresholds, prioritized electrical demand, hourly PV recharge, inverter and stored-energy constraints, outages/common-cause asset failure windows, four synthetic scenarios (baseline/distributed/networked/degraded), hourly trace and continuity results.

**Important limitations:** The four examples are NOT matched-capacity architectural comparisons; networked has larger energy resources. The model does not represent actual independent feeder power flows, electrical protection, islanding switchgear, safe black start, multi-resource restart scheduling, operator unavailability, flood hydraulics, coastal physics, wastewater or validated local data. A detected cycle is conservatively blocked unless restart is explicitly provided in a future model. Do not use for physical equipment design or claim validated seven-day autonomy.

Next required gates: matched MW/MWh scenarios; independent power islands and guarded interties; resource-constrained dependency and operator scheduler; regional source-provenance adapters for Maui and Dongjiakou; COAST01 hazard + conditional-value ledger; QOL activity staffing. All historical field reports (Lahaina two solar-battery nodes, weeks operation) remain testimony, not calibration.

Context: [Draft PR #285](https://github.com/atlaslattice/manus-artifacts/pull/285).