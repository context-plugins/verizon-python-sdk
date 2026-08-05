
# Data Percentage 75 Trigger Attribute

Trigger attribute for when data percentage is over 75% used.

## Structure

`DataPercentage75TriggerAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | Key data percentage 75. |
| `value` | `bool` | Optional | DataPercentage75<br />True - Trigger on Data percentage is over 75% used<br />False - Do not trigger when over 75% used. |

## Example

```python
from verizon.models.data_percentage_75_trigger_attribute import DataPercentage75TriggerAttribute

data_percentage_75_trigger_attribute = DataPercentage75TriggerAttribute(
    key='DataPercentage75',
    value=False
)
```

