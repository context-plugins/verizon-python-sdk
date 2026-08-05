
# Message 2

## Structure

`Message2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_private` | `bool` | Required | Defines whether the message is private or public.<br>Private messages are published under the Vendor ID defined in the configuration and only visible to devices of selected vendors.<br>Public messages are published under the Public vendor and are visible to all the users. |
| `road_user_type` | [`List[RoadUserTypesEnum]`](../../doc/models/road-user-types-enum.md) | Required | Type of the Road User.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `trigger_conditions` | [`List[TriggerConditionEnum]`](../../doc/models/trigger-condition-enum.md) | Required | Trigger conditions that define on which road user action the message will be sent. If multiple Trigger Conditions are defined any of them will trigger the message.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `3` |
| `limits` | List[[SpeedItem](../../doc/models/speed-item.md) \| [HeadingItem](../../doc/models/heading-item.md)] \| None | Optional | List of limitations. These limitations can be used for making the trigger condition more precise by defining speed and motion direction requirements to be met before the messages are sent out.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `distribution_type` | [`List[DistributionTypesEnum]`](../../doc/models/distribution-types-enum.md) | Optional | Type of the distribution.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `distribution_schedule` | [`DistributionSchedule`](../../doc/models/distribution-schedule.md) | Optional | The distribution schedule parameters for broadcast messages. |
| `sae_info` | [`SaeInfoPayload`](../../doc/models/sae-info-payload.md) | Required | Traveler Information Message (TIM) payload as defined in SAE J2735. |

## Example

```python
import dateutil.parser

from verizon.models.advisory_content import AdvisoryContent
from verizon.models.data_frame import DataFrame
from verizon.models.distribution_schedule import DistributionSchedule
from verizon.models.distribution_types_enum import DistributionTypesEnum
from verizon.models.frame_type_enum import FrameTypeEnum
from verizon.models.further_info_msg_id import FurtherInfoMsgId
from verizon.models.geographical_path import GeographicalPath
from verizon.models.geographical_path_description import GeographicalPathDescription
from verizon.models.itis_item_content import ITISItemContent
from verizon.models.itis_item_wrapper import ITISItemWrapper
from verizon.models.message_2 import Message2
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_list_ll import NodeListLL
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL
from verizon.models.offset import Offset
from verizon.models.offset_system import OffsetSystem
from verizon.models.road_user_types_enum import RoadUserTypesEnum
from verizon.models.sae_info_payload import SaeInfoPayload
from verizon.models.speed_item import SpeedItem
from verizon.models.speed_range import SpeedRange
from verizon.models.trigger_condition_enum import TriggerConditionEnum

message_2 = Message2(
    is_private=False,
    road_user_type=[
        RoadUserTypesEnum.VULNERABLEROADUSER,
        RoadUserTypesEnum.VEHICLE
    ],
    trigger_conditions=[
        TriggerConditionEnum.CROSSING,
        TriggerConditionEnum.ENTER,
        TriggerConditionEnum.LEAVE
    ],
    sae_info=SaeInfoPayload(
        data_frames=[
            DataFrame(
                frame_type=FrameTypeEnum.UNKNOWN,
                msg_id=FurtherInfoMsgId(
                    further_info_id='1101'
                ),
                start_time=186,
                duration_time=44,
                priority=7,
                regions=[
                    GeographicalPath(
                        description=GeographicalPathDescription(
                            path=OffsetSystem(
                                offset=Offset(
                                    ll=NodeListLL(
                                        nodes=[
                                            NodeLL(
                                                delta=NodeOffsetPointLL(
                                                    node_lat_lon=NodeLLmD64b(
                                                        lon=40,
                                                        lat=10
                                                    )
                                                )
                                            ),
                                            NodeLL(
                                                delta=NodeOffsetPointLL(
                                                    node_lat_lon=NodeLLmD64b(
                                                        lon=40,
                                                        lat=10
                                                    )
                                                )
                                            )
                                        ]
                                    )
                                )
                            )
                        ),
                        direction='1101'
                    )
                ],
                content=AdvisoryContent(
                    advisory=[
                        ITISItemWrapper(
                            item=ITISItemContent(
                                itis=10
                            )
                        )
                    ]
                ),
                do_not_use_1=0,
                start_year=12,
                do_not_use_2=0,
                do_not_use_3=0,
                do_not_use_4=0
            )
        ],
        msg_cnt=0,
        time_stamp=5,
        packet_id='B343B343B343B343A5',
        url_b='http://example.com'
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
        ),
        SpeedItem(
            speed=SpeedRange(
                min=64.76,
                max=138.18
            )
        )
    ],
    distribution_type=[
        DistributionTypesEnum.BROADCAST,
        DistributionTypesEnum.TARGETED
    ],
    distribution_schedule=DistributionSchedule(
        repeat_period=90,
        duration=88,
        start_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

