
# Friction Information

## Structure

`FrictionInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `road_surface_description` | [DescriptionOfRoadSurface_PortlandCement](../../doc/models/description-of-road-surface-portland-cement.md) \| [DescriptionOfRoadSurface_AsphaltOrTar](../../doc/models/description-of-road-surface-asphalt-or-tar.md) \| [DescriptionOfRoadSurface_Gravel](../../doc/models/description-of-road-surface-gravel.md) \| [DescriptionOfRoadSurface_Grass](../../doc/models/description-of-road-surface-grass.md) \| [DescriptionOfRoadSurface_Cinders](../../doc/models/description-of-road-surface-cinders.md) \| [DescriptionOfRoadSurface_Rock](../../doc/models/description-of-road-surface-rock.md) \| [DescriptionOfRoadSurface_Ice](../../doc/models/description-of-road-surface-ice.md) \| [DescriptionOfRoadSurface_Snow](../../doc/models/description-of-road-surface-snow.md) | Required | Indicates the composition of the surface of the roadway for use in estimation of friction. |

## Example

```python
from verizon.models.description_of_road_surface_portland_cement import DescriptionOfRoadSurfacePortlandCement
from verizon.models.friction_information import FrictionInformation
from verizon.models.portland_cement import PortlandCement
from verizon.models.type_6_enum import Type6Enum

friction_information = FrictionInformation(
    road_surface_description=DescriptionOfRoadSurfacePortlandCement(
        portland_cement=PortlandCement(
            mtype=Type6Enum.TRAVELED
        )
    )
)
```

