
# Content Friction Info

## Structure

`ContentFrictionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `friction_info` | [`FrictionInformation`](../../doc/models/friction-information.md) | Required | - |

## Example

```python
from verizon.models.content_friction_info import ContentFrictionInfo
from verizon.models.description_of_road_surface_portland_cement import DescriptionOfRoadSurfacePortlandCement
from verizon.models.friction_information import FrictionInformation
from verizon.models.portland_cement import PortlandCement
from verizon.models.type_6_enum import Type6Enum

content_friction_info = ContentFrictionInfo(
    friction_info=FrictionInformation(
        road_surface_description=DescriptionOfRoadSurfacePortlandCement(
            portland_cement=PortlandCement(
                mtype=Type6Enum.TRAVELED
            )
        )
    )
)
```

