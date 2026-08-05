
# Session Report

Session report for a device.

## Structure

`SessionReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The 10-digit ID of the device. |
| `txid` | `str` | Required | A unique string (UUID) that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have a txid. |
| `sessions` | [`List[DailyUsageItem]`](../../doc/models/daily-usage-item.md) | Optional | An object containing the start and end time of the session with the amount of data transferred. |

## Example

```python
from verizon.models.daily_usage_item import DailyUsageItem
from verizon.models.session_report import SessionReport

session_report = SessionReport(
    id='id4',
    txid='60c07fff-eeee-ffff-gggg-75e6a7c238f6',
    sessions=[
        DailyUsageItem(
            start_time='startTime4',
            end_time='endTime8',
            num_bytes=106
        ),
        DailyUsageItem(
            start_time='startTime4',
            end_time='endTime8',
            num_bytes=106
        ),
        DailyUsageItem(
            start_time='startTime4',
            end_time='endTime8',
            num_bytes=106
        )
    ]
)
```

