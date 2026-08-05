
# Description of Road Surface Asphalt or Tar

## Structure

`DescriptionOfRoadSurfaceAsphaltOrTar`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asphalt_or_tar` | [`AsphaltOrTar`](../../doc/models/asphalt-or-tar.md) | Required | Indicates the surface of the roadway is asphalt or tar. |

## Example

```python
from verizon.models.asphalt_or_tar import AsphaltOrTar
from verizon.models.description_of_road_surface_asphalt_or_tar import DescriptionOfRoadSurfaceAsphaltOrTar
from verizon.models.type_7_enum import Type7Enum

description_of_road_surface_asphalt_or_tar = DescriptionOfRoadSurfaceAsphaltOrTar(
    asphalt_or_tar=AsphaltOrTar(
        mtype=Type7Enum.NEWSHARP
    )
)
```

