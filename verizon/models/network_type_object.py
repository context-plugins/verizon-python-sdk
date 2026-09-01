from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NetworkTypeObject(SdkBaseModel):
    """Network type."""

    network_type: Optional[str] = Field(default=UNSET, alias="networkType")


class NetworkTypeObjectDict(TypedDict):
    network_type: NotRequired[str]
