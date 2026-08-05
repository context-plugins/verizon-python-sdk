
# Payload

## Structure

`Payload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `addsensor` | [`ResourceOnBoardSensor`](../../doc/models/resource-on-board-sensor.md) | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.payload import Payload
from verizon.models.resource_on_board_sensor import ResourceOnBoardSensor

payload = Payload(
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
```

