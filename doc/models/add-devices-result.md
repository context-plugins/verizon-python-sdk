
# Add Devices Result

Contains the device identifiers and a success or failure response for each device in the request.

## Structure

`AddDevicesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Identifiers for the device. |
| `response` | `str` | Optional | The status message for the current device. This will be Success or Failed |

## Example

```python
from verizon.models.add_devices_result import AddDevicesResult
from verizon.models.device_id import DeviceId

add_devices_result = AddDevicesResult(
    device_ids=[
        DeviceId(
            id='20-digit ICCID',
            kind='iccid'
        )
    ],
    response='Success'
)
```

