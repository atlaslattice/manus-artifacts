"""Negative and positive tests: v0.2.2 schema shape is not cryptographic proof."""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from validate_v022_packet import check_packet, load_json

HERE = Path(__file__).resolve().parent
VALID = HERE / "examples" / "GANGASEEK_v022_SYNTHETIC_VALID.json"
INVALID = HERE / "examples" / "GANGASEEK_v022_SYNTHETIC_INVALID.json"


class Packet022Tests(unittest.TestCase):
    def setUp(self):
        self.base = json.loads(VALID.read_text(encoding="utf-8"))

    def verify(self, mutation, error=None):
        pkt = copy.deepcopy(self.base)
        mutation(pkt)
        result = check_packet(pkt)
        self.assertEqual(result["disposition"], "HOLD", result)
        self.assertFalse(result["cryptographic_authenticity_verified"])
        self.assertFalse(result["authority_verified"])
        self.assertFalse(result["host_executed"])
        if error:
            self.assertIn(error, result["errors"])

    def test_valid_synthetic_shape_never_authenticates(self):
        result = check_packet(self.base)
        self.assertEqual(result["disposition"], "CANDIDATE_STRUCTURE_ONLY", result)
        self.assertFalse(result["cryptographic_authenticity_verified"])
        self.assertFalse(result["source_rights_verified"])
        self.assertFalse(result["authority_verified"])
        self.assertFalse(result["host_executed"])

    def test_known_negative_fixture(self):
        pkt = json.loads(INVALID.read_text(encoding="utf-8"))
        self.assertEqual(check_packet(pkt)["disposition"], "HOLD")

    def test_aad_can_be_empty(self):
        self.assertEqual(check_packet(self.base)["disposition"], "CANDIDATE_STRUCTURE_ONLY")

    def test_tag_and_state_plane_are_separate_even_when_3_and_11(self):
        self.assertEqual(self.base["header"]["tag_class"], 3)
        self.assertEqual(self.base["header"]["state_plane"], 11)
        self.assertEqual(check_packet(self.base)["disposition"], "CANDIDATE_STRUCTURE_ONLY")

    def test_approval_grant_forbidden(self):
        self.verify(lambda p: p["header"].update(authority_scope="EXECUTION"),
                    "inferred_authority_forbidden")

    def test_canon_forbidden(self):
        self.verify(lambda p: p.update(canon=True), "authority_or_deployment_inflation")

    def test_deployment_forbidden(self):
        self.verify(lambda p: p.update(deployed=True), "authority_or_deployment_inflation")

    def test_missing_source(self):
        self.verify(lambda p: p.update(source_ref=""), "source_ref_required")

    def test_missing_raw_export_status(self):
        self.verify(lambda p: p.pop("raw_export_status"), "packet_missing_or_extra_fields")

    def test_claimed_complete_raw_is_not_verified(self):
        self.verify(lambda p: p.update(raw_export_status="raw_complete_hashed"),
                    "source_completeness_not_verified_by_synthetic_packet")

    def test_malformed_swa_length(self):
        self.verify(lambda p: p["header"].update(swa_mask="0xFF"),
                    "invalid_16_bit_swa_mask")

    def test_reserved_swa_bits(self):
        self.verify(lambda p: p["header"].update(swa_mask="0xC000"),
                    "reserved_swa_bits_unapproved")

    def test_swa_fully_16_bit(self):
        self.base["header"]["swa_mask"] = "0x3FFF"
        self.assertEqual(check_packet(self.base)["disposition"], "CANDIDATE_STRUCTURE_ONLY")

    def test_invalid_operator(self):
        self.verify(lambda p: p["header"].update(source_operator="O_UNAUTHORIZED"),
                    "unknown_operator")

    def test_o_ai_operator_allowed(self):
        self.base["header"]["source_operator"] = "O_AI"
        self.assertEqual(check_packet(self.base)["disposition"], "CANDIDATE_STRUCTURE_ONLY")

    def test_goog_alphabet_distinct(self):
        self.base["header"]["source_operator"] = "O_ALPHA"
        self.base["header"]["target_operator"] = "O_GOOGLE"
        self.assertEqual(check_packet(self.base)["disposition"], "CANDIDATE_STRUCTURE_ONLY")

    def test_zero_coordinate_rejected(self):
        self.verify(lambda p: p["header"]["coordinate"].update(node=0),
                    "coordinate_node_out_of_range")

    def test_boolean_coordinate_rejected(self):
        self.verify(lambda p: p["header"]["coordinate"].update(node=True),
                    "coordinate_node_out_of_range")

    def test_tag_class_out_of_range(self):
        self.verify(lambda p: p["header"].update(tag_class=4), "invalid_tag_class")

    def test_state_plane_out_of_range(self):
        self.verify(lambda p: p["header"].update(state_plane=16), "invalid_state_plane")

    def test_bad_nonce_bytes(self):
        self.verify(lambda p: p["aead_envelope"].update(nonce_base64="AAAA"),
                    "nonce_base64_decoded_length_wrong")

    def test_bad_tag_bytes(self):
        self.verify(lambda p: p["aead_envelope"].update(tag_base64="AAAA"),
                    "tag_base64_decoded_length_wrong")

    def test_bad_b64_ciphertext(self):
        self.verify(lambda p: p["aead_envelope"].update(ciphertext_base64="!!"),
                    "ciphertext_base64_invalid_base64")

    def test_encoded_length_wrong(self):
        self.verify(lambda p: p["aead_envelope"].update(encoded_ciphertext_base64_chars=4096),
                    "incorrect_byte_vs_encoding_lengths")

    def test_wrong_ciphertext_decoded_length(self):
        self.verify(lambda p: p["aead_envelope"].update(ciphertext_base64="A" * 5464),
                    "ciphertext_base64_decoded_length_wrong")

    def test_synthetic_flag_required(self):
        self.verify(lambda p: p["aead_envelope"].update(synthetic_fixture=False),
                    "only_synthetic_fixtures_allowed")

    def test_secret_unknown_field_rejected(self):
        self.verify(lambda p: p["header"].update(admin_token="private"),
                    "header_missing_or_extra_fields")

    def test_duplicate_json_key_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate key"):
            load_json(b'{"canon":false,"canon":true}')

    def test_invalid_top_type_holds(self):
        self.assertEqual(check_packet([])["disposition"], "HOLD")

    def test_wrong_aad_encoding(self):
        self.verify(lambda p: p["aead_envelope"].update(aad_base64="@"),
                    "aad_base64_invalid_base64")


if __name__ == "__main__":
    unittest.main()
