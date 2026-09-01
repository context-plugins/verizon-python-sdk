from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .provisioning_history import ProvisioningHistory, ProvisioningHistoryDict


class DeviceProvisioningHistoryListResult(SdkBaseModel):
    """Response to return the provisioning history of a specified device during a specified time period."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """False for a status 200 response.True for a status 202 response, indicating that there is more data to be
    retrieved."""

    provisioning_history: Optional[list[ProvisioningHistory]] = Field(default=UNSET, alias="provisioningHistory")
    """The provisioning history of a specified device during a specified time period."""


class DeviceProvisioningHistoryListResultDict(TypedDict):
    has_more_data: NotRequired[bool]
    provisioning_history: NotRequired[list[ProvisioningHistory | ProvisioningHistoryDict]]
