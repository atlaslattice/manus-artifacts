"""Krakoa gate source-index checker negative/positive cases, no host calls."""
from __future__ import annotations
import json
from pathlib import Path
import tempfile
import unittest

from krakoa_gate_check import inspect_gate, validate_index


def gate():
    return {
        "gate_id": "KRAKOA-GATE-TEST-0001", "title": "Synthetic gate",
        "gate_type": "issue",
        "source": "https://github.com/atlaslattice/manus-artifacts/issues/11",
        "allowed_runtime_labels": ["WORK", "PLAY"],
        "purpose": "Synthetic source review", "canon_authority": False,
        "human_root_required": True, "notes": "No real permission."
    }


def index(rows):
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "gate.jsonl"
        f.write_text("".join(json.dumps(x) + "\n" for x in rows), encoding="utf-8")
        return validate_index(f)


class GateCheckTests(unittest.TestCase):
    def test_synthetic_gate_is_candidate_only(self):
        result = inspect_gate(gate())
        self.assertEqual(result["status"], "CANDIDATE_POINTER_ONLY")
        self.assertFalse(result["authority_verified"])
        self.assertFalse(result["private_body_loaded"])

    def test_play_label_does_not_grant_access(self):
        result = inspect_gate(gate())
        self.assertFalse(result["executed"])
        self.assertFalse(result["source_rights_verified"])

    def test_governance_flag_requires_review_not_authorization(self):
        g = gate()
        g.update(gate_type="governance_gate", source="self-declared review", canon_authority=True)
        result = inspect_gate(g)
        self.assertEqual(result["status"], "REVIEW_REQUIRED")
        self.assertFalse(result["authority_verified"])

    def test_non_governance_canon_flag_holds(self):
        g = gate()
        g["canon_authority"] = True
        self.assertIn("NON_GOVERNANCE_CANON_FLAG", inspect_gate(g)["problems"])

    def test_human_root_gate_required(self):
        g = gate()
        g["human_root_required"] = False
        self.assertEqual(inspect_gate(g)["status"], "HOLD")

    def test_remote_private_source_not_accepted_as_file(self):
        g = gate()
        g.update(gate_type="code_anchor", source="https://private.example/x")
        self.assertEqual(inspect_gate(g)["status"], "HOLD")

    def test_relative_code_pointer_is_accepted_without_open(self):
        g = gate()
        g.update(gate_type="code_anchor", source="codebases/atlas-vault/a.py")
        self.assertEqual(inspect_gate(g)["status"], "CANDIDATE_POINTER_ONLY")

    def test_traversal_source_holds(self):
        g = gate()
        g.update(gate_type="code_anchor", source="../../personal/secrets")
        self.assertEqual(inspect_gate(g)["status"], "HOLD")

    def test_unknown_label_holds(self):
        g = gate()
        g["allowed_runtime_labels"] = ["ROOT"]
        self.assertIn("INVALID_LABELS", inspect_gate(g)["problems"])

    def test_duplicate_labels_hold(self):
        g = gate()
        g["allowed_runtime_labels"] = ["WORK", "WORK"]
        self.assertEqual(inspect_gate(g)["status"], "HOLD")

    def test_duplicates_in_index_hold(self):
        self.assertTrue(index([gate(), gate()])["duplicate_ids"])
        self.assertEqual(index([gate(), gate()])["status"], "HOLD")

    def test_mixed_index_returns_review_required(self):
        g = gate()
        h = gate()
        h.update(gate_id="KRAKOA-GATE-TEST-0002", gate_type="governance_gate",
                 source="unverified decision", canon_authority=True)
        result = index([g, h])
        self.assertEqual(result["status"], "REVIEW_REQUIRED")
        self.assertEqual(result["gate_count"], 2)
        self.assertEqual(result["canon_flags_for_review"], 1)
        self.assertFalse(result["authority_verified"])

    def test_bad_json_line_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "broken.jsonl"
            p.write_bytes(b'{"gate_id":"x","gate_id":"y"}\n')
            self.assertEqual(validate_index(p)["status"], "HOLD")

    def test_empty_index_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "empty.jsonl"
            p.write_bytes(b"")
            self.assertEqual(validate_index(p)["status"], "HOLD")


if __name__ == "__main__":
    unittest.main()
