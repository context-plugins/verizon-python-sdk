
# Device Group Filter

## Structure

`DeviceGroupFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_group_name` | `str` | Optional | - |
| `individual_or_combined` | `str` | Optional | - |
| `account_name` | `str` | Optional | The numeric name of the account and must include leading zeroes |

## Example

```python
from verizon.models.device_group_filter import DeviceGroupFilter

device_group_filter = DeviceGroupFilter(
    device_group_name='User defined group name',
    individual_or_combined='Combined',
    account_name='0000123456-00001'
)
```

