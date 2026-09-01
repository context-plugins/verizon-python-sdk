from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class ChangeDeviceIdRequest(SdkBaseModel):
    """Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this
    request to transfer the line of service and the MDN to new hardware, or to change the MDN."""

    assign_non_geo_mdn: Optional[bool] = Field(default=UNSET, alias="assignNonGeoMdn")
    """Set to true to assign a non-Geo MDN and MSISDN, or false to assign an MDN and MSISDN from a specific NPA-NXX."""

    change4g_option: Optional[str] = Field(default=UNSET, alias="change4gOption")
    """The type of change that you want to make for a 4G device."""

    device_ids: list[DeviceId] = Field(alias="deviceIds")
    """The device that you want to change, specified by a device identifier."""

    device_ids_to: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIdsTo")
    """The new identifier for the device. Required for all change4GOptions except ChangeMSISDN."""

    npa_nxx: Optional[str] = Field(default=UNSET, alias="npaNxx")
    """The NPA NXX (area code and prefix) from which the MDN and MSISDN will be derived when assignNonGeoMDN is false.
    Specify the 6-digit NPA NXX of the location where the line of service will primarily be used. This API checks to see
    if a number starting with the NPA NXX is available. If not, this API uses the zipCode parameter, if specified, to
    assign a number in the area of the line of service. This parameter is required when you change an MDN/MSISDN for a
    B2B carrier, such as Verizon Wireless."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The code for a different service plan, if you want to change the service plan while changing the device
    identifier. Set this parameter to one of the Code values returned by GET /plans."""

    zip_code: Optional[str] = Field(default=UNSET, alias="zipCode")
    """The ZIP code from which the MDN and MSISDN will be derived when assignNonGeoMDN is true. Specify the zip code of
    the location where the line of service will primarily be used."""

    smsr_oid: Optional[str] = Field(default=UNSET, alias="smsrOid")


class ChangeDeviceIdRequestDict(TypedDict):
    assign_non_geo_mdn: NotRequired[bool]
    change4g_option: NotRequired[str]
    device_ids: list[DeviceId | DeviceIdDict]
    device_ids_to: NotRequired[list[DeviceId | DeviceIdDict]]
    npa_nxx: NotRequired[str]
    service_plan: NotRequired[str]
    zip_code: NotRequired[str]
    smsr_oid: NotRequired[str]
