"""Test integrated gypsum/shell resource separation and conservative qualification."""
import unittest,copy,json,pathlib
from integrated_gypsum_shell_v03 import run
ROOT=pathlib.Path(__file__).parent
class IntegratedTests(unittest.TestCase):
 def setUp(self):self.d=json.loads((ROOT/"integrated_synthetic.json").read_text())
 def test_closed_gates_no_allocation(self):
  r=run(self.d)
  self.assertEqual(sum(y["gypsum_to_soil_t"]+y["gypsum_to_acid_hub_t"] for y in r["annual"]),0)
  self.assertEqual(r["annual"][0]["unqualified_residual_t"],r["annual"][0]["brine_gypsum_produced_t"])
 def test_chemistry_supply_feeds_allocation(self):
  self.d["brine"]["lab_measured"]=True;self.d["brine"]["batch_assay_pass"]=True
  self.d["industrial"]["measured_batch_assay_pass"]=True;self.d["industrial"]["hub_acceptance"]=True
  r=run(self.d)
  self.assertAlmostEqual(r["annual"][0]["gypsum_to_acid_hub_t"],r["annual_max_dry_gypsum_t"],places=2)
 def test_soil_and_acid_allocation_conserves(self):
  self.d["brine"]["lab_measured"]=True;self.d["brine"]["batch_assay_pass"]=True
  self.d["industrial"]["measured_batch_assay_pass"]=True;self.d["industrial"]["hub_acceptance"]=True
  z=self.d["soil_classes"][0]
  for key in ["soil_measured","sodic_reclamation_verified","gypsum_batch_safe","trial_verified","drainage_safe","farm_consent"]:z[key]=True
  r=run(self.d)
  for row in r["annual"]:
   self.assertAlmostEqual(row["gypsum_to_soil_t"]+row["gypsum_to_acid_hub_t"]+row["ending_inventory_t"],row["qualified_gypsum_t"],delta=.02)
 def test_shell_acid_is_not_new_sulfur(self):
  self.d["shell"]["recovered_sulfuric_acid_t_y"]=100
  self.d["shell"]["acid_assay_pass"]=True;self.d["shell"]["conversion_qualified"]=True
  r=run(self.d)
  self.assertGreater(r["shell"]["potential_shell_gypsum_t_y"],0)
  self.assertEqual(r["shell"]["shell_gypsum_counted_as_NEW_sulfur_t"],0)
 def test_unknown_brine_fails_closed(self):
  self.d["brine"]["calcium_mg_l"]=None
  self.assertEqual(run(self.d)["status"],"EVIDENCE_GATES_CLOSED")
if __name__=="__main__":unittest.main()
