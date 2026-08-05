
# Account Device List

A list of deviceId objects to use when requesting information from multiple devices.

## Structure

`AccountDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Required | All identifiers for the device. |
| `ipaddress` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9].[0-9].[0-9].[0-9]{3,32}$` |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.device_id import DeviceId

account_device_list = AccountDeviceList(
    device_ids=[
        DeviceId(
            id='990013907835573',
            kind='imei'
        ),
        DeviceId(
            id='89141390780800784259',
            kind='iccid'
        )
    ],
    ipaddress='ipAddress8'
)
```

