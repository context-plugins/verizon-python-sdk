
# Sensorinsightsconfig

The configuration of the remove request

## Structure

`Sensorinsightsconfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `removesensor` | [`DtoOffBoardSensor`](../../doc/models/dto-off-board-sensor.md) | Optional | The EUI64 address of the device being removed |

## Example

```python
from verizon.models.dto_off_board_sensor import DtoOffBoardSensor
from verizon.models.sensorinsightsconfig import Sensorinsightsconfig

sensorinsightsconfig = Sensorinsightsconfig(
    removesensor=DtoOffBoardSensor(
        deveui='deveui6'
    )
)
```

