from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoDeviceResourceIdentifier(SdkBaseModel):
    """Device identifiers, one or more are required"""

    deveui: Optional[str] = UNSET
    """the IEEE EUI64 address space used to identify a device. It is supplied by the device manufacturer"""

    deviceid: Optional[str] = UNSET
    """This is a UUID value of the device created when the device is onboarded"""

    esn: Optional[int] = UNSET
    """The Electronic Serial Number (ESN) of the device"""

    iccid: Optional[str] = UNSET
    """The 20-digit Integrated Circuit Card ID (SIM card ID)"""

    imei: Optional[int] = UNSET
    """The 15-digit International Mobile Equipment ID"""

    imsi: Optional[int] = UNSET
    """The 64-bit International Mobile Subscriber Identity"""

    mac: Optional[str] = UNSET
    """The Media Access Control address of the device, listed on the device in the format XX-XX-XX-XX-XX-XX or
    XX:XX:XX:XX:XX:XX"""

    manufacturer: Optional[str] = UNSET
    """The manufacturer of the device"""

    meid: Optional[str] = UNSET
    """The 56-bit Mobile Equipment ID"""

    msisdn: Optional[str] = UNSET
    """The Mobile Station International Subscriber Directory Number. In the USA, this is 1+ a 10-digit phone number"""

    node_uuid: Optional[str] = UNSET
    """The UUID of the node the device is associated with"""

    qrcode: Optional[str] = UNSET
    """The numeric value of the Quick Response (QR) code"""

    serial: Optional[str] = UNSET
    """The device's serial number"""


class DtoDeviceResourceIdentifierDict(TypedDict):
    deveui: NotRequired[str]
    deviceid: NotRequired[str]
    esn: NotRequired[int]
    iccid: NotRequired[str]
    imei: NotRequired[int]
    imsi: NotRequired[int]
    mac: NotRequired[str]
    manufacturer: NotRequired[str]
    meid: NotRequired[str]
    msisdn: NotRequired[str]
    node_uuid: NotRequired[str]
    qrcode: NotRequired[str]
    serial: NotRequired[str]
