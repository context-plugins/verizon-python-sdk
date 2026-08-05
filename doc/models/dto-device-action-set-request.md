
# Dto Device Action Set Request

## Structure

`DtoDeviceActionSetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `configuration` | [`DtoDeviceActionSetConfiguration`](../../doc/models/dto-device-action-set-configuration.md) | Optional | - |
| `resourceidentifier` | [`DtoDeviceResourceIdentifier`](../../doc/models/dto-device-resource-identifier.md) | Optional | Device identifiers, one or more are required |

## Example

```python
from verizon.models.dto_device_action_set_configuration import DtoDeviceActionSetConfiguration
from verizon.models.dto_device_action_set_request import DtoDeviceActionSetRequest
from verizon.models.dto_device_config import DtoDeviceConfig
from verizon.models.dto_device_resource_identifier import DtoDeviceResourceIdentifier
from verizon.models.sensor_insights_ble import SensorInsightsBLE

dto_device_action_set_request = DtoDeviceActionSetRequest(
    accountname='0000123456-00001',
    configuration=DtoDeviceActionSetConfiguration(
        device_config=DtoDeviceConfig(
            ble=SensorInsightsBLE(
                data_mode=216,
                manufacturer_id=180,
                max_num_scan=126,
                min_sig_str=60,
                monitor_period=88
            )
        )
    ),
    resourceidentifier=DtoDeviceResourceIdentifier(
        deveui='deveui2',
        deviceid='deviceid6',
        esn=86,
        iccid='iccid0',
        imei=2
    )
)
```

