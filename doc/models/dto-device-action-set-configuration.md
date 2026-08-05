
# Dto Device Action Set Configuration

## Structure

`DtoDeviceActionSetConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_config` | [`DtoDeviceConfig`](../../doc/models/dto-device-config.md) | Optional | - |

## Example

```python
from verizon.models.dto_device_action_set_configuration import DtoDeviceActionSetConfiguration
from verizon.models.dto_device_config import DtoDeviceConfig
from verizon.models.sensor_insights_ble import SensorInsightsBLE

dto_device_action_set_configuration = DtoDeviceActionSetConfiguration(
    device_config=DtoDeviceConfig(
        ble=SensorInsightsBLE(
            data_mode=216,
            manufacturer_id=180,
            max_num_scan=126,
            min_sig_str=60,
            monitor_period=88
        )
    )
)
```

