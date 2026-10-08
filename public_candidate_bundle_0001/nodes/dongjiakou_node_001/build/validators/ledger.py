"""The Node-001 credit ledger.

Every accounting credit taken anywhere in the node is registered here as an
entry against a *physical resource*. Double-counting then becomes a mechanical
check: a resource may receive at most one primary credit, and the total credited
quantity may not exceed the resource's sourced availability.

If a resource has no measured availability, its bound is UNKNOWN and any
positive credit against it is a violation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

from models.common import EvidenceClass, UNKNOWN, is_unknown

#: Domains in which a credit may be taken.
DOMAINS = ("energy", "heat", "water", "mass", "carbon", "revenue", "service")

#: Evidence classes strong enough to carry a primary credit on their own.
PRIMARY_CREDITING_CLASSES = frozenset(
    {EvidenceClass.MEASURED, EvidenceClass.REPORTED, EvidenceClass.DERIVED}
)


@dataclass(frozen=True)
class CreditEntry:
    """One accounting credit against one physical resource."""

    entry_id: str
    domain: str
    resource_id: str
    quantity: float
    units: str
    evidence_class: EvidenceClass
    receipt_ids: tuple[str, ...] = ()
    notes: str = ""

    def __post_init__(self) -> None:
        if self.domain not in DOMAINS:
            raise ValueError(f"unknown credit domain {self.domain!r}")

    @property
    def is_primary(self) -> bool:
        """True when this entry claims a primary accounting credit."""
        return self.quantity > 0 and self.evidence_class in PRIMARY_CREDITING_CLASSES


@dataclass
class ResourceBound:
    """Sourced availability ceiling for one physical resource."""

    resource_id: str
    domain: str
    bound: Any                 # float, or UNKNOWN when availability is not established
    units: str
    basis: str
    note: str = ""


@dataclass
class CreditLedger:
    """An append-only set of credit entries."""

    entries: list[CreditEntry] = field(default_factory=list)

    def add(self, entry: CreditEntry) -> None:
        self.entries.append(entry)

    def extend(self, entries: Iterable[CreditEntry]) -> None:
        for e in entries:
            self.add(e)

    def for_resource(self, resource_id: str) -> list[CreditEntry]:
        return [e for e in self.entries if e.resource_id == resource_id]

    def total_for(self, resource_id: str) -> float:
        """Sum of all credited quantity against a resource."""
        return sum(e.quantity for e in self.for_resource(resource_id))

    def primary_credits_for(self, resource_id: str) -> list[CreditEntry]:
        return [e for e in self.for_resource(resource_id) if e.is_primary]

    def domains(self) -> set[str]:
        return {e.domain for e in self.entries}


#: Availability ceilings for every resource that could attract a credit.
#:
#: An UNKNOWN bound means the resource's availability has not been established
#: at Node-001, so no primary credit may be taken against it at all.
RESOURCE_BOUNDS: dict[str, ResourceBound] = {
    b.resource_id: b
    for b in [
        ResourceBound(
            "S01_PV_energy", "energy", UNKNOWN, "kWh/year",
            basis="No measured PV generation at Node-001; roof layout is MODELED and "
                  "roof structure is UNKNOWN.",
            note="S01 generation is not incremental to the node and may be credited once only.",
        ),
        ResourceBound(
            "G01_regional_green_energy", "energy", 0.0, "kWh/year",
            basis="INTEGRATED_NODE_PROFILE_v0_2 green_direct_status.energy_credit = 0; "
                  "node001_access = UNKNOWN.",
            note="Planned regional capacity is not a node allocation.",
        ),
        ResourceBound(
            "B01_storage_service", "energy", 0.0, "kWh/year",
            basis="No hourly mismatch trace; S02_BESS_TRANSFER_FUNCTION_v0_1 baseline_credit = 0.",
        ),
        ResourceBound(
            "C01_useful_heat", "heat", 0.0, "GWh_th/year",
            basis="No CIP setpoint, thermal duty, coolant temperature, heat-pump COP "
                  "map or temporal-overlap receipt.",
        ),
        ResourceBound(
            "C01_model_service_benefit", "service", 0.0, "dimensionless",
            basis="No before/after KPI evidence for model-assisted operation.",
        ),
        ResourceBound(
            "H01_unused_head_energy", "energy", 0.0, "kWh/year",
            basis="No public receipt identifies unused dissipated head.",
            note="Motor-supplied SWRO pump head is excluded and may not be recovered twice.",
        ),
        ResourceBound(
            "BIO01_biogas_energy", "energy", 0.0, "kWh/year",
            basis="No Node-001 feedstock allocation, gas composition or conversion receipt.",
        ),
        ResourceBound(
            "BIO01_N_mass", "mass", 0.0, "kg N/year",
            basis="No measured digestate nutrient mass or product assay.",
            note="One N mass cannot receive both a fertilizer and a compost credit.",
        ),
        ResourceBound(
            "BIO01_P_mass", "mass", 0.0, "kg P/year",
            basis="No measured digestate nutrient mass or product assay.",
            note="One P mass cannot receive both a struvite and a compost credit.",
        ),
        ResourceBound(
            "BIO01_Mg_mass", "mass", 0.0, "kg Mg/year",
            basis="No material-purity or nutrient-chemistry receipt.",
            note="One Mg mass cannot be both a commodity and a nutrient-recovery reagent.",
        ),
        ResourceBound(
            "BIO01_reclaimed_water", "water", 0.0, "m3/year",
            basis="No verified reuse displacing another water source.",
        ),
        ResourceBound(
            "BIO01_compost_mass", "mass", 0.0, "t/year",
            basis="No mass, contaminant, pathogen, maturity or off-take data.",
        ),
        ResourceBound(
            "W01_reject_marine_discharge", "water", 0.0, "m3/year",
            basis="Feed-minus-product reject-equivalent is modelled, not measured marine "
                  "discharge.",
            note="Modelled residual may never be restated as a discharge claim.",
        ),
    ]
}


def build_ledger_from_artifacts(artifacts: dict[str, Any]) -> CreditLedger:
    """Extract every credit-bearing claim from the run artifacts.

    With the current evidence base essentially every quantity is zero, which is
    the intended state: the ledger exists so that the moment a nonzero credit is
    claimed it must name a resource, a receipt and an evidence class.
    """
    ledger = CreditLedger()

    # --- Run 0: retrofit credits are explicitly zero across the board --------
    run0 = artifacts.get("RUN_0", {})
    for name, value in (run0.get("retrofit_credit") or {}).items():
        ledger.add(
            CreditEntry(
                entry_id=f"RUN_0.retrofit_credit.{name}",
                domain="energy",
                resource_id=_resource_for_retrofit(name),
                quantity=0.0 if value in (0, 0.0) else float(value),
                units="kWh/year",
                evidence_class=EvidenceClass.UNKNOWN if value == 0 else EvidenceClass.DERIVED,
                notes="Explicit zero retrofit credit in the baseline artifact.",
            )
        )

    # --- Run 3: useful heat and model service benefit ------------------------
    run3 = artifacts.get("RUN_3", {})
    heat = run3.get("heat_credit") or {}
    ledger.add(
        CreditEntry(
            entry_id="RUN_3.heat_credit.baseline_useful_heat_GWhth",
            domain="heat",
            resource_id="C01_useful_heat",
            quantity=float(heat.get("baseline_useful_heat_GWhth", 0) or 0),
            units="GWh_th/year",
            evidence_class=EvidenceClass.UNKNOWN,
            notes="Zero until a measured thermal sink exists.",
        )
    )

    # --- Run 2: hydro credit --------------------------------------------------
    run2 = artifacts.get("RUN_2", {})
    hydro_credit = (run2.get("baseline") or {}).get("hydro_credit_GWh_year", 0)
    ledger.add(
        CreditEntry(
            entry_id="RUN_2.baseline.hydro_credit_GWh_year",
            domain="energy",
            resource_id="H01_unused_head_energy",
            quantity=float(hydro_credit or 0) * 1e6,
            units="kWh/year",
            evidence_class=EvidenceClass.UNKNOWN,
            notes="No receipt identifies unused dissipated head.",
        )
    )

    # --- S02: BESS service credit --------------------------------------------
    s02 = artifacts.get("S02", {})
    ledger.add(
        CreditEntry(
            entry_id="S02.baseline_credit",
            domain="energy",
            resource_id="B01_storage_service",
            quantity=float(s02.get("baseline_credit", 0) or 0),
            units="kWh/year",
            evidence_class=EvidenceClass.UNKNOWN,
            notes="No hourly mismatch trace.",
        )
    )

    # --- Run 4A: every BIO01 product stream ----------------------------------
    run4a = artifacts.get("RUN_4A", {})
    mapping = {
        "biogas_m3_year": ("BIO01_biogas_energy", "energy", "kWh/year"),
        "methane_energy_credit": ("BIO01_biogas_energy", "energy", "kWh/year"),
        "reclaimed_water_credit": ("BIO01_reclaimed_water", "water", "m3/year"),
        "struvite_credit": ("BIO01_P_mass", "mass", "kg P/year"),
        "ammonium_credit": ("BIO01_N_mass", "mass", "kg N/year"),
        "compost_credit": ("BIO01_compost_mass", "mass", "t/year"),
        "wastewater_bioreactor_credit": ("BIO01_biogas_energy", "energy", "kWh/year"),
    }
    for key, (resource_id, domain, units) in mapping.items():
        value = (run4a.get("baseline_credit") or {}).get(key, 0)
        ledger.add(
            CreditEntry(
                entry_id=f"RUN_4A.baseline_credit.{key}",
                domain=domain,
                resource_id=resource_id,
                quantity=float(value or 0),
                units=units,
                evidence_class=EvidenceClass.UNKNOWN,
                notes="Zero until feedstock, chemistry and off-take receipts close.",
            )
        )

    # --- Integrated node profile: green direct and storage -------------------
    profile = artifacts.get("INTEGRATED_NODE_PROFILE", {})
    green = profile.get("green_direct_status") or {}
    ledger.add(
        CreditEntry(
            entry_id="INTEGRATED_NODE_PROFILE.green_direct_status.energy_credit",
            domain="energy",
            resource_id="G01_regional_green_energy",
            quantity=float(green.get("energy_credit", 0) or 0),
            units="kWh/year",
            evidence_class=EvidenceClass.UNKNOWN,
            notes="Regional plan is REPORTED; node allocation is UNKNOWN.",
        )
    )

    return ledger


def _resource_for_retrofit(name: str) -> str:
    """Map a Run 0 retrofit-credit label onto a ledger resource."""
    table = {
        "S01_solar": "S01_PV_energy",
        "H01_mini_hydro": "H01_unused_head_energy",
        "C01_compute": "C01_model_service_benefit",
        "F01_adaptive_fouling": "C01_model_service_benefit",
        "F02_sono_CIP": "C01_model_service_benefit",
        "resource_recovery": "BIO01_reclaimed_water",
        "OAE": "W01_reject_marine_discharge",
    }
    return table.get(name, f"UNMAPPED.{name}")


def bound_violations(ledger: CreditLedger) -> list[dict[str, Any]]:
    """Return every credit that exceeds its resource bound or double-claims."""
    violations: list[dict[str, Any]] = []

    for resource_id, entries in _group(ledger).items():
        bound = RESOURCE_BOUNDS.get(resource_id)
        total = sum(e.quantity for e in entries)

        if bound is None:
            if total > 0:
                violations.append({
                    "kind": "UNBOUNDED_RESOURCE",
                    "resource_id": resource_id,
                    "total": total,
                    "detail": "Credit taken against a resource with no declared bound.",
                })
            continue

        if is_unknown(bound.bound):
            if total > 0:
                violations.append({
                    "kind": "CREDIT_WITHOUT_ESTABLISHED_AVAILABILITY",
                    "resource_id": resource_id,
                    "total": total,
                    "units": bound.units,
                    "detail": f"Availability is UNKNOWN. {bound.basis}",
                })
        elif total > bound.bound + 1e-12:
            violations.append({
                "kind": "BOUND_EXCEEDED",
                "resource_id": resource_id,
                "total": total,
                "bound": bound.bound,
                "units": bound.units,
                "detail": bound.basis,
            })

        primaries = [e for e in entries if e.is_primary]
        if len(primaries) > 1:
            violations.append({
                "kind": "DOUBLE_PRIMARY_CREDIT",
                "resource_id": resource_id,
                "entry_ids": [e.entry_id for e in primaries],
                "detail": "One physical resource received more than one primary credit.",
            })

    return violations


def _group(ledger: CreditLedger) -> dict[str, list[CreditEntry]]:
    grouped: dict[str, list[CreditEntry]] = {}
    for entry in ledger.entries:
        grouped.setdefault(entry.resource_id, []).append(entry)
    return grouped
