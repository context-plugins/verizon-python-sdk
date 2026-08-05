
# Device Filter without Account

Filter for devices without account.

## Structure

`DeviceFilterWithoutAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_name` | `str` | Optional | Only include devices that are in this device group. |
| `service_plan` | `str` | Optional | Only include devices that have this service plan. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.device_filter_without_account import DeviceFilterWithoutAccount

device_filter_without_account = DeviceFilterWithoutAccount(
    group_name='suspended devices',
    service_plan='servicePlan8',
    custom_fields=[
        CustomFields(
            key='key0',
            value='value2'
        ),
        CustomFields(
            key='key0',
            value='value2'
        ),
        CustomFields(
            key='key0',
            value='value2'
        )
    ]
)
```

