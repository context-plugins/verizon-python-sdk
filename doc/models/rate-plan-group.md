
# Rate Plan Group

## Structure

`RatePlanGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rate_plan_group_description` | `str` | Optional | - |
| `rate_plan_type` | `Any` | Optional | - |
| `rate_plan` | [`List[Rateplantype2]`](../../doc/models/rateplantype-2.md) | Optional | An array of rateplan names |
| `description` | `str` | Optional | - |
| `size_kb` | `str` | Optional | - |
| `carrier_rate_plan_code` | `str` | Optional | - |
| `zero_dollar_billing` | `bool` | Optional | - |
| `promotion_offered` | `bool` | Optional | - |
| `promotion_days` | `int` | Optional | - |
| `account` | [`List[Accountid]`](../../doc/models/accountid.md) | Optional | Account information |

## Example

```python
import jsonpickle

from verizon.models.rate_plan_group import RatePlanGroup
from verizon.models.rateplantype_2 import Rateplantype2

rate_plan_group = RatePlanGroup(
    rate_plan_group_description='AGS Description_73',
    rate_plan_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    rate_plan=[
        Rateplantype2(
            description='description2',
            size_kb='sizeKb2',
            carrier_rate_plan_code='carrierRatePlanCode8',
            zero_dollar_billing=False,
            promotion_offered=False
        )
    ],
    description='PlanDescription 2',
    size_kb='1048576',
    carrier_rate_plan_code='Service plan code value',
    zero_dollar_billing=False,
    promotion_offered=False,
    promotion_days=-2147483648
)
```

