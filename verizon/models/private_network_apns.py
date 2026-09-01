from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PrivateNetworkApns(SdkBaseModel):
    apn_name: OptionalNullable[str] = Field(default=UNSET, alias="apnName")
    """the Access Point Name"""

    address_assignment_method: OptionalNullable[str] = Field(default=UNSET, alias="addressAssignmentMethod")
    """The method used for address assignment."""

    ip_address: OptionalNullable[str] = Field(default=UNSET, alias="ipAddress")
    """A IPv4 address"""


class PrivateNetworkApnsDict(TypedDict):
    apn_name: NotRequired[str | None]
    address_assignment_method: NotRequired[str | None]
    ip_address: NotRequired[str | None]
