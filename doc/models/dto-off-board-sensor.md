
# Dto Off Board Sensor

The EUI64 address of the device being removed

## Structure

`DtoOffBoardSensor`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deveui` | `str` | Optional | the IEEE EUI64 address space used to identify a device. It is supplied by the device manufacturer |

## Example

```python
from verizon.models.dto_off_board_sensor import DtoOffBoardSensor

dto_off_board_sensor = DtoOffBoardSensor(
    deveui='The unique EUI64 address of the device'
)
```

