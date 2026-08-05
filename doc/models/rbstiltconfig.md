
# Rbstiltconfig

## Structure

`Rbstiltconfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rbs_high_precision_tilt_config` | [`RbsHighPrecisionTiltConfig`](../../doc/models/rbs-high-precision-tilt-config.md) | Optional | - |

## Example

```python
from verizon.models.mode_enum import ModeEnum
from verizon.models.periodic_reporting import PeriodicReporting
from verizon.models.rbs_high_precision_tilt_config import RbsHighPrecisionTiltConfig
from verizon.models.rbstiltconfig import Rbstiltconfig
from verizon.models.unit_enum import UnitEnum

rbstiltconfig = Rbstiltconfig(
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

