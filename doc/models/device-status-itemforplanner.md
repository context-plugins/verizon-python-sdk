
# Device Status Itemforplanner

## Structure

`DeviceStatusItemforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceIdforplanner]`](../../doc/models/device-idforplanner.md) | Optional | - |
| `status` | `str` | Optional | - |
| `reason` | `str` | Optional | - |

## Example

```python
from verizon.models.device_idforplanner import DeviceIdforplanner
from verizon.models.device_status_itemforplanner import DeviceStatusItemforplanner

device_status_itemforplanner = DeviceStatusItemforplanner(
    device_ids=[
        DeviceIdforplanner(
            kind='kind8',
            id='id0'
        )
    ],
    status='status8',
    reason='reason8'
)
```

