
# Device Log

Device logging information.

## Structure

`DeviceLog`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `log_time` | `datetime` | Required | Time of log. |
| `log_type` | `str` | Required | Log type (one of SoftwareUpdate, Event, UserNotification, AgentService, Wireless, WirelessWeb, MobileBroadbandModem, WindowsMDM). |
| `event_log` | `str` | Required | Event log. |
| `binary_log_file_base_64` | `str` | Required | Base64-encoded contents of binary log file. |
| `binary_log_filename` | `str` | Required | File name of binary log file. |

## Example

```python
import dateutil.parser

from verizon.models.device_log import DeviceLog

device_log = DeviceLog(
    device_id='990013907835573',
    log_time=dateutil.parser.parse('2020-10-22T19:29:50.901Z'),
    log_type='logType2',
    event_log='eventLog6',
    binary_log_file_base_64='binaryLogFileBase640',
    binary_log_filename='binaryLogFilename6'
)
```

