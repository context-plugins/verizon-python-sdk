
# Dm V1 Devices Actions Set Request

## Structure

`DmV1DevicesActionsSetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `configuration` | [`DtoDeviceActionSetConfiguration1`](../../doc/models/dto-device-action-set-configuration-1.md) | Optional | - |
| `resourceidentifier` | [`DtoDeviceResourceIdentifier1`](../../doc/models/dto-device-resource-identifier-1.md) | Optional | Device identifiers, one or more are required |

## Example

```python
from verizon.models.dm_v1_devices_actions_set_request import DmV1DevicesActionsSetRequest
from verizon.models.dto_device_action_set_configuration_1 import DtoDeviceActionSetConfiguration1
from verizon.models.dto_device_config import DtoDeviceConfig
from verizon.models.dto_device_resource_identifier_1 import DtoDeviceResourceIdentifier1
from verizon.models.mode_enum import ModeEnum
from verizon.models.periodic_reporting import PeriodicReporting
from verizon.models.rbs_high_precision_tilt_config import RbsHighPrecisionTiltConfig
from verizon.models.sensor_insights_ble import SensorInsightsBLE
from verizon.models.unit_enum import UnitEnum

dm_v1_devices_actions_set_request = DmV1DevicesActionsSetRequest(
    accountname='0000123456-00001',
    configuration=DtoDeviceActionSetConfiguration1(
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
    ),
    resourceidentifier=DtoDeviceResourceIdentifier1(
        deveui='deveui2',
        deviceid='deviceid6',
        esn=86,
        iccid='iccid0',
        imei=2
    )
)
```

