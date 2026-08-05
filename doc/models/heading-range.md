
# Heading Range

Acceptable heading range for road users in degrees.

## Structure

`HeadingRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `float` | Required | The minimum value of heading in unit of degrees.<br><br>**Constraints**: `>= 0`, `<= 360` |
| `max` | `float` | Required | The maximum value of heading in unit of degrees.<br><br>**Constraints**: `>= 0`, `<= 360` |

## Example

```python
from verizon.models.heading_range import HeadingRange

heading_range = HeadingRange(
    min=88.06,
    max=161.48
)
```

