
# Position Error

Position error.

## Structure

`PositionError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time` | `str` | Optional | Time location obtained. |
| `utcoffset` | `str` | Optional | UTC offset of time. |
| `mtype` | `str` | Optional | Error type returned from location server. |
| `info` | `str` | Optional | Additional information about the error. |

## Example

```python
from verizon.models.position_error import PositionError

position_error = PositionError(
    time='20170525214342',
    utcoffset='utcoffset2',
    mtype='POSITION METHOD FAILURE',
    info='Exception code=ABSENT SUBSCRIBER'
)
```

