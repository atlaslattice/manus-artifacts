"""Unit tests for the evidence-class primitives.

The central claim under test: UNKNOWN is loud. It cannot become 0, False, nan,
or a plausible number by accident.
"""

from __future__ import annotations

import json

import pytest

from models.common import (
    NON_CREDITING_CLASSES,
    NON_CURRENT_CLASSES,
    UNKNOWN,
    EvidenceClass,
    UnknownPropagationError,
    as_value,
    flatten,
    guard_fraction,
    is_unknown,
    require_number,
    resolve_path,
    to_jsonable,
)


@pytest.mark.parametrize(
    "operation",
    [
        lambda: UNKNOWN + 1,
        lambda: 1 + UNKNOWN,
        lambda: UNKNOWN - 1,
        lambda: 1 - UNKNOWN,
        lambda: UNKNOWN * 2,
        lambda: 2 * UNKNOWN,
        lambda: UNKNOWN / 2,
        lambda: 2 / UNKNOWN,
        lambda: UNKNOWN**2,
        lambda: -UNKNOWN,
        lambda: abs(UNKNOWN),
        lambda: round(UNKNOWN, 2),
    ],
)
def test_unknown_arithmetic_raises(operation):
    with pytest.raises(UnknownPropagationError):
        operation()


@pytest.mark.parametrize(
    "operation",
    [
        lambda: bool(UNKNOWN),
        lambda: float(UNKNOWN),
        lambda: int(UNKNOWN),
        lambda: UNKNOWN < 1,
        lambda: UNKNOWN > 1,
    ],
)
def test_unknown_coercion_raises(operation):
    """There must be no coercion path from UNKNOWN to a scalar or a bool."""
    with pytest.raises(UnknownPropagationError):
        operation()


def test_unknown_is_a_singleton():
    from models.common import UnknownValue

    assert UnknownValue() is UNKNOWN
    assert UnknownValue() is UNKNOWN


def test_unknown_repr_and_hash_are_stable():
    assert repr(UNKNOWN) == "UNKNOWN"
    assert str(UNKNOWN) == "UNKNOWN"
    assert hash(UNKNOWN) == hash("UNKNOWN")


def test_is_unknown_accepts_the_json_sentinel():
    assert is_unknown(UNKNOWN)
    assert is_unknown("UNKNOWN")
    assert not is_unknown("MEASURED")
    assert not is_unknown(0)
    assert not is_unknown(0.0)
    assert not is_unknown(None)


def test_as_value_normalizes_the_json_string():
    assert as_value("UNKNOWN") is UNKNOWN
    assert as_value(3.5) == 3.5
    assert as_value("REPORTED") == "REPORTED"


def test_require_number_refuses_unknown():
    with pytest.raises(UnknownPropagationError):
        require_number(UNKNOWN, "tariff")


def test_require_number_rejects_bool_and_nan():
    with pytest.raises(TypeError):
        require_number(True, "flag")
    with pytest.raises(ValueError):
        require_number(float("nan"), "value")


def test_guard_fraction_bounds():
    assert guard_fraction(0.5, "f") == 0.5
    with pytest.raises(ValueError):
        guard_fraction(1.5, "f")
    with pytest.raises(ValueError):
        guard_fraction(-0.1, "f")


def test_to_jsonable_round_trips_unknown():
    payload = {"a": UNKNOWN, "b": [1, UNKNOWN], "c": {"d": UNKNOWN}}
    encoded = json.dumps(to_jsonable(payload))
    assert json.loads(encoded) == {"a": "UNKNOWN", "b": [1, "UNKNOWN"], "c": {"d": "UNKNOWN"}}


def test_resolve_path_handles_quoted_keys_with_dots():
    doc = {"mass_balance": {"0.45": {"feed_m3_day": 222222.22222222222}}}
    assert resolve_path(doc, 'mass_balance["0.45"].feed_m3_day') == 222222.22222222222


def test_resolve_path_handles_list_indices():
    doc = {"tiers": [{"case_id": "C01-PILOT-100"}, {"case_id": "C01-PILOT-250"}]}
    assert resolve_path(doc, "tiers[1].case_id") == "C01-PILOT-250"


def test_resolve_path_raises_on_missing_key():
    with pytest.raises(KeyError):
        resolve_path({"a": 1}, "b")


def test_flatten_walks_nested_structures():
    doc = {"a": {"b": [1, 2]}, "c": "x"}
    assert dict(flatten(doc)) == {"a.b[0]": 1, "a.b[1]": 2, "c": "x"}


def test_non_crediting_classes_are_closed():
    """The non-crediting set is exactly the classes that cannot stand alone."""
    assert EvidenceClass.UNKNOWN in NON_CREDITING_CLASSES
    assert EvidenceClass.SENSITIVITY in NON_CREDITING_CLASSES
    assert EvidenceClass.PROPOSED in NON_CREDITING_CLASSES
    assert EvidenceClass.MEASURED not in NON_CREDITING_CLASSES
    assert EvidenceClass.REPORTED not in NON_CREDITING_CLASSES
    assert EvidenceClass.DERIVED not in NON_CREDITING_CLASSES


def test_non_current_classes_exclude_measured():
    assert EvidenceClass.HISTORICAL in NON_CURRENT_CLASSES
    assert EvidenceClass.PLANNED in NON_CURRENT_CLASSES
    assert EvidenceClass.MEASURED not in NON_CURRENT_CLASSES
