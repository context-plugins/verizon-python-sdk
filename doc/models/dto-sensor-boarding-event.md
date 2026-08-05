
# Dto Sensor Boarding Event

## Structure

`DtoSensorBoardingEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `createdon` | `datetime` | Optional | Timestamp of the record |
| `errmsg` | `str` | Optional | Error message |
| `fields` | [`DtoFields`](../../doc/models/dto-fields.md) | Optional | Fields to return needed by search |
| `state` | `str` | Optional | The current status of the device or transaction and will be `success` or `failed` |
| `transactionid` | `str` | Optional | The system-generated UUID of the transaction |

## Example

```python
import dateutil.parser

from verizon.models.dto_fields import DtoFields
from verizon.models.dto_sensor_boarding_event import DtoSensorBoardingEvent

dto_sensor_boarding_event = DtoSensorBoardingEvent(
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    errmsg='provider_service_error',
    fields=DtoFields(
        additional_prop_1='string',
        additional_prop_2='string',
        additional_prop_3='string'
    ),
    state='success',
    transactionid='afbcc00d-eeee-ffff-gggg-38b4333fcf06'
)
```

