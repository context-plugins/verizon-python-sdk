
# Offset

The sequence of node offsets then describes a path or polygon in the Lat-Long system.

## Structure

`Offset`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ll` | [`NodeListLL`](../../doc/models/node-list-ll.md) | Required | The NodeListLL data structure provides the sequence of signed offset node point values for determining the latitude and longitude. Each LL point is referred to as a node point. |

## Example

```python
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_list_ll import NodeListLL
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL
from verizon.models.offset import Offset

offset = Offset(
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
```

