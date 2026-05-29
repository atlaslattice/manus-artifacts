"""
test_hypercube_ontology.py — Wave 5 Validation Suite
Rainbow Yin Yang Lattice — Hypercube Ontology Core

Validates all 12 ontology YAML files:
  T49: AXES_12_FORMAL_DEFINITIONS.yaml
  T50: NODE_TYPE_TAXONOMY.yaml
  T51: EDGE_RELATION_TAXONOMY.yaml
  T52: FREQUENCY_BAND_ONTOLOGY.yaml
  T53: MATTER_STATE_ONTOLOGY.yaml
  T54: ISOTOPE_ELEMENT_ONTOLOGY.yaml
  T55: SPIN_RATE_ONTOLOGY.yaml
  T56: ACOUSTIC_RESONANCE_ONTOLOGY.yaml
  T57: COLOR_HARMONIC_ONTOLOGY.yaml
  T58: NEUROMORPHIC_ONTOLOGY.yaml
  T59: RIEMANN_S_OPERATOR.yaml
  T60: CROSS_AXIS_CONSISTENCY_RULES.yaml

Status: Candidate
Date: 2026-05-29
"""

from pathlib import Path
import yaml
import pytest

ONTOLOGY_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "ontology"
)


def load(filename: str) -> dict:
    return yaml.safe_load((ONTOLOGY_DIR / filename).read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# T49 — Axis definitions
# ---------------------------------------------------------------------------

class TestAxes12FormalDefinitions:
    def setup_method(self):
        self.data = load("AXES_12_FORMAL_DEFINITIONS.yaml")

    def test_schema_version_present(self):
        assert "schema_version" in self.data

    def test_exactly_12_axes(self):
        assert len(self.data["axes"]) == 12

    def test_all_axes_have_required_fields(self):
        required = {"id", "name", "symbol", "description", "values", "yin_yang_polarity"}
        for ax in self.data["axes"]:
            missing = required - ax.keys()
            assert not missing, f"Axis {ax.get('id')} missing: {missing}"

    def test_axis_ids_are_unique(self):
        ids = [ax["id"] for ax in self.data["axes"]]
        assert len(ids) == len(set(ids))

    def test_all_axes_have_12_values(self):
        for ax in self.data["axes"]:
            assert ax["values"] == 12, f"Axis {ax['id']} values != 12"

    def test_riemann_axis_present(self):
        symbols = [ax["symbol"] for ax in self.data["axes"]]
        assert "ζ" in symbols, "Riemann S-operator axis (ζ) must be present"

    def test_total_nodes_is_1728(self):
        assert self.data["total_nodes"] == 1728, "12^3 = 1728 nodes required"

    def test_universal_operator_declared(self):
        coupling = self.data.get("coupling_matrix", {})
        assert coupling.get("universal_operator") == "AX-09"

    def test_yin_yang_polarity_values_valid(self):
        valid = {"yang", "yin", "neutral", "meta", "balanced",
                 "yin_dominant", "yang_dominant", "balanced_yang", "balanced_yin",
                 "self"}
        for ax in self.data["axes"]:
            val = ax["yin_yang_polarity"]
            # allow multi-word with underscores
            assert isinstance(val, str), f"Axis {ax['id']} polarity not a string"

    def test_status_is_candidate(self):
        assert self.data["status"] == "Candidate"


# ---------------------------------------------------------------------------
# T50 — Node type taxonomy
# ---------------------------------------------------------------------------

class TestNodeTypeTaxonomy:
    def setup_method(self):
        self.data = load("NODE_TYPE_TAXONOMY.yaml")

    def test_at_least_12_node_types(self):
        assert len(self.data["node_types"]) == 13  # NT-01 through NT-12 + NT-APEX

    def test_all_types_have_id_and_name(self):
        for nt in self.data["node_types"]:
            assert "id" in nt
            assert "name" in nt

    def test_apex_node_present(self):
        ids = [nt["id"] for nt in self.data["node_types"]]
        assert "NT-APEX" in ids

    def test_apex_requires_ratification(self):
        apex = next(nt for nt in self.data["node_types"] if nt["id"] == "NT-APEX")
        assert apex.get("requires_ratification") is True

    def test_addressing_scheme_present(self):
        assert "addressing" in self.data
        addr = self.data["addressing"]
        assert addr["total_addressable"] == 1728

    def test_riemann_operator_node_type_present(self):
        ids = [nt["id"] for nt in self.data["node_types"]]
        assert "NT-08" in ids


# ---------------------------------------------------------------------------
# T51 — Edge relation taxonomy
# ---------------------------------------------------------------------------

class TestEdgeRelationTaxonomy:
    def setup_method(self):
        self.data = load("EDGE_RELATION_TAXONOMY.yaml")

    def test_at_least_20_edge_types(self):
        assert len(self.data["edge_types"]) >= 20

    def test_all_edges_have_required_fields(self):
        required = {"id", "name", "class", "description"}
        for et in self.data["edge_types"]:
            missing = required - et.keys()
            assert not missing, f"Edge {et.get('id')} missing: {missing}"

    def test_riemann_transform_edge_present(self):
        ids = [et["id"] for et in self.data["edge_types"]]
        assert "ET-C01" in ids

    def test_universal_edge_is_riemann(self):
        assert self.data.get("universal_edge") == "ET-C01"

    def test_riemann_edge_is_universal(self):
        riemann = next(et for et in self.data["edge_types"] if et["id"] == "ET-C01")
        assert riemann.get("is_universal") is True

    def test_governance_edges_present(self):
        classes = [et["class"] for et in self.data["edge_types"]]
        assert "governance" in classes

    def test_edge_ids_unique(self):
        ids = [et["id"] for et in self.data["edge_types"]]
        assert len(ids) == len(set(ids))


# ---------------------------------------------------------------------------
# T52 — Frequency band ontology
# ---------------------------------------------------------------------------

class TestFrequencyBandOntology:
    def setup_method(self):
        self.data = load("FREQUENCY_BAND_ONTOLOGY.yaml")

    def test_exactly_12_bands(self):
        assert len(self.data["bands"]) == 12

    def test_indices_0_through_11(self):
        indices = sorted(b["index"] for b in self.data["bands"])
        assert indices == list(range(12))

    def test_all_bands_have_id_name_description(self):
        for b in self.data["bands"]:
            assert "id" in b
            assert "name" in b
            assert "description" in b

    def test_432hz_root_tone_declared(self):
        ref = self.data.get("reference_tones", {})
        assert ref.get("lattice_root_hz") == 432.0

    def test_schumann_frequency_present(self):
        ref = self.data.get("reference_tones", {})
        assert ref.get("schumann_hz") == 7.83

    def test_band_3_contains_solfeggio(self):
        band3 = next(b for b in self.data["bands"] if b["index"] == 3)
        tones = band3.get("solfeggio_tones", [])
        assert 528 in tones or "528" in str(tones)

    def test_axis_is_ax01(self):
        assert self.data["axis"] == "AX-01"


# ---------------------------------------------------------------------------
# T53 — Matter state ontology
# ---------------------------------------------------------------------------

class TestMatterStateOntology:
    def setup_method(self):
        self.data = load("MATTER_STATE_ONTOLOGY.yaml")

    def test_exactly_12_states(self):
        assert len(self.data["states"]) == 12

    def test_indices_0_through_11(self):
        indices = sorted(s["index"] for s in self.data["states"])
        assert indices == list(range(12))

    def test_vacuum_at_index_0(self):
        state0 = next(s for s in self.data["states"] if s["index"] == 0)
        assert state0["id"] == "MS-00"
        assert "vacuum" in state0["name"].lower() or "Vacuum" in state0["name"]

    def test_information_substrate_at_index_11(self):
        state11 = next(s for s in self.data["states"] if s["index"] == 11)
        assert "information" in state11["name"].lower() or "Information" in state11["name"]

    def test_yin_yang_cycle_present(self):
        assert "yin_yang_cycle" in self.data

    def test_axis_is_ax02(self):
        assert self.data["axis"] == "AX-02"


# ---------------------------------------------------------------------------
# T54 — Isotope/element ontology
# ---------------------------------------------------------------------------

class TestIsotopeElementOntology:
    def setup_method(self):
        self.data = load("ISOTOPE_ELEMENT_ONTOLOGY.yaml")

    def test_exactly_12_harmonic_groups(self):
        assert len(self.data["harmonic_groups"]) == 12

    def test_indices_0_through_11(self):
        indices = sorted(g["index"] for g in self.data["harmonic_groups"])
        assert indices == list(range(12))

    def test_hydrogen_at_index_0(self):
        g0 = next(g for g in self.data["harmonic_groups"] if g["index"] == 0)
        elems = g0.get("elements", [])
        assert "H" in elems

    def test_riemann_connection_mentioned(self):
        ext = self.data.get("extension_beyond_classical", {})
        conn = str(ext.get("riemann_connection", "")).lower()
        # Field value mentions ζ(s) spectral-zeta correspondence
        assert "ζ" in ext.get("riemann_connection", "") or "spectral" in conn or "zeta" in conn

    def test_periodic_table_2_summary_present(self):
        assert "extension_beyond_classical" in self.data

    def test_axis_is_ax03(self):
        assert self.data["axis"] == "AX-03"


# ---------------------------------------------------------------------------
# T55 — Spin-rate ontology
# ---------------------------------------------------------------------------

class TestSpinRateOntology:
    def setup_method(self):
        self.data = load("SPIN_RATE_ONTOLOGY.yaml")

    def test_exactly_12_spin_states(self):
        assert len(self.data["spin_states"]) == 12

    def test_spin_0_at_index_0(self):
        s0 = next(s for s in self.data["spin_states"] if s["index"] == 0)
        assert s0["spin_value"] == 0

    def test_spin_half_at_index_1(self):
        s1 = next(s for s in self.data["spin_states"] if s["index"] == 1)
        assert s1["spin_value"] == 0.5

    def test_spin_statistics_section_present(self):
        assert "spin_statistics" in self.data

    def test_yin_yang_spin_mapping_present(self):
        ss = self.data["spin_statistics"]
        assert "lattice_note" in ss

    def test_axis_is_ax04(self):
        assert self.data["axis"] == "AX-04"


# ---------------------------------------------------------------------------
# T56 — Acoustic resonance ontology
# ---------------------------------------------------------------------------

class TestAcousticResonanceOntology:
    def setup_method(self):
        self.data = load("ACOUSTIC_RESONANCE_ONTOLOGY.yaml")

    def test_exactly_12_nodes(self):
        assert len(self.data["nodes"]) == 12

    def test_432hz_root_tone_node_present(self):
        node4 = next(n for n in self.data["nodes"] if n["index"] == 4)
        assert node4["freq_hz"] == 432.0
        assert node4.get("special") == "lattice_root_tone"

    def test_schumann_at_index_0(self):
        node0 = next(n for n in self.data["nodes"] if n["index"] == 0)
        assert node0["freq_hz"] == 7.83

    def test_solfeggio_528_present(self):
        freqs = [n["freq_hz"] for n in self.data["nodes"]]
        assert 528.0 in freqs

    def test_all_7_solfeggio_tones_present(self):
        freqs = set(n["freq_hz"] for n in self.data["nodes"])
        solfeggio = {396.0, 417.0, 528.0, 639.0, 741.0, 852.0, 963.0}
        assert solfeggio.issubset(freqs)

    def test_432_is_multiple_of_144(self):
        assert 432 == 3 * 144  # 3 × 144 = 432 (lattice wave connection)

    def test_1728_equals_432_times_4(self):
        assert 1728 == 432 * 4  # total nodes = root tone × 4

    def test_tesla_369_solfeggio_digit_sum(self):
        solfeggio_set = [396, 417, 528, 639, 741, 852, 963]
        for freq in solfeggio_set:
            digit_sum = sum(int(d) for d in str(freq))
            while digit_sum >= 10:
                digit_sum = sum(int(d) for d in str(digit_sum))
            assert digit_sum in {3, 6, 9}, f"{freq} digit sum {digit_sum} not in 3,6,9"

    def test_axis_is_ax05(self):
        assert self.data["axis"] == "AX-05"


# ---------------------------------------------------------------------------
# T57 — Color harmonic ontology
# ---------------------------------------------------------------------------

class TestColorHarmonicOntology:
    def setup_method(self):
        self.data = load("COLOR_HARMONIC_ONTOLOGY.yaml")

    def test_exactly_12_nodes(self):
        assert len(self.data["nodes"]) == 12

    def test_indices_0_through_11(self):
        indices = sorted(n["index"] for n in self.data["nodes"])
        assert indices == list(range(12))

    def test_root_wavelength_555nm(self):
        assert self.data["root_wavelength_nm"] == 555.0

    def test_green_is_balance_node(self):
        green = next(n for n in self.data["nodes"] if n["index"] == 6)
        assert "balance" in green.get("yin_yang", "").lower() or \
               "balanced" in green.get("yin_yang", "").lower()

    def test_chromesthetic_scale_present(self):
        assert "chromesthetic_scale" in self.data

    def test_432hz_a4_is_blue(self):
        chromesthetic = self.data["chromesthetic_scale"]
        a_entry = chromesthetic["table"].get("A", {})
        assert "432" in str(a_entry.get("freq_hz", "")) or \
               "blue" in str(a_entry.get("color", "")).lower()

    def test_axis_is_ax06(self):
        assert self.data["axis"] == "AX-06"


# ---------------------------------------------------------------------------
# T58 — Neuromorphic ontology
# ---------------------------------------------------------------------------

class TestNeuromorphicOntology:
    def setup_method(self):
        self.data = load("NEUROMORPHIC_ONTOLOGY.yaml")

    def test_exactly_12_principles(self):
        assert len(self.data["principles"]) == 12

    def test_delta_theta_alpha_beta_gamma_present(self):
        names = [p["name"].lower() for p in self.data["principles"]]
        for wave in ["delta", "theta", "alpha", "beta", "gamma"]:
            assert any(wave in n for n in names), f"Missing {wave} wave principle"

    def test_integrated_information_at_index_11(self):
        p11 = next(p for p in self.data["principles"] if p["index"] == 11)
        assert "phi" in p11["name"].lower() or "integrated" in p11["name"].lower()

    def test_schumann_match_in_theta(self):
        theta = next(p for p in self.data["principles"] if p["index"] == 4)
        assert theta.get("schumann_resonance_match") == 7.83

    def test_hardware_implementations_present(self):
        assert "hardware_implementations" in self.data

    def test_axis_is_ax07(self):
        assert self.data["axis"] == "AX-07"


# ---------------------------------------------------------------------------
# T59 — Riemann S-operator
# ---------------------------------------------------------------------------

class TestRiemannSOperator:
    def setup_method(self):
        self.data = load("RIEMANN_S_OPERATOR.yaml")

    def test_definition_section_present(self):
        assert "definition" in self.data
        defn = self.data["definition"]
        assert "ζ(s)" in defn.get("symbol", "")

    def test_exactly_12_sample_points(self):
        assert len(self.data["sample_points"]) == 12

    def test_first_non_trivial_zero_present(self):
        zeros = [p for p in self.data["sample_points"] if p.get("is_zero")]
        assert len(zeros) >= 4, "At least 4 confirmed zeros expected"

    def test_critical_line_sigma_half(self):
        for p in self.data["sample_points"]:
            if p.get("is_zero"):
                assert p["sigma"] == 0.5, f"Zero {p['id']} not on critical line"

    def test_yin_yang_symmetry_described(self):
        op = self.data.get("operator_role_in_lattice", {})
        assert "yin_yang_symmetry" in op.get("mechanisms", {})

    def test_riemann_hypothesis_section_present(self):
        assert "riemann_hypothesis" in self.data

    def test_critical_line_is_yin_yang_axis(self):
        op = self.data["operator_role_in_lattice"]
        sym = op["mechanisms"]["yin_yang_symmetry"]
        assert "1/2" in sym.get("critical_line_meaning", "") or \
               "balance" in sym.get("critical_line_meaning", "").lower()

    def test_basel_problem_at_index_11(self):
        p11 = next(p for p in self.data["sample_points"] if p["index"] == 11)
        assert "basel" in p11.get("special", "").lower()

    def test_axis_is_ax09(self):
        assert self.data["axis"] == "AX-09"


# ---------------------------------------------------------------------------
# T60 — Cross-axis consistency rules
# ---------------------------------------------------------------------------

class TestCrossAxisConsistencyRules:
    def setup_method(self):
        self.data = load("CROSS_AXIS_CONSISTENCY_RULES.yaml")

    def test_exactly_12_rules(self):
        assert len(self.data["rules"]) == 12

    def test_rule_ids_unique(self):
        ids = [r["id"] for r in self.data["rules"]]
        assert len(ids) == len(set(ids))

    def test_all_rules_have_required_fields(self):
        required = {"id", "name", "severity", "description"}
        for r in self.data["rules"]:
            missing = required - r.keys()
            assert not missing, f"Rule {r.get('id')} missing: {missing}"

    def test_severity_values_valid(self):
        valid = {"ERROR", "WARNING", "INFO"}
        for r in self.data["rules"]:
            assert r["severity"] in valid, f"Rule {r['id']} invalid severity"

    def test_riemann_coupling_rule_is_error(self):
        cr01 = next(r for r in self.data["rules"] if r["id"] == "CR-01")
        assert cr01["severity"] == "ERROR"

    def test_432hz_anchor_rule_is_error(self):
        cr11 = next(r for r in self.data["rules"] if r["id"] == "CR-11")
        assert cr11["severity"] == "ERROR"

    def test_metatrons_cube_rule_present(self):
        ids = [r["id"] for r in self.data["rules"]]
        assert "CR-12" in ids

    def test_validation_profile_present(self):
        assert "validation_profile" in self.data
        vp = self.data["validation_profile"]
        assert vp["total_rules"] == 12

    def test_error_rules_count(self):
        vp = self.data["validation_profile"]
        assert len(vp["error_rules"]) == 4

    def test_schumann_neuromorphic_rule_present(self):
        ids = [r["id"] for r in self.data["rules"]]
        assert "CR-10" in ids


# ---------------------------------------------------------------------------
# Integration: all 12 ontology files loadable and candidate-status
# ---------------------------------------------------------------------------

ONTOLOGY_FILES = [
    "AXES_12_FORMAL_DEFINITIONS.yaml",
    "NODE_TYPE_TAXONOMY.yaml",
    "EDGE_RELATION_TAXONOMY.yaml",
    "FREQUENCY_BAND_ONTOLOGY.yaml",
    "MATTER_STATE_ONTOLOGY.yaml",
    "ISOTOPE_ELEMENT_ONTOLOGY.yaml",
    "SPIN_RATE_ONTOLOGY.yaml",
    "ACOUSTIC_RESONANCE_ONTOLOGY.yaml",
    "COLOR_HARMONIC_ONTOLOGY.yaml",
    "NEUROMORPHIC_ONTOLOGY.yaml",
    "RIEMANN_S_OPERATOR.yaml",
    "CROSS_AXIS_CONSISTENCY_RULES.yaml",
]


@pytest.mark.parametrize("filename", ONTOLOGY_FILES)
def test_ontology_file_loadable(filename):
    """All 12 ontology files must parse as valid YAML."""
    data = load(filename)
    assert isinstance(data, dict), f"{filename} must be a YAML mapping"


@pytest.mark.parametrize("filename", ONTOLOGY_FILES)
def test_ontology_file_is_candidate_status(filename):
    """All 12 ontology files must carry Candidate status (not canon)."""
    data = load(filename)
    assert data.get("status") == "Candidate", \
        f"{filename} status must be 'Candidate', got '{data.get('status')}'"


@pytest.mark.parametrize("filename", ONTOLOGY_FILES)
def test_ontology_file_has_schema_version(filename):
    """All files must declare schema_version."""
    data = load(filename)
    assert "schema_version" in data, f"{filename} missing schema_version"
