"""Synthetic Council plan hash + split-review negative cases; no host actions."""
from __future__ import annotations

import copy
import unittest
from plan_hash_candidate import digest_plan, inspect_binding, canonical_plan, PlanHold, MAX_PLAN_BYTES

PLAN = b'{"status":"candidate","canon":false,"steps":[{"type":"synthetic","id":1}]}'
HASH = digest_plan(PLAN)


def packets():
    return (
        {"plan_sha256": HASH, "dry_run_only": True, "effects_executed": False,
         "source_ref": "synthetic:plan-v1"},
        {"lane": "logic_verifier", "plan_sha256": HASH, "verdict": "PASS",
         "evidence_ref": "synthetic:logic-review"},
        {"lane": "security_verifier", "plan_sha256": HASH, "verdict": "PASS",
         "evidence_ref": "synthetic:security-review"},
    )


class PlanHashTests(unittest.TestCase):
    def check(self, plan=PLAN, change=None, expected=None):
        e, logic, security = (copy.deepcopy(p) for p in packets())
        if change:
            change(e, logic, security)
        r = inspect_binding(plan, e, logic, security)
        if expected:
            self.assertEqual(r["status"], "HOLD")
            self.assertIn(expected, r["errors"])
        return r

    def test_two_passes_still_no_authority(self):
        r = self.check()
        self.assertEqual(r["status"], "STRUCTURAL_CANDIDATE_READY_NOT_AUTHORIZED")
        self.assertFalse(r["approval_granted"])
        self.assertFalse(r["host_execution_permitted"])
        self.assertFalse(r["canon"])
        self.assertFalse(r["deployed"])
        self.assertFalse(r["logic_verifier_identity_authenticated"])

    def test_plan_field_order_normalized(self):
        self.assertEqual(HASH, digest_plan(b'{"steps":[{"id":1,"type":"synthetic"}],"canon":false,"status":"candidate"}'))

    def test_hash_is_stable(self):
        self.assertEqual(digest_plan(PLAN), digest_plan(PLAN))

    def test_duplicate_json_key_holds(self):
        self.check(b'{"status":"candidate","status":"candidate","canon":false}', expected="DUPLICATE_JSON_KEY")

    def test_float_plan_holds(self):
        self.check(b'{"status":"candidate","canon":false,"x":0.4}', expected="NON_INTEGER_JSON_NUMBER")

    def test_exponent_overflow_holds(self):
        self.check(b'{"status":"candidate","canon":false,"x":1e10000}', expected="NON_INTEGER_JSON_NUMBER")

    def test_nan_holds(self):
        self.check(b'{"status":"candidate","canon":false,"x":NaN}', expected="NON_INTEGER_JSON_NUMBER")

    def test_not_candidate_holds(self):
        self.check(b'{"status":"ratified","canon":false}', expected="NOT_A_CANDIDATE_PLAN")

    def test_canon_self_claim_holds(self):
        self.check(b'{"status":"candidate","canon":true}', expected="NOT_A_CANDIDATE_PLAN")

    def test_invalid_utf8_holds(self):
        self.check(b"\xff", expected="INVALID_PLAN_JSON")

    def test_too_large_holds(self):
        self.check(b" "*(MAX_PLAN_BYTES + 1), expected="PLAN_MISSING_OR_TOO_LARGE")

    def test_missing_execution_source_holds(self):
        self.check(change=lambda e,l,s:e.update(source_ref=""), expected="EXECUTION_SOURCE_REF_MISSING")

    def test_effects_must_be_false(self):
        self.check(change=lambda e,l,s:e.update(effects_executed=True), expected="EXECUTION_NOT_DRY_RUN")

    def test_dry_run_must_be_true(self):
        self.check(change=lambda e,l,s:e.update(dry_run_only=False), expected="EXECUTION_NOT_DRY_RUN")

    def test_wrong_execution_hash_holds(self):
        self.check(change=lambda e,l,s:e.update(plan_sha256="0"*64), expected="EXECUTION_PLAN_HASH_MISMATCH")

    def test_logic_verifier_hash_mismatch(self):
        self.check(change=lambda e,l,s:l.update(plan_sha256="0"*64), expected="LOGIC_VERIFIER_PLAN_HASH_MISMATCH")

    def test_security_verifier_hash_mismatch(self):
        self.check(change=lambda e,l,s:s.update(plan_sha256="0"*64), expected="SECURITY_VERIFIER_PLAN_HASH_MISMATCH")

    def test_wrong_lane_label_holds(self):
        self.check(change=lambda e,l,s:l.update(lane="security_verifier"), expected="LOGIC_VERIFIER_LANE_MISMATCH")

    def test_verifier_hold_blocks_candidate(self):
        self.check(change=lambda e,l,s:s.update(verdict="HOLD"), expected="SECURITY_VERIFIER_NO_PASS")

    def test_verifier_missing_receipt_holds(self):
        self.check(change=lambda e,l,s:l.update(evidence_ref=""), expected="LOGIC_VERIFIER_MISSING_EVIDENCE")

    def test_extra_execution_field_holds(self):
        self.check(change=lambda e,l,s:e.update(authorized=True), expected="INVALID_EXECUTION_PACKET")

    def test_integer_above_53_bit_holds(self):
        self.check(b'{"status":"candidate","canon":false,"count":99999999999999999999}', expected="PLAN_NOT_STRICT_PLAIN_OBJECT")

    def test_canonical_plan_bytes_sorted(self):
        b = canonical_plan(b'{"status":"candidate", "canon":false, "b":2, "a":1}')
        self.assertIn(b'"a":1,"b":2', b)


if __name__ == "__main__":
    unittest.main()
