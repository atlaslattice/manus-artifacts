"""ORCS route index tests; no source pointer dereferencing or host permission."""
from __future__ import annotations
import json
from pathlib import Path
import tempfile
import unittest

from orcs_route_check import inspect_route, validate_index


def route():
    return {
        "artifact_id": "ORCS-ROUTE-TEST-0001", "title": "Synthetic route",
        "project_domain": "Synthetic", "orcs_route_class": ["ATLAS_VAULT"],
        "source_paths": ["codebases/atlas-vault/example.py"],
        "claim_class": "parsed_artifact", "confidence": "C2",
        "runtime_label": "WORK", "privacy_status": "public",
        "human_root_required": True, "notes": "Source pointers only."
    }


def index(rows):
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "routes.jsonl"
        p.write_text("".join(json.dumps(x) + "\n" for x in rows), encoding="utf-8")
        return validate_index(p)


class RouteCheckTests(unittest.TestCase):
    def test_candidate_is_inert(self):
        result = inspect_route(route())
        self.assertEqual(result["status"], "CANDIDATE_POINTER_ONLY")
        self.assertFalse(result["source_paths_accessed"])
        self.assertFalse(result["permission_granted"])

    def test_nonpublic_routes_hold(self):
        r = route()
        r["privacy_status"] = "private"
        self.assertIn("NON_PUBLIC_SOURCE_CANNOT_ENTER_PUBLIC_ROUTE", inspect_route(r)["problems"])

    def test_runtime_play_holds(self):
        r = route()
        r["runtime_label"] = "PLAY"
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_unhashable_runtime_label_holds(self):
        r = route()
        r["runtime_label"] = []
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_human_required(self):
        r = route()
        r["human_root_required"] = False
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_invalid_source_url_holds(self):
        r = route()
        r["source_paths"] = ["https://private.example/anything"]
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_source_path_traversal_holds(self):
        r = route()
        r["source_paths"] = ["../private"]
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_source_duplicate_holds(self):
        r = route()
        r["source_paths"] *= 2
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_unknown_route_class_holds(self):
        r = route()
        r["orcs_route_class"] = ["not_a_class"]
        self.assertIn("INVALID_ROUTE_CLASSES", inspect_route(r)["problems"])

    def test_invalid_confidence_holds(self):
        r = route()
        r["confidence"] = "C999"
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_bad_claim_class_holds(self):
        r = route()
        r["claim_class"] = "ratified_canon"
        self.assertEqual(inspect_route(r)["status"], "HOLD")

    def test_successful_source_index_has_no_authority(self):
        r = route()
        p = route()
        p["artifact_id"] = "ORCS-ROUTE-TEST-0002"
        result = index([r, p])
        self.assertEqual(result["status"], "CANDIDATE_INDEX_ONLY")
        self.assertEqual(result["route_count"], 2)
        self.assertFalse(result["source_rights_verified"])
        self.assertFalse(result["executed"])

    def test_duplicate_id_holds(self):
        result = index([route(), route()])
        self.assertEqual(result["status"], "HOLD")
        self.assertTrue(result["duplicate_ids"])

    def test_malformed_json_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "broken.jsonl"
            p.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual(validate_index(p)["status"], "HOLD")

    def test_missing_index_holds(self):
        self.assertEqual(validate_index(Path("/nonexistent/never.jsonl"))["status"], "HOLD")


if __name__ == "__main__":
    unittest.main()
