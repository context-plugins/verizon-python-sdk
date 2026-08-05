
# Rbs High Precision Tilt Config

## Structure

`RbsHighPrecisionTiltConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mode` | [`ModeEnum`](../../doc/models/mode-enum.md) | Optional | the reporting mode of the tilt sensor |
| `periodic_reporting` | [`PeriodicReporting`](../../doc/models/periodic-reporting.md) | Optional | The units and values of the time interval for the sensor to send a report |
| `hold_time` | `int` | Optional | The time the threshold condition exists, in milliseconds, to recognize an event |
| `angle_away` | `int` | Optional | the threshold value, from verticle, to recognize an event |
| `angle_toward` | `int` | Optional | the threshold value, moving towards  verticle, to recognize an event |
| `tscore` | [`Tscore`](../../doc/models/tscore.md) | Optional | - |

## Example

```python
from verizon.models.mode_enum import ModeEnum
from verizon.models.periodic_reporting import PeriodicReporting
from verizon.models.rbs_high_precision_tilt_config import RbsHighPrecisionTiltConfig
from verizon.models.unit_enum import UnitEnum

rbs_high_precision_tilt_config = RbsHighPrecisionTiltConfig(
    mode=ModeEnum.REPORTONCHANGE,
    periodic_reporting=PeriodicReporting(
        unit=UnitEnum.MINUTES,
        hours=250,
        minutes=232
    ),
    hold_time=5000,
    angle_away=5,
    angle_toward=5
)
```

