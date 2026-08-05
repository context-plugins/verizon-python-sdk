
# Dto Device Config

## Structure

`DtoDeviceConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ble` | [`SensorInsightsBLE`](../../doc/models/sensor-insights-ble.md) | Optional | Property objects for Bluetooth Low-Energy (BLE) devices |

## Example

```python
from verizon.models.dto_device_config import DtoDeviceConfig
from verizon.models.sensor_insights_ble import SensorInsightsBLE

dto_device_config = DtoDeviceConfig(
    ble=SensorInsightsBLE(
        data_mode=216,
        manufacturer_id=180,
        max_num_scan=126,
        min_sig_str=60,
        monitor_period=88
    )
)
```

