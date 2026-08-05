
# Rateplantype Object

## Structure

`RateplantypeObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rate_plan_group_description` | `str` | Optional | - |
| `rate_plan_type` | `str` | Optional | - |
| `rate_plan` | [`List[Rateplantype2]`](../../doc/models/rateplantype-2.md) | Optional | An array of rateplan names |

## Example

```python
from verizon.models.rateplantype_2 import Rateplantype2
from verizon.models.rateplantype_object import RateplantypeObject

rateplantype_object = RateplantypeObject(
    rate_plan_group_description='AGS Description_73',
    rate_plan_type='ratePlanType4',
    rate_plan=[
        Rateplantype2(
            description='description2',
            size_kb='sizeKb2',
            carrier_rate_plan_code='carrierRatePlanCode8',
            zero_dollar_billing=False,
            promotion_offered=False
        ),
        Rateplantype2(
            description='description2',
            size_kb='sizeKb2',
            carrier_rate_plan_code='carrierRatePlanCode8',
            zero_dollar_billing=False,
            promotion_offered=False
        )
    ]
)
```

