
# SMS Messages Query Result

Response to SMS messages sent by all M2M devices associated with a billing account.

## Structure

`SMSMessagesQueryResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | False for a status 200 response.True for a status 202 response, indicating that there is more data to be retrieved. |
| `messages` | [`List[SMSMessage]`](../../doc/models/sms-message.md) | Optional | An array of up to 100 SMS messages that were sent by devices in the account. |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.sms_message import SMSMessage
from verizon.models.sms_messages_query_result import SMSMessagesQueryResult

sms_messages_query_result = SMSMessagesQueryResult(
    has_more_data=False,
    messages=[
        SMSMessage(
            device_ids=[
                DeviceId(
                    id='09623489171',
                    kind='esn'
                )
            ],
            message='testmessage1',
            timestamp='2016-01-01T12:29:49-08:00'
        ),
        SMSMessage(
            device_ids=[
                DeviceId(
                    id='09623489171',
                    kind='esn'
                )
            ],
            message='testmessage2',
            timestamp='2016-01-01T12:31:02-08:00'
        )
    ]
)
```

