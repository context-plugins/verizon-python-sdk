
# GIO Sms Message

## Structure

`GIOSmsMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[GIODeviceId]`](../../doc/models/gio-device-id.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `message` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `120`, *Pattern*: `^[A-Za-z0-9 ]{3,120}$` |
| `timestamp` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.gio_device_id import GIODeviceId
from verizon.models.gio_sms_message import GIOSmsMessage

gio_sms_message = GIOSmsMessage(
    device_ids=[
        GIODeviceId(
            kind='kind8',
            id='id0'
        )
    ],
    message='a text message',
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

