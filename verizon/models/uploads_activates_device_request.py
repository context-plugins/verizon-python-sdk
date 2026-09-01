from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class UploadsActivatesDeviceRequest(SdkBaseModel):
    """The request body identifies the devices to upload."""

    account_name: str = Field(alias="accountName")
    """The name of a billing account. An account name is usually numeric, and must include any leading zeros."""

    email_address: str = Field(alias="emailAddress")
    """The email address that the report should be sent to when the upload is complete."""

    device_sku: str = Field(alias="deviceSku")
    """The stock keeping unit that identifies the type of devices in the upload and activation."""

    upload_type: str = Field(alias="uploadType")
    """The format of the device identifiers in the upload and activation."""

    service_plan: str = Field(alias="servicePlan")
    """The service plan code that you want to assign to all specified devices."""

    carrier_ip_pool_name: Optional[str] = Field(default=UNSET, alias="carrierIpPoolName")
    """The pool from which your device IP addresses is derived."""

    mdn_zip_code: str = Field(alias="mdnZipCode")
    """The Zip code of the location where the line of service is primarily used, or a Zip code that you have been told
    to use with these devices."""

    devices: list[DeviceList]
    """The devices to upload, specified by device IDs in a format matching uploadType."""


class UploadsActivatesDeviceRequestDict(TypedDict):
    account_name: str
    email_address: str
    device_sku: str
    upload_type: str
    service_plan: str
    carrier_ip_pool_name: NotRequired[str]
    mdn_zip_code: str
    devices: list[DeviceList | DeviceListDict]
