
# Limits

List of limitations. These limitations can be used for making the trigger condition more precise by defining speed and motion direction requirements to be met before the messages are sent out.

## Data Type

`SpeedItem | HeadingItem`

## Cases

| Type |
|  --- |
| [`SpeedItem`](../../../doc/models/speed-item.md) |
| [`HeadingItem`](../../../doc/models/heading-item.md) |

## SpeedItem

### Initialization Code

#### Example

```python
value = SpeedItem(
    speed=SpeedRange(
        min=64.76,
        max=138.18
    )
)
```

## HeadingItem

### Initialization Code

#### Example

```python
value = HeadingItem(
    heading=HeadingRange(
        min=70.7,
        max=144.12
    )
)
```

