from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .dto_fields import DtoFields, DtoFieldsDict


class ResourceDevice(SdkBaseModel):
    accountclientid: Optional[str] = UNSET
    """Not used in this release, future functionality"""

    billingaccountid: Optional[str] = UNSET
    """The billing account ID. This is the same value as the Account ID"""

    chipset: Optional[str] = UNSET
    """The Identifier of chipset used by the device"""

    createdon: RFC3339DateTime
    """Timestamp of the record"""

    customdata: Optional[dict[str, Any]] = UNSET
    """Name/value pair, where the value is client defined. The purpose is to keep track of current state per device
    action."""

    description: Optional[str] = UNSET
    """a short description"""

    esn: Optional[int] = UNSET
    """The Electronic Serial Number (ESN) of the device"""

    fields: Optional[DtoFields] = UNSET
    """Fields to return needed by search"""

    foreignid: str
    """UUID of the ECPD account the user belongs to"""

    hardwareversion: Optional[str] = UNSET
    """The manufacturer's hardware version of the device"""

    iccid: Optional[str] = UNSET
    """The 20-digit Integrated Circuit Card ID (SIM card ID)"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    imei: Optional[int] = UNSET
    """The 15-digit International Mobile Equipment ID"""

    imsi: Optional[int] = UNSET
    """The 64-bit International Mobile Subscriber Identity"""

    lastupdated: RFC3339DateTime
    """Timestamp of the record"""

    licenses: Optional[list[str]] = UNSET
    """licenses assigned to the device"""

    mac: Optional[str] = UNSET
    """The Media Access Control address of the device, listed on the device in the format XX-XX-XX-XX-XX-XX or
    XX:XX:XX:XX:XX:XX"""

    manufacturer: Optional[str] = UNSET
    """The manufacturer of the device"""

    meid: Optional[str] = UNSET
    """The 56-bit Mobile Equipment ID"""

    msisdn: Optional[str] = UNSET
    """The Mobile Station International Subscriber Directory Number. In the USA, this is 1+ a 10-digit phone number"""

    name: Optional[str] = UNSET
    """User defined name of the record"""

    parentdeviceid: Optional[str] = UNSET
    """this field is applicable for BLE sensors. This represents the value of parent gateway device"""

    productmodel: Optional[str] = UNSET
    """The device model name"""

    providerid: Optional[str] = UNSET
    """The id of the provider who is responible for talking to the device"""

    qrcode: Optional[str] = UNSET
    """The numeric value of the Quick Response (QR) code"""

    refid: Optional[str] = UNSET
    """The device reference ID"""

    refidtype: Optional[str] = UNSET
    """The type of value represented by ``refid``"""

    serial: Optional[str] = UNSET
    """The device's serial number"""

    services: Optional[list[str]] = UNSET
    sku: Optional[str] = UNSET
    """The Stock Keeping Unit (SKU) number of the device"""

    softwareversion: Optional[str] = UNSET
    """the current device software version"""

    state: str
    """The current status of the device or transaction and will be ``success`` or ``failed``"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: str
    """The UUID of the resource version"""

    eventretention: Optional[int] = UNSET
    """Data retention period"""


class ResourceDeviceDict(TypedDict):
    accountclientid: NotRequired[str]
    billingaccountid: NotRequired[str]
    chipset: NotRequired[str]
    createdon: RFC3339DateTime
    customdata: NotRequired[dict[str, Any]]
    description: NotRequired[str]
    esn: NotRequired[int]
    fields: NotRequired[DtoFields | DtoFieldsDict]
    foreignid: str
    hardwareversion: NotRequired[str]
    iccid: NotRequired[str]
    id: NotRequired[str]
    imei: NotRequired[int]
    imsi: NotRequired[int]
    lastupdated: RFC3339DateTime
    licenses: NotRequired[list[str]]
    mac: NotRequired[str]
    manufacturer: NotRequired[str]
    meid: NotRequired[str]
    msisdn: NotRequired[str]
    name: NotRequired[str]
    parentdeviceid: NotRequired[str]
    productmodel: NotRequired[str]
    providerid: NotRequired[str]
    qrcode: NotRequired[str]
    refid: NotRequired[str]
    refidtype: NotRequired[str]
    serial: NotRequired[str]
    services: NotRequired[list[str]]
    sku: NotRequired[str]
    softwareversion: NotRequired[str]
    state: str
    version: NotRequired[str]
    versionid: str
    eventretention: NotRequired[int]
