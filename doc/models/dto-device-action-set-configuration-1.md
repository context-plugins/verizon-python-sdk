
# Dto Device Action Set Configuration 1

## Structure

`DtoDeviceActionSetConfiguration1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_config` | [`DtoDeviceConfig`](../../doc/models/dto-device-config.md) | Optional | - |
| `rbs_high_precision_tilt_config` | [`RbsHighPrecisionTiltConfig`](../../doc/models/rbs-high-precision-tilt-config.md) | Optional | - |

## Example

```python
from verizon.models.dto_device_action_set_configuration_1 import DtoDeviceActionSetConfiguration1
from verizon.models.dto_device_config import DtoDeviceConfig
from verizon.models.mode_enum import ModeEnum
from verizon.models.periodic_reporting import PeriodicReporting
from verizon.models.rbs_high_precision_tilt_config import RbsHighPrecisionTiltConfig
from verizon.models.sensor_insights_ble import SensorInsightsBLE
from verizon.models.unit_enum import UnitEnum

dto_device_action_set_configuration_1 = DtoDeviceActionSetConfiguration1(
    device_config=DtoDeviceConfig(
        ble=SensorInsightsBLE(
            data_mode=216,
            manufacturer_id=180,
            max_num_scan=126,
            min_sig_str=60,
            monitor_period=88
        )
    ),
    rbs_high_precision_tilt_config=RbsHighPrecisionTiltConfig(
        mode=ModeEnum.REPORTONCHANGE,
        periodic_reporting=PeriodicReporting(
            unit=UnitEnum.MINUTES,
            hours=250,
            minutes=232
        ),
        hold_time=62,
        angle_away=90,
        angle_toward=30
    )
)
```

