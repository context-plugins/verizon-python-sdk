
# Data Percentage 100 Trigger Attribute

Trigger attribute for when data percentage is over 100% used.

## Structure

`DataPercentage100TriggerAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | Key data percentage 100. |
| `value` | `bool` | Optional | DataPercentage100<br />True - Trigger on Data percentage is over 100% used<br />False - Do not trigger when over 100% used. |

## Example

```python
from verizon.models.data_percentage_100_trigger_attribute import DataPercentage100TriggerAttribute

data_percentage_100_trigger_attribute = DataPercentage100TriggerAttribute(
    key='DataPercentage100',
    value=False
)
```

