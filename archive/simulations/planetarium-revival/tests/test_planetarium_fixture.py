"""Source-linked consistency checks for the existing Planetarium Revival simulator.

Not canon, not deployed, no partner approval, zero real participant data.
"""
from __future__ import annotations

from dataclasses import asdict
import csv
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[4]
PROJECT = Path(__file__).resolve().parents[1]
SIMULATOR = ROOT / "tools" / "simulate_planetarium_144_matrix.py"
JSON_FIXTURE = PROJECT / "fixtures" / "PLANETARIUM_144_TASKS_v0.1.json"
CSV_FIXTURE = PROJECT / "fixtures" / "PLANETARIUM_144_TASKS_v0.1.csv"


def load_simulator():
    spec = importlib.util.spec_from_file_location("planetarium_sim_v01", SIMULATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("simulator_not_importable")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


class PlanetariumFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_simulator()
        cls.tasks = list(cls.mod.iter_tasks())
        cls.json_rows = json.loads(JSON_FIXTURE.read_text(encoding="utf-8"))

    def test_12_houses(self):
        self.assertEqual(len(self.mod.MATRIX), 12)

    def test_12_tasks_per_house(self):
        self.assertTrue(all(len(tasks) == 12 for tasks in self.mod.MATRIX.values()))

    def test_144_total(self):
        self.assertEqual(len(self.tasks), 144)
        self.assertEqual(len(self.json_rows), 144)

    def test_unique_task_ids(self):
        ids = [x.task_id for x in self.tasks]
        self.assertEqual(len(ids), len(set(ids)))

    def test_task_ids_match_12x12(self):
        self.assertEqual(self.tasks[0].task_id, "H01-T01")
        self.assertEqual(self.tasks[-1].task_id, "H12-T12")

    def test_simulator_invariants(self):
        self.assertEqual(self.mod.validate(self.tasks), [])

    def test_json_is_simulator_equivalent(self):
        expected = []
        for task in self.tasks:
            entry = asdict(task)
            entry["review_flags"] = self.mod.review_flags(task)
            entry["readiness_score"] = self.mod.readiness_score(task)
            expected.append(entry)
        self.assertEqual(self.json_rows, expected)

    def test_csv_matches_python_simulator_bytes(self):
        self.assertEqual(CSV_FIXTURE.read_bytes(), self.mod.to_csv(self.tasks).encode("utf-8"))

    def test_csv_readback_has_144_rows(self):
        with CSV_FIXTURE.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 144)
        self.assertEqual(rows[0]["task_id"], "H01-T01")

    def test_review_flags_are_explicit(self):
        flagged = sum(bool(self.mod.review_flags(x)) for x in self.tasks)
        self.assertEqual(flagged, 28)

    def test_all_fixtures_inert(self):
        for row in self.json_rows:
            self.assertEqual(row["status"], "candidate")
            self.assertEqual(row["canon_status"], "not_canon")
            self.assertEqual(row["deployment_status"], "not_deployed")
            self.assertEqual(row["authority_scope"], "none")
            self.assertTrue(0 <= row["readiness_score"] <= 100)


if __name__ == "__main__":
    unittest.main()
