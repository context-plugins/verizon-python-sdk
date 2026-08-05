
# License Device List

List of all devices.

## Structure

`LicenseDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[LicenseDeviceId]`](../../doc/models/license-device-id.md) | Optional | For 4G devices, IMEI (decimal, up to 15 digits).<br><br>**Constraints**: *Maximum Items*: `100` |
| `ipaddress` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9].[0-9].[0-9].[0-9]{3,32}$` |

## Example

```python
from verizon.models.license_device_id import LicenseDeviceId
from verizon.models.license_device_list import LicenseDeviceList

license_device_list = LicenseDeviceList(
    device_ids=[
        LicenseDeviceId(
            id='864508030109877',
            kind='IMEI'
        )
    ],
    ipaddress='ipAddress2'
)
```

