import unittest,importlib.util,pathlib,json
root=pathlib.Path(__file__).parent
spec=importlib.util.spec_from_file_location("sulfur_model",root/"sulfur_model.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class SulfurTests(unittest.TestCase):
 def setUp(self):self.d=json.loads((root/"sulfur_synthetic.json").read_text())
 def test_import_gate_closed(self):
  r=m.run(self.d);self.assertEqual(r["attributable_import_displacement_t_year"],0)
  self.assertTrue(r["external_export_gate"].startswith("UNKNOWN"))
 def test_no_assay(self):
  self.d["calcium_mg_l"]=None
  with self.assertRaises(AssertionError):m.run(self.d)
 def test_calcium_limit(self):
  r=m.run(self.d);self.assertEqual(r["limiting_element"],"Ca")
 def test_chemical_ceiling(self):
  self.d["qualified_acid_t_per_dry_gypsum_t"]=0.75
  with self.assertRaises(AssertionError):m.run(self.d)
 def test_zero_calcium(self):
  self.d["calcium_mg_l"]=0
  self.assertEqual(m.run(self.d)["qualified_dry_gypsum_t_year"],0)
if __name__=="__main__":unittest.main()
