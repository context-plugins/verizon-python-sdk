
# Delete Devices Result

Response for a request made to delete a device.

## Structure

`DeleteDevicesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | List[[DeviceId](../../doc/models/device-id.md)] \| [DeviceId](../../doc/models/device-id.md) \| None | Optional | This is a container for one-of cases. |
| `status` | `str` | Optional | “Success” if the device was deleted, or “Failed” if there was a problem. |
| `message` | `str` | Optional | Not present if status=Success. One of these messages if status=Failed:The device is not in deactivate state.The user does not have access to delete the device. |

## Example

```python
from verizon.models.delete_devices_result import DeleteDevicesResult
from verizon.models.device_id import DeviceId

delete_devices_result = DeleteDevicesResult(
    device_ids=[
        DeviceId(
            id='09005470263',
            kind='esn'
        )
    ],
    status='Success',
    message='message4'
)
```

