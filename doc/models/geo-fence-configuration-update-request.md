
# Geo Fence Configuration Update Request

Request for /api/v1/application/configurations/geofence PUT endpoint. It requires at least one of vendorId, name, description, geofence, messages and isActive fields to be populated.

## Structure

`GeoFenceConfigurationUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the configuration.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `256`, *Pattern*: ``^[\w\+\-!()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |
| `description` | `str` | Optional | Description of the configuration.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2048`, *Pattern*: ``^[\w\+\-!()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |
| `geo_fence` | [`GeoFence`](../../doc/models/geo-fence.md) | Optional | The GeoJSON representation of geofence. Geofence supports the following geometry types: LineString, Polygon, MultiLineString, and MultiPolygon. The system only supports a single Feature in the FeatureCollection, so only one Line, Polygon, MultiLine or MultiPolygon can be defined within one Geofencing configuration. |
| `message_standard` | [`MessageStandardEnum`](../../doc/models/message-standard-enum.md) | Optional | Select which V2X messaging standard will be used for the message generation. The following options are supported:<br><br>- "etsi": The message will be generated using the ETSI (European) standard (e.g. DENM).<br>- "sae": The message will be generated using the SAE J2735 (North American) standard (e.g. RSA, TIM).<br>- if not sent while POST, defaults to "sae"<br>- mandatory to send "etsi" standard here, if ETSI messages are being sent in config<br><br>**Default**: `"sae"` |
| `messages` | List[[Message](../../doc/models/message.md) \| [Message1](../../doc/models/message-1.md) \| [Message2](../../doc/models/message-2.md) \| [Message3](../../doc/models/message-3.md)] \| None | Optional | List of predefined messages that belongs to the geofence. These are the messages that are sent out by the system when the Trigger Condition for the message is met.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `is_active` | `bool` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from verizon.models.distribution_schedule import DistributionSchedule
from verizon.models.distribution_types_enum import DistributionTypesEnum
from verizon.models.feature_item import FeatureItem
from verizon.models.generic_payload import GenericPayload
from verizon.models.geo_fence import GeoFence
from verizon.models.geo_fence_configuration_update_request import GeoFenceConfigurationUpdateRequest
from verizon.models.line_string import LineString
from verizon.models.message import Message
from verizon.models.message_standard_enum import MessageStandardEnum
from verizon.models.road_user_types_enum import RoadUserTypesEnum
from verizon.models.speed_item import SpeedItem
from verizon.models.speed_range import SpeedRange
from verizon.models.trigger_condition_enum import TriggerConditionEnum
from verizon.models.type_1_enum import Type1Enum
from verizon.models.type_2_enum import Type2Enum
from verizon.models.type_enum import TypeEnum

geo_fence_configuration_update_request = GeoFenceConfigurationUpdateRequest(
    name='name8',
    description='description8',
    geo_fence=GeoFence(
        mtype=TypeEnum.FEATURECOLLECTION,
        features=[
            FeatureItem(
                mtype=Type1Enum.FEATURE,
                geometry=LineString(
                    mtype=Type2Enum.LINESTRING,
                    coordinates=[
                        [
                            51.53,
                            51.54
                        ],
                        [
                            51.53,
                            51.54
                        ]
                    ]
                ),
                properties=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            )
        ]
    ),
    message_standard=MessageStandardEnum.SAE,
    messages=[
        Message(
            is_private=False,
            road_user_type=[
                RoadUserTypesEnum.VULNERABLEROADUSER
            ],
            trigger_conditions=[
                TriggerConditionEnum.CROSSING
            ],
            generic=GenericPayload(
                message_type='messageType4',
                message_format='messageFormat6',
                payload='payload0'
            ),
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
                DistributionTypesEnum.TARGETED
            ],
            distribution_schedule=DistributionSchedule(
                repeat_period=90,
                duration=88,
                start_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
            )
        )
    ]
)
```

