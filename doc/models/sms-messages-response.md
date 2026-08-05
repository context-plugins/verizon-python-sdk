
# Sms Messages Response

## Structure

`SmsMessagesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `messages` | List[[GIOSmsMessage](../../doc/models/gio-sms-message.md)] \| None | Optional | This is List of a container for any-of cases.<br><br>**Constraints**: *Maximum Items*: `5` |
| `has_more_data` | `bool` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.gio_device_id import GIODeviceId
from verizon.models.gio_sms_message import GIOSmsMessage
from verizon.models.sms_messages_response import SmsMessagesResponse

sms_messages_response = SmsMessagesResponse(
    messages=[
        GIOSmsMessage(
            device_ids=[
                GIODeviceId(
                    kind='kind8',
                    id='id0'
                )
            ],
            message='message4',
            timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    has_more_data=False
)
```

