from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Ippoolforplanner(SdkBaseModel):
    is_default_pool: Optional[bool] = Field(default=UNSET, alias="isDefaultPool")
    pool_name: Optional[str] = Field(default=UNSET, alias="poolName")
    pool_type: Optional[str] = Field(default=UNSET, alias="poolType")


class IppoolforplannerDict(TypedDict):
    is_default_pool: NotRequired[bool]
    pool_name: NotRequired[str]
    pool_type: NotRequired[str]
