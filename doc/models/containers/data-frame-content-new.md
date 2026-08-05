
# Data Frame Content New

## Data Type

`ContentFrictionInfo`

## Cases

| Type |
|  --- |
| [`ContentFrictionInfo`](../../../doc/models/content-friction-info.md) |

## ContentFrictionInfo

### Initialization Code

#### Example

```python
value = ContentFrictionInfo(
    friction_info=FrictionInformation(
        road_surface_description=DescriptionOfRoadSurfacePortlandCement(
            portland_cement=PortlandCement(
                mtype=Type6Enum.TRAVELED
            )
        )
    )
)
```

