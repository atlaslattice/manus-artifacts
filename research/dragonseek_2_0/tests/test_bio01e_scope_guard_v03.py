#!/usr/bin/env python3
"""Research-only safety tests, not a v1/v2 parity test."""
import importlib.util
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "scope_guard", Path(__file__).resolve().parents[1] / "bio01e_scope_guard_v03.py"
)
mod = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class GeoAccountingGuards(unittest.TestCase):
    def test_xiaojianxi_is_design_not_djk_receipt(self):
        self.assertEqual(mod.design_year_capacity(500), 182500)
        self.assertEqual(mod.design_year_capacity(500, 300), 150000)

    def test_city_scenario_stays_city(self):
        x = mod.qingdao_food_sensitivity()
        self.assertEqual(x["scope"], "QINGDAO_CITY")
        self.assertIsNone(x["djk_booked_actual_t"])
        self.assertEqual(x["city_eligible_sensitivity_t"]["50%"], 100000)

    def test_desal_capacity_is_scenario_not_actual(self):
        x = mod.desal_design_sensitivity()
        self.assertEqual(x["design_m3_per_year"], 36_500_000)
        self.assertAlmostEqual(x["scenario_kwh_per_year"], 80_300_000)
        self.assertIsNone(x["actual_brine_volume_m3"])

    def test_dry_moisture(self):
        self.assertAlmostEqual(mod.dry_solids(100.0, 0.8), 20.0)
        with self.assertRaises(ValueError):
            mod.dry_solids(100, 1.2)

    def test_mass_balance_needs_all_outputs(self):
        mod.close_mass({"wet feed": 100}, {"product": 50, "residue": 30, "evap": 20})
        with self.assertRaises(ValueError):
            mod.close_mass({"wet feed": 100}, {"product": 50, "residue": 30})

    def test_unknown_and_city_report_cannot_book_as_djk(self):
        for evidence in (mod.Evidence.SCENARIO, mod.Evidence.DESIGNED, mod.Evidence.REPORTED):
            city = mod.MaterialRecord("QD-1", mod.Scope.QINGDAO, 2025,
                                      "food_waste", 200000, evidence, "source-ref")
            with self.assertRaises(ValueError):
                mod.book_to_djk(city, 1000, None)

    def test_receipted_transfer_cannot_double_book(self):
        physical = mod.MaterialRecord("QD-2", mod.Scope.QINGDAO, 2025,
                                      "organics", 100, mod.Evidence.MEASURED,
                                      "weighbridge-ref", prior_allocation_t=40)
        proof = mod.TransferEvidence("QD-2", "DJK-1", "contract",
                                     "entry-scale", "exit-scale", "approval",
                                     already_committed_t=20)
        self.assertEqual(mod.book_to_djk(physical, 40, proof), 40)
        with self.assertRaises(ValueError):
            mod.book_to_djk(physical, 41, proof)

    def test_missing_permission_fails_closed(self):
        physical = mod.MaterialRecord("QD-3", mod.Scope.QINGDAO, 2025,
                                      "organics", 100, mod.Evidence.MEASURED, "meter")
        proof = mod.TransferEvidence("QD-3", "DJK-1", "", "gate-a", "gate-b", "permit")
        with self.assertRaises(ValueError):
            mod.book_to_djk(physical, 10, proof)

    def test_unknown_amount_kept_unknown(self):
        obj = mod.MaterialRecord("DJK-unknown", mod.Scope.DONGJIAKOU, 2025,
                                 "industrial-acid-use", None, mod.Evidence.UNKNOWN, "gap-register")
        obj.validate()
        self.assertIsNone(obj.wet_t)


if __name__ == "__main__":
    unittest.main()
