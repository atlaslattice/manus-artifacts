"""Dongjiakou Locality Stream Register v0.2.

The architectural shift this module encodes:

    Dongjiakou is not a desalination plant with extras.
    It is a **locality-scale parent node** whose intelligence lives in the
    metered transfer edges between its subnodes.

v0.2 hardens four things found in review:

1. **No credit before measurement.** A modeled or projected stream cannot carry
   realized credit. v0.1 accidentally gave the modeled rooftop-PV stream a
   credit owner. Now: one ledger owner per physical quantity, a *candidate*
   allocation owner that is not a credit, and `realized_credit = 0` until an
   edge is MEASURED_PHYSICAL.

2. **Physical and opportunity edges are different things.** A graph that draws
   an operational steel-slag link and a hypothetical CO2 coupling the same way
   looks connected when it is not. Every edge now carries `edge_state`, and the
   register projects two graphs: the **Physical StreamGraph** (what flows today)
   and the **Opportunity Graph** (what could flow if contracts and gates close).

3. **A stream must not claim a sink it has not got.** v0.1 sent the entire
   17.93 Mm3/year product volume to the port, and drew brine straight to
   resource recovery. Neither sink is established. Both are now REPORTED_PHYSICAL
   to an external boundary, with separate CANDIDATE_COUPLING edges.

4. **Simulator validation is not locality clearance.** The software passing its
   epistemic checks is not the locality passing its physical vetoes. The two are
   reported under separate names.

And the standing rules:

    A stream may be counted once.
    A component may not claim a stream it does not own.
    An aggregate may never backfill a subnode UNKNOWN.
    NODE_PASS = AND(all component vetoes pass).
    An unresolved veto is not a pass.
"""

from __future__ import annotations

from typing import Any

# ---------------------------------------------------------------------------
# Evidence vocabulary
# ---------------------------------------------------------------------------
EVIDENCE_CLASSES = (
    "MEASURED",            # instrumented at this site, boundary stated
    "REPORTED",            # stated by a named source, not instrumented here
    "DERIVED",             # computed from reported/measured inputs
    "MODELED",             # produced by a model in this package
    "PLANNED",             # a documented plan or signed project not yet operating
    "UNDER_CONSTRUCTION",  # physically being built
    "VERIFIED_PROJECT",    # contract or official record of a real project
    "OPERATIONAL",         # observed operating infrastructure
    "SECONDARY",           # secondary summary, not primary data
    "UNKNOWN",             # no receipt exists
)

# ---------------------------------------------------------------------------
# Edge state — the sixteenth field, and the one that stops a graph lying
# ---------------------------------------------------------------------------
EDGE_STATES = (
    "MEASURED_PHYSICAL",    # instrumented flow, boundary stated
    "REPORTED_PHYSICAL",    # the flow is real and reported, not metered here
    "CONTRACTED",           # agreed, not yet flowing
    "UNDER_CONSTRUCTION",   # being built
    "PLANNED",              # in a plan, no contract
    "CANDIDATE_COUPLING",   # physically plausible, nothing agreed
    "REFERENCE_ONLY",       # an analogue from another site, not this one
)

#: What actually flows today.
PHYSICAL_EDGE_STATES = frozenset({"MEASURED_PHYSICAL", "REPORTED_PHYSICAL"})

#: What could flow. Ordered by commitment, strongest first.
OPPORTUNITY_EDGE_STATES = frozenset(
    {"CONTRACTED", "UNDER_CONSTRUCTION", "PLANNED", "CANDIDATE_COUPLING", "REFERENCE_ONLY"}
)

#: **Only a measured physical flow can realize credit.**
#: No module receives benefit before measurement.
CREDIT_REALIZING_EDGE_STATES = frozenset({"MEASURED_PHYSICAL"})

# ---------------------------------------------------------------------------
# Subnodes
# ---------------------------------------------------------------------------
SUBNODES: dict[str, str] = {
    "W01": "Water / desalination (UF+RO, 100,000 m3/day nameplate)",
    "C01": "Compute + ORCS advisory lattice (a load, never a source)",
    "P01": "Port / rail / logistics metabolism",
    "E01": "Grid / wind / PV / storage",
    "E02": "LNG cold-energy cascade and air separation",
    "R01": "Resource extraction from brine (Li, D, Mg/Ca/K/Br, trace)",
    "BIO01": "Organics / wastewater / nutrients",
    "M01": "Additive manufacturing / 3D print (a load; material credit only for assayed contracted output)",
    "MAT01": "Steel slag / tires / construction materials",
    "CHEM01": "Chemical-park process streams",
    "AGR01": "Grain / food / controlled-environment agriculture",
    "CARB01": "CO2 capture / utilization / mineralization",
    "ECO01": "Coastal and ecological monitoring",
    "GOV01": "Provenance / contracts / vetoes",
    "EXT01": "External boundary — current sink or fate not established at subnode level",
    "IND01": "Contracted industrial offtake cluster — Qingdao Special Steel, Jinneng Chemical, "
             "Bangtuo New Materials, West Coast Water Affairs (which further supplies Haiwan "
             "Chemical and Huicheng Environmental Protection)",
}

#: The 12-layer flywheel. Layer summary status is DERIVED from the streams,
#: never hand-written, so there is one source of epistemic truth.
FLYWHEEL_LAYER_SUBNODES: dict[int, tuple[str, ...]] = {
    1: ("C01",),
    2: ("E01", "E02"),
    3: ("W01",),
    4: ("E02", "CHEM01"),
    5: ("MAT01", "M01"),
    6: ("CARB01", "CHEM01"),
    7: ("ECO01",),
    8: ("BIO01",),
    9: ("AGR01",),
    10: (),  # jobs / community: no metered stream is registered
    11: ("P01",),
    12: ("GOV01",),
}

FLYWHEEL_LAYER_NAMES: dict[int, str] = {
    1: "Compute productivity", 2: "Energy", 3: "Water", 4: "Heat",
    5: "Materials", 6: "Carbon", 7: "Ocean / coastal ecology",
    8: "Pollution / toxins", 9: "Food / agriculture", 10: "Jobs / community",
    11: "Resilience", 12: "Governance / provenance",
}

#: What a layer is actually derived from.
#:
#: Deriving every layer from stream edges alone forced governance and ecology to
#: report NO_REGISTERED_STREAM, which is misleading: absence of a physical stream
#: is not absence of a functioning layer. Governance operates through vetoes,
#: permits and control rules; ecology through monitoring evidence. For Jobs,
#: NO_METERED_STREAM is genuinely the right answer.
LAYER_BASIS: dict[int, str] = {
    1: "STREAM_DERIVED",
    2: "STREAM_DERIVED",
    3: "STREAM_DERIVED",
    4: "STREAM_DERIVED",
    5: "STREAM_DERIVED",
    6: "STREAM_DERIVED",
    7: "EVIDENCE_DERIVED",
    8: "STREAM_DERIVED",
    9: "STREAM_DERIVED",
    10: "SOCIAL_METRIC_DERIVED",
    11: "STREAM_DERIVED",
    12: "CONTROL_DERIVED",
}

LAYER_BASES = (
    "STREAM_DERIVED",
    "CONTROL_DERIVED",
    "EVIDENCE_DERIVED",
    "SOCIAL_METRIC_DERIVED",
)

#: The complete stream schema. An edge missing a field is not a ledger entry.
STREAM_FIELDS = (
    "stream_id",
    "source_subnode",
    "sink_subnode",
    "material_or_energy",
    "quantity",
    "quality_composition",
    "temperature_pressure",
    "time_profile",
    "ownership",
    "contract_status",
    "evidence_class",
    "edge_state",
    "conversion_losses",
    "residual_fate",
    "vetoes",
    "primary_credit_owner",
    "candidate_allocation_owner",
    "realized_credit",
)

UNK = "UNKNOWN"
NONE = "NONE"


def _realizes_credit(edge_state: str, evidence_class: str, credit_owner: str) -> bool:
    """Credit requires all three: measured physical flow, MEASURED evidence, valid owner.

    Trusting `edge_state` alone was a real loophole. A stream tagged
    MEASURED_PHYSICAL while its evidence remained merely REPORTED would have
    realized credit, so the intended rule "no credit before measurement" was not
    enforced at the type boundary. All three conditions are now required, and an
    edge that is internally inconsistent is reported rather than silently
    withheld.
    """
    return (
        edge_state == "MEASURED_PHYSICAL"
        and evidence_class == "MEASURED"
        and credit_owner not in (NONE, UNK, "")
    )


def _s(stream_id: str, source: str, sink: str, what: str, quantity: str,
       evidence: str, edge_state: str, *, quality: str = UNK, temp_press: str = UNK,
       time_profile: str = UNK, ownership: str = UNK, contract: str = UNK,
       losses: str = UNK, residual: str = UNK, vetoes: tuple[str, ...] = (),
       credit_owner: str = NONE, allocation_owner: str = NONE) -> dict[str, Any]:
    """Build one first-class stream edge.

    `credit_owner` is the SINGLE ledger owner of the physical quantity.
    `allocation_owner` is who might later receive an allocated portion. An
    allocation owner is not a credit, and shared credit ownership is avoided
    entirely because that is where double counting sneaks back in.
    """
    if edge_state not in EDGE_STATES:
        raise ValueError(f"undeclared edge_state: {edge_state}")
    realized = _realizes_credit(edge_state, evidence, credit_owner)
    return {
        "stream_id": stream_id,
        "source_subnode": source,
        "sink_subnode": sink,
        "material_or_energy": what,
        "quantity": quantity,
        "quality_composition": quality,
        "temperature_pressure": temp_press,
        "time_profile": time_profile,
        "ownership": ownership,
        "contract_status": contract,
        "evidence_class": evidence,
        "edge_state": edge_state,
        "conversion_losses": losses,
        "residual_fate": residual,
        "vetoes": list(vetoes),
        "primary_credit_owner": credit_owner,
        "candidate_allocation_owner": allocation_owner,
        "realized_credit": realized,
    }


# ---------------------------------------------------------------------------
# The register
# ---------------------------------------------------------------------------
def known_streams() -> list[dict[str, Any]]:
    """Every known flow, split by whether it is physical or an opportunity."""
    return [
        # ================= PHYSICAL STREAMGRAPH ============================
        # What actually flows today. Note that neither the product water nor
        # the brine is drawn to a subnode sink, because neither sink is
        # established. Those are candidate edges below.

        # RESOLVED in review round 1: the sink is no longer unknown. The product
        # water is CONTRACTED to a named industrial cluster under a 2015 PPP, not
        # to the port. This replaces the previous EXT01 stream entirely rather
        # than adding to it, because it is the SAME water and may be counted once.
        _s("S-W01-IND-01", "W01", "IND01", "product water to contracted industrial offtakers",
           "17,930,000 m3/year actual (2025); 70,000 m3/day contractual take-or-pay minimum",
           "REPORTED", "REPORTED_PHYSICAL",
           quality="desalinated UF+RO permeate, treatment fee CNY 4.25/m3",
           temp_press="ambient, low pressure",
           time_profile="PPP guaranteed minimum volume; daily profile UNKNOWN",
           ownership="青岛水务海水淡化有限公司 (operator); PPP signed 2015",
           contract="PPP 2015: CNY 4.25/m3, 70,000 m3/day take-or-pay minimum. "
                    "Dongjiakou Water Supply Co buys at 4.25 and resells at 4.00, a "
                    "policy-driven loss subsidised by the district government.",
           losses="distribution losses UNKNOWN",
           residual="n/a",
           credit_owner="W01"),

        _s("S-W01-EXT-02", "W01", "EXT01", "reject-equivalent brine / concentrate",
           "21,914,444 m3/year at 45% recovery; 17,930,000 at 50%",
           "MODELED", "REPORTED_PHYSICAL",
           quality="brine chemistry UNKNOWN", temp_press=UNK,
           time_profile="follows product demand; profile UNKNOWN",
           ownership=UNK, contract=UNK, losses="n/a",
           residual="ecologically bounded discharge; discharge point UNKNOWN",
           vetoes=("INV-19",), credit_owner="W01"),

        _s("S-P01-EXT-01", "P01", "EXT01", "port throughput and logistics metabolism",
           "30 berths operating; first 400,000 t ore terminal handled >40 Mt in 2024 at ~90% utilisation",
           "OPERATIONAL", "REPORTED_PHYSICAL",
           quality="bulk ore, liquid chemicals, grain, containers",
           ownership="Qingdao Port", contract=UNK, losses=UNK, residual=UNK,
           credit_owner="P01"),

        _s("S-MAT01-M01-01", "MAT01", "M01", "steel slag and water slag to building materials",
           "operational processing link at Qingdao Special Steel",
           "OPERATIONAL", "REPORTED_PHYSICAL",
           quality="slag chemistry UNKNOWN", residual="residual fate UNKNOWN",
           ownership="Qingdao Runyi Fengtai New Materials", contract=UNK,
           credit_owner="MAT01"),

        _s("S-MAT01-M01-02", "MAT01", "M01", "waste tire pyrolysis products",
           "operational demonstration base; oil, carbon black, steel wire, gas",
           "OPERATIONAL", "REPORTED_PHYSICAL",
           quality="carbon black grade UNKNOWN",
           residual="claimed zero residue, unverified here",
           ownership="Doublestar Exista", contract=UNK, credit_owner="MAT01"),

        _s("S-MAT01-EXT-01", "MAT01", "EXT01", "regional construction waste generation",
           "Qingdao 27.879 Mt generated / 14.653 Mt utilised (2025)",
           "REPORTED", "REPORTED_PHYSICAL",
           quality="composition UNKNOWN", residual="processing rejects UNKNOWN",
           ownership="61 registered processors (37 operating)", contract=UNK,
           credit_owner="MAT01"),

        # ================= OPPORTUNITY GRAPH ==============================
        # What could flow, strongest commitment first.

        _s("S-E02-GRID-01", "E02", "E01", "LNG cold-energy power generation",
           "26,000,000 kWh/year PROJECTED at commissioning",
           "VERIFIED_PROJECT", "UNDER_CONSTRUCTION",
           quality="electrical", temp_press="cryogenic source",
           time_profile="follows LNG send-out; profile UNKNOWN",
           ownership="Sinopec Qingdao LNG / project SPV",
           contract="bid completed Jun 2026; detailed design and construction",
           losses="conversion losses UNKNOWN",
           residual="cold rejection to environment",
           allocation_owner="E02"),

        _s("S-E02-IND-01", "E02", "P01",
           "LNG cold-energy cooling service, avoiding external grid consumption",
           "8,000,000 kWh/year avoided PROJECTED",
           "VERIFIED_PROJECT", "UNDER_CONSTRUCTION",
           quality="cooling service", temp_press="cryogenic to chilled water",
           time_profile=UNK, ownership=UNK, contract="under detailed design",
           losses=UNK, residual=UNK, allocation_owner="E02"),

        _s("S-E02-CHEM01-01", "E02", "CHEM01",
           "cold-energy air separation output (LN2, LO2, LAr)",
           "~660 t/day air separation unit",
           "VERIFIED_PROJECT", "UNDER_CONSTRUCTION",
           quality="liquid nitrogen, oxygen, argon", temp_press="cryogenic",
           time_profile=UNK, ownership="Sichuan Air Separation Group",
           contract="signed 2025-09-02, CNY 230M", losses=UNK, residual=UNK,
           allocation_owner="E02"),

        _s("S-AGR01-BIO01-01", "AGR01", "BIO01", "food-processing residues and wastewater",
           "1.5 Mt/yr feed protein, 370 kt/yr refined oil, 15 kt/yr lecithin planned from 2027",
           "UNDER_CONSTRUCTION", "UNDER_CONSTRUCTION",
           quality="composition UNKNOWN", ownership="Louis Dreyfus Company",
           contract=UNK, residual=UNK, allocation_owner="AGR01"),

        _s("S-E01-C01-01", "E01", "C01", "regional wind and PV allocation",
           "~214 MW wind + ~81 MW PV proposed; node allocation UNKNOWN",
           "PLANNED", "PLANNED",
           quality="electrical", time_profile="hourly profile UNKNOWN",
           ownership="Qingdao Port Green Transformation Action Plan 2026-2028",
           contract="plan only, no PPA or meter", losses=UNK, residual=UNK,
           allocation_owner="E01"),

        _s("S-S01-C01-01", "E01", "C01",
           "on-site rooftop PV (S01_A / S01_B) technical sensitivity",
           "2.70619355 / 2.917982611 GWh/year MODELED; panels not installed",
           "MODELED", "CANDIDATE_COUPLING",
           quality="electrical", time_profile="hourly overlap UNKNOWN",
           ownership="node (proposed)", contract="no installation contract",
           losses=UNK, residual="n/a", allocation_owner="E01/S01"),

        _s("S-C01-W01-C1", "C01", "W01", "compute waste heat to CIP thermal duty",
           UNK, "UNKNOWN", "CANDIDATE_COUPLING",
           quality="low-grade heat, temperature UNKNOWN",
           vetoes=("INV-19",)),

        _s("S-BIO01-W01-C1", "BIO01", "W01",
           "reclaimed water displacing product water",
           UNK, "UNKNOWN", "CANDIDATE_COUPLING",
           residual="treatment residuals UNKNOWN", vetoes=("INV-19",)),

        _s("S-W01-P01-C1", "W01", "P01", "product water routed to port demand",
           "candidate: portion of 17.93 Mm3/year, allocation UNKNOWN. "
           "REVIEW ROUND 1 EVIDENCE AGAINST: the named PPP offtakers are Qingdao "
           "Special Steel, Jinneng Chemical, Bangtuo New Materials and West Coast "
           "Water Affairs. The port is NOT among them.",
           "UNKNOWN", "CANDIDATE_COUPLING",
           quality="desalinated permeate", ownership=UNK,
           contract="no port water supply contract located; and the port is absent "
                    "from the contracted offtaker list",
           allocation_owner="P01"),

        _s("S-W01-R01-C1", "W01", "R01",
           "reject-equivalent brine routed to resource extraction",
           "candidate: portion of 21.914 Mm3/year, allocation UNKNOWN",
           "UNKNOWN", "CANDIDATE_COUPLING",
           quality="brine chemistry UNKNOWN",
           residual="spent brine and eluate fate UNKNOWN",
           vetoes=("INV-19",), allocation_owner="R01"),

        _s("S-CHEM01-CARB01-01", "CHEM01", "CARB01",
           "CO2 from chemical and LNG processes",
           UNK, "UNKNOWN", "CANDIDATE_COUPLING",
           quality="concentration UNKNOWN"),

        _s("S-CARB01-M01-01", "CARB01", "M01", "CO2 to 3D-printed concrete curing",
           UNK, "UNKNOWN", "CANDIDATE_COUPLING",
           quality="purity UNKNOWN",
           residual="mineralized carbon; durability UNKNOWN",
           vetoes=("CARB-01",), allocation_owner="CARB01"),

        _s("S-CARB01-AGR01-01", "CARB01", "AGR01",
           "CO2 enrichment for controlled-environment agriculture",
           UNK, "UNKNOWN", "CANDIDATE_COUPLING", vetoes=("CARB-01",)),

        _s("S-MAT01-M01-C1", "MAT01", "M01",
           "construction waste to additive manufacturing feedstock — CAPABILITY GAP, NOT SURPLUS",
           "candidate: the zone has no processing capacity of its own. A Qingdao planning "
           "document identifies Dongjiakou and its surroundings as LACKING construction "
           "waste resource-utilisation enterprises, and recommends siting one to two "
           "facilities there.",
           "UNKNOWN", "CANDIDATE_COUPLING",
           quality="composition UNKNOWN",
           contract="no waste supply contract and no allocation. The relationship is "
                    "inverted from our prior assumption: this is not waste seeking a sink, "
                    "it is a missing processing capability the city plans to fill.",
           allocation_owner="M01"),

        _s("S-P01-C01-01", "P01", "C01", "shore power and port electrical demand",
           UNK, "UNKNOWN", "CANDIDATE_COUPLING"),

        _s("S-CHEM01-AGR01-01", "CHEM01", "AGR01", "industrial waste heat to greenhouses",
           "68 C class heat — reference from Xinfa Liaocheng, a DIFFERENT site",
           "SECONDARY", "REFERENCE_ONLY",
           quality="heat at ~68 C (reference system only)",
           temp_press="~68 C (reference)", ownership=UNK, contract=UNK,
           residual="not applicable to this locality"),
    ]


def physical_streams() -> list[dict[str, Any]]:
    """What actually flows today."""
    return [s for s in known_streams() if s["edge_state"] in PHYSICAL_EDGE_STATES]


def opportunity_streams() -> list[dict[str, Any]]:
    """What could flow if contracts, infrastructure and gates close."""
    return [s for s in known_streams() if s["edge_state"] in OPPORTUNITY_EDGE_STATES]


# ---------------------------------------------------------------------------
# Allocation conservation
# ---------------------------------------------------------------------------
def allocation_conservation(stream_id: str, measured_quantity: float,
                            allocations: dict[str, float], *,
                            measured_basis: str = UNK,
                            allocation_basis: str = UNK) -> dict[str, Any]:
    """Bounded allocation replacing shared credit ownership.

    The physical quantity has exactly one ledger owner; everyone else receives a
    bounded allocation from it. Four conditions must hold, and the first version
    of this function only checked the third:

      1. measured_quantity >= 0
      2. every allocation >= 0
      3. sum(allocations) <= measured_quantity
      4. measured_basis == allocation_basis, and both are stated

    Condition 4 matters as soon as this goes from one locality to dozens:
    `2.7 GWh/year` and `2.7 MWh/hour` must never enter the same conservation
    check, and a negative allocation is not a credit returned to the pool.
    """
    errors: list[str] = []
    if measured_quantity < 0:
        errors.append("measured_quantity is negative")
    negative = sorted(k for k, v in allocations.items() if v < 0)
    if negative:
        errors.append(f"negative allocation(s): {', '.join(negative)}")
    if measured_basis in (UNK, "") or allocation_basis in (UNK, ""):
        errors.append("unit/time basis is not stated for the quantity and its allocations")
    elif measured_basis != allocation_basis:
        errors.append(f"basis mismatch: measured '{measured_basis}' vs allocation '{allocation_basis}'")

    total = sum(allocations.values())
    if total > measured_quantity:
        errors.append(
            f"allocated {total} exceeds measured {measured_quantity}"
        )

    return {
        "stream_id": stream_id,
        "measured_quantity": measured_quantity,
        "measured_basis": measured_basis,
        "allocation_basis": allocation_basis,
        "allocations": dict(allocations),
        "total_allocated": total,
        "unallocated": measured_quantity - total,
        "conserved": not errors,
        "errors": errors,
    }


# ---------------------------------------------------------------------------
# Veto evaluation
# ---------------------------------------------------------------------------
VETO_DEFINITIONS: dict[str, str] = {
    "INV-19": "Downstream water quality must not deteriorate. A facility may not claim net positive while it does.",
    "ECO-01": "Coastal and ecological status must be measured at primary level, not inferred from secondary summaries.",
    "CERT-01": "MARINE and PRESSURE-BOUNDARY components must be certified. An uncertified printed "
               "part is a safety problem, not a saving. SCOPE NARROWED in review round 1: concrete "
               "structural printing DOES have a current Chinese standards path (T/CBMF 378-2026 / "
               "T/CCPA 90-2026 printers, effective 2026-09-06; T/CCPA 85-2025 / T/CBMF 366-2025 "
               "premix; and a national qualification standard in development based on "
               "ISO/ASTM 52939:2023). No classification-society or pressure-vessel code pathway "
               "was found.",
    "CARB-01": "Transferred CO2 may be counted once. CO2 used in curing cannot also be claimed as permanent removal.",
    "GRID-01": "Renewable attributes may not be claimed by node, generator and PPA buyer simultaneously.",
}

#: UNRESOLVED and FAIL are semantically distinct. Neither is a pass.
VETO_STATES = ("PASS", "FAIL", "UNRESOLVED")


def veto_register() -> dict[str, dict[str, str]]:
    """Current veto state at Node-001."""
    return {
        "INV-19": {
            "definition": VETO_DEFINITIONS["INV-19"],
            "state": "UNRESOLVED",
            "why": "Review round 1 advanced this without resolving it. The outfall is now located "
                   "with coordinates (119°44'33.10\"E, 35°34'47.17\"N, between the west breakwater "
                   "and the eastern trestle section) and an approval instrument exists "
                   "(鲁海渔函[2015]330号). A 2024 peer-reviewed study finds impact confined within "
                   "200 m of the outfall. But that study is a SECONDARY analysis, and no discharge "
                   "permit number or permitted limits were located. A secondary summary may never "
                   "be promoted to a primary ecological receipt.",
        },
        "ECO-01": {
            "definition": VETO_DEFINITIONS["ECO-01"],
            "state": "UNRESOLVED",
            "why": "Confirmed as a genuine gap, not a search failure. Review round 1 searched "
                   "directly for the 2017 and 2022 Ocean University of China station-level series "
                   "and returned NULL. Only secondary summaries are publicly available. This "
                   "remains the critical path for the node.",
        },
        "CERT-01": {
            "definition": VETO_DEFINITIONS["CERT-01"],
            "state": "UNRESOLVED",
            "why": "Narrowed, but still unresolved. Concrete structural AM has a current standards "
                   "path, so the veto does not block material reuse or structural printing. It "
                   "blocks additively manufactured MARINE and PRESSURE-BOUNDARY components, for "
                   "which no classification-society or pressure-vessel code pathway was located. "
                   "This makes the veto sharper, not softer: it now names exactly what cannot be "
                   "cleared.",
        },
        "CARB-01": {
            "definition": VETO_DEFINITIONS["CARB-01"],
            "state": "UNRESOLVED",
            "why": "No CO2 flow is metered and no transfer ledger entry exists yet.",
        },
        "GRID-01": {
            "definition": VETO_DEFINITIONS["GRID-01"],
            "state": "UNRESOLVED",
            "why": "The POLICY route is now confirmed but node participation is not. The Qingdao "
                   "Port Green Transformation Three-Year Action Plan (2026-2028) is official and "
                   "names roughly 214 MW wind and 81 MW PV around Qianwan and Dongjiakou with "
                   "dedicated transmission lines. National 2026 green-direct rules allow "
                   "multi-user park projects and give PRIORITY support to compute facilities at "
                   ">=60% self-consumption and >=30% load share. No document names this node as an "
                   "enrolled user, and no PPA, meter or allocation exists. A plan is not an "
                   "allocation.",
        },
    }


def node_pass(vetoes: dict[str, dict[str, str]] | None = None) -> dict[str, Any]:
    """NODE_PASS = AND(all vetoes pass). An unresolved veto is not a pass."""
    reg = vetoes if vetoes is not None else veto_register()
    states = {k: v["state"] for k, v in reg.items()}
    all_pass = all(s == "PASS" for s in states.values())
    return {
        "rule": "NODE_PASS = AND(all component vetoes pass)",
        "states": states,
        "node_pass": all_pass,
        "unresolved": sorted(k for k, s in states.items() if s == "UNRESOLVED"),
        "failed": sorted(k for k, s in states.items() if s == "FAIL"),
        "verdict": "NODE_PASS_ESTABLISHED" if all_pass else "NODE_PASS_NOT_ESTABLISHED",
        "explanation": (
            "An unresolved veto is not a pass, and an unresolved veto is not a "
            "failure either. It is an absence of evidence. A component that cannot "
            "be evaluated cannot be cleared, and no profit elsewhere resolves it."
        ),
    }


# ---------------------------------------------------------------------------
# Clearance separation
# ---------------------------------------------------------------------------
def clearance_status() -> dict[str, Any]:
    """Two different questions that must never be read as one.

    SIMULATOR_VALIDATION asks whether the software passed its own epistemic
    checks. LOCALITY_CLEARANCE asks whether the physical node passed its
    physical vetoes. The simulator can pass *because* it refused to clear.
    """
    return {
        "SIMULATOR_VALIDATION": {
            "question": "Did the software pass its epistemic checks?",
            "answer": "PASS",
            "note": "15 of 16 gates pass on the real evidence base; 154/155 values reproduce.",
        },
        "LOCALITY_CLEARANCE": {
            "question": "Has the physical locality node passed its vetoes?",
            "answer": "NOT_ESTABLISHED",
            "note": "5 of 5 vetoes UNRESOLVED. No clearance is claimed.",
        },
        "warning": (
            "SIMULATOR_VALIDATION = PASS is compatible with "
            "LOCALITY_CLEARANCE = NOT_ESTABLISHED. The simulator passed because it "
            "correctly refused to clear the physical node. Never present the gate "
            "count as evidence that Dongjiakou itself has passed certification, "
            "ecology or grid gates."
        ),
    }


# ---------------------------------------------------------------------------
# Scale comparison
# ---------------------------------------------------------------------------
def scale_comparison() -> dict[str, Any]:
    """Compare the locality's flows against the W01 baseline."""
    w01_process_gwh = 39.446
    e02_generation_gwh = 26.0
    e02_cooling_avoided_gwh = 8.0
    # NOTE: these are NOT one physical stream. One is projected generation, the
    # other is projected avoided grid consumption from cooling. Their sum is an
    # electrical-system impact, not a flow.
    e02_impact_gwh = e02_generation_gwh + e02_cooling_avoided_gwh

    it_40mw_gwh = 40_000.0 / 1000.0 * 8.76
    facility_40mw_gwh = it_40mw_gwh * 1.25

    return {
        "w01_2025_process_energy_gwh": w01_process_gwh,
        "e02_generation_gwh": e02_generation_gwh,
        "e02_cooling_avoided_gwh": e02_cooling_avoided_gwh,
        "projected_grid_electricity_impact_gwh": e02_impact_gwh,
        "e02_impact_share_of_w01_process_energy": e02_impact_gwh / w01_process_gwh,
        "e02_note": (
            "26 GWh is projected generation; 8 GWh is projected avoided grid "
            "consumption from cooling. They are separate edges and are never "
            "summed into one physical energy stream. The total is an "
            "electrical-system impact only."
        ),
        "e02_status": "VERIFIED_PROJECT_UNDER_CONSTRUCTION_CURRENT_CREDIT_ZERO",
        "c01_40mw_it_gwh": it_40mw_gwh,
        "c01_40mw_facility_gwh_at_pue_1_25": facility_40mw_gwh,
        "c01_40mw_share_of_w01_process_energy": facility_40mw_gwh / w01_process_gwh,
        "c01_40mw_share_of_e02_impact": facility_40mw_gwh / e02_impact_gwh,
        "finding": (
            "The LNG cold-energy cascade is projected at a 34 GWh/year "
            "electrical-system impact across generation and avoided cooling, "
            "about 86% of W01's entire 2025 process energy. A 40 MW compute "
            "subnode would draw 438 GWh/year at the PUE 1.25 reference, about 11x "
            "W01's process energy and about 13x that whole impact. The locality's "
            "energy resources are large; the compute load is larger. Neither "
            "figure may be netted against the other, and both are zero credit."
        ),
    }


# ---------------------------------------------------------------------------
# Mechanical flywheel derivation
# ---------------------------------------------------------------------------
def price_anchors() -> dict[str, Any]:
    """The first real prices in the build, from review round 1.

    Before this, every CNY line in Runs 0-3 was UNKNOWN. The 2015 PPP gives a
    treatment fee and a take-or-pay minimum. It also reveals something important:
    actual 2025 offtake sits BELOW the contractual minimum, so the take-or-pay
    clause is binding.
    """
    actual_per_day = 17_930_000.0 / 365.0
    guaranteed = 70_000.0
    fee = 4.25
    resale = 4.00
    return {
        "water_treatment_fee_cny_per_m3": fee,
        "water_resale_cny_per_m3": resale,
        "resale_margin_cny_per_m3": resale - fee,
        "guaranteed_minimum_m3_per_day": guaranteed,
        "actual_2025_m3_per_year": 17_930_000.0,
        "actual_2025_m3_per_day": actual_per_day,
        "take_or_pay_shortfall_m3_per_day": guaranteed - actual_per_day,
        "take_or_pay_is_binding": actual_per_day < guaranteed,
        "electricity_cny_per_kwh_2018_2020": 0.555,
        "electricity_2026": "UNKNOWN",
        "findings": [
            "The plant is paid at the guaranteed volume rate when actual usage is lower, and "
            f"actual 2025 offtake ({actual_per_day:,.0f} m3/day) is BELOW the contractual minimum "
            f"({guaranteed:,.0f} m3/day), so the take-or-pay clause is binding.",
            f"The distribution entity buys at CNY {fee} and resells at CNY {resale}, a "
            f"CNY {resale - fee:.2f}/m3 policy-driven loss subsidised by the district government. "
            "This is a FINANCIAL-RISK finding, not merely an input price: a margin-negative "
            "distribution layer depends on continued subsidy.",
            "The 2018-2020 electricity figure of CNY 0.555/kWh with a demand-charge waiver is a "
            "historical anchor only. The waiver expired at the end of 2025, so the 2026 shape is "
            "genuinely UNKNOWN rather than merely unpublished, and no CNY line may be carried "
            "forward on it.",
        ],
    }


def derive_flywheel(streams: list[dict[str, Any]] | None = None) -> dict[int, dict[str, Any]]:
    """Derive each layer's status from the register, not from a second opinion.

    Still mechanical, but the status vocabulary depends on what the layer is
    actually derived from, so that governance and ecology are not made to
    masquerade as material flows.
    """
    streams = streams if streams is not None else known_streams()
    out: dict[int, dict[str, Any]] = {}
    for layer, subnodes in FLYWHEEL_LAYER_SUBNODES.items():
        touching = [
            s for s in streams
            if s["source_subnode"] in subnodes or s["sink_subnode"] in subnodes
        ]
        states: dict[str, int] = {}
        for s in touching:
            states[s["edge_state"]] = states.get(s["edge_state"], 0) + 1
        physical = [s for s in touching if s["edge_state"] in PHYSICAL_EDGE_STATES]
        basis = LAYER_BASIS[layer]

        if basis == "STREAM_DERIVED":
            status = (
                "NO_REGISTERED_STREAM" if not touching
                else "PHYSICAL_FLOW_PRESENT" if physical
                else "OPPORTUNITY_ONLY"
            )
        elif basis == "CONTROL_DERIVED":
            status = "CONTROLLED_BY_VETO_AND_PERMIT_STATE"
        elif basis == "EVIDENCE_DERIVED":
            status = "AWAITING_PRIMARY_ECOLOGICAL_EVIDENCE"
        else:  # SOCIAL_METRIC_DERIVED
            status = "NO_METERED_STREAM"

        out[layer] = {
            "layer": FLYWHEEL_LAYER_NAMES[layer],
            "layer_basis": basis,
            "subnodes": list(subnodes),
            "streams": len(touching),
            "physical_streams": len(physical),
            "edge_states": states,
            "realized_credit": sum(1 for s in touching if s["realized_credit"]),
            "status": status,
        }
    return out


def stream_inconsistencies(streams: list[dict[str, Any]] | None = None) -> list[dict[str, str]]:
    """Edges whose evidence class contradicts their edge state.

    A MEASURED_PHYSICAL edge must carry MEASURED evidence. Where it does not,
    the edge is internally inconsistent and is reported rather than silently
    denied credit, so the defect is visible instead of absorbed.
    """
    streams = streams if streams is not None else known_streams()
    out: list[dict[str, str]] = []
    for s in streams:
        physical_claim = s["edge_state"] == "MEASURED_PHYSICAL"
        measured_evidence = s["evidence_class"] == "MEASURED"
        if physical_claim != measured_evidence:
            out.append({
                "stream_id": s["stream_id"],
                "edge_state": s["edge_state"],
                "evidence_class": s["evidence_class"],
                "problem": (
                    "claims a measured physical flow without measured evidence"
                    if physical_claim else
                    "claims measured evidence without a measured physical flow"
                ),
            })
    return out


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
def _field_research_summary() -> dict[str, Any]:
    """Round-1 field research, folded in as receipts."""
    from . import receipts as _rc
    return _rc.round_summary()


def contradictions() -> list[dict[str, Any]]:
    """Working assumptions the field research actively overturned.

    These are the most valuable outcomes of a review round, because they correct
    an assumption before it propagates to 120 localities.
    """
    from . import receipts as _rc
    return _rc.contradictions()


def run() -> dict[str, Any]:
    streams = known_streams()
    physical = physical_streams()
    opportunity = opportunity_streams()

    missing_fields = [s["stream_id"] for s in streams if any(f not in s for f in STREAM_FIELDS)]
    by_evidence: dict[str, int] = {}
    by_edge: dict[str, int] = {}
    for s in streams:
        by_evidence[s["evidence_class"]] = by_evidence.get(s["evidence_class"], 0) + 1
        by_edge[s["edge_state"]] = by_edge.get(s["edge_state"], 0) + 1

    return {
        "artifact_id": "DJK-NODE-001-LOCALITY-STREAM-REGISTER-v0.2",
        "supersedes": "DJK-NODE-001-LOCALITY-STREAM-REGISTER-v0.1",
        "status": "PUBLIC_CANDIDATE_NON_CANON",
        "boundary": "Dongjiakou locality node — a parent node containing subnodes",
        "v0_2_changes": [
            "Realized credit now requires MEASURED_PHYSICAL. Modeled and projected streams carry none.",
            "Credit ownership is singular; allocation is separate and conservation-bounded.",
            "Every edge carries edge_state, and the register projects two graphs.",
            "No stream claims a sink that is not established; product and brine route to an external boundary.",
            "Simulator validation and locality clearance are reported separately.",
            "The flywheel layer summary is derived from the streams, not hand-written.",
            "The 34 GWh figure is renamed to an electrical-system impact, not a stream.",
            "Credit now requires edge_state == MEASURED_PHYSICAL AND evidence == MEASURED AND a valid owner; edge_state alone was a loophole.",
            "Allocation conservation rejects negative allocations and requires a stated matching unit/time basis.",
            "Each flywheel layer declares a layer_basis, so governance and ecology are not forced to masquerade as material flows.",
        ],
        "governing_rules": [
            "A stream may be counted once.",
            "A component may not claim a stream it does not own.",
            "No module receives benefit before measurement.",
            "An aggregate may never backfill a subnode UNKNOWN.",
            "NODE_PASS = AND(all component vetoes pass).",
            "An unresolved veto is not a pass, and is not a failure either.",
        ],
        "subnodes": SUBNODES,
        "stream_schema_fields": list(STREAM_FIELDS),
        "edge_states": list(EDGE_STATES),
        "credit_realizing_edge_states": sorted(CREDIT_REALIZING_EDGE_STATES),
        "layer_bases": list(LAYER_BASES),
        "physical_streamgraph": physical,
        "opportunity_graph": opportunity,
        "flywheel_layers": derive_flywheel(streams),
        "counts": {
            "subnodes": len(SUBNODES),
            "streams_total": len(streams),
            "physical_streams": len(physical),
            "opportunity_streams": len(opportunity),
            "streams_realizing_credit": sum(1 for s in streams if s["realized_credit"]),
            "streams_with_incomplete_schema": len(missing_fields),
            "streams_with_inconsistent_evidence": len(stream_inconsistencies(streams)),
            "by_evidence_class": by_evidence,
            "by_edge_state": by_edge,
        },
        "stream_inconsistencies": stream_inconsistencies(streams),
        "vetoes": veto_register(),
        "node_pass": node_pass(),
        "price_anchors": price_anchors(),
        "field_research": _field_research_summary(),
        "clearance": clearance_status(),
        "scale": scale_comparison(),
        "pareto_rule": (
            "The optimizer is a Pareto front, not a scalar score. There is no "
            "single number that can rank a locality, because a scalar score is "
            "exactly what allows a local failure to be washed out by a gain "
            "somewhere else."
        ),
        "what_this_changes": (
            "Runs 0-3 do not become obsolete. They become the audited history of "
            "one subnode. The locality is not a bigger plant; it is a metabolism, "
            "and the intelligence lives in the metered edges between subnodes."
        ),
        "next_receipts": [
            "Dongjiakou circular-economy implementation plan: which arrows the locality may legally connect",
            "Chemical-park utility map: waste heat, steam, CO2, wastewater by plant",
            "LNG cold-energy cascade EIA: thermal output specs and CO2 liquefaction potential",
            "Pilot base project list: which of the 30 concurrent slots are materials/3D printing",
            "Node-001 green-direct eligibility confirmation",
            "Dongjiakou construction-waste allocation (contractual)",
        ],
    }
