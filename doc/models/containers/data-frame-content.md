
# Data Frame Content

## Data Type

`AdvisoryContent | WorkZoneContent | GenericSignContent | SpeedLimitContent | ExitServiceContent`

## Cases

| Type |
|  --- |
| [`AdvisoryContent`](../../../doc/models/advisory-content.md) |
| [`WorkZoneContent`](../../../doc/models/work-zone-content.md) |
| [`GenericSignContent`](../../../doc/models/generic-sign-content.md) |
| [`SpeedLimitContent`](../../../doc/models/speed-limit-content.md) |
| [`ExitServiceContent`](../../../doc/models/exit-service-content.md) |

## AdvisoryContent

### Initialization Code

#### Example

```python
value = AdvisoryContent(
    advisory=[
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        )
    ]
)
```

## WorkZoneContent

### Initialization Code

#### Example

```python
value = WorkZoneContent(
    work_zone=[
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        ),
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        )
    ]
)
```

## GenericSignContent

### Initialization Code

#### Example

```python
value = GenericSignContent(
    generic_sign=[
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        )
    ]
)
```

## SpeedLimitContent

### Initialization Code

#### Example

```python
value = SpeedLimitContent(
    speed_limit=[
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        ),
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        )
    ]
)
```

## ExitServiceContent

### Initialization Code

#### Example

```python
value = ExitServiceContent(
    exit_service=[
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        )
    ]
)
```

