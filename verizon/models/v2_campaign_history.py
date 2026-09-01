from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v2_campaign_meta_info import V2CampaignMetaInfo, V2CampaignMetaInfoDict


class V2CampaignHistory(SdkBaseModel):
    """Campaign history details."""

    has_more_data: bool = Field(alias="hasMoreData")
    """Has more report flag."""

    last_seen_campaign_id: Optional[str] = Field(default=UNSET, alias="lastSeenCampaignId")
    """Campaign identifier."""

    campaign_list: list[V2CampaignMetaInfo | None] = Field(alias="campaignList")
    """Software upgrade list."""


class V2CampaignHistoryDict(TypedDict):
    has_more_data: bool
    last_seen_campaign_id: NotRequired[str]
    campaign_list: list[V2CampaignMetaInfo | V2CampaignMetaInfoDict | None]
