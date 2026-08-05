
# Etsi Alert Payload

DENM (Decentralized Environmental Notification Message) payload as defined in ETSI.

## Structure

`EtsiAlertPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `header` | [`Header`](../../doc/models/header.md) | Required | The header of the DENM PDU. |
| `denm` | [`DenmPayload`](../../doc/models/denm-payload.md) | Required | The payload of the DENM PDU. |

## Example

```python
from verizon.models.action_id import ActionId
from verizon.models.altitude import Altitude
from verizon.models.altitude_confidence_enum import AltitudeConfidenceEnum
from verizon.models.awareness_distance_enum import AwarenessDistanceEnum
from verizon.models.denm_payload import DenmPayload
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

etsi_alert_payload = EtsiAlertPayload(
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
```

