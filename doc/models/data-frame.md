
# Data Frame

The data frame allows sending various advisory and road sign types of information to equipped devices.

## Structure

`DataFrame`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `do_not_use_1` | `int` | Optional | Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 31` |
| `frame_type` | [`FrameTypeEnum`](../../doc/models/frame-type-enum.md) | Required | The frameType data element provides the type of message to follow in the rest of the message frame structure. The following frame types are supported:<br><br>- unknown<br>- advisory<br>- roadSignage<br>- commercialSignage |
| `msg_id` | [FurtherInfoMsgId](../../doc/models/further-info-msg-id.md) \| [RoadSignMsgId](../../doc/models/road-sign-msg-id.md) | Required | This is a container for one-of cases. |
| `start_year` | `int` | Optional | The V2X year consists of integer values from zero to 4095 representing the year according to the Gregorian calendar date system. The value of zero shall represent an unknown value.<br><br>**Constraints**: `>= 0`, `<= 4095` |
| `start_time` | `int` | Required | Start time expresses the number of elapsed minutes of the current year in the time system being used (typically UTC time). The value 527040 shall be used for invalid.<br><br>**Constraints**: `>= 0`, `<= 527040` |
| `duration_time` | `int` | Required | The duration, in units of whole minutes, that a object persists for. A value of 32000 means that the object persists forever. The range 0..32000 provides for about 22.2 days of maximum duration.<br><br>**Constraints**: `>= 0`, `<= 32000` |
| `priority` | `int` | Required | The relative importance of the sign, on a scale from zero (least important) to seven (most important).<br><br>**Constraints**: `>= 0`, `<= 7` |
| `do_not_use_2` | `int` | Optional | Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 31` |
| `regions` | [`List[GeographicalPath]`](../../doc/models/geographical-path.md) | Required | The data frame is used to support the cross-cutting need in many V2X messages to describe arbitrary spatial areas (polygons, boundary lines, and other basic shapes) required by various message types in a small message size. This data frame can describe a complex path or region of arbitrary size using either one of the two supported node offset methods (XY offsets or LL offsets) or using simple geometric projections.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `16` |
| `do_not_use_3` | `int` | Optional | Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 31` |
| `do_not_use_4` | `int` | Optional | Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 31` |
| `content` | [AdvisoryContent](../../doc/models/advisory-content.md) \| [WorkZoneContent](../../doc/models/work-zone-content.md) \| [GenericSignContent](../../doc/models/generic-sign-content.md) \| [SpeedLimitContent](../../doc/models/speed-limit-content.md) \| [ExitServiceContent](../../doc/models/exit-service-content.md) | Required | This is a container for one-of cases. |
| `content_new` | [Content_frictionInfo](../../doc/models/content-friction-info.md) \| None | Optional | This is a container for one-of cases. |

## Example

```python
from verizon.models.advisory_content import AdvisoryContent
from verizon.models.data_frame import DataFrame
from verizon.models.frame_type_enum import FrameTypeEnum
from verizon.models.further_info_msg_id import FurtherInfoMsgId
from verizon.models.geographical_path import GeographicalPath
from verizon.models.geographical_path_description import GeographicalPathDescription
from verizon.models.itis_item_content import ITISItemContent
from verizon.models.itis_item_wrapper import ITISItemWrapper
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_list_ll import NodeListLL
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL
from verizon.models.offset import Offset
from verizon.models.offset_system import OffsetSystem

data_frame = DataFrame(
    frame_type=FrameTypeEnum.UNKNOWN,
    msg_id=FurtherInfoMsgId(
        further_info_id='1101'
    ),
    start_time=146,
    duration_time=84,
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
    start_year=52,
    do_not_use_2=0,
    do_not_use_3=0,
    do_not_use_4=0
)
```

