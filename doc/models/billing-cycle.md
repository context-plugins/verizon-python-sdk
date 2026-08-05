
# Billing Cycle

## Structure

`BillingCycle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `year` | `str` | Optional | - |
| `month` | `str` | Optional | - |

## Example

```python
from verizon.models.billing_cycle import BillingCycle

billing_cycle = BillingCycle(
    year='2020',
    month='3'
)
```

