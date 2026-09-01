from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .firmware_upgrade import FirmwareUpgrade, FirmwareUpgradeDict


class UpgradeListQueryResult(SdkBaseModel):
    """Upgrade information."""

    has_more_flag: Optional[bool] = Field(default=UNSET, alias="hasMoreFlag")
    """True if there are more devices to retrieve."""

    last_seen_upgrade_id: Optional[int] = Field(default=UNSET, alias="lastSeenUpgradeId")
    """If hasMoreData=true, the startIndex to use for the next request. 0 if hasMoreData=false."""

    report_list: Optional[list[FirmwareUpgrade | None]] = Field(default=UNSET, alias="reportList")
    """Array of upgrade objects with the specified status."""


class UpgradeListQueryResultDict(TypedDict):
    has_more_flag: NotRequired[bool]
    last_seen_upgrade_id: NotRequired[int]
    report_list: NotRequired[list[FirmwareUpgrade | FirmwareUpgradeDict | None]]
