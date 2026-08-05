
# Message 3

## Structure

`Message3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_private` | `bool` | Required | Defines whether the message is private or public.<br>Private messages are published under the Vendor ID defined in the configuration and only visible to devices of selected vendors.<br>Public messages are published under the Public vendor and are visible to all the users. |
| `road_user_type` | [`List[RoadUserTypesEnum]`](../../doc/models/road-user-types-enum.md) | Required | Type of the Road User.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `trigger_conditions` | [`List[TriggerConditionEnum]`](../../doc/models/trigger-condition-enum.md) | Required | Trigger conditions that define on which road user action the message will be sent. If multiple Trigger Conditions are defined any of them will trigger the message.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `3` |
| `limits` | List[[SpeedItem](../../doc/models/speed-item.md) \| [HeadingItem](../../doc/models/heading-item.md)] \| None | Optional | List of limitations. These limitations can be used for making the trigger condition more precise by defining speed and motion direction requirements to be met before the messages are sent out.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `distribution_type` | [`List[DistributionTypesEnum]`](../../doc/models/distribution-types-enum.md) | Optional | Type of the distribution.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `distribution_schedule` | [`DistributionSchedule`](../../doc/models/distribution-schedule.md) | Optional | The distribution schedule parameters for broadcast messages. |
| `etsi_alert` | [`EtsiAlertPayload`](../../doc/models/etsi-alert-payload.md) | Required | DENM (Decentralized Environmental Notification Message) payload as defined in ETSI. |

## Example

```python
import dateutil.parser

from verizon.models.action_id import ActionId
from verizon.models.altitude import Altitude
from verizon.models.altitude_confidence_enum import AltitudeConfidenceEnum
from verizon.models.awareness_distance_enum import AwarenessDistanceEnum
from verizon.models.denm_payload import DenmPayload
from verizon.models.distribution_schedule import DistributionSchedule
from verizon.models.distribution_types_enum import DistributionTypesEnum
from verizon.models.etsi_alert_payload import EtsiAlertPayload
from verizon.models.event_position import EventPosition
from verizon.models.event_type import EventType
from verizon.models.header import Header
from verizon.models.management import Management
from verizon.models.message_3 import Message3
from verizon.models.message_id_enum import MessageIdEnum
from verizon.models.pos_confidence_ellipse import PosConfidenceEllipse
from verizon.models.protocol_version_enum import ProtocolVersionEnum
from verizon.models.road_user_types_enum import RoadUserTypesEnum
from verizon.models.situation import Situation
from verizon.models.speed_item import SpeedItem
from verizon.models.speed_range import SpeedRange
from verizon.models.traffic_condition_cause_code import TrafficConditionCauseCode
from verizon.models.trigger_condition_enum import TriggerConditionEnum

message_3 = Message3(
    is_private=False,
    road_user_type=[
        RoadUserTypesEnum.VULNERABLEROADUSER,
        RoadUserTypesEnum.VEHICLE,
        RoadUserTypesEnum.VULNERABLEROADUSER
    ],
    trigger_conditions=[
        TriggerConditionEnum.CROSSING,
        TriggerConditionEnum.ENTER
    ],
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
    ),
    limits=[
        SpeedItem(
            speed=SpeedRange(
                min=64.76,
                max=138.18
            )
        ),
        SpeedItem(
            speed=SpeedRange(
                min=64.76,
                max=138.18
            )
        )
    ],
    distribution_type=[
        DistributionTypesEnum.BROADCAST
    ],
    distribution_schedule=DistributionSchedule(
        repeat_period=90,
        duration=88,
        start_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

