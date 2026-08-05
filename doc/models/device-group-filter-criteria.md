
# Device Group Filter Criteria

## Structure

`DeviceGroupFilterCriteria`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`DeviceGroupFilter`](../../doc/models/device-group-filter.md) | Optional | - |

## Example

```python
from verizon.models.device_group_filter import DeviceGroupFilter
from verizon.models.device_group_filter_criteria import DeviceGroupFilterCriteria

device_group_filter_criteria = DeviceGroupFilterCriteria(
    filter_criteria=DeviceGroupFilter(
        device_group_name='deviceGroupName4',
        individual_or_combined='IndividualOrCombined4',
        account_name='accountName0'
    )
)
```

