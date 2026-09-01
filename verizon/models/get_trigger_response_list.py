from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_trigger_response import GetTriggerResponse, GetTriggerResponseDict


class GetTriggerResponseList(SdkBaseModel):
    triggers: Optional[list[GetTriggerResponse]] = UNSET


class GetTriggerResponseListDict(TypedDict):
    triggers: NotRequired[list[GetTriggerResponse | GetTriggerResponseDict]]
