"""DragonSeek 1.1: conservative READ-ONLY synthetic science/event gate and microgrid screener.
Not certified regulatory control, collision-avoidance, epidemiological diagnosis, or warning software.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from hashlib import sha256
from math import sin, pi
import json

KINDS={'node','flood','fire','typhoon','heat','marine','outage','supply','resilience','weather',
       'seismic','geophysical','airspace','orbital','meteor','neo','locust','pathogen','wastewater','global-project'}
PROVENANCE={'MEASURED','OFFICIAL_ALERT','MODEL_FORECAST','SATELLITE_RETRIEVAL','COLLABORATOR_REPORTED','SYNTHETIC','CATALOG_ONLY'}
PUBLIC_CLASS='GENERAL_PUBLIC'
ISO_UTC='2026-10-11T00:00:00+00:00'


def utc_dt(value):
    if not isinstance(value,str):raise ValueError('datetime must be offset-aware ISO string')
    dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    if dt.tzinfo is None or dt.utcoffset() is None:raise ValueError('explicit time offset required')
    return dt.astimezone(timezone.utc)


def canonical_hash(d):
    return sha256(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()


@dataclass(frozen=True)
class Viewer:
    role:str='public'
    organization:str=''
    identity:str=''


@dataclass(frozen=True)
class AuthorizationRecord:
    authorization_id:str
    issuer:str
    data_owner:str
    viewer_identity:str
    purposes:tuple[str,...]
    scopes:tuple[str,...]
    jurisdiction:str
    expiry:str
    document_sha256:str
    aggregation_review_ref:str


class AuthorizationRegistry:
    """Demo registry only. Trusted issuer+document SHA supplied by verifier, NOT user checkbox.
    No network verification, cryptographic signature, revocation service, or regulator certification.
    For test demonstration, a trusted set must be configured out-of-band by human reviewer.
    """
    def __init__(self,records=None,trusted_document_hashes=None,trusted_issuers=None):
        self.records={r.authorization_id:r for r in (records or [])}
        self.trusted_document_hashes=set(trusted_document_hashes or [])
        self.trusted_issuers=set(trusted_issuers or [])

    def valid(self,authorization_id,event,viewer,now):
        r=self.records.get(authorization_id)
        if not r:return False
        if (r.issuer not in self.trusted_issuers or r.document_sha256 not in self.trusted_document_hashes or
            not r.aggregation_review_ref or r.viewer_identity!=viewer.identity or r.data_owner!=event.get('data_owner') or
            event.get('jurisdiction')!=r.jurisdiction or viewer.role!='authorized_aggregated' or
            event.get('purpose') not in r.purposes or event.get('scope') not in r.scopes):return False
        try:return utc_dt(r.expiry)>now
        except ValueError:return False


def feed_state(event,now=None):
    """Synthetic events never imply a live feed. Real feeds fail closed without retrieval/TTL."""
    if event.get('event_provenance')=='SYNTHETIC':return 'SIMULATED'
    if event.get('event_provenance')=='CATALOG_ONLY':return 'NOT_CONNECTED'
    if now is None:now=datetime.now(timezone.utc)
    try:
        retrieved=utc_dt(event['retrieved_at']);ttl=int(event['ttl_seconds'])
        if ttl<=0 or ttl>604800:return 'INVALID_TTL'
        if retrieved>now+timedelta(minutes=2):return 'FUTURE_TIMESTAMP'
        return 'FRESH' if now<=retrieved+timedelta(seconds=ttl) else 'STALE'
    except (KeyError,ValueError,TypeError,OverflowError):return 'FRESHNESS_UNKNOWN'


def release_gate(event,viewer=Viewer(),registry=None,now=None):
    """Demo release policy; never use as legal classification, security attestation or auth service."""
    if not isinstance(event,dict):return False,'INCOMPLETE_EVENT'
    required={'id','kind','label','classification','event_provenance','timestamp','geometry_precision',
              'data_flow_authorization','data_owner','jurisdiction','scope','crs'}
    if required-set(event):return False,'INCOMPLETE_EVENT'
    if not event['id'] or event['kind'] not in KINDS:return False,'BAD_KIND_OR_ID'
    if event['event_provenance'] not in PROVENANCE:return False,'BAD_PROVENANCE'
    try:utc_dt(event['timestamp'])
    except (ValueError,TypeError,OverflowError):return False,'INVALID_UTC_OFFSET'
    if event['crs'] not in ('EPSG:4326','EPSG:4490','NONE_CELESTIAL','NONE_NONSPATIAL'):
        return False,'UNSUPPORTED_CRS'
    if event['classification'] in ('CORE','UNKNOWN'):return False,'CORE_OR_UNKNOWN_NODE_ONLY'
    if event.get('contains_personal_data') or event.get('contains_raw_critical_infrastructure'):
        return False,'SENSITIVE_CONTENT'
    if event['classification']=='IMPORTANT':
        if (event.get('geometry_precision') not in ('province','region','ocean-basin') or
           event.get('aggregation_certified') is not True or
           event.get('reidentification_review_pass') is not True or
           event.get('export_destination') not in (None,'CHINA_DOMESTIC_AUTHORIZED')):
            return False,'AGGREGATE_DOMESTIC_REVIEW_REQUIRED'
        if not registry or not registry.valid(event.get('authorization_id'),event,viewer,now or datetime.now(timezone.utc)):
            return False,'VERIFIED_AUTHORIZATION_REQUIRED'
        # This demo returns a policy assessment, not a digitally signed operational release permit.
        return True,'RESEARCH_ONLY_DOMESTIC_AGGREGATE'
    if event['classification']!=PUBLIC_CLASS:return False,'INVALID_CLASSIFICATION'
    if event['data_flow_authorization'] not in ('SIMULATED_DEMO','PUBLIC_OPEN_LICENSE'):
        return False,'NO_PUBLIC_RIGHTS'
    if event.get('geometry_precision') not in ('city','province','region','ocean-basin','celestial-nonlocalized'):
        return False,'PRECISE_COORDINATE_BLOCKED'
    if event['event_provenance']=='COLLABORATOR_REPORTED' and event.get('display_badge')!='REPORTED_NOT_VERIFIED':
        return False,'REPORTED_BADGE_REQUIRED'
    if event['event_provenance'] not in ('SYNTHETIC','CATALOG_ONLY'):
        state=feed_state(event,now)
        if state!='FRESH':return False,'NOT_CURRENT_'+state
        if not event.get('source_url') or not event.get('license_ref'):
            return False,'SOURCE_LICENSE_MISSING'
    return True,'PUBLIC_RESEARCH_VIEW'


def filter_public(events,now=None):
    safe=[];denied=[]
    for e in events:
        ok,reason=release_gate(e,now=now)
        (safe if ok else denied).append(e if ok else {'id':e.get('id'),'reason':reason})
    return safe,denied


def microgrid_168h(*,critical_load_kw,pv_nameplate_kw,battery_usable_kwh,
                    cloud_attenuation=.65,battery_max_charge_kw=95.,battery_max_discharge_kw=95.,
                    battery_charge_efficiency=.92,battery_discharge_efficiency=.92,
                    initial_soc_fraction=1.,mode='replenishment',blackout_hours=168):
    """Crude synthetic 06:00-18:00 local sine; NOT weather/latitude/tilt or AC power-flow.
    Baseline and replenishment run identical loads, SOC and capacity, except PV toggling.
    Battery discharge cap is AC output kW; charge cap is AC input kW. Hourly step is 1h.
    """
    v=(critical_load_kw,pv_nameplate_kw,battery_usable_kwh,cloud_attenuation,
       battery_max_charge_kw,battery_max_discharge_kw,battery_charge_efficiency,
       battery_discharge_efficiency,initial_soc_fraction)
    if (not all(isinstance(t,(int,float)) and t==t and abs(t)<1e10 for t in v)
        or not (critical_load_kw>0 and pv_nameplate_kw>=0 and battery_usable_kwh>=0 and
        0<=cloud_attenuation<=1 and battery_max_charge_kw>=0 and battery_max_discharge_kw>=0 and
        0<battery_charge_efficiency<=1 and 0<battery_discharge_efficiency<=1 and
        0<=initial_soc_fraction<=1 and isinstance(blackout_hours,int) and 0<blackout_hours<=168)
        or mode not in ('storage_only','replenishment')):raise ValueError('invalid synthetic assumptions')
    soc=battery_usable_kwh*initial_soc_fraction
    served=0;unserved=0.;trace=[];solar_total=0.
    for h in range(168):
        solar=(pv_nameplate_kw*cloud_attenuation*max(0,sin((h%24-6)/12*pi))*.85
               if mode=='replenishment' else 0.)
        solar_total+=solar
        demand=critical_load_kw if h<blackout_hours else 0.
        direct=min(demand,solar)
        surplus=max(0.,solar-demand)
        deficit=max(0.,demand-direct)
        charge=min(surplus,battery_max_charge_kw,(battery_usable_kwh-soc)/battery_charge_efficiency)
        soc+=charge*battery_charge_efficiency
        batt=min(deficit,battery_max_discharge_kw,soc*battery_discharge_efficiency)
        soc-=batt/battery_discharge_efficiency
        delivered=direct+batt
        if h<blackout_hours:
            if delivered>=demand-1e-9:served+=1
            unserved+=max(0.,demand-delivered)
        trace.append({'hour':h+1,'demand_kw':round(demand,5),'solar_kw':round(solar,5),
                      'battery_charge_kw':round(charge,5),'battery_discharge_kw':round(batt,5),
                      'served_kw':round(delivered,5),'soc_kwh':round(soc,5)})
    return {'mode':mode,'synthetic':True,'model':'CRUDE_12H_SINE_NO_WEATHER','weather_derived':False,
            'horizon_hours':168,'blackout_hours':blackout_hours,'solar_generated_kwh':round(solar_total,3),
            'essential_hours_fully_served':served,'unserved_kwh':round(unserved,3),
            'end_soc_kwh':round(soc,3),
            'seven_day_target_met':served==168 and blackout_hours==168,'trace':trace}


def compare_microgrid(**kwargs):
    a=microgrid_168h(mode='storage_only',**kwargs)
    b=microgrid_168h(mode='replenishment',**kwargs)
    return {'storage_only':a,'replenishment':b,'isolated_variable':'pv_replenishment_on_off',
            'status':'SYNTHETIC_SCREENING_ONLY_NO_PHYSICAL_VALIDATION'}

if __name__=='__main__':
    print(json.dumps(compare_microgrid(critical_load_kw=20,pv_nameplate_kw=35,battery_usable_kwh=380),indent=2))