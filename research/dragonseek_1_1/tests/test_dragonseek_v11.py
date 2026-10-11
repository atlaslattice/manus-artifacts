import sys, unittest
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'engine'))
from dragonseek_v11 import *
NOW=datetime(2026,10,11,12,tzinfo=timezone.utc)
BASE={'id':'x','kind':'seismic','label':'Demo only','classification':'GENERAL_PUBLIC','event_provenance':'SYNTHETIC','timestamp':'2026-10-11T12:00:00+00:00','geometry_precision':'region','data_flow_authorization':'SIMULATED_DEMO','data_owner':'RESEARCH_AUTHOR','jurisdiction':'GLOBAL_PUBLIC','scope':'China','crs':'EPSG:4326'}
class Gate(unittest.TestCase):
 def test_public_synthetic(self):self.assertTrue(release_gate(BASE,now=NOW)[0])
 def test_no_raw_critical(self):self.assertFalse(release_gate({**BASE,'contains_raw_critical_infrastructure':True},now=NOW)[0])
 def test_no_identifiable_person(self):self.assertFalse(release_gate({**BASE,'contains_personal_data':True},now=NOW)[0])
 def test_no_unknown_class(self):self.assertFalse(release_gate({**BASE,'classification':'UNKNOWN'},now=NOW)[0])
 def test_core_fail(self):self.assertFalse(release_gate({**BASE,'classification':'CORE'},now=NOW)[0])
 def test_important_bool_not_sufficient(self):
  e={**BASE,'classification':'IMPORTANT','aggregation_certified':True,'reidentification_review_pass':True,'has_documented_authorization':True};self.assertFalse(release_gate(e,Viewer(role='authorized_aggregated'),now=NOW)[0])
 def test_important_untrusted_registry(self):
  e={**BASE,'classification':'IMPORTANT','aggregation_certified':True,'reidentification_review_pass':True,'purpose':'aggregate','authorization_id':'A1'};r=AuthorizationRecord('A1','issuer','RESEARCH_AUTHOR','person',('aggregate',),('China',),'GLOBAL_PUBLIC','2026-10-12T12:00:00Z','a'*64,'review');self.assertFalse(release_gate(e,Viewer(role='authorized_aggregated',identity='person'),AuthorizationRegistry([r]),now=NOW)[0])
 def test_important_trusted_registry(self):
  e={**BASE,'classification':'IMPORTANT','aggregation_certified':True,'reidentification_review_pass':True,'purpose':'aggregate','authorization_id':'A1','geometry_precision':'region'};r=AuthorizationRecord('A1','issuer','RESEARCH_AUTHOR','person',('aggregate',),('China',),'GLOBAL_PUBLIC','2026-10-12T12:00:00Z','a'*64,'review');auth=AuthorizationRegistry([r],trusted_document_hashes=['a'*64],trusted_issuers=['issuer']);self.assertTrue(release_gate(e,Viewer(role='authorized_aggregated',identity='person'),auth,now=NOW)[0])
 def test_important_expired(self):
  e={**BASE,'classification':'IMPORTANT','aggregation_certified':True,'reidentification_review_pass':True,'purpose':'aggregate','authorization_id':'A1'};r=AuthorizationRecord('A1','issuer','RESEARCH_AUTHOR','person',('aggregate',),('China',),'GLOBAL_PUBLIC','2026-10-10T12:00:00Z','a'*64,'review');auth=AuthorizationRegistry([r],trusted_document_hashes=['a'*64],trusted_issuers=['issuer']);self.assertFalse(release_gate(e,Viewer(role='authorized_aggregated',identity='person'),auth,now=NOW)[0])
 def test_important_cross_border(self):
  e={**BASE,'classification':'IMPORTANT','aggregation_certified':True,'reidentification_review_pass':True,'purpose':'aggregate','authorization_id':'A1','export_destination':'OVERSEAS'};r=AuthorizationRecord('A1','issuer','RESEARCH_AUTHOR','person',('aggregate',),('China',),'GLOBAL_PUBLIC','2026-10-12T12:00:00Z','a'*64,'review');auth=AuthorizationRegistry([r],trusted_document_hashes=['a'*64],trusted_issuers=['issuer']);self.assertFalse(release_gate(e,Viewer(role='authorized_aggregated',identity='person'),auth,now=NOW)[0])
 def test_no_missing_owner(self):self.assertFalse(release_gate({k:v for k,v in BASE.items() if k!='data_owner'},now=NOW)[0])
 def test_precise_location_reject(self):self.assertFalse(release_gate({**BASE,'geometry_precision':'facility'},now=NOW)[0])
 def test_timezone_offset_required(self):self.assertFalse(release_gate({**BASE,'timestamp':'2026-10-11T12:00:00'},now=NOW)[0])
 def test_utc_plus_offset(self):self.assertTrue(release_gate({**BASE,'timestamp':'2026-10-11T20:00:00+08:00'},now=NOW)[0])
 def test_future_timestamp_doesnt_affect_synthetic(self):self.assertTrue(release_gate({**BASE,'timestamp':'2026-10-12T12:00:00+00:00'},now=NOW)[0])
 def test_celestial_not_georeferenced(self):self.assertTrue(release_gate({**BASE,'kind':'neo','geometry_precision':'celestial-nonlocalized','crs':'NONE_CELESTIAL'},now=NOW)[0])
 def test_mixed_crs_reject(self):self.assertFalse(release_gate({**BASE,'crs':'GCJ02'},now=NOW)[0])
 def test_reported_badge(self):self.assertFalse(release_gate({**BASE,'event_provenance':'COLLABORATOR_REPORTED'},now=NOW)[0])
 def test_reported_requires_source(self):self.assertFalse(release_gate({**BASE,'event_provenance':'COLLABORATOR_REPORTED','display_badge':'REPORTED_NOT_VERIFIED'},now=NOW)[0])
 def test_model_fresh(self):
  e={**BASE,'event_provenance':'MODEL_FORECAST','data_flow_authorization':'PUBLIC_OPEN_LICENSE','retrieved_at':'2026-10-11T11:00:00Z','ttl_seconds':7200,'source_url':'https://example.org','license_ref':'public'};self.assertTrue(release_gate(e,now=NOW)[0])
 def test_model_stale_rejected(self):
  e={**BASE,'event_provenance':'MODEL_FORECAST','data_flow_authorization':'PUBLIC_OPEN_LICENSE','retrieved_at':'2026-10-11T08:00:00Z','ttl_seconds':7200,'source_url':'https://example.org','license_ref':'public'};self.assertFalse(release_gate(e,now=NOW)[0])
 def test_no_license(self):
  e={**BASE,'event_provenance':'MEASURED','data_flow_authorization':'PUBLIC_OPEN_LICENSE','retrieved_at':'2026-10-11T11:00:00Z','ttl_seconds':7200};self.assertFalse(release_gate(e,now=NOW)[0])
 def test_no_clearance_for_core_even_trusted(self):self.assertFalse(release_gate({**BASE,'classification':'CORE'},now=NOW)[0])
 def test_filter_public(self):self.assertEqual(len(filter_public([BASE,{**BASE,'id':'bad','classification':'CORE'}],now=NOW)[0]),1)
 def test_hash_order(self):self.assertEqual(canonical_hash(BASE),canonical_hash(dict(reversed(list(BASE.items())))))
 def test_timestamp_parser(self):self.assertEqual(utc_dt('2026-10-11T20:00:00+08:00'),NOW)
 def test_missing_ttl(self):self.assertEqual(feed_state({**BASE,'event_provenance':'MEASURED'},NOW),'FRESHNESS_UNKNOWN')
 def test_expired_ttl(self):self.assertEqual(feed_state({**BASE,'event_provenance':'MEASURED','retrieved_at':'2026-10-11T09:00:00Z','ttl_seconds':3600},NOW),'STALE')
 def test_future_fetch(self):self.assertEqual(feed_state({**BASE,'event_provenance':'MEASURED','retrieved_at':'2026-10-11T13:00:00Z','ttl_seconds':3600},NOW),'FUTURE_TIMESTAMP')
 def test_synthetic_state(self):self.assertEqual(feed_state(BASE,NOW),'SIMULATED')
class Power(unittest.TestCase):
 def args(self,**kwargs):return dict(critical_load_kw=20,pv_nameplate_kw=35,battery_usable_kwh=380,cloud_attenuation=.65,**kwargs)
 def test_v10_reproduced_24(self):self.assertEqual(microgrid_168h(**self.args())['essential_hours_fully_served'],24)
 def test_storage_only_17(self):self.assertEqual(microgrid_168h(**self.args(),mode='storage_only')['essential_hours_fully_served'],17)
 def test_replenishment_better(self):
  a=compare_microgrid(**self.args());self.assertGreater(a['replenishment']['essential_hours_fully_served'],a['storage_only']['essential_hours_fully_served'])
 def test_discharge_capped(self):
  a=microgrid_168h(critical_load_kw=20,pv_nameplate_kw=0,battery_usable_kwh=380,battery_max_discharge_kw=5);self.assertEqual(a['essential_hours_fully_served'],0);self.assertLessEqual(max(x['battery_discharge_kw'] for x in a['trace']),5)
 def test_charge_capped(self):
  a=microgrid_168h(critical_load_kw=1,pv_nameplate_kw=100,battery_usable_kwh=30,initial_soc_fraction=0,battery_max_charge_kw=2);self.assertLessEqual(max(x['battery_charge_kw'] for x in a['trace']),2)
 def test_soc_nonnegative(self):self.assertGreaterEqual(min(x['soc_kwh'] for x in microgrid_168h(**self.args())['trace']),0)
 def test_baseline_no_solar(self):self.assertEqual(microgrid_168h(**self.args(),mode='storage_only')['solar_generated_kwh'],0)
 def test_honest_failing_stress(self):self.assertFalse(microgrid_168h(**self.args())['seven_day_target_met'])
 def test_load_always_served_if_firm_battery_huge(self):self.assertTrue(microgrid_168h(critical_load_kw=10,pv_nameplate_kw=0,battery_usable_kwh=1900)['seven_day_target_met'])
 def test_crude_label(self):self.assertFalse(microgrid_168h(**self.args())['weather_derived'])
 def test_reject_negative(self):
  with self.assertRaises(ValueError):microgrid_168h(critical_load_kw=-1,pv_nameplate_kw=0,battery_usable_kwh=0)
 def test_reject_unknown_mode(self):
  with self.assertRaises(ValueError):microgrid_168h(critical_load_kw=1,pv_nameplate_kw=0,battery_usable_kwh=1,mode='planetary')
 def test_non_replenish_soc_decay(self):
  a=microgrid_168h(**self.args(),mode='storage_only');self.assertEqual(a['trace'][-1]['soc_kwh'],0)
 def test_charge_less_than_capacity(self):
  a=microgrid_168h(critical_load_kw=5,pv_nameplate_kw=100,battery_usable_kwh=30);self.assertLessEqual(max(x['soc_kwh'] for x in a['trace']),30)
 def test_reject_battery_power_negative(self):
  with self.assertRaises(ValueError):microgrid_168h(critical_load_kw=1,pv_nameplate_kw=0,battery_usable_kwh=1,battery_max_discharge_kw=-1)
if __name__=='__main__':unittest.main()