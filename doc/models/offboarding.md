
# Offboarding

## Structure

`Offboarding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sensoridentifier` | `str` | Optional | the IEEE EUI64 address space used to identify a device. It is supplied by the device manufacturer |

## Example

```python
from verizon.models.offboarding import Offboarding

offboarding = Offboarding(
    sensoridentifier='The unique EUI64 address of the device'
)
```

