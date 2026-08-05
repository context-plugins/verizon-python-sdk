
# Device List

## Structure

`DeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList

device_list = DeviceList(
    device_ids=[
        DeviceId(
            id='id0',
            kind='kind8'
        )
    ]
)
```

