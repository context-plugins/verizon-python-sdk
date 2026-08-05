
# Road Sign Position

Precise location of a road sign in the WGS-84 coordinate system, from which short offsets may be used to create additional data using a flat earth projection centered on this location.

## Structure

`RoadSignPosition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lat` | `int` | Required | The geographic latitude of an object, expressed in 1/10th integer microdegrees, as a 31 bit value, and with reference to the horizontal datum then in use. The value 900000001 shall be used when unavailable.<br><br>**Constraints**: `>= -900000000`, `<= 900000001` |
| `long` | `int` | Required | The geographic longitude of an object, expressed in 1/10th integer microdegrees, as a 32-bit value, and with reference to the horizontal datum then in use. The value 1800000001 shall be used when unavailable.<br><br>**Constraints**: `>= -1799999999`, `<= 1800000001` |

## Example

```python
from verizon.models.road_sign_position import RoadSignPosition

road_sign_position = RoadSignPosition(
    lat=8,
    long=166
)
```

