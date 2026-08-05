
# Data Frame Msg Id

## Data Type

`FurtherInfoMsgId | RoadSignMsgId`

## Cases

| Type |
|  --- |
| [`FurtherInfoMsgId`](../../../doc/models/further-info-msg-id.md) |
| [`RoadSignMsgId`](../../../doc/models/road-sign-msg-id.md) |

## FurtherInfoMsgId

### Initialization Code

#### Example

```python
value = FurtherInfoMsgId(
    further_info_id='1101'
)
```

## RoadSignMsgId

### Initialization Code

#### Example

```python
value = RoadSignMsgId(
    road_sign_id=RoadSignID(
        position=RoadSignPosition(
            lat=14,
            long=172
        ),
        view_angle='1101'
    )
)
```

