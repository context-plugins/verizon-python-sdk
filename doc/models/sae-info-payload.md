
# Sae Info Payload

Traveler Information Message (TIM) payload as defined in SAE J2735.

## Structure

`SaeInfoPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msg_cnt` | `int` | Optional | It is used to provide a sequence number within a stream of messages with the same DSRCmsgID (here RoadSideAlert) and from the same sender.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 127` |
| `time_stamp` | `int` | Optional | The number of elapsed minutes of the current year in the time system being used (typically UTC time).<br>-- the value 527040 shall be used for invalid<br><br>**Constraints**: `>= 0`, `<= 527040` |
| `packet_id` | `str` | Optional | Provides a relatively unique value which can be used to connect to (link to) other supporting messages in other formats.<br><br>The value is described as a 18-character hexadecimal string.<br><br>**Constraints**: *Pattern*: `^[0-9A-Fa-f]{18}$` |
| `url_b` | `str` | Optional | A valid internet style URI/URL in the form of a text string which will form the base of a compound string which, when<br>combined with the URL-short data element, will link to the designated resource.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `45` |
| `data_frames` | [`List[DataFrame]`](../../doc/models/data-frame.md) | Required | List of data frames.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `8` |

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
from verizon.models.sae_info_payload import SaeInfoPayload

sae_info_payload = SaeInfoPayload(
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
)
```

