
# Check In History Item

Check-in history for a device.

## Structure

`CheckInHistoryItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `client_type` | `str` | Required | Type of client. |
| `result` | `str` | Required | - |
| `failure_type` | `str` | Required | - |
| `time_completed` | `datetime` | Required | - |

## Example

```python
import dateutil.parser

from verizon.models.check_in_history_item import CheckInHistoryItem

check_in_history_item = CheckInHistoryItem(
    device_id='990013907835573',
    client_type='clientType4',
    result='result8',
    failure_type='failureType8',
    time_completed=dateutil.parser.parse('2020-10-22T19:35:07.753Z')
)
```

