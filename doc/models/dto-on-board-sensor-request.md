
# Dto on Board Sensor Request

## Structure

`DtoOnBoardSensorRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `payload` | [`Payload`](../../doc/models/payload.md) | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.dto_on_board_sensor_request import DtoOnBoardSensorRequest
from verizon.models.payload import Payload
from verizon.models.resource_on_board_sensor import ResourceOnBoardSensor

dto_on_board_sensor_request = DtoOnBoardSensorRequest(
    accountname='0000123456-00001',
    payload=Payload(
        addsensor=ResourceOnBoardSensor(
            deveui='deveui6',
            appeui='appeui0',
            appkey='appkey0',
            mclass='class4',
            kind='kind8',
            description='description0',
            name='name0',
            customdata={
                'key0': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                'key1': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                'key2': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    )
)
```

