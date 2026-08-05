
# Message Base

## Structure

`MessageBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_private` | `bool` | Required | Defines whether the message is private or public.<br>Private messages are published under the Vendor ID defined in the configuration and only visible to devices of selected vendors.<br>Public messages are published under the Public vendor and are visible to all the users. |
| `road_user_type` | [`List[RoadUserTypesEnum]`](../../doc/models/road-user-types-enum.md) | Required | Type of the Road User.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `trigger_conditions` | [`List[TriggerConditionEnum]`](../../doc/models/trigger-condition-enum.md) | Optional | Trigger conditions that define on which road user action the message will be sent. If multiple Trigger Conditions are defined any of them will trigger the message.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `3` |
| `limits` | List[[SpeedItem](../../doc/models/speed-item.md) \| [HeadingItem](../../doc/models/heading-item.md)] \| None | Optional | List of limitations. These limitations can be used for making the trigger condition more precise by defining speed and motion direction requirements to be met before the messages are sent out.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `distribution_type` | [`List[DistributionTypesEnum]`](../../doc/models/distribution-types-enum.md) | Optional | Type of the distribution.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2` |
| `distribution_schedule` | [`DistributionSchedule`](../../doc/models/distribution-schedule.md) | Optional | The distribution schedule parameters for broadcast messages. |

## Example

```python
import dateutil.parser

from verizon.models.distribution_schedule import DistributionSchedule
from verizon.models.distribution_types_enum import DistributionTypesEnum
from verizon.models.message_base import MessageBase
from verizon.models.road_user_types_enum import RoadUserTypesEnum
from verizon.models.speed_item import SpeedItem
from verizon.models.speed_range import SpeedRange
from verizon.models.trigger_condition_enum import TriggerConditionEnum

message_base = MessageBase(
    is_private=False,
    road_user_type=[
        RoadUserTypesEnum.VULNERABLEROADUSER
    ],
    trigger_conditions=[
        TriggerConditionEnum.LEAVE
    ],
    limits=[
        SpeedItem(
            speed=SpeedRange(
                min=64.76,
                max=138.18
            )
        )
    ],
    distribution_type=[
        DistributionTypesEnum.BROADCAST,
        DistributionTypesEnum.TARGETED,
        DistributionTypesEnum.BROADCAST
    ],
    distribution_schedule=DistributionSchedule(
        repeat_period=90,
        duration=88,
        start_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

