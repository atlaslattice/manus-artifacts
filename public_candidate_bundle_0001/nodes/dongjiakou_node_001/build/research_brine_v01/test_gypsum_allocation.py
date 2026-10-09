"""Run: python3 -m unittest discover -s research_brine_v01 -p 'test_*.py'"""
import unittest,copy
from gypsum_allocation import run
class TestAllocation(unittest.TestCase):
 def setUp(self):
  self.s={"years":20,"qualified_dry_gypsum_t_y":100,"acid_t_per_dry_gypsum_t":0.4,
  "sulfur_shortfall_ag_cap_fraction":0.5,
  "national_sulfur":{"balance_s_equivalent_t_y":-200,"imports_actual_zero_verified":False},
  "industrial_quality":{"assay_measured":True,"hub_acceptance_verified":True,
   "measured_gypsum_purity":0.90,"minimum_gypsum_purity":0.85,
   "measured_moisture_fraction":0.05,"maximum_moisture_fraction":0.10},
  "soil_classes":[{"name":"test","hectares":10,"initial_t_ha":10,"maintenance_t_ha_y":0,
   "reclamation_decline_fraction_y":0.3,"reclamation_years":10,
   "soil_test_measured":True,"ag_product_batch_assay_pass":True,
   "field_trial_verified":True,"approved_drainage_plan":True,"farm_consent_verified":True}]}
 def test_no_soil_receipt_means_zero_allocation(self):
  self.s["soil_classes"][0]["soil_test_measured"]=False
  self.assertEqual(run(self.s)["years"][0]["ag_allocated_t"],0)
 def test_years_decline_soil_need(self):
  a=run(self.s)["years"]
  self.assertGreater(a[0]["ag_assayed_soil_demand_t"],a[5]["ag_assayed_soil_demand_t"])
  self.assertEqual(a[10]["ag_assayed_soil_demand_t"],0)
 def test_sulfur_shortfall_cap(self):
  a=run(self.s)["years"][0]
  self.assertEqual(a["ag_allocated_t"],50)
  self.assertEqual(a["acid_feed_allocated_t"],50)
 def test_unqualified_industrial_stored(self):
  self.s["industrial_quality"]["hub_acceptance_verified"]=False
  a=run(self.s)["years"][0]
  self.assertEqual(a["acid_feed_allocated_t"],0)
  self.assertEqual(a["closing_inventory_t"],50)
 def test_no_double_claim(self):
  a=run(self.s)["years"]
  for i,v in enumerate(a):
   opening=a[i-1]["closing_inventory_t"] if i else 0
   self.assertAlmostEqual(100+opening,v["ag_allocated_t"]+v["acid_feed_allocated_t"]+v["closing_inventory_t"],places=2)
 def test_never_award_actual_credit(self):
  self.assertTrue(all(y["realized_credit_t"]==0 and y["external_sale_credit_t"]==0 for y in run(self.s)["years"]))
if __name__=="__main__":unittest.main()
