from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V2AddOrRemoveDeviceResult(SdkBaseModel):
    """Add or remove devices from the existing software upgrade information."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    campaign_id: str = Field(alias="campaignId")
    """Campaign identifier."""

    request_id: str = Field(alias="requestId")
    """Request identifier."""


class V2AddOrRemoveDeviceResultDict(TypedDict):
    account_name: str
    campaign_id: str
    request_id: str
