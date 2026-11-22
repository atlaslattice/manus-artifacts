"""Synthetic-only regression tests for fail-closed GPTBrain S1 memory preview."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import gptbrain_memory as gm


class S1PreviewTests(unittest.TestCase):
    def preview(self, **changes):
        args = dict(
            title="Synthetic recall cue", memory_type="project",
            summary="Synthetic local test only", source="synthetic_fixture", confidence="C1"
        )
        args.update(changes)
        return gm.remember(**args)

    def test_preview_has_explicit_nonpersisted_status(self):
        p = self.preview()
        self.assertEqual(p["status"], "CANDIDATE_PREVIEW_NOT_SAVED")
        self.assertIs(p["persisted"], False)
        self.assertIs(p["execution_authority"], False)
        self.assertIs(p["canon"], False)
        self.assertIs(p["deployed"], False)

    def test_candidate_is_not_identity_or_permission(self):
        candidate = self.preview()["candidate"]
        self.assertTrue(candidate["memory_id"].startswith("S1-UNSAVED-PREVIEW-"))
        self.assertEqual(candidate["retention"]["status"], "not_saved")
        self.assertEqual(candidate["permissions"]["access_class"], "preview_only")
        self.assertEqual(candidate["permissions"]["consent_level"], "not_attested")
        self.assertIs(candidate["permissions"]["executable"], False)
        self.assertIs(candidate["provenance"]["source_rights_verified"], False)

    def test_legacy_seed_is_never_modified(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "seed.jsonl"
            raw = b'{"memory_id":"S1-OLD","summary":"synthetic preexisting"}\n'
            p.write_bytes(raw)
            with patch.object(gm, "MEMORY_OBJECTS", p):
                self.preview()
            self.assertEqual(p.read_bytes(), raw)

    def test_missing_seed_file_not_created(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "seed.jsonl"
            with patch.object(gm, "MEMORY_OBJECTS", p):
                self.preview()
            self.assertFalse(p.exists())

    def test_no_append_function_called(self):
        with patch.object(gm, "append_jsonl", side_effect=AssertionError("must not write")):
            self.preview()

    def test_invalid_source_class_rejected(self):
        for value in ("play", "imagine", "dream", "private_play", "external_host"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.preview(source=value)

    def test_unhashable_source_rejected(self):
        with self.assertRaises(ValueError):
            self.preview(source=[])

    def test_source_user_message_is_unverified_claim(self):
        p = self.preview(source="user_message")
        self.assertEqual(p["candidate"]["epistemic_status"], "user_claim")
        self.assertFalse(p["source_rights_verified"])
        self.assertFalse(p["persisted"])

    def test_blank_title_rejected(self):
        with self.assertRaises(ValueError):
            self.preview(title=" ")

    def test_empty_summary_rejected(self):
        with self.assertRaises(ValueError):
            self.preview(summary="")

    def test_excessive_summary_rejected(self):
        with self.assertRaises(ValueError):
            self.preview(summary="x" * 10001)

    def test_confidence_is_typed(self):
        for confidence in (None, [], {}, 0, "C6"):
            with self.subTest(confidence=repr(confidence)), self.assertRaises(ValueError):
                self.preview(confidence=confidence)

    def test_no_fabricated_ontology_address(self):
        candidate = self.preview()["candidate"]
        self.assertEqual(candidate["ontology"]["sphere_tags"], [])
        self.assertEqual(candidate["provenance"]["source_refs"], [])

    def test_synthesis_uses_current_candidate_status_not_stale_patch(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            files = [root / "claims.jsonl", root / "artifacts.jsonl", root / "memories.jsonl"]
            for path in files:
                path.write_text(json.dumps({"id": "synthetic"}) + "\n", encoding="utf-8")
            with patch.object(gm, "CLAIM_LEDGER", files[0]), \
                 patch.object(gm, "ARTIFACT_REGISTRY", files[1]), \
                 patch.object(gm, "MEMORY_OBJECTS", files[2]):
                result = gm.synthesize("synthetic")
        self.assertEqual(result["counts"], {"claims": 1, "artifacts": 1, "memories": 1})
        self.assertFalse(any("Patch canonical candidate to integrate Variant E" in x
                             for x in result["next_actions"]))
        self.assertTrue(any("human-root ratification remains pending" in x
                            for x in result["next_actions"]))
        self.assertEqual(result["status"], "implementation_scaffold_not_canon")


if __name__ == "__main__":
    unittest.main()
