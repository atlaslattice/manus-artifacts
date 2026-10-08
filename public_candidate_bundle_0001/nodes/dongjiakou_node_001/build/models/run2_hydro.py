"""Run 2 — unused hydraulic head, parametric transfer function only.

Reproduces the derived numerics of RUN_2_HYDRO_v0_1.json.

Invariants exercised here:
  * no public receipt identifies unused dissipated head, so the credit is ZERO;
  * the sensitivity table is a transfer function, not evidence the head exists;
  * product-water pressure is not asserted to be disposable;
  * the 400-630 m SWRO pump head is motor-supplied and is excluded, so it can
    never be counted a second time as recovered hydro energy.
"""

from __future__ import annotations

from typing import Any

from .common import UNKNOWN, guard_fraction, require_number

RHO_KG_M3 = 1000.0
G_M_S2 = 9.80665
SECONDS_PER_YEAR = 365.0 * 24.0 * 3600.0
HOURS_PER_YEAR = 8760.0
JOULES_PER_GWH = 3.6e12

PRODUCT_SUPPLY_2025_M3 = 17_930_000.0
PROCESS_ENERGY_2025_GWH = 39.446

#: The 2025 reported product-water volume is the stream basis.
STREAM_VOLUME_M3_YEAR = PRODUCT_SUPPLY_2025_M3

#: Illustrative efficiency used for the published sensitivity table.
ILLUSTRATIVE_ETA = 0.8
ILLUSTRATIVE_HEADS_M = (1.0, 5.0, 10.0, 20.0, 50.0)


def average_flow_m3_s(volume_m3_year: float) -> float:
    """Annual-average volumetric flow."""
    volume = require_number(volume_m3_year, "volume_m3_year")
    return volume / SECONDS_PER_YEAR


def hydro_energy_gwh(volume_m3_year: float, head_m: float, eta: float) -> float:
    """E = rho * g * V * H * eta, returned in GWh."""
    volume = require_number(volume_m3_year, "volume_m3_year")
    head = require_number(head_m, "head_m")
    eff = guard_fraction(eta, "eta")
    if volume < 0 or head < 0:
        raise ValueError("volume_m3_year and head_m must be non-negative")
    return RHO_KG_M3 * G_M_S2 * volume * head * eff / JOULES_PER_GWH


def hydro_case(volume_m3_year: float, head_m: float, eta: float) -> dict[str, float]:
    """Full derived case for one (volume, head, eta) triple."""
    gwh = hydro_energy_gwh(volume_m3_year, head_m, eta)
    return {
        "annual_energy_GWh": gwh,
        "average_power_kW": gwh * 1e6 / HOURS_PER_YEAR,
        "fraction_of_2025_UF_RO_process_energy": gwh / PROCESS_ENERGY_2025_GWH,
    }


def run(head_available_m: Any = UNKNOWN) -> dict[str, Any]:
    """Run 2 — parametric sensitivity with a hard zero baseline credit."""
    ideal_per_m = hydro_energy_gwh(STREAM_VOLUME_M3_YEAR, 1.0, 1.0)
    illustrative_per_m = hydro_energy_gwh(STREAM_VOLUME_M3_YEAR, 1.0, ILLUSTRATIVE_ETA)

    out: dict[str, Any] = {
        "artifact_id": "DJK-NODE-001-RUN-2-HYDRO-v0.1",
        "status": "EXECUTED_PARAMETRIC_SENSITIVITY_NON_CANON",
        "baseline": {
            "H_available_m": head_available_m,
            "hydro_credit_GWh_year": 0,
            "reason": "No public Dongjiakou receipt identifies unused dissipated head.",
        },
        "stream_basis": {
            "stream": "2025 reported product-water volume",
            "annual_volume_m3": STREAM_VOLUME_M3_YEAR,
            "average_flow_m3_s": average_flow_m3_s(STREAM_VOLUME_M3_YEAR),
            "note": "Does not assert product-water pressure is disposable.",
        },
        "physics": {
            "equation": "E = rho*g*V*H*eta",
            "rho_kg_m3": RHO_KG_M3,
            "g_m_s2": G_M_S2,
            "ideal_energy_GWh_per_m_head_at_eta_1": ideal_per_m,
            "illustrative_energy_GWh_per_m_head_at_eta_0_8": illustrative_per_m,
            "illustrative_average_power_kW_per_m_head_at_eta_0_8": (
                illustrative_per_m * 1e6 / HOURS_PER_YEAR
            ),
            "illustrative_process_energy_fraction_per_m_head_at_eta_0_8": (
                illustrative_per_m / PROCESS_ENERGY_2025_GWH
            ),
        },
        "illustrative_eta_0_8_sensitivity": [
            {
                "H_m": head,
                **hydro_case(STREAM_VOLUME_M3_YEAR, head, ILLUSTRATIVE_ETA),
            }
            for head in ILLUSTRATIVE_HEADS_M
        ],
        "excluded_head": {
            "SWRO_pump_head_m": "400-630",
            "status": "MOTOR_SUPPLIED_NOT_RECOVERABLE",
            "note": (
                "Intake seawater gravity-flows to the pump suction pool; the "
                "high-pressure head is motor-supplied and may never be counted "
                "as recovered hydro energy."
            ),
        },
    }
    return out
