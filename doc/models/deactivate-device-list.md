
# Deactivate Device List

## Structure

`DeactivateDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | List[[DeviceId](../../doc/models/device-id.md) \| [PropertyDeviceId](../../doc/models/property-device-id.md)] \| None | Optional | This is List of a container for any-of cases.<br><br>**Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.deactivate_device_list import DeactivateDeviceList
from verizon.models.device_id import DeviceId

deactivate_device_list = DeactivateDeviceList(
    ids=[
        DeviceId(
            id='id2',
            kind='kind0'
        ),
        DeviceId(
            id='id2',
            kind='kind0'
        ),
        DeviceId(
            id='id2',
            kind='kind0'
        )
    ]
)
```

