from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .management import Management, ManagementDict
from .situation import Situation, SituationDict


class DenmPayload(SdkBaseModel):
    """The payload of the DENM PDU."""

    management: Management
    """This represent the management container describing the meta information about the event, such as the detection
    time, the event's location, the source of the event, and the notification distance."""

    situation: Optional[Situation] = UNSET
    """This represents the situation container describing the event and the reliability of the detection source."""


class DenmPayloadDict(TypedDict):
    management: Management | ManagementDict
    situation: NotRequired[Situation | SituationDict]
