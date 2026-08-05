
# Device List 2

## Structure

`DeviceList2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | List[[eSIMDeviceId](../../doc/models/esim-device-id.md) \| [DeviceId2](../../doc/models/device-id-2.md)] \| None | Optional | This is List of a container for any-of cases.<br><br>**Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.device_list_2 import DeviceList2
from verizon.models.esim_device_id import ESIMDeviceId

device_list_2 = DeviceList2(
    ids=[
        ESIMDeviceId(
            id='id4',
            kind='kind2'
        ),
        ESIMDeviceId(
            id='id4',
            kind='kind2'
        )
    ]
)
```

