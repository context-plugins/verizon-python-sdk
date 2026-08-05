
# Dto Sensor Off Boarding Status Response

## Structure

`DtoSensorOffBoardingStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List[DtoSensorBoardingEvent]`](../../doc/models/dto-sensor-boarding-event.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `isstillregistered` | `bool` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.dto_fields import DtoFields
from verizon.models.dto_sensor_boarding_event import DtoSensorBoardingEvent
from verizon.models.dto_sensor_off_boarding_status_response import DtoSensorOffBoardingStatusResponse

dto_sensor_off_boarding_status_response = DtoSensorOffBoardingStatusResponse(
    events=[
        DtoSensorBoardingEvent(
            createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            errmsg='errmsg2',
            fields=DtoFields(),
            state='state6',
            transactionid='transactionid8'
        ),
        DtoSensorBoardingEvent(
            createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            errmsg='errmsg2',
            fields=DtoFields(),
            state='state6',
            transactionid='transactionid8'
        ),
        DtoSensorBoardingEvent(
            createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            errmsg='errmsg2',
            fields=DtoFields(),
            state='state6',
            transactionid='transactionid8'
        )
    ],
    isstillregistered=True
)
```

