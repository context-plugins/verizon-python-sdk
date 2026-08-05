
# Daily Usage Item

Contains only dates when device had sessions.

## Structure

`DailyUsageItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_time` | `str` | Optional | Start date of session. ISO 8601 format. |
| `end_time` | `str` | Optional | End date of session. ISO 8601 format. |
| `num_bytes` | `int` | Optional | Amount of data transferred, measured in Bytes. |

## Example

```python
from verizon.models.daily_usage_item import DailyUsageItem

daily_usage_item = DailyUsageItem(
    start_time='startTime2',
    end_time='endTime0',
    num_bytes=144
)
```

