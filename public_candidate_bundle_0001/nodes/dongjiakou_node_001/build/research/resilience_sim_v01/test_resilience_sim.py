import unittest
from resilience_sim import Service,Resource,simulate,strongly_connected,example_case

class TestResilience(unittest.TestCase):
    def test_four_cases(self):
        r={k:example_case(k) for k in ("baseline","distributed","networked","degraded")}
        self.assertEqual(r["networked"]["full_service_hours"]["comms"],168)
        self.assertLess(r["degraded"]["served_kwh"],r["networked"]["served_kwh"])
        self.assertEqual(len(r["baseline"]["trace"]),168)
    def test_cycle_blocks_when_no_seed(self):
        s=[Service("control",1,0,["comms"]),Service("comms",1,0,["control"])]
        r=simulate("cycle",s,[Resource("battery",20,5,0,20)],[0]*5,5)
        self.assertEqual(r["served_kwh"],0)
        self.assertEqual(r["cyclic_components"],[["comms","control"]])
    def test_capacity_gate(self):
        s=[Service("water",10,0,minimum=.8)]
        r=simulate("gate",s,[Resource("battery",20,5,0,20)],[0],1)
        self.assertEqual(r["served_kwh"],0)
    def test_solar_recharges(self):
        s=[Service("comms",2)]
        r=simulate("pv",s,[Resource("battery",100,10,10,20)],[1]*6,6)
        self.assertGreater(r["final_soc_kwh"],20)
    def test_missing_dependency(self):
        with self.assertRaises(ValueError):
            simulate("invalid",[Service("a",1,requires=["x"])],[],[0],1)

if __name__=="__main__":unittest.main()
