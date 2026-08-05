
# Event Position

## Structure

`EventPosition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `int` | Required | Latitude of the event location in microdegrees (900000001 shall be used when unavailable).<br><br>**Constraints**: `>= -900000000`, `<= 900000001` |
| `longitude` | `int` | Required | Longitude of the event location in microdegrees (1800000001 shall be used when unavailable).<br><br>**Constraints**: `>= -1800000000`, `<= 1800000001` |
| `position_confidence_ellipse` | [`PosConfidenceEllipse`](../../doc/models/pos-confidence-ellipse.md) | Required | - |
| `altitude` | [`Altitude`](../../doc/models/altitude.md) | Required | - |

## Example

```python
from verizon.models.altitude import Altitude
from verizon.models.altitude_confidence_enum import AltitudeConfidenceEnum
from verizon.models.event_position import EventPosition
from verizon.models.pos_confidence_ellipse import PosConfidenceEllipse

event_position = EventPosition(
    latitude=246,
    longitude=46,
    position_confidence_ellipse=PosConfidenceEllipse(
        semi_major_confidence=16,
        semi_minor_confidence=114,
        semi_major_orientation=100
    ),
    altitude=Altitude(
        altitude_value=236,
        altitude_confidence=AltitudeConfidenceEnum.ALT00001
    )
)
```

