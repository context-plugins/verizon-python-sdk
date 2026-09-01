from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_update_smartalert import BulkUpdateSmartalert, BulkUpdateSmartalertDict
from .the_idresourceand_device_id import TheIdresourceandDeviceId, TheIdresourceandDeviceIdDict


class DtoBulkUpdate(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    resourceidentifiers: Optional[list[TheIdresourceandDeviceId]] = UNSET
    smartalert: Optional[BulkUpdateSmartalert] = UNSET


class DtoBulkUpdateDict(TypedDict):
    accountname: NotRequired[str]
    resourceidentifiers: NotRequired[list[TheIdresourceandDeviceId | TheIdresourceandDeviceIdDict]]
    smartalert: NotRequired[BulkUpdateSmartalert | BulkUpdateSmartalertDict]
