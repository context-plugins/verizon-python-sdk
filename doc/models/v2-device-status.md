
# V2 Device Status

Device with id in IMEI.

## Structure

`V2DeviceStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `status` | `str` | Required | Success or failure. |
| `result_reason` | `str` | Optional | Result reason. |

## Example

```python
from verizon.models.v2_device_status import V2DeviceStatus

v2_device_status = V2DeviceStatus(
    device_id='990000473475967',
    status='Failure',
    result_reason='Device does not exist.'
)
```

