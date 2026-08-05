
# V3 Time Window

Time window.

## Structure

`V3TimeWindow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_time` | `int` | Required | Start hour in range [0..23], current hour >= startTime. |
| `end_time` | `int` | Required | End hour in range [1..24], current hour < endTime. |

## Example

```python
from verizon.models.v3_time_window import V3TimeWindow

v3_time_window = V3TimeWindow(
    start_time=18,
    end_time=22
)
```

