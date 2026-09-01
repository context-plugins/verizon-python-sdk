from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v3_campaign_meta_info import V3CampaignMetaInfo, V3CampaignMetaInfoDict


class V3CampaignHistory(SdkBaseModel):
    """Campaign history."""

    has_more_data: bool = Field(alias="hasMoreData")
    """Has more report flag?"""

    last_seen_campaign_id: Optional[str] = Field(default=UNSET, alias="lastSeenCampaignId")
    """Campaign identifier."""

    campaign_list: list[V3CampaignMetaInfo | None] = Field(alias="campaignList")
    """Firmware upgrade list."""


class V3CampaignHistoryDict(TypedDict):
    has_more_data: bool
    last_seen_campaign_id: NotRequired[str]
    campaign_list: list[V3CampaignMetaInfo | V3CampaignMetaInfoDict | None]
