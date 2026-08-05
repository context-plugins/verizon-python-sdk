
# Position Data

Position data.

## Structure

`PositionData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time` | `str` | Optional | Time location obtained. |
| `utcoffset` | `str` | Optional | UTC offset of time. |
| `x` | `str` | Optional | X coordinate of location. |
| `y` | `str` | Optional | Y coordinate of location. |
| `radius` | `str` | Optional | Radius of the location in meters. |
| `qos` | `bool` | Optional | Whether requested accurary is met or not. |

## Example

```python
from verizon.models.position_data import PositionData

position_data = PositionData(
    time='20170520004421',
    utcoffset='utcoffset0',
    x='33.45324',
    y='-84.59621',
    radius='5571',
    qos=False
)
```

