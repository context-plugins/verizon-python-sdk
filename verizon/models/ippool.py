from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Ippool(SdkBaseModel):
    """IP pool that is available to the account."""

    pool_name: Optional[str] = Field(default=UNSET, alias="poolName")
    """The name of the IP pool."""

    pool_type: Optional[str] = Field(default=UNSET, alias="poolType")
    """The type of IP pool, such as “Static IP” or “Dynamic IP.”"""

    is_default_pool: Optional[bool] = Field(default=UNSET, alias="isDefaultPool")
    """True if this is the default IP pool for the account."""


class IppoolDict(TypedDict):
    pool_name: NotRequired[str]
    pool_type: NotRequired[str]
    is_default_pool: NotRequired[bool]
