"""Offline acceptance tests for the candidate LivingOS interface, issue #40."""
import unittest
from living_os_interface import (
    ApprovalContext, BoundaryError, Gate, LivingOS, Service
)


class LivingOSBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.os = LivingOS("Atlas candidate")
        self.os.register_service(Service("adapter"))
        self.os.register_gate(Gate("read-receipt", "adapter", "read:receipt"))
        self.os.register_gate(Gate("stage-patch", "adapter", "write:patch", "write"))

    @staticmethod
    def approve(scope):
        return ApprovalContext(True, "HUMAN_ROOT", scope, "fixture-only decision")

    def test_service_registration_never_grants_root(self):
        with self.assertRaises(BoundaryError):
            self.os.register_service(Service("rootbot", authority_scope="root"))
        self.assertEqual(self.os.request_gate("adapter", "read-receipt").status, "DENIED")

    def test_unknown_gate_denied(self):
        self.assertEqual(self.os.request_gate("reader", "absent").reason, "unknown_gate")

    def test_unregistered_service_for_gate_rejected(self):
        with self.assertRaises(BoundaryError):
            self.os.register_gate(Gate("bad", "none", "read"))

    def test_capability_not_granted_by_default(self):
        self.assertFalse(self.os.grant_capability("reader", "read:receipt"))
        self.assertEqual(self.os.request_gate("reader", "read-receipt").reason, "missing_capability")

    def test_grant_requires_exact_scope(self):
        wrong = self.approve("grant:any:*/*")
        self.assertFalse(self.os.grant_capability("reader", "read:receipt", wrong))
        self.assertTrue(self.os.grant_capability("reader", "read:receipt",
                                                 self.approve("grant:reader:read:receipt")))

    def test_grant_requires_human_root_declaration(self):
        false_approval = ApprovalContext(True, "RESIDENT", "grant:x:y", "fixture")
        self.assertFalse(self.os.grant_capability("x", "y", false_approval))

    def test_gate_requires_scoped_approval_even_after_capability(self):
        self.os.grant_capability("reader", "read:receipt",
                                 self.approve("grant:reader:read:receipt"))
        self.assertEqual(self.os.request_gate("reader", "read-receipt").reason,
                         "missing_scoped_approval")

    def test_gate_scope_not_reusable_across_subjects(self):
        self.os.grant_capability("reader", "read:receipt",
                                 self.approve("grant:reader:read:receipt"))
        wrong = self.approve("gate:other:read-receipt")
        self.assertEqual(self.os.request_gate("reader", "read-receipt", wrong).status, "DENIED")

    def test_valid_local_gate_previews_but_never_executes(self):
        self.os.grant_capability("reader", "read:receipt",
                                 self.approve("grant:reader:read:receipt"))
        d = self.os.request_gate("reader", "read-receipt",
                                 self.approve("gate:reader:read-receipt"))
        self.assertEqual(d.status, "PREVIEW_ONLY")
        self.assertFalse(d.executed)
        self.assertFalse(d.authority_verified)

    def test_write_gate_blocked_without_approval(self):
        self.os.grant_capability("editor", "write:patch",
                                 self.approve("grant:editor:write:patch"))
        self.assertEqual(self.os.request_gate("editor", "stage-patch").status, "DENIED")

    def test_write_gate_with_local_approval_still_no_effect(self):
        self.os.grant_capability("editor", "write:patch",
                                 self.approve("grant:editor:write:patch"))
        d = self.os.request_gate("editor", "stage-patch",
                                 self.approve("gate:editor:stage-patch"))
        self.assertEqual(d.status, "PREVIEW_ONLY")
        self.assertFalse(d.executed)

    def test_non_authorized_approval_missing_reason(self):
        ctx = ApprovalContext(True, "HUMAN_ROOT", "grant:x:y", "")
        self.assertFalse(self.os.grant_capability("x", "y", ctx))

    def test_rehydrate_known_is_source_backed_copy_not_identity(self):
        payload = {"signal": ["a"]}
        self.os.register_artifact("evidence-1", payload, source_ref="synthetic:fixture1")
        result = self.os.rehydrate_context("evidence-1")
        self.assertEqual(result.status, "CONTEXT_PACKET_ONLY")
        self.assertEqual(result.source_ref, "synthetic:fixture1")
        self.assertFalse(result.identity_restored)
        self.assertFalse(result.source_verified)
        result.payload["signal"].append("b")
        self.assertEqual(self.os.rehydrate_context("evidence-1").payload["signal"], ["a"])

    def test_rehydrate_missing_never_fabricates(self):
        result = self.os.rehydrate_context("not-here")
        self.assertEqual(result.status, "NOT_FOUND")
        self.assertIsNone(result.payload)

    def test_restricted_play_dream_sources_rejected(self):
        for mode in ("play", "social", "imagine", "dream", "quiet", "unknown"):
            with self.subTest(mode=mode):
                with self.assertRaises(BoundaryError):
                    self.os.register_artifact("x", {"private": True},
                                              source_ref="private:room", source_mode=mode)

    def test_artifact_cannot_overwrite_original(self):
        self.os.register_artifact("source1", "original", source_ref="synthetic:one")
        with self.assertRaises(BoundaryError):
            self.os.register_artifact("source1", "replacement", source_ref="synthetic:two")
        self.assertEqual(self.os.rehydrate_context("source1").payload, "original")

    def test_registration_requires_valid_names_and_actions(self):
        with self.assertRaises(BoundaryError):
            LivingOS("")
        with self.assertRaises(BoundaryError):
            self.os.register_gate(Gate("broken", "adapter", "cap", "promote-canon"))

    def test_audit_is_copy_and_not_persistent_authority(self):
        self.os.request_gate("nobody", "read-receipt")
        audit = self.os.audit_events()
        self.assertEqual(audit[-1]["result"], "DENIED")
        audit[-1]["result"] = "FAKE_OK"
        self.assertEqual(self.os.audit_events()[-1]["result"], "DENIED")


if __name__ == "__main__":
    unittest.main()
