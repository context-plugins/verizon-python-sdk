
# Service Plan Trigger Attribute

Key service plan trigger attribute.

## Structure

`ServicePlanTriggerAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | The ServicePlan name will be listed here. |

## Example

```python
from verizon.models.service_plan_trigger_attribute import ServicePlanTriggerAttribute

service_plan_trigger_attribute = ServicePlanTriggerAttribute(
    key='ServicePlan'
)
```

