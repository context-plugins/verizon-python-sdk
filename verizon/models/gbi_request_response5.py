from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GbiRequestResponse5(SdkBaseModel):
    request_id: Optional[str] = Field(default=UNSET, alias="requestId")


class GbiRequestResponse5Dict(TypedDict):
    request_id: NotRequired[str]
