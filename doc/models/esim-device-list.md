
# ESIM Device List

## Structure

`ESIMDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | List[[eSIMDeviceId](../../doc/models/esim-device-id.md) \| [DeviceId2](../../doc/models/device-id-2.md)] \| None | Optional | This is List of a container for any-of cases.<br><br>**Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.esim_device_id import ESIMDeviceId
from verizon.models.esim_device_list import ESIMDeviceList

e_sim_device_list = ESIMDeviceList(
    device_ids=[
        ESIMDeviceId(
            id='id4',
            kind='kind2'
        ),
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

