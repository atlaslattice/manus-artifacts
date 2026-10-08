"""Evidence-class primitives shared by every Node-001 model and validator.

Keeper rule: UNKNOWN is a first-class value. It propagates loudly and never
silently becomes a number, a zero, or an assumption.

This module deliberately makes UNKNOWN arithmetic raise. Any model that tries
to compute through an unestablished value fails at the point of the error
instead of producing a plausible-looking number downstream.
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Any, Iterable


class EvidenceClass(str, Enum):
    """Closed evidence vocabulary.

    Declaration order is NOT a strength ranking. `MEASURED` is the only class
    that can establish a current physical state at Node-001.
    """

    MEASURED = "MEASURED"        # primary instrumented data at Node-001
    REPORTED = "REPORTED"        # published/reported value with a source record
    DERIVED = "DERIVED"          # arithmetic over cited inputs
    HISTORICAL = "HISTORICAL"    # dated past state; never a current state
    PLANNED = "PLANNED"          # future intent; never an operating state
    MODELED = "MODELED"          # site-layout or design assumption
    SENSITIVITY = "SENSITIVITY"  # parametric transfer function; carries no credit
    PROPOSED = "PROPOSED"        # architecture proposal; carries no credit
    REFERENCE = "REFERENCE"      # external benchmark, not a node receipt
    UNKNOWN = "UNKNOWN"          # not established; must remain unknown


#: Classes that may never carry a primary accounting credit on their own.
NON_CREDITING_CLASSES: frozenset[EvidenceClass] = frozenset(
    {
        EvidenceClass.SENSITIVITY,
        EvidenceClass.PROPOSED,
        EvidenceClass.PLANNED,
        EvidenceClass.MODELED,
        EvidenceClass.REFERENCE,
        EvidenceClass.UNKNOWN,
    }
)

#: Classes that may not populate a *current operating* state.
NON_CURRENT_CLASSES: frozenset[EvidenceClass] = frozenset(
    {
        EvidenceClass.HISTORICAL,
        EvidenceClass.PLANNED,
        EvidenceClass.PROPOSED,
        EvidenceClass.SENSITIVITY,
    }
)


class UnknownPropagationError(ArithmeticError):
    """Raised when UNKNOWN is used where a number is required."""


class UnknownValue:
    """Singleton sentinel for an unestablished value.

    Every numeric protocol raises :class:`UnknownPropagationError`. There is no
    coercion path to ``0``, ``0.0``, ``False``, or ``nan``.
    """

    __slots__ = ()
    _instance: "UnknownValue | None" = None

    def __new__(cls) -> "UnknownValue":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # -- representation -------------------------------------------------
    def __repr__(self) -> str:
        return "UNKNOWN"

    def __str__(self) -> str:
        return "UNKNOWN"

    def __hash__(self) -> int:
        return hash("UNKNOWN")

    # -- refusal helpers ------------------------------------------------
    def _fail(self, op: str) -> Any:
        raise UnknownPropagationError(
            f"UNKNOWN used in numeric operation {op!r}: an unestablished value "
            "cannot be computed with. Source a receipt or keep the result UNKNOWN."
        )

    # -- arithmetic -----------------------------------------------------
    def __add__(self, other: Any) -> Any: return self._fail("+")
    def __radd__(self, other: Any) -> Any: return self._fail("+")
    def __sub__(self, other: Any) -> Any: return self._fail("-")
    def __rsub__(self, other: Any) -> Any: return self._fail("-")
    def __mul__(self, other: Any) -> Any: return self._fail("*")
    def __rmul__(self, other: Any) -> Any: return self._fail("*")
    def __truediv__(self, other: Any) -> Any: return self._fail("/")
    def __rtruediv__(self, other: Any) -> Any: return self._fail("/")
    def __floordiv__(self, other: Any) -> Any: return self._fail("//")
    def __rfloordiv__(self, other: Any) -> Any: return self._fail("//")
    def __mod__(self, other: Any) -> Any: return self._fail("%")
    def __rmod__(self, other: Any) -> Any: return self._fail("%")
    def __pow__(self, other: Any) -> Any: return self._fail("**")
    def __rpow__(self, other: Any) -> Any: return self._fail("**")
    def __neg__(self) -> Any: return self._fail("neg")
    def __pos__(self) -> Any: return self._fail("pos")
    def __abs__(self) -> Any: return self._fail("abs")

    # -- comparisons ----------------------------------------------------
    def __lt__(self, other: Any) -> Any: return self._fail("<")
    def __le__(self, other: Any) -> Any: return self._fail("<=")
    def __gt__(self, other: Any) -> Any: return self._fail(">")
    def __ge__(self, other: Any) -> Any: return self._fail(">=")

    # -- conversions ----------------------------------------------------
    def __bool__(self) -> Any: return self._fail("bool()")
    def __float__(self) -> Any: return self._fail("float()")
    def __int__(self) -> Any: return self._fail("int()")
    def __index__(self) -> Any: return self._fail("index()")
    def __round__(self, ndigits: int | None = None) -> Any: return self._fail("round()")
    def __format__(self, spec: str) -> Any: return self._fail("format()")


#: The single UNKNOWN sentinel.
UNKNOWN = UnknownValue()


def is_unknown(value: Any) -> bool:
    """True when ``value`` is the UNKNOWN sentinel (or the string "UNKNOWN")."""
    return value is UNKNOWN or (isinstance(value, str) and value == "UNKNOWN")


def as_value(value: Any) -> Any:
    """Normalize a JSON-loaded value: the string "UNKNOWN" becomes the sentinel."""
    if isinstance(value, str) and value == "UNKNOWN":
        return UNKNOWN
    return value


def require_number(value: Any, label: str) -> float:
    """Return ``value`` as a float or raise if it is UNKNOWN/non-numeric."""
    if is_unknown(value):
        raise UnknownPropagationError(
            f"{label} is UNKNOWN; refusing to compute. Source a receipt first."
        )
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{label} must be a real number, got {type(value).__name__}")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{label} must be finite, got {value}")
    return float(value)


def guard_fraction(value: Any, label: str, *, low: float = 0.0, high: float = 1.0) -> float:
    """Validate that ``value`` is a real fraction in [low, high]."""
    x = require_number(value, label)
    if not low <= x <= high:
        raise ValueError(f"{label} must lie in [{low}, {high}], got {x}")
    return x


def to_jsonable(obj: Any) -> Any:
    """Recursively convert UNKNOWN sentinels to the JSON string "UNKNOWN"."""
    if obj is UNKNOWN:
        return "UNKNOWN"
    if isinstance(obj, dict):
        return {k: to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(v) for v in obj]
    if isinstance(obj, EvidenceClass):
        return obj.value
    return obj


def fmt(value: Any, nd: int = 6) -> str:
    """Format a value for human-readable reports; UNKNOWN stays UNKNOWN."""
    if is_unknown(value):
        return "UNKNOWN"
    if isinstance(value, float):
        return f"{value:,.{nd}f}"
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)


def rel_diff(a: float, b: float) -> float:
    """Relative difference with a safe denominator for zero-valued references."""
    denom = max(abs(a), abs(b), 1e-12)
    return abs(a - b) / denom


def flatten(obj: Any, prefix: str = "") -> Iterable[tuple[str, Any]]:
    """Yield ``(dotted.path, value)`` pairs for nested dicts/lists."""
    if isinstance(obj, dict):
        for key, val in obj.items():
            yield from flatten(val, f"{prefix}.{key}" if prefix else str(key))
    elif isinstance(obj, list):
        for idx, val in enumerate(obj):
            yield from flatten(val, f"{prefix}[{idx}]")
    else:
        yield prefix, obj


def resolve_path(obj: Any, path: str) -> Any:
    """Resolve a dotted path with ``[i]`` list indices against ``obj``."""
    cur = obj
    token = ""
    i = 0
    parts: list[str] = []
    while i < len(path):
        ch = path[i]
        if ch == ".":
            if token:
                parts.append(token)
                token = ""
        elif ch == "[":
            if token:
                parts.append(token)
                token = ""
            j = path.index("]", i)
            raw = path[i + 1 : j].strip()
            if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
                raw = raw[1:-1]
            parts.append(raw)
            i = j
        else:
            token += ch
        i += 1
    if token:
        parts.append(token)
    for part in parts:
        if isinstance(cur, list):
            cur = cur[int(part)]
        elif isinstance(cur, dict):
            if part not in cur:
                raise KeyError(f"path {path!r} not found (missing {part!r})")
            cur = cur[part]
        else:
            raise KeyError(f"path {path!r} descends into a scalar at {part!r}")
    return cur
