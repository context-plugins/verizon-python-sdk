
# Promo Alert Trigger Request

## Structure

`PromoAlertTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_percentage_50` | `bool` | Optional | - |
| `data_percentage_75` | `bool` | Optional | - |
| `data_percentage_90` | `bool` | Optional | - |
| `no_of_days_b_4_promo_exp` | `int` | Optional | **Constraints**: `>= 0`, `<= 180` |
| `sms_percentage_50` | `bool` | Optional | - |
| `sms_percentage_75` | `bool` | Optional | - |
| `sms_percentage_90` | `bool` | Optional | - |

## Example

```python
from verizon.models.promo_alert_trigger_request import PromoAlertTriggerRequest

promo_alert_trigger_request = PromoAlertTriggerRequest(
    data_percentage_50=False,
    data_percentage_75=False,
    data_percentage_90=False,
    no_of_days_b_4_promo_exp=48,
    sms_percentage_50=False
)
```

