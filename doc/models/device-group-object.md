
# Device Group Object

## Structure

`DeviceGroupObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_group` | [`DeviceGroupFilterCriteria`](../../doc/models/device-group-filter-criteria.md) | Optional | - |

## Example

```python
from verizon.models.device_group_filter import DeviceGroupFilter
from verizon.models.device_group_filter_criteria import DeviceGroupFilterCriteria
from verizon.models.device_group_object import DeviceGroupObject

device_group_object = DeviceGroupObject(
    device_group=DeviceGroupFilterCriteria(
        filter_criteria=DeviceGroupFilter(
            device_group_name='deviceGroupName4',
            individual_or_combined='IndividualOrCombined4',
            account_name='accountName0'
        )
    )
)
```

