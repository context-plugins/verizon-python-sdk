from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CampaignMetaInfoProtocol(str, Enum):
    """Firmware protocol. Valid values include: LWM2M, OMD-DM."""

    LWM2_M = "LWM2M"
    OMD_DM = "OMD-DM"

    __str__ = str.__str__


CampaignMetaInfoProtocolOrStr: TypeAlias = Annotated[
    CampaignMetaInfoProtocol | str, open_enum_validator(CampaignMetaInfoProtocol)
]
