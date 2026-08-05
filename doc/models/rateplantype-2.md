
# Rateplantype 2

## Structure

`Rateplantype2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | - |
| `size_kb` | `str` | Optional | - |
| `carrier_rate_plan_code` | `str` | Optional | - |
| `zero_dollar_billing` | `bool` | Optional | - |
| `promotion_offered` | `bool` | Optional | - |
| `promotion_days` | `int` | Optional | - |
| `rate_plan_type` | `str` | Optional | - |
| `account` | [`List[Accountid]`](../../doc/models/accountid.md) | Optional | Account information |

## Example

```python
from verizon.models.rateplantype_2 import Rateplantype2

rateplantype_2 = Rateplantype2(
    description='PlanDescription 2',
    size_kb='1048576',
    carrier_rate_plan_code='Service plan code value',
    zero_dollar_billing=False,
    promotion_offered=False,
    promotion_days=-2147483648
)
```

