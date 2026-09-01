from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subrequest import Subrequest, SubrequestDict


class StatusResponse(SdkBaseModel):
    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    status: Optional[str] = UNSET
    subrequests: Optional[list[Subrequest]] = UNSET


class StatusResponseDict(TypedDict):
    request_id: NotRequired[str]
    status: NotRequired[str]
    subrequests: NotRequired[list[Subrequest | SubrequestDict]]
