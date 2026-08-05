
# GIO Device List

## Structure

`GIODeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[GIODeviceId]`](../../doc/models/gio-device-id.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.gio_device_id import GIODeviceId
from verizon.models.gio_device_list import GIODeviceList

gio_device_list = GIODeviceList(
    device_ids=[
        GIODeviceId(
            kind='kind8',
            id='id0'
        ),
        GIODeviceId(
            kind='kind8',
            id='id0'
        ),
        GIODeviceId(
            kind='kind8',
            id='id0'
        )
    ]
)
```

