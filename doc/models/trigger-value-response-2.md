
# Trigger Value Response 2

## Structure

`TriggerValueResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `triggers` | List[[Triggervalues2](../../doc/models/triggervalues-2.md)] \| None | Optional | - |

## Example

```python
from verizon.models.trigger_value_response_2 import TriggerValueResponse2
from verizon.models.triggervalues_2 import Triggervalues2

trigger_value_response_2 = TriggerValueResponse2(
    triggers=[
        Triggervalues2(
            trigger_id='triggerId8',
            trigger_name='triggerName6',
            account_name='accountName2',
            organization_name='organizationName0',
            trigger_category='triggerCategory0'
        ),
        Triggervalues2(
            trigger_id='triggerId8',
            trigger_name='triggerName6',
            account_name='accountName2',
            organization_name='organizationName0',
            trigger_category='triggerCategory0'
        ),
        Triggervalues2(
            trigger_id='triggerId8',
            trigger_name='triggerName6',
            account_name='accountName2',
            organization_name='organizationName0',
            trigger_category='triggerCategory0'
        )
    ]
)
```

