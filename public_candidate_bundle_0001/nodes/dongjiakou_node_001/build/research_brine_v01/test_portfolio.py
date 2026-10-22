"""Static regression tests of the illustrative portfolio, standard-library unittest."""
import importlib.util, json, pathlib, unittest
ROOT=pathlib.Path(__file__).parent
spec=importlib.util.spec_from_file_location("portfolio",ROOT/"portfolio.py")
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class PortfolioTests(unittest.TestCase):
    def setUp(self): self.s=json.loads((ROOT/"scenario_synthetic.json").read_text())
    def test_conservation(self):
        r=mod.simulate(self.s)
        for p in r["products"].values():
            self.assertLessEqual(p["elemental_recovered_t_y"],p["elemental_feed_t_y"])
            self.assertAlmostEqual(p["network_transfer_t_y"]+p["external_sale_t_y"],p["product_t_y"])
        self.assertAlmostEqual(r["elemental_feed_t_year"]["Br"],250000*67*365/1e6)
    def test_at_cost_transfers_cancel(self):
        r=mod.simulate(self.s)
        for v in r["scenario_results"].values():
            self.assertAlmostEqual(v["node_cash_after_internal_cost_recovery_usd_y"]-v["network_consolidated_cash_usd_y"],v["internal_transfer_at_cost_usd_y"],delta=.02)
    def test_external_price_not_internal_cost(self):
        self.s["products"]["bromine"]["external_price_usd_t"]*=2
        high=mod.simulate(self.s)["products"]["bromine"]
        self.assertAlmostEqual(high["network_transfer_at_cost_usd_y"],
            self.s["intake_m3_day"]*67*365/1e6*.55*.2*1500)
    def test_no_duplicate_elements(self):
        self.s["products"]["second_bromine"]=dict(self.s["products"]["bromine"])
        with self.assertRaises(AssertionError):mod.simulate(self.s)
    def test_recovery_bounds(self):
        self.s["products"]["bromine"]["capture_fraction"]=1.1
        with self.assertRaises(AssertionError):mod.simulate(self.s)
if __name__=="__main__":unittest.main()
