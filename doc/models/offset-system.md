
# Offset System

The OffsetSystem data frame selects a sequence of node offsets described in the Lat-Long offset method.

## Structure

`OffsetSystem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | [`Offset`](../../doc/models/offset.md) | Required | The sequence of node offsets then describes a path or polygon in the Lat-Long system. |

## Example

```python
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_list_ll import NodeListLL
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL
from verizon.models.offset import Offset
from verizon.models.offset_system import OffsetSystem

offset_system = OffsetSystem(
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
```

