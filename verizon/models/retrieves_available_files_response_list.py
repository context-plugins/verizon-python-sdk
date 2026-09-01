from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .retrieves_available_files_response import RetrievesAvailableFilesResponse, RetrievesAvailableFilesResponseDict


class RetrievesAvailableFilesResponseList(SdkBaseModel):
    available_files_response: Optional[list[RetrievesAvailableFilesResponse]] = Field(
        default=UNSET, alias="AvailableFilesResponse"
    )


class RetrievesAvailableFilesResponseListDict(TypedDict):
    available_files_response: NotRequired[list[RetrievesAvailableFilesResponse | RetrievesAvailableFilesResponseDict]]
