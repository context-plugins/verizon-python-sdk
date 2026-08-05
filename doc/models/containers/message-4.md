
# Message 4

## Data Type

`Message | Message1 | Message2 | Message3`

## Cases

| Type |
|  --- |
| [`Message`](../../../doc/models/message.md) |
| [`Message1`](../../../doc/models/message-1.md) |
| [`Message2`](../../../doc/models/message-2.md) |
| [`Message3`](../../../doc/models/message-3.md) |

## Message

### Initialization Code

#### Example

```python
value = Message(
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
    )
)
```

## Message1

### Initialization Code

#### Example

```python
value = Message1(
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
    sae_alert=SaeAlertPayload(
        type_event=160,
        msg_cnt=0
    )
)
```

## Message2

### Initialization Code

#### Example

```python
value = Message2(
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

## Message3

### Initialization Code

#### Example

```python
value = Message3(
    is_private=False,
    road_user_type=[
        RoadUserTypesEnum.VULNERABLEROADUSER,
        RoadUserTypesEnum.VEHICLE
    ],
    trigger_conditions=[
        TriggerConditionEnum.LEAVE,
        TriggerConditionEnum.INSIDE
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
                    altitude=Altitude()
                ),
                station_type=148
            )
        )
    )
)
```

