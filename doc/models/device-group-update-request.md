
# Device Group Update Request

Make changes to a device group, including changing the name and description, and adding or removing devices.

## Structure

`DeviceGroupUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices_to_add` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Zero or more devices to add to the device group, specified by device ID. The devices will be removed from their current device groups. You can use POST /devices/actions/list to get a list of all devices in the account. |
| `devices_to_remove` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Zero or more devices to remove from the device group, specified by device ID. The devices will be added to the default device group. |
| `new_group_description` | `str` | Optional | A new description for the device group. Do not include this parameter to leave the group description unchanged. |
| `new_group_name` | `str` | Optional | A new name for the device group. Do not include this parameter if you want to leave the group name unchanged. |

## Example

```python
from verizon.models.device_group_update_request import DeviceGroupUpdateRequest
from verizon.models.device_id import DeviceId

device_group_update_request = DeviceGroupUpdateRequest(
    devices_to_add=[
        DeviceId(
            id='990003420535537',
            kind='imei'
        )
    ],
    devices_to_remove=[
        DeviceId(
            id='id0',
            kind='kind8'
        ),
        DeviceId(
            id='id0',
            kind='kind8'
        )
    ],
    new_group_description='All western region tank level monitors.',
    new_group_name='Western region tanks'
)
```

