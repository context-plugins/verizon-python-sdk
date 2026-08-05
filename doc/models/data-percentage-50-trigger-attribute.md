
# Data Percentage 50 Trigger Attribute

Trigger attribute for when data percentage is over 50% used.

## Structure

`DataPercentage50TriggerAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | Key data percentage 50. |
| `value` | `bool` | Optional | DataPercentage50<br />True - Trigger on Data percentage is over 50% used<br />False - Do not trigger when over 50% used. |

## Example

```python
from verizon.models.data_percentage_50_trigger_attribute import DataPercentage50TriggerAttribute

data_percentage_50_trigger_attribute = DataPercentage50TriggerAttribute(
    key='DataPercentage50',
    value=False
)
```

