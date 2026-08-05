
# V2 Time Window

Allowed start and end time windows.

## Structure

`V2TimeWindow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_time` | `int` | Required | Start hour in range [0..23], current hour >= startTime. |
| `end_time` | `int` | Required | End hour in range [1..24], current hour < endTime. |

## Example

```python
from verizon.models.v2_time_window import V2TimeWindow

v2_time_window = V2TimeWindow(
    start_time=20,
    end_time=21
)
```

