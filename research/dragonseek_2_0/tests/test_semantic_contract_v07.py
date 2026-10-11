"""Mock evidence validation for v0.7 semantics. NOT physical metrology or GitHub CI."""
import unittest
from decimal import Decimal
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from semantic_contract_v07 import *
BASE=dict(basis={'mass_basis':'as_reported_unknown_moisture'},period='2025-annual',boundary='municipal_generation',scope='QINGDAO_CITY',source_uri='https://www.qingdao.gov.cn/',evidence_class='REPORTED',statistic='annual_generated')
class RegistryTests(unittest.TestCase):
    def test_wan_t(self):self.assertEqual(Decimal(canonicalize(original_value='422.7',original_unit='万吨',**BASE)['canonical']['value']),Decimal('4227000000'))
    def test_source_literal_retained(self):self.assertEqual(canonicalize(original_value='422.7',original_unit='万吨',original_lexeme='422.7 万吨',**BASE)['original']['lexeme'],'422.7 万吨')
    def test_dry_mass(self):self.assertEqual(Decimal(dry_mass_from_wet('4227000000','0.15')['dry_mass_kg']),Decimal('3592950000'))
    def test_sludge(self):self.assertEqual(Decimal(canonicalize(original_value='82.75',original_unit='万吨',**BASE)['canonical']['value']),Decimal('827500000'))
    def test_yi_volume(self):
        d={**BASE,'basis':{'phase':'liquid'}};self.assertEqual(canonicalize(original_value=1,original_unit='亿m³',**d)['canonical']['value'],'100000000')
    def test_tce(self):
        d={**BASE,'basis':{'energy_basis':'standard_coal_equivalent'}};self.assertEqual(canonicalize(original_value=1,original_unit='tce',**d)['canonical']['value'],'29307000000')
    def test_mg_l(self):
        d={**BASE,'basis':{'phase':'ambient_seawater'}};self.assertEqual(canonicalize(original_value='0.144',original_unit='mg/L',**d)['canonical']['value'],'0.000144')
    def test_less_than_detection(self):
        d={**BASE,'basis':{'phase':'ambient_seawater'}};r=normalize_censored('0.004','mg/L',**d);self.assertEqual(r['canonical']['qualifier'],'<');self.assertEqual(r['canonical']['value'],'0.000004')
    def test_celsius_offset(self):self.assertEqual(canonicalize(original_value='25',original_unit='°C',**BASE)['canonical']['value'],'298.15')
    def test_mu(self):self.assertEqual(Decimal(canonicalize(original_value=3,original_unit='亩',**BASE)['canonical']['value']),Decimal('2000'))
    def test_yi_cny(self):
        d={**BASE,'basis':{'price_year':'2025','currency_basis':'nominal'}};self.assertEqual(canonicalize(original_value='1',original_unit='亿元',**d)['canonical']['value'],'100000000')
    def test_unknown_unit(self):
        with self.assertRaises(SemanticError):canonicalize(original_value=1,original_unit='ligma',**BASE)
    def test_ambiguous_ppm(self):
        with self.assertRaises(SemanticError):canonicalize(original_value=1,original_unit='ppm',**BASE)
    def test_contextual_Nm3(self):
        with self.assertRaises(SemanticError):canonicalize(original_value=1,original_unit='mg/Nm³',**BASE)
    def test_basis_missing(self):
        with self.assertRaises(SemanticError):canonicalize(original_value='1',original_unit='万吨',**{**BASE,'basis':{}})
    def test_source_missing(self):
        with self.assertRaises(SemanticError):canonicalize(original_value='1',original_unit='万吨',**{**BASE,'source_uri':''})
    def test_negative_material(self):
        with self.assertRaises(SemanticError):canonicalize(original_value='-1',original_unit='万吨',**BASE)
    def test_bool_fail(self):
        with self.assertRaises(SemanticError):canonicalize(original_value=True,original_unit='万吨',**BASE)
    def test_no_aggregation_different_scope(self):
        a=canonicalize(original_value=1,original_unit='万吨',**BASE)
        b=canonicalize(original_value=1,original_unit='万吨',**{**BASE,'scope':'DJK_ECON_ZONE'})
        with self.assertRaises(SemanticError):compare_compatible(a,b)
    def test_no_aggregation_censored(self):
        a=canonicalize(original_value=1,original_unit='万吨',**BASE)
        b=canonicalize(original_value=1,original_unit='万吨',qualifier='<',**BASE)
        with self.assertRaises(SemanticError):compare_compatible(a,b)
    def test_no_aggregation_different_basis(self):
        a=canonicalize(original_value=1,original_unit='万吨',**BASE)
        b=canonicalize(original_value=1,original_unit='万吨',**{**BASE,'basis':{'mass_basis':'dry'}})
        with self.assertRaises(SemanticError):compare_compatible(a,b)
    def test_recipe_sha_stable(self):
        a=canonicalize(original_value=1,original_unit='万吨',**BASE)
        b=canonicalize(original_value=2,original_unit='万吨',**BASE)
        self.assertEqual(a['recipe_sha256'],b['recipe_sha256'])
    def test_report_value_not_measured(self):
        a=canonicalize(original_value='0.144',original_unit='mg/L',**{**BASE,'basis':{'phase':'ambient_seawater'}})
        self.assertEqual(a['source_evidence_class'],'REPORTED');self.assertEqual(a['transformation_class'],'DERIVED')
    def test_qualifier_not_zero(self):
        a=normalize_censored('0.01','mg/L',**{**BASE,'basis':{'phase':'ambient_seawater'}})
        self.assertNotEqual(a['canonical']['value'],'0')
    def test_year_to_seconds_not_assumed(self):
        with self.assertRaises(SemanticError):canonicalize(original_value=1,original_unit='万吨/年',**BASE)
if __name__=='__main__':unittest.main()
