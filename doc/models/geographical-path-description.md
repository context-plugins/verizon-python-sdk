
# Geographical Path Description

This data frame can describe a complex path of arbitrary size using node offset method (LL offsets).

## Structure

`GeographicalPathDescription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `path` | [`OffsetSystem`](../../doc/models/offset-system.md) | Required | The OffsetSystem data frame selects a sequence of node offsets described in the Lat-Long offset method. |

## Example

```python
from verizon.models.geographical_path_description import GeographicalPathDescription
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_list_ll import NodeListLL
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL
from verizon.models.offset import Offset
from verizon.models.offset_system import OffsetSystem

geographical_path_description = GeographicalPathDescription(
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
                    )
                ]
            )
        )
    )
)
```

