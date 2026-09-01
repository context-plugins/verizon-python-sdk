from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.cause_code_choice import CauseCodeChoice, CauseCodeChoiceDict


class EventType(SdkBaseModel):
    """The type of event including direct and sub cause."""

    cc_and_scc: Optional[CauseCodeChoice] = Field(default=UNSET, alias="ccAndScc")
    """The main cause of a detected event. Each entry is of a different type and represents the sub cause code."""


class EventTypeDict(TypedDict):
    cc_and_scc: NotRequired[CauseCodeChoice | CauseCodeChoiceDict]
