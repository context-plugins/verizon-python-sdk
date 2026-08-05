
# Service Plan Responseforplanner

## Structure

`ServicePlanResponseforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_service_plan_code` | `str` | Optional | The name of the service plan code |
| `code` | `str` | Optional | The actiavtion code value. |
| `extended_attributes` | [`List[KvPairforplanner]`](../../doc/models/kv-pairforplanner.md) | Optional | key/value pairs assigned by the user for filtering.<br><br>**Constraints**: *Maximum Items*: `5` |
| `name` | `str` | Optional | The carrier name of the active profile. |
| `size_kb` | `int` | Optional | size in Kilobytes of the service plan |

## Example

```python
from verizon.models.kv_pairforplanner import KvPairforplanner
from verizon.models.service_plan_responseforplanner import ServicePlanResponseforplanner

service_plan_responseforplanner = ServicePlanResponseforplanner(
    carrier_service_plan_code='carrierServicePlanCode2',
    code='code2',
    extended_attributes=[
        KvPairforplanner(
            key='key8',
            value='value0'
        ),
        KvPairforplanner(
            key='key8',
            value='value0'
        ),
        KvPairforplanner(
            key='key8',
            value='value0'
        )
    ],
    name='name4',
    size_kb=194
)
```

