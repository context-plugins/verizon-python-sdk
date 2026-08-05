
# Emergency Vehicle Approaching Cause Code

Cause code wrapper for emergency vehicle approaching events.

## Structure

`EmergencyVehicleApproachingCauseCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `emergency_vehicle_approaching_95` | `int` | Required | The value shall be set to:<br><br>- 0 `unavailable`                   - in case further detailed information on the emergency vehicle approaching event is unavailable,<br>- 1 `emergencyVehicleApproaching`   - in case an operating emergency vehicle is approaching,<br>- 2 `prioritizedVehicleApproaching` - in case a prioritized vehicle is approaching,<br>- 3-255                             - reserved for future usage.<br><br>**Constraints**: `>= 0`, `<= 255` |

## Example

```python
from verizon.models.emergency_vehicle_approaching_cause_code import EmergencyVehicleApproachingCauseCode

emergency_vehicle_approaching_cause_code = EmergencyVehicleApproachingCauseCode(
    emergency_vehicle_approaching_95=144
)
```

