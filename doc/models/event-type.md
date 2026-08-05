
# Event Type

The type of event including direct and sub cause.

## Structure

`EventType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cc_and_scc` | [TrafficConditionCauseCode](../../doc/models/traffic-condition-cause-code.md) \| [AccidentCauseCode](../../doc/models/accident-cause-code.md) \| [RoadworksCauseCode](../../doc/models/roadworks-cause-code.md) \| [ImpassabilityCauseCode](../../doc/models/impassability-cause-code.md) \| [WrongWayDrivingCauseCode](../../doc/models/wrong-way-driving-cause-code.md) \| [EmergencyVehicleApproachingCauseCode](../../doc/models/emergency-vehicle-approaching-cause-code.md) \| None | Optional | The main cause of a detected event. Each entry is of a different type and represents the sub cause code. |

## Example

```python
from verizon.models.event_type import EventType
from verizon.models.traffic_condition_cause_code import TrafficConditionCauseCode

event_type = EventType(
    cc_and_scc=TrafficConditionCauseCode(
        traffic_condition_1=26
    )
)
```

