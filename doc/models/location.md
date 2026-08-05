
# Location

Device location information.

## Structure

`Location`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msid` | `str` | Optional | MDN. |
| `pd` | [`PositionData`](../../doc/models/position-data.md) | Optional | Position data. |
| `error` | [`PositionError`](../../doc/models/position-error.md) | Optional | Position error. |

## Example

```python
from verizon.models.location import Location
from verizon.models.position_data import PositionData
from verizon.models.position_error import PositionError

location = Location(
    msid='7892345678',
    pd=PositionData(
        time='20170520004421',
        utcoffset='utcoffset2',
        x='33.45324',
        y='-84.59621',
        radius='5571',
        qos=False
    ),
    error=PositionError(
        time='time4',
        utcoffset='utcoffset4',
        mtype='type6',
        info='info4'
    )
)
```

