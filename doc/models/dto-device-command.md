
# Dto Device Command

## Structure

`DtoDeviceCommand`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric account name, which must include leading zeros |
| `configuration` | [`Rbstiltconfig`](../../doc/models/rbstiltconfig.md) | Optional | - |
| `resourceidentifier` | [`DtoResourceidentifier`](../../doc/models/dto-resourceidentifier.md) | Optional | - |

## Example

```python
from verizon.models.dto_device_command import DtoDeviceCommand
from verizon.models.dto_resourceidentifier import DtoResourceidentifier
from verizon.models.mode_enum import ModeEnum
from verizon.models.periodic_reporting import PeriodicReporting
from verizon.models.rbs_high_precision_tilt_config import RbsHighPrecisionTiltConfig
from verizon.models.rbstiltconfig import Rbstiltconfig
from verizon.models.unit_enum import UnitEnum

dto_device_command = DtoDeviceCommand(
    account_name='0000123456-00001',
    configuration=Rbstiltconfig(
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
    ),
    resourceidentifier=DtoResourceidentifier(
        id='id4'
    )
)
```

