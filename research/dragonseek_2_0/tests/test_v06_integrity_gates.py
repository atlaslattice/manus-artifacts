import sys, unittest
from pathlib import Path
from dataclasses import replace
from decimal import Decimal
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from v06_integrity_gates import *
class EvidenceGateTests(unittest.TestCase):
    def setUp(self):
        self.w = TruckWeighing('WB-1','WB-1','LOT-1','LOT-1',1050,1050,'2026-10','2026-10',True,True,'R-1',True)
        self.s = FoodSafetyEvidence('CERTIFIED_FOOD_GRADE_BYPRODUCT','CERT-1',True,True,True,True,'HACCP-1',True, {k:'INDEPENDENTLY_VERIFIED_COMPLIANT' for k in REQUIRED_FOOD_PANEL},True,True,True)
    def test_exact_match_accepts_hypothetical(self):self.assertTrue(exact_manifest_gate(self.w))
    def test_reject_one_kg_difference(self):self.assertFalse(exact_manifest_gate(replace(self.w,manifest_net_kg=1049)))
    def test_reject_other_ticket(self):self.assertFalse(exact_manifest_gate(replace(self.w,carrier_manifest_ticket_id='WB-2')))
    def test_reject_other_lot(self):self.assertFalse(exact_manifest_gate(replace(self.w,manifest_lot_id='LOT-2')))
    def test_reject_other_period(self):self.assertFalse(exact_manifest_gate(replace(self.w,period_manifest='2026-11')))
    def test_reject_unverified_scale(self):self.assertFalse(exact_manifest_gate(replace(self.w,meter_calibration_verified=False)))
    def test_reject_no_receipt(self):self.assertFalse(exact_manifest_gate(replace(self.w,destination_receipt_verified=False)))
    def test_reject_no_carrier_auth(self):self.assertFalse(exact_manifest_gate(replace(self.w,carrier_authorization_verified=False)))
    def test_reject_bool_mass(self):self.assertFalse(exact_manifest_gate(replace(self.w,weighed_net_kg=True)))
    def test_hypothetical_food_panel(self):self.assertTrue(food_safety_gate(self.s))
    def test_reject_mixed_waste(self):self.assertFalse(food_safety_gate(replace(self.s,feedstock_class='MIXED_MUNICIPAL_FOOD_WASTE')))
    def test_reject_hazardous_feed(self):self.assertFalse(food_safety_gate(replace(self.s,feedstock_class='HAZARDOUS_WASTE')))
    def test_reject_absent_salmonella(self):self.assertFalse(food_safety_gate(replace(self.s,lab_panel={k:v for k,v in self.s.lab_panel.items() if k!='salmonella'})))
    def test_reject_unverified_metals(self):self.assertFalse(food_safety_gate(replace(self.s,lab_panel={**self.s.lab_panel,'lead':'PASS'})))
    def test_reject_no_product_permission(self):self.assertFalse(food_safety_gate(replace(self.s,target_product_class_approved=False)))
    def test_reject_no_strain_safety(self):self.assertFalse(food_safety_gate(replace(self.s,organism_safety_review_verified=False)))
    def test_reject_no_haccp(self):self.assertFalse(food_safety_gate(replace(self.s,haccp_reference='')))
    def test_scope_transfer_not_autobooked(self):self.assertFalse(boundary_allows_measured_transfer(MaterialBoundary(Scope.QINGDAO_CITY,Scope.DJK_ECON_ZONE,Evidence.REPORTED,True,True,True)))
    def test_scope_transfer_explicit_measured(self):self.assertTrue(boundary_allows_measured_transfer(MaterialBoundary(Scope.QINGDAO_CITY,Scope.DJK_ECON_ZONE,Evidence.MEASURED,True,True,True)))
    def test_no_verified_receiver(self):self.assertFalse(boundary_allows_measured_transfer(MaterialBoundary(Scope.QINGDAO_CITY,Scope.DJK_PORT_AREA,Evidence.MEASURED,True,True,False)))
    def test_gypsum_ratio_design(self):self.assertEqual(phosphogypsum_design_ratio(1_000_000,400_000),Decimal('0.4'))
    def test_gypsum_invalid(self):
        with self.assertRaises(ValueError):phosphogypsum_design_ratio(0,10)
    def test_sludge_82_75_wan_t(self):self.assertEqual(normalized_mass_t('82.75','万吨'),Decimal(827500))
    def test_units_do_not_equate(self):self.assertNotEqual(normalized_mass_t('82.75','Mt'),normalized_mass_t('82.75','万吨'))
    def test_port_design_not_actual(self):self.assertFalse(may_report_as_actual_capacity(DeclaredCapacity(Scope.DJK_PORT_AREA,'CRUDE_OIL_DOCKS',Decimal(25_500_000),2020)))
if __name__=='__main__':unittest.main()
