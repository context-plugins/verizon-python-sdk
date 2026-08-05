
# Etsi Alert Message

Decentralized Environmental Notification Message (DENM) message and its mandatory fields. It is used in order to alert road users of a detected event using ITS communication technologies.

## Structure

`EtsiAlertMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `etsi_alert` | [`EtsiAlertPayload`](../../doc/models/etsi-alert-payload.md) | Required | DENM (Decentralized Environmental Notification Message) payload as defined in ETSI. |

## Example

```python
from verizon.models.action_id import ActionId
from verizon.models.altitude import Altitude
from verizon.models.altitude_confidence_enum import AltitudeConfidenceEnum
from verizon.models.awareness_distance_enum import AwarenessDistanceEnum
from verizon.models.denm_payload import DenmPayload
from verizon.models.etsi_alert_message import EtsiAlertMessage
from verizon.models.etsi_alert_payload import EtsiAlertPayload
from verizon.models.event_position import EventPosition
from verizon.models.event_type import EventType
from verizon.models.header import Header
from verizon.models.management import Management
from verizon.models.message_id_enum import MessageIdEnum
from verizon.models.pos_confidence_ellipse import PosConfidenceEllipse
from verizon.models.protocol_version_enum import ProtocolVersionEnum
from verizon.models.situation import Situation
from verizon.models.traffic_condition_cause_code import TrafficConditionCauseCode

etsi_alert_message = EtsiAlertMessage(
    etsi_alert=EtsiAlertPayload(
        header=Header(
            protocol_version=ProtocolVersionEnum.ENUM_2,
            message_id=MessageIdEnum.ENUM_1,
            station_id=12345
        ),
        denm=DenmPayload(
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
    )
)
```

