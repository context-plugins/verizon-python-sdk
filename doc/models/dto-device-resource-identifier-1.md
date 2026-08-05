
# Dto Device Resource Identifier 1

Device identifiers, one or more are required

## Structure

`DtoDeviceResourceIdentifier1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deveui` | `str` | Optional | the IEEE EUI64 address space used to identify a device. It is supplied by the device manufacturer |
| `deviceid` | `str` | Optional | This is a UUID value of the device created when the device is onboarded |
| `esn` | `int` | Optional | The Electronic Serial Number (ESN) of the device |
| `iccid` | `str` | Optional | The 20-digit Integrated Circuit Card ID (SIM card ID) |
| `imei` | `int` | Optional | The 15-digit International Mobile Equipment ID |
| `imsi` | `int` | Optional | The 64-bit International Mobile Subscriber Identity |
| `mac` | `str` | Optional | The Media Access Control address of the device, listed on the device in the format XX-XX-XX-XX-XX-XX or XX:XX:XX:XX:XX:XX |
| `manufacturer` | `str` | Optional | The manufacturer of the device |
| `meid` | `str` | Optional | The 56-bit Mobile Equipment ID |
| `msisdn` | `str` | Optional | The Mobile Station International Subscriber Directory Number. In the USA, this is 1+ a 10-digit phone number |
| `node_uuid` | `str` | Optional | The UUID of the node the device is associated with |
| `qrcode` | `str` | Optional | The numeric value of the Quick Response (QR) code |
| `serial` | `str` | Optional | The device's serial number |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |

## Example

```python
from verizon.models.dto_device_resource_identifier_1 import DtoDeviceResourceIdentifier1

dto_device_resource_identifier_1 = DtoDeviceResourceIdentifier1(
    deveui='The unique EUI64 address of the device',
    deviceid='The UUID of the device',
    esn=160,
    iccid='The 20-digit ICCID',
    imei=184,
    mac='The Media Access Control (MAC) address',
    manufacturer='REOLINK',
    meid='The 56-bit Mobile Equipment ID',
    msisdn='The Mobile Station International Subscriber Directory Number',
    node_uuid='The UUID of the node',
    qrcode='The Quick Response (QR) code',
    serial='The device\'s serial number'
)
```

