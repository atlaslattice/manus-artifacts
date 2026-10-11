"""DragonSeek DJK-001 semantics v0.7 research prototype.
Provenance-sensitive unit translation, NOT certified engineering software.
No source authenticity, legal authorization, or regulatory compliance inferred.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import json
from typing import Any

REGISTRY_ID='DJK-SEMANTICS-0.7.0'

@dataclass(frozen=True)
class Recipe:
    id: str
    dimension: str
    original_unit: str
    canonical_unit: str
    numerator: str
    denominator: str='1'
    basis_required: tuple[str,...]=()
    def factor(self)->Decimal:return Decimal(self.numerator)/Decimal(self.denominator)

REGISTRY={r.original_unit:r for r in (
    Recipe('wan_t_to_kg@1.0.0','mass','万吨','kg','10000000',basis_required=('mass_basis',)),
    Recipe('t_to_kg@1.0.0','mass','吨','kg','1000',basis_required=('mass_basis',)),
    Recipe('kg_identity@1.0.0','mass','kg','kg','1',basis_required=('mass_basis',)),
    Recipe('yi_m3_to_m3@1.0.0','volume','亿m³','m³','100000000',basis_required=('phase',)),
    Recipe('m3_identity@1.0.0','volume','m³','m³','1',basis_required=('phase',)),
    Recipe('mu_to_m2@1.0.0','area','亩','m²','2000','3'),
    Recipe('tce_to_j@1.0.0','energy','tce','J','29307000000',basis_required=('energy_basis',)),
    Recipe('kwh_to_j@1.0.0','energy','kWh','J','3600000',basis_required=('energy_basis',)),
    Recipe('wan_cny_to_cny@1.0.0','currency','万元','CNY','10000',basis_required=('price_year','currency_basis')),
    Recipe('yi_cny_to_cny@1.0.0','currency','亿元','CNY','100000000',basis_required=('price_year','currency_basis')),
    Recipe('cny_identity@1.0.0','currency','元','CNY','1',basis_required=('price_year','currency_basis')),
    Recipe('mg_l_to_kg_m3@1.0.0','mass_per_liquid_volume','mg/L','kg/m³','0.001',basis_required=('phase',)),
    Recipe('mg_kg_to_kg_kg@1.0.0','mass_per_mass','mg/kg','kg/kg','0.000001',basis_required=('mass_basis',)),
    Recipe('celsius_to_k@1.0.0','temperature','°C','K','1'),
    Recipe('k_identity@1.0.0','temperature','K','K','1'),
)}
SPECIAL_CONTEXT_UNITS={'ppm','ppmv','mg/Nm³','Nm³','kg/s','m³/s','pH','dB(A)','bcm'}
class SemanticError(ValueError):pass

def D(value:Any)->Decimal:
    if isinstance(value,bool):raise SemanticError('Boolean is not numeric evidence')
    try:d=Decimal(str(value))
    except (InvalidOperation,TypeError) as err:raise SemanticError('Invalid decimal') from err
    if not d.is_finite():raise SemanticError('Non-finite numeric evidence')
    return d

def canonicalize(*,original_value:Any,original_unit:str,basis:dict[str,Any],
                 period:str,boundary:str,scope:str,source_uri:str,
                 evidence_class:str,statistic:str,qualifier:str='=',
                 original_lexeme:str|None=None)->dict[str,Any]:
    """Retain original; DERIVED conversion is never relabeled measured."""
    if original_unit in SPECIAL_CONTEXT_UNITS:
        raise SemanticError('Ambiguous/contextual unit needs separate reviewed recipe')
    if original_unit not in REGISTRY:raise SemanticError('Unknown or unversioned unit')
    if not isinstance(basis,dict):raise SemanticError('Basis dictionary required')
    for k in ('period','boundary','scope','source_uri','evidence_class','statistic'):
        if not isinstance(locals()[k],str) or not locals()[k].strip():
            raise SemanticError(f'{k} required; cannot silently default')
    if qualifier not in ('=','<','<=','>','>='):
        raise SemanticError('Explicit measurement qualifier required')
    r=REGISTRY[original_unit]
    for k in r.basis_required:
        if k not in basis or basis[k] in (None,'','UNKNOWN'):
            raise SemanticError(f'Missing contextual basis {k}')
    number=D(original_value)
    if r.dimension in ('mass','volume','area','mass_per_liquid_volume','mass_per_mass','energy') and number<0:
        raise SemanticError('Negative material/energy measurement unsupported')
    value=(number+Decimal('273.15')) if original_unit=='°C' else number*r.factor()
    result={
        'original':{'value':str(original_value),'unit':original_unit,
                    'lexeme':original_lexeme or str(original_value),'qualifier':qualifier},
        'canonical':{'value':str(value),'unit':r.canonical_unit,'qualifier':qualifier},
        'recipe_id':r.id,'registry_id':REGISTRY_ID,
        'basis':basis,'period':period,'boundary':boundary,'scope':scope,
        'source_uri':source_uri,'source_evidence_class':evidence_class,
        'source_statistic':statistic,'transformation_class':'DERIVED',
        'source_verification':'NOT_AUTOMATICALLY_VERIFIED',
    }
    result['recipe_sha256']=sha256(json.dumps(asdict(r),sort_keys=True,ensure_ascii=False).encode('utf8')).hexdigest()
    return result

def dry_mass_from_wet(wet_kg:Any,moisture_fraction:Any)->dict[str,str]:
    wet,water=D(wet_kg),D(moisture_fraction)
    if wet<0 or not (Decimal(0)<=water<=Decimal(1)):
        raise SemanticError('Invalid mass/moisture')
    return {'dry_mass_kg':str(wet*(1-water)),'wet_mass_kg':str(wet),
            'moisture_fraction_wet_basis':str(water),'transformation_class':'DERIVED',
            'assumption':'uniform representative moisture fraction on wet-mass basis'}

def normalize_censored(value:Any,unit:str,**kw):
    """Preserve <LOD: never equate not-detected with true zero."""
    return canonicalize(original_value=value,original_unit=unit,qualifier='<',**kw)

def compare_compatible(a,b):
    """Refuse aggregation when source scope or reporting basis differs."""
    for field in ('scope','boundary','period','source_statistic'):
        if a.get(field)!=b.get(field):raise SemanticError(f'Mismatched aggregation {field}')
    if a.get('basis')!=b.get('basis'):raise SemanticError('Mismatched basis')
    if a['canonical']['unit']!=b['canonical']['unit']:raise SemanticError('Mismatched canonical unit')
    if a['canonical']['qualifier']!='=' or b['canonical']['qualifier']!='=':
        raise SemanticError('Censored or bounded values need separate aggregation logic')
    return D(a['canonical']['value'])+D(b['canonical']['value'])
