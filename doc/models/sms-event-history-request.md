
# SMS Event History Request

## Structure

`SMSEventHistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`GIODeviceId`](../../doc/models/gio-device-id.md) | Required | - |
| `earliest` | `datetime` | Optional | - |
| `latest` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.gio_device_id import GIODeviceId
from verizon.models.sms_event_history_request import SMSEventHistoryRequest

sms_event_history_request = SMSEventHistoryRequest(
    device_id=GIODeviceId(
        kind='eid',
        id='12345678901234567890123456789012'
    ),
    earliest=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    latest=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

