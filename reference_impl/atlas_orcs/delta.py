from dataclasses import dataclass
from typing import Optional

from .state import TrustState


@dataclass
class TransitionDelta:
    target_state: TrustState
    ratification_event_id: Optional[str] = None
    governance_event_id: Optional[str] = None
    new_canon_status: Optional[str] = None
    new_deployment_status: Optional[str] = None
    contradiction_note: Optional[str] = None
