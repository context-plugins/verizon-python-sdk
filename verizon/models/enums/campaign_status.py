from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CampaignStatus(str, Enum):
    """Current status of the campaign."""

    CAMPAIGN_REQUEST_PENDING = "CampaignRequestPending"
    CAMPAIGN_REQUEST_FAILED = "CampaignRequestFailed"
    CAMPAIGN_REQUEST_QUEUED = "CampaignRequestQueued"
    CAMPAIGN_CANCELLED = "CampaignCancelled"
    CAMPAIGN_ABORTED = "CampaignAborted"
    CAMPAIGN_FAILED = "CampaignFailed"
    CAMPAIGN_SCHEDULED = "CampaignScheduled"
    CAMPAIGN_ENDED = "CampaignEnded"

    __str__ = str.__str__


CampaignStatusOrStr: TypeAlias = Annotated[CampaignStatus | str, open_enum_validator(CampaignStatus)]
