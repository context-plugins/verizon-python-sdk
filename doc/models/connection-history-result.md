
# Connection History Result

Response containing the connection history. It is a list of Network Connection Events for a device.

## Structure

`ConnectionHistoryResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `connection_history` | [`List[ConnectionEvent]`](../../doc/models/connection-event.md) | Optional | Device connection events, sorted by the occurredAt timestamp, oldest first. |
| `has_more_data` | `bool` | Optional | False for a status 200 response.True for a status 202 response, indicating that there is more data to be retrieved. Send another request, adjusting the earliest value in the request based on the occuredAt value for the last device in the current response. |

## Example

```python
from verizon.models.connection_event import ConnectionEvent
from verizon.models.connection_history_result import ConnectionHistoryResult
from verizon.models.custom_fields import CustomFields

connection_history_result = ConnectionHistoryResult(
    connection_history=[
        ConnectionEvent(
            connection_event_attributes=[
                CustomFields(
                    key='BytesUsed',
                    value='0'
                ),
                CustomFields(
                    key='Event',
                    value='Start'
                )
            ],
            extended_attributes=[],
            occurred_at='2015-12-17T14:12:36-05:00'
        ),
        ConnectionEvent(
            connection_event_attributes=[
                CustomFields(
                    key='BytesUsed',
                    value='419863234'
                ),
                CustomFields(
                    key='Event',
                    value='Stop'
                ),
                CustomFields(
                    key='Msisdn',
                    value='15086303371'
                )
            ],
            extended_attributes=[],
            occurred_at='2015-12-19T01:20:00-05:00'
        )
    ],
    has_more_data=False
)
```

