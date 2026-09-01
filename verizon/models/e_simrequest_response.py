from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ESimrequestResponse(SdkBaseModel):
    request_id: Optional[str] = Field(default=UNSET, alias="requestId")


class ESimrequestResponseDict(TypedDict):
    request_id: NotRequired[str]
