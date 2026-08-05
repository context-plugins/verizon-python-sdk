
# Service Plan

Details of the service plan.

## Structure

`ServicePlan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_service_plan_code` | `str` | Optional | The code that is used by the carrier for the service plan. |
| `code` | `str` | Optional | The code of the service plan, which may not be the same as the name. |
| `extended_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Any extended attributes for the service plan, as Key and Value pairs. |
| `name` | `str` | Optional | The name of the service plan. |
| `size_kb` | `int` | Optional | The size of the service plan in kilobytes. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.service_plan import ServicePlan

service_plan = ServicePlan(
    carrier_service_plan_code='84638',
    code='M2MSHR5GB',
    extended_attributes=[
        CustomFields(
            key='key8',
            value='value0'
        )
    ],
    name='2MSHR5GB',
    size_kb=0
)
```

