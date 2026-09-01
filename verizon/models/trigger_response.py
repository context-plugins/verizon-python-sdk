from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TriggerResponse(SdkBaseModel):
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    """The system assigned UUID of the trigger"""


class TriggerResponseDict(TypedDict):
    trigger_id: NotRequired[str]
