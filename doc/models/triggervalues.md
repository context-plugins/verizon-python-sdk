
# Triggervalues

## Structure

`Triggervalues`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | - |
| `trigger_name` | `str` | Optional | - |
| `account_name` | `str` | Optional | - |
| `organization_name` | `str` | Optional | - |
| `trigger_category` | `str` | Optional | - |
| `trigger_attributes` | List[[keyServicePlan](../../doc/models/key-service-plan.md) \| [keyDataPercentage50](../../doc/models/key-data-percentage-50.md) \| [keysmsPercentage50](../../doc/models/keysms-percentage-50.md) \| [NoOfDaysB4PromoExp](../../doc/models/no-of-days-b4-promo-exp.md) \| [EnablePromoExp](../../doc/models/enable-promo-exp.md)] \| None | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `modified_at` | `datetime` | Optional | - |

## Example

```python
from verizon.models.triggervalues import Triggervalues

triggervalues = Triggervalues(
    trigger_id='2874DEC7-26CF-4797-9C6A-B5A2AC72D526',
    trigger_name='PromoAlerts_0000000000-00001_23456789',
    account_name='0000123456-000001',
    organization_name='Optional group name',
    trigger_category='PromoAlerts'
)
```

