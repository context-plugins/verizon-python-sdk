
# Rateplan

## Structure

`Rateplan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rate_plan_group` | List[[rateplantypeObject](../../doc/models/rateplantype-object.md) \| [rateplantype2](../../doc/models/rateplantype-2.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example

```python
from verizon.models.rateplan import Rateplan
from verizon.models.rateplantype_2 import Rateplantype2
from verizon.models.rateplantype_object import RateplantypeObject

rateplan = Rateplan(
    rate_plan_group=[
        RateplantypeObject(
            rate_plan_group_description='ratePlanGroupDescription4',
            rate_plan_type='ratePlanType2',
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
        ),
        RateplantypeObject(
            rate_plan_group_description='ratePlanGroupDescription4',
            rate_plan_type='ratePlanType2',
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
        ),
        RateplantypeObject(
            rate_plan_group_description='ratePlanGroupDescription4',
            rate_plan_type='ratePlanType2',
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
    ]
)
```

