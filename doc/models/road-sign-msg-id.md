
# Road Sign Msg Id

Message ID referencing a road sign location.

## Structure

`RoadSignMsgId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `road_sign_id` | [`RoadSignID`](../../doc/models/road-sign-id.md) | Required | It provide a precise location of one or more roadside signs. |

## Example

```python
from verizon.models.road_sign_id import RoadSignID
from verizon.models.road_sign_msg_id import RoadSignMsgId
from verizon.models.road_sign_position import RoadSignPosition

road_sign_msg_id = RoadSignMsgId(
    road_sign_id=RoadSignID(
        position=RoadSignPosition(
            lat=14,
            long=172
        ),
        view_angle='1101'
    )
)
```

