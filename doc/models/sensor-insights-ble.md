
# Sensor Insights BLE

Property objects for Bluetooth Low-Energy (BLE) devices

## Structure

`SensorInsightsBLE`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_mode` | `int` | Optional | The data mode the sensor is using |
| `manufacturer_id` | `int` | Optional | The numeric manufacturer ID |
| `max_num_scan` | `int` | Optional | How frequently the device can be scanned |
| `min_sig_str` | `int` | Optional | The minimum signal strength needed for the sensor to transmit (in Decibels or dB) |
| `monitor_period` | `int` | Optional | The ammount of time to monitor the sensor and varies by device |
| `more_manuf_id` | `List[Any]` | Optional | Values for the manufacturer and these vary by device |
| `op_mode` | `int` | Optional | The operation mode |
| `report_offset` | `int` | Optional | The ammount of time between sensor readings and reports |
| `report_period` | `int` | Optional | The ammount of time between reports |
| `report_type` | `int` | Optional | The report type |
| `scan_duration` | `int` | Optional | The ammount of time the sensor is queried for data |

## Example

```python
from verizon.models.sensor_insights_ble import SensorInsightsBLE

sensor_insights_ble = SensorInsightsBLE(
    data_mode=1,
    manufacturer_id=13200,
    max_num_scan=100,
    min_sig_str=-115,
    monitor_period=300,
    op_mode=1,
    report_offset=0,
    report_period=300,
    report_type=2,
    scan_duration=20
)
```

