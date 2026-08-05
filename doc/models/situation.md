
# Situation

This represents the situation container describing the event and the reliability of the detection source.

## Structure

`Situation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `information_quality` | `int` | Required | The quality or reliability level of the information provided by the ITS-S application of the originating ITS-S.<br><br>**Constraints**: `>= 0`, `<= 7` |
| `event_type` | [`EventType`](../../doc/models/event-type.md) | Required | The type of event including direct and sub cause. |

## Example

```python
from verizon.models.event_type import EventType
from verizon.models.situation import Situation
from verizon.models.traffic_condition_cause_code import TrafficConditionCauseCode

situation = Situation(
    information_quality=7,
    event_type=EventType(
        cc_and_scc=TrafficConditionCauseCode(
            traffic_condition_1=26
        )
    )
)
```

