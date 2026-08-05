
# Connection Event

Network connection events for a device during a specified time period.

## Structure

`ConnectionEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `connection_event_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The attributes that describe the connection event. |
| `extended_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Currently not used. |
| `occurred_at` | `str` | Optional | The date and time when the connection event occured. |

## Example

```python
from verizon.models.connection_event import ConnectionEvent
from verizon.models.custom_fields import CustomFields

connection_event = ConnectionEvent(
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
)
```

