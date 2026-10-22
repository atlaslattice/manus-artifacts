import copy
import json
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from companion import calculate, illustrate_outfall, finance_sensitivity

class CompanionTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((Path(__file__).resolve().parents[1]/"dongjiakou_candidate.json").read_text())
    def test_baseline_no_invented_credit(self):
        out=calculate(self.data)
        self.assertEqual(out["realized_credit"],0)
        self.assertEqual(out["locality_clearance"],"NOT_ESTABLISHED")
        self.assertIsNone(out["outfalls"][0]["nitrogen_input_t_year"])
        self.assertIsNone(out["finance"]["unfunded_remainder"])
    def test_known_hypothetical_example(self):
        o={"id":"SYNTHETIC","status":"SENSITIVITY","flow_m3_day":10000,"nitrogen_mg_l":10,"phosphorus_mg_l":1}
        r=illustrate_outfall(o)
        self.assertAlmostEqual(r["nitrogen_input_t_year"],36.5)
        self.assertAlmostEqual(r["phosphorus_input_t_year"],3.65)
        self.assertFalse(r["closure_verified"])
    def test_finance_sensitivity(self):
        d={"total_cost":100,"recovery_fraction":0.4,"currency":"CNY","cost_basis":"TOTAL_PROJECT"}
        self.assertAlmostEqual(finance_sensitivity(d)["unfunded_remainder"],60)
    def test_no_unknown_to_zero(self):
        d={"id":"UNKNOWN","status":"UNKNOWN","flow_m3_day":None,"nitrogen_mg_l":0,"phosphorus_mg_l":1}
        self.assertIsNone(illustrate_outfall(d)["nitrogen_input_t_year"])
    def test_bad_source_fails(self):
        d=copy.deepcopy(self.data)
        d["programs"][0]["source_ids"]=["not-a-source"]
        with self.assertRaises(ValueError):calculate(d)
    def test_credit_fails(self):
        d=copy.deepcopy(self.data)
        d["programs"][0]["realized_credit"]=1
        with self.assertRaises(ValueError):calculate(d)
    def test_reject_negative_mass(self):
        with self.assertRaises(ValueError):
            illustrate_outfall({"id":"bad","status":"SENSITIVITY","flow_m3_day":-1,"nitrogen_mg_l":2,"phosphorus_mg_l":1})
if __name__=="__main__":unittest.main()
