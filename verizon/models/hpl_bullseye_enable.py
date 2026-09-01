from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HplBullseyeEnable(SdkBaseModel):
    """A flag that shows if Hyper Precise is enabled (true) or disabled (false)."""

    bullseye_enable: Optional[bool] = Field(default=UNSET, alias="BullseyeEnable")


class HplBullseyeEnableDict(TypedDict):
    bullseye_enable: NotRequired[bool]
