
# Active Trigger Indicator

Whether the trigger is active or not.

## Structure

`ActiveTriggerIndicator`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | Indicates if the trigger is active<br />True - trigger is active<br />False - trigger is not active. |

## Example

```python
from verizon.models.active_trigger_indicator import ActiveTriggerIndicator

active_trigger_indicator = ActiveTriggerIndicator(
    active=True
)
```

