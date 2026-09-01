from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FindDeviceByPropertyResponse(SdkBaseModel):
    """Change Configuration resource definition."""

    billingaccountid: Optional[str] = UNSET
    """Billing account ID of the resource."""

    createdon: Optional[str] = UNSET
    """The date the resource was created."""

    eventretention: Optional[str] = UNSET
    iccid: Optional[str] = UNSET
    """Cellular SIM card identifier."""

    id: Optional[str] = UNSET
    """ThingSpace unique ID for the device that was added."""

    imei: Optional[str] = UNSET
    """4G hardware device identifier."""

    kind: Optional[str] = UNSET
    """Identifies the resource kind."""

    lastupdated: Optional[str] = UNSET
    """The date the resource was last updated."""

    providerid: Optional[str] = UNSET
    """The device’s service provider."""

    refid: Optional[str] = UNSET
    """The value of the refidtype identifier."""

    refidtype: Optional[str] = UNSET
    """The device identifier type used to refer to this device."""

    state: Optional[str] = UNSET
    """Service state of the device."""

    version: Optional[str] = UNSET
    """Version of the underlying schema resource."""

    versionid: Optional[str] = UNSET
    """The version of the resource."""


class FindDeviceByPropertyResponseDict(TypedDict):
    billingaccountid: NotRequired[str]
    createdon: NotRequired[str]
    eventretention: NotRequired[str]
    iccid: NotRequired[str]
    id: NotRequired[str]
    imei: NotRequired[str]
    kind: NotRequired[str]
    lastupdated: NotRequired[str]
    providerid: NotRequired[str]
    refid: NotRequired[str]
    refidtype: NotRequired[str]
    state: NotRequired[str]
    version: NotRequired[str]
    versionid: NotRequired[str]
