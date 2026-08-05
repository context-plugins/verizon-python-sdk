
# Speed Range

Acceptable speed range for road users in m/s.

## Structure

`SpeedRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `float` | Required | The minimum required speed in m/s.<br><br>**Constraints**: `>= 0`, `<= 160` |
| `max` | `float` | Required | The maximum acceptable speed in m/s.<br><br>**Constraints**: `>= 0`, `<= 160` |

## Example

```python
from verizon.models.speed_range import SpeedRange

speed_range = SpeedRange(
    min=53.76,
    max=19.66
)
```

