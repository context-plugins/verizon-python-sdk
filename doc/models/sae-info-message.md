
# Sae Info Message

Traveler Information Message (TIM) message and its mandatory fields. The traveler information message is used to send various types of information (advisory and road sign types) to equipped devices.

## Structure

`SaeInfoMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sae_info` | [`SaeInfoPayload`](../../doc/models/sae-info-payload.md) | Required | Traveler Information Message (TIM) payload as defined in SAE J2735. |

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
from verizon.models.sae_info_message import SaeInfoMessage
from verizon.models.sae_info_payload import SaeInfoPayload

sae_info_message = SaeInfoMessage(
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
    )
)
```

