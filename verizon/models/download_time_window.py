from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DownloadTimeWindow(SdkBaseModel):
    start_time: Optional[str] = Field(default=UNSET, alias="startTime")
    """Device IMEI list."""

    end_time: Optional[str] = Field(default=UNSET, alias="endTime")
    """Device IMEI list."""


class DownloadTimeWindowDict(TypedDict):
    start_time: NotRequired[str]
    end_time: NotRequired[str]
