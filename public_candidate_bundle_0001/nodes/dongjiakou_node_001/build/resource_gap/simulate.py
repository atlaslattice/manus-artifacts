#!/usr/bin/env python3
"""Candidate interval resource model; no plant controls or realized credits.

Zero runtime dependencies. The validator implements the keyword subset used by
the adjacent JSON Schema, not a general-purpose JSON Schema implementation.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECEIPTS = ('yield', 'selectivity', 'energy', 'reagents', 'material_life',
            'residual_fate', 'market_ceiling', 'ecology')
LOOPS = ('source', 'mass', 'quality', 'right_to_transfer', 'time',
         'displacement', 'residual_fate', 'allocation')


def validate(value, rule, path='$'):
    """Validate exactly the schema keywords used by this project."""
    if 'anyOf' in rule:
        for option in rule['anyOf']:
            try:
                validate(value, option, path)
                return
            except ValueError:
                pass
        raise ValueError(f'{path}: does not match any allowed shape')
    kind = rule.get('type')
    ok = {'object': isinstance(value, dict), 'array': isinstance(value, list),
          'string': isinstance(value, str), 'null': value is None,
          'number': type(value) in (int, float) and math.isfinite(value),
          'integer': type(value) is int, 'boolean': type(value) is bool}
    if kind and not ok[kind]:
        raise ValueError(f'{path}: expected {kind}')
    if 'enum' in rule and value not in rule['enum']:
        raise ValueError(f'{path}: invalid enum value')
    if isinstance(value, dict):
        for key in rule.get('required', []):
            if key not in value:
                raise ValueError(f'{path}.{key}: required (use null for unknown)')
        props = rule.get('properties', {})
        if rule.get('additionalProperties') is False and set(value) - set(props):
            raise ValueError(f'{path}: unknown fields {sorted(set(value)-set(props))}')
        for key, val in value.items():
            if key in props:
                validate(val, props[key], f'{path}.{key}')
    if isinstance(value, list):
        if len(value) < rule.get('minItems', 0):
            raise ValueError(f'{path}: too few items')
        for i, val in enumerate(value):
            validate(val, rule.get('items', {}), f'{path}[{i}]')
    if type(value) in (float, int):
        if value < rule.get('minimum', -math.inf) or value > rule.get('maximum', math.inf):
            raise ValueError(f'{path}: outside bounds')
    if isinstance(value, str) and len(value.strip()) < rule.get('minLength', 0):
        raise ValueError(f'{path}: empty text')


def read_case(path):
    raw = Path(path).read_bytes()
    case = json.loads(raw)
    return case, hashlib.sha256(raw).hexdigest()


def quantity(q):
    return None if q['low'] is None else (q['low'], q['high'])


def multiply(*pairs):
    if any(p is None for p in pairs):
        return None
    return (math.prod(p[0] for p in pairs), math.prod(p[1] for p in pairs))


def cap(pair, *limits):
    if pair is None or any(p is None for p in limits):
        return None
    return tuple(min(p[i] for p in (pair, *limits)) for i in (0, 1))


def exported(pair):
    return None if pair is None else {'low': pair[0], 'high': pair[1]}


def check_quantities(case):
    """Cross-field checks beyond structural JSON Schema."""
    missing = []
    def walk(value, path='$'):
        if isinstance(value, dict):
            if {'low', 'high', 'unit', 'status', 'source'} <= value.keys():
                low, high = value['low'], value['high']
                if (low is None) != (high is None):
                    raise ValueError(f'{path}: both interval endpoints must be null or numeric')
                if low is not None and low > high:
                    raise ValueError(f'{path}: inverted interval')
                if value['unit'] == 'fraction' and low is not None and high > 1:
                    raise ValueError(f'{path}: fraction exceeds one')
                if (value['status'] == 'UNKNOWN') != (low is None):
                    raise ValueError(f'{path}: UNKNOWN requires null; numbers require a labeled basis')
                if value['status'] in ('REFERENCE', 'MEASURED') and not value['source']:
                    raise ValueError(f'{path}: reference/measured input requires source')
                if low is None:
                    missing.append(path)
            for key, val in value.items():
                walk(val, f'{path}.{key}')
        elif isinstance(value, list):
            for i, val in enumerate(value):
                walk(val, f'{path}[{i}]')
    walk(case)
    identities = set()
    for route in case['routes']:
        identity = route['stream_id']
        if identity in identities:
            raise ValueError(f'duplicate stream_id {identity}: allocate once; split streams upstream')
        identities.add(identity)
        for group in ('module_receipts', 'loop_receipts'):
            for key, receipt in route[group].items():
                if receipt['status'] == 'PASS' and not receipt['source']:
                    raise ValueError(f'{route["id"]}.{group}.{key}: PASS requires source')
                if receipt['status'] != 'PASS':
                    missing.append(f'{route["id"]}.{group}.{key}:{receipt["status"]}')
        f, p = route['feed'], route['process']
        if f['mass']['unit'] != 't_feed_as_received/y':
            raise ValueError('feed mass unit mismatch')
        for key in ('dry_fraction', 'allocated_fraction', 'delivered_fraction', 'accepted_fraction'):
            if f[key]['unit'] != 'fraction':
                raise ValueError(f'{key}: expected fraction')
        if p['yield']['unit'] != 't_product/t_dry_accepted_feed':
            raise ValueError('yield unit mismatch')
        if p['conservation_ceiling']['unit'] != p['yield']['unit']:
            raise ValueError('ceiling unit mismatch')
        y, ceiling = quantity(p['yield']), quantity(p['conservation_ceiling'])
        if y and ceiling and y[1] > ceiling[1] + 1e-12:
            raise ValueError('yield exceeds declared constituent/stoichiometric ceiling')
        if route['product_basis'] != case['resource_basis']:
            raise ValueError('product and demand bases differ; convert explicitly upstream')
        if p['energy_intensity']['unit'] != 'MWh/t_dry_accepted_feed':
            raise ValueError('energy intensity unit mismatch')
        for q in (p['hub_capacity'], route['market_ceiling']):
            if q['unit'] != 't_product/y':
                raise ValueError('capacity/market unit mismatch')
    if len({r['id'] for r in case['routes']}) != len(case['routes']):
        raise ValueError('duplicate route id')
    for key in ('requirement', 'secure_domestic_supply'):
        if case['demand'][key]['unit'] != 't_product/y':
            raise ValueError('demand unit mismatch')
    if case['demand']['reserve_stock']['unit'] != 't_product':
        raise ValueError('reserve must be stock, not annual flow')
    return missing


def simulate(case, input_sha256=None):
    validate(case, json.loads((ROOT / 'scenario.schema.json').read_text()))
    missing = check_quantities(case)
    results = []
    for r in case['routes']:
        f, p = r['feed'], r['process']
        feed = multiply(*(quantity(f[k]) for k in ('mass', 'dry_fraction',
                        'allocated_fraction', 'delivered_fraction', 'accepted_fraction')))
        yield_bound = cap(quantity(p['yield']), quantity(p['conservation_ceiling']))
        gross = multiply(feed, yield_bound)
        limited = cap(gross, quantity(p['hub_capacity']), quantity(r['market_ceiling']))
        receipts = [v for group in ('module_receipts', 'loop_receipts') for v in r[group].values()]
        veto = any(r[group][key]['status'] == 'FAIL'
                   for group in ('module_receipts', 'loop_receipts')
                   for key in ('ecology', 'residual_fate') if key in r[group])
        all_pass = all(v['status'] == 'PASS' for v in receipts)
        if veto or any(v['status'] == 'FAIL' for v in receipts):
            eligible, state = (0.0, 0.0), 'BLOCKED'
        elif all_pass and limited is not None and quantity(p['energy_intensity']) is not None:
            eligible, state = limited, 'CONDITIONAL_MODEL_ONLY'
        else:
            eligible, state = None, 'UNKNOWN_PENDING_RECEIPTS'
        results.append({'route_id': r['id'], 'pathway_kind': r['pathway_kind'],
            'accepted_dry_feed_t_y': exported(feed),
            'gross_product_t_y': exported(gross),
            'capacity_and_market_limited_product_t_y': exported(limited),
            'evidence_gated_product_t_y': exported(eligible),
            'energy_load_MWh_y': exported(multiply(feed, quantity(p['energy_intensity']))),
            'gate_state': state, 'module_receipts_passed': sum(
                v['status'] == 'PASS' for v in r['module_receipts'].values()),
            'module_receipts_required': 8, 'ecological_or_residual_veto': veto,
            'realized_credit_t_y': 0})
    gated = [x['evidence_gated_product_t_y'] for x in results]
    total = None if any(x is None for x in gated) else (
        sum(x['low'] for x in gated), sum(x['high'] for x in gated))
    d = case['demand']
    req, supply, reserve = (quantity(d[k]) for k in
                           ('requirement', 'secure_domestic_supply', 'reserve_stock'))
    target = None
    if all(v is not None for v in (req, supply, reserve)):
        years = d['reserve_build_years']
        target = (max(0, req[0] + reserve[0] / years - supply[1]),
                  max(0, req[1] + reserve[1] / years - supply[0]))
    remaining = None if total is None or target is None else (
        max(0, target[0] - total[1]), max(0, target[1] - total[0]))
    return {'schema_version': '0.1', 'scenario_id': case['scenario_id'],
        'classification': 'SIMULATED_NON_CANON', 'input_sha256': input_sha256,
        'resource_basis': case['resource_basis'], 'demand_basis': d['basis'],
        'routes': results, 'evidence_gated_total_t_y': exported(total),
        'gap_plus_reserve_build_t_y': exported(target),
        'remaining_gap_t_y': exported(remaining), 'realized_credit_t_y': 0,
        'missing_inputs_and_receipts': sorted(missing),
        'limitations': ['Endpoint envelopes are bounds, not probabilities or forecasts.',
          'Source labels and PASS records are supplied assertions; engine does not authenticate them.',
          'Declared conservation ceiling requires independent chemistry review.',
          'No network optimizer, seasonal dynamics, LCA, net-energy, capex or operating economics.',
          'Energy is a gross load; reagents/coproducts/land/water remain receipt requirements.',
          'A stress-proxy target is not a verified domestic shortage.',
          'Secure domestic supply must exclude the modeled incremental streams.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scenario', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        case, sha = read_case(args.scenario)
        result = simulate(case, sha)
        rendered = json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + '\n'
        if args.output:
            args.output.write_text(rendered)
        else:
            print(rendered, end='')
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(2, f'Invalid scenario: {exc}\n')


if __name__ == '__main__':
    main()
