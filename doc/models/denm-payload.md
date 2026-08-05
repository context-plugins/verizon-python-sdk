
# Denm Payload

The payload of the DENM PDU.

## Structure

`DenmPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `management` | [`Management`](../../doc/models/management.md) | Required | This represent the management container describing the meta information about the event, such as the detection time, the event's location, the source of the event, and the notification distance. |
| `situation` | [`Situation`](../../doc/models/situation.md) | Optional | This represents the situation container describing the event and the reliability of the detection source. |

## Example

```python
from verizon.models.action_id import ActionId
from verizon.models.altitude import Altitude
from verizon.models.altitude_confidence_enum import AltitudeConfidenceEnum
from verizon.models.awareness_distance_enum import AwarenessDistanceEnum
from verizon.models.denm_payload import DenmPayload
from verizon.models.event_position import EventPosition
from verizon.models.event_type import EventType
from verizon.models.management import Management
from verizon.models.pos_confidence_ellipse import PosConfidenceEllipse
from verizon.models.situation import Situation
from verizon.models.traffic_condition_cause_code import TrafficConditionCauseCode

denm_payload = DenmPayload(
    management=Management(
        action_id=ActionId(
            originating_station_id=28,
            sequence_number=42
        ),
        detection_time=123456789,
        reference_time=123456789,
        event_position=EventPosition(
            latitude=198,
            longitude=234,
            position_confidence_ellipse=PosConfidenceEllipse(
                semi_major_confidence=16,
                semi_minor_confidence=114,
                semi_major_orientation=100
            ),
            altitude=Altitude(
                altitude_value=236,
                altitude_confidence=AltitudeConfidenceEnum.ALT00001
            )
        ),
        station_type=148,
        awareness_distance=AwarenessDistanceEnum.LESSTHAN50M
    ),
    situation=Situation(
        information_quality=7,
        event_type=EventType(
            cc_and_scc=TrafficConditionCauseCode(
                traffic_condition_1=26
            )
        )
    )
)
```

