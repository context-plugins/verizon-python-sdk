
# Dto Off Board Sensor Request

## Structure

`DtoOffBoardSensorRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `configuration` | [`Sensorinsightsconfig`](../../doc/models/sensorinsightsconfig.md) | Optional | The configuration of the remove request |

## Example

```python
from verizon.models.dto_off_board_sensor import DtoOffBoardSensor
from verizon.models.dto_off_board_sensor_request import DtoOffBoardSensorRequest
from verizon.models.sensorinsightsconfig import Sensorinsightsconfig

dto_off_board_sensor_request = DtoOffBoardSensorRequest(
    accountname='0000123456-00001',
    configuration=Sensorinsightsconfig(
        removesensor=DtoOffBoardSensor(
            deveui='deveui6'
        )
    )
)
```

