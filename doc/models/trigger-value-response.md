
# Trigger Value Response

## Structure

`TriggerValueResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `triggers` | List[[Triggervalues](../../doc/models/triggervalues.md)] \| None | Optional | - |

## Example

```python
from verizon.models.trigger_value_response import TriggerValueResponse
from verizon.models.triggervalues import Triggervalues

trigger_value_response = TriggerValueResponse(
    triggers=[
        Triggervalues(
            trigger_id='triggerId4',
            trigger_name='triggerName2',
            account_name='accountName8',
            organization_name='organizationName6',
            trigger_category='triggerCategory6'
        )
    ]
)
```

