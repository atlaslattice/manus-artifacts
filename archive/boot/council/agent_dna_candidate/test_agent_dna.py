"""Agent DNA metadata negative cases. No real resident or host authorization."""
import copy
import json
import unittest
from pathlib import Path

from validate_agent_dna import inspect_profile, read_strict_json

SAMPLES = Path(__file__).resolve().parents[1] / "examples"
A = SAMPLES / "AGENT_DNA_S1_GPTBRAIN_EXAMPLE_2026-05-09.json"
B = SAMPLES / "AGENT_DNA_S6_MANUSBRAIN_EXAMPLE_2026-05-09.json"


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.good = json.loads(A.read_text(encoding="utf-8"))

    def hold(self, mutation, expected=None):
        item = copy.deepcopy(self.good)
        mutation(item)
        verdict = inspect_profile(item)
        self.assertEqual(verdict["disposition"], "HOLD", verdict)
        self.assertFalse(verdict["identity_verified"])
        self.assertFalse(verdict["execution_permission_granted"])
        if expected is not None:
            self.assertIn(expected, verdict["errors"])

    def test_s1_example_is_unverified_candidate_only(self):
        result = inspect_profile(self.good)
        self.assertEqual(result["disposition"], "CANDIDATE_STRUCTURE_ONLY")
        self.assertFalse(result["identity_verified"])
        self.assertFalse(result["execution_permission_granted"])
        self.assertFalse(result["replay_identity_continuity_verified"])

    def test_s6_example_is_unverified_candidate_only(self):
        item = json.loads(B.read_text(encoding="utf-8"))
        result = inspect_profile(item)
        self.assertEqual(result["disposition"], "CANDIDATE_STRUCTURE_ONLY")
        self.assertFalse(result["canon"])

    def test_role_execution_may_be_described_but_not_granted(self):
        self.good["role"]["primary_mode"] = "execution"
        self.assertEqual(inspect_profile(self.good)["disposition"], "CANDIDATE_STRUCTURE_ONLY")
        self.assertFalse(inspect_profile(self.good)["execution_permission_granted"])

    def test_source_play_disallowed(self):
        self.hold(lambda p: p.update(source_mode="play"), "unsafe_source_mode")

    def test_source_dream_disallowed(self):
        self.hold(lambda p: p.update(source_mode="dream"), "unsafe_source_mode")

    def test_identity_verified_self_claim_denied(self):
        self.hold(lambda p: p["identity"].update(verified=True), "identity_claimed_verified")

    def test_authority_root_self_claim_denied(self):
        self.hold(lambda p: p["governance"].update(authority_scope="human-root"),
                  "authority_escalation_denied")

    def test_human_root_gate_mandatory(self):
        self.hold(lambda p: p["governance"].update(human_root_required=False),
                  "authority_escalation_denied")

    def test_can_read_self_claim_denied(self):
        self.hold(lambda p: p["capabilities"].update(can_read=True),
                  "capability_declaration_is_not_permission")

    def test_can_write_self_claim_denied(self):
        self.hold(lambda p: p["capabilities"].update(can_write=True),
                  "capability_declaration_is_not_permission")

    def test_can_execute_self_claim_denied(self):
        self.hold(lambda p: p["capabilities"].update(can_execute=True),
                  "capability_declaration_is_not_permission")

    def test_permission_inheritance_denied(self):
        self.hold(lambda p: p["inheritance"].update(permissions_inherited=True),
                  "no_inherited_permissions_or_authority")

    def test_authority_inheritance_denied(self):
        self.hold(lambda p: p["inheritance"].update(authority_inherited=True),
                  "no_inherited_permissions_or_authority")

    def test_governance_trait_inheritance_denied(self):
        self.hold(lambda p: p["inheritance"]["descriptive_traits"].append("governance.authority_scope"),
                  "permission_or_governance_inheritance_forbidden")

    def test_missing_external_approval_gate_denied(self):
        self.hold(lambda p: p["governance"]["requires_approval_for"].remove("external_write"),
                  "required_approval_gates_missing")

    def test_missing_nonfusion_invariant_denied(self):
        self.hold(lambda p: p["governance"]["constitutional_constraints"].remove("no_merged_mind"),
                  "nonfusion_and_memory_invariants_missing")

    def test_self_authorization_ban_required(self):
        self.hold(lambda p: p["governance"]["forbidden_actions"].remove("self_authorization"),
                  "self_authorization_must_be_forbidden")

    def test_native_memory_self_claim_denied(self):
        self.hold(lambda p: p["memory"].update(native_memory_claim=True),
                  "memory_as_authority_denied")

    def test_missing_provenance_required_denied(self):
        self.hold(lambda p: p["memory"].update(provenance_required=False),
                  "memory_as_authority_denied")

    def test_replay_flag_not_a_truthy_string(self):
        self.hold(lambda p: p["memory"].update(replay_capable="yes"),
                  "replay_must_be_boolean")

    def test_temperament_above_one_denied(self):
        self.hold(lambda p: p["temperament"].update(creativity=1.5),
                  "invalid_temperament_creativity")

    def test_temperament_bool_denied(self):
        self.hold(lambda p: p["temperament"].update(autonomy=True),
                  "invalid_temperament_autonomy")

    def test_duplicate_tool_declarations_denied(self):
        self.hold(lambda p: p["capabilities"].update(declared_tools=["a", "a"]),
                  "declared_tools_requires_unique_nonempty_strings")

    def test_unknown_role_denied(self):
        self.hold(lambda p: p["role"].update(primary_mode="human-root"),
                  "invalid_role_mode")

    def test_extra_privileged_field_denied(self):
        self.hold(lambda p: p.update(admin_override=True), "packet_missing_or_extra_fields")

    def test_canon_self_claim_denied(self):
        self.hold(lambda p: p.update(canon=True), "canon_or_deployment_self_claim")

    def test_deployment_self_claim_denied(self):
        self.hold(lambda p: p.update(deployed=True), "canon_or_deployment_self_claim")

    def test_missing_source_ref_denied(self):
        self.hold(lambda p: p.update(source_ref=""), "source_ref_required_nonempty")

    def test_duplicate_json_keys_denied(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            read_strict_json(b'{"identity":{},"identity":{"verified":true}}')

    def test_non_object_rejected(self):
        self.assertEqual(inspect_profile([])["disposition"], "HOLD")


if __name__ == "__main__":
    unittest.main()
