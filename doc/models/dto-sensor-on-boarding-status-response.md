
# Dto Sensor on Boarding Status Response

## Structure

`DtoSensorOnBoardingStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List[DtoSensorBoardingEvent]`](../../doc/models/dto-sensor-boarding-event.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
import dateutil.parser

from verizon.models.dto_fields import DtoFields
from verizon.models.dto_sensor_boarding_event import DtoSensorBoardingEvent
from verizon.models.dto_sensor_on_boarding_status_response import DtoSensorOnBoardingStatusResponse

dto_sensor_on_boarding_status_response = DtoSensorOnBoardingStatusResponse(
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
        )
    ]
)
```

