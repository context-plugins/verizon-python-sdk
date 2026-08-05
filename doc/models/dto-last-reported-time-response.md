
# Dto Last Reported Time Response

## Structure

`DtoLastReportedTimeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event` | [`ResourceEvent`](../../doc/models/resource-event.md) | Optional | - |
| `timestamp` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.dto_last_reported_time_response import DtoLastReportedTimeResponse
from verizon.models.resource_event import ResourceEvent

dto_last_reported_time_response = DtoLastReportedTimeResponse(
    event=ResourceEvent(
        createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        fieldid='fieldid6',
        foreignid='foreignid8',
        lastupdated=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        state='state4',
        versionid='versionid2',
        accountclientid='accountclientid4',
        callbackurl='callbackurl0',
        description='description0',
        deviceid='deviceid0',
        errmsg='errmsg2'
    ),
    timestamp='timestamp8'
)
```

