
# Geographical Path

The data frame is used to support the cross-cutting need in many V2X messages to describe arbitrary spatial areas (polygons, boundary lines, and other basic shapes) required by various message types in a small message size.

## Structure

`GeographicalPath`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | [`GeographicalPathDescription`](../../doc/models/geographical-path-description.md) | Optional | This data frame can describe a complex path of arbitrary size using node offset method (LL offsets). |
| `direction` | `str` | Optional | OctetStrings are described as hexadecimal strings, where each octet is represented by two hexadecimal characters.<br><br>**Constraints**: *Pattern*: `^[0-9A-Fa-f]{4}$` |

## Example

```python
from verizon.models.geographical_path import GeographicalPath
from verizon.models.geographical_path_description import GeographicalPathDescription
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_list_ll import NodeListLL
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL
from verizon.models.offset import Offset
from verizon.models.offset_system import OffsetSystem

geographical_path = GeographicalPath(
    description=GeographicalPathDescription(
        path=OffsetSystem(
            offset=Offset(
                ll=NodeListLL(
                    nodes=[
                        NodeLL(
                            delta=NodeOffsetPointLL(
                                node_lat_lon=NodeLLmD64b(
                                    lon=40,
                                    lat=10
                                )
                            )
                        ),
                        NodeLL(
                            delta=NodeOffsetPointLL(
                                node_lat_lon=NodeLLmD64b(
                                    lon=40,
                                    lat=10
                                )
                            )
                        )
                    ]
                )
            )
        )
    ),
    direction='1101'
)
```

