
# Device Group Devices Data

Returns the name, description, and list of devices in a device group.

## Structure

`DeviceGroupDevicesData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the device group. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | The devices in the device group. |
| `has_more_data` | `bool` | Optional | False for a status 200 response.True for a status 202 response, indicating that there is more data to be retrieved. |
| `name` | `str` | Optional | The name of the device group. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.device_group_devices_data import DeviceGroupDevicesData
from verizon.models.device_id import DeviceId

device_group_devices_data = DeviceGroupDevicesData(
    description='All service trucks in Nebraska.',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='12345',
                    kind='meid'
                ),
                DeviceId(
                    id='54321',
                    kind='mdn'
                )
            ],
            ipaddress='ipAddress4'
        )
    ],
    has_more_data=False,
    name='Nebraska Trucks'
)
```

