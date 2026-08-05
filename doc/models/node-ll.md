
# Node LL

The NodeLL data frame presents a structure to hold data for a signal node point in a lane. Each selected node has a complete lat-long representation.

## Structure

`NodeLL`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delta` | [`NodeOffsetPointLL`](../../doc/models/node-offset-point-ll.md) | Required | The NodeOffsetPointLL data frame presents a structure to hold 64 bits sized data frames for a single node geometry path. Nodes are described in terms of latitude and longitude. |

## Example

```python
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL

node_ll = NodeLL(
    delta=NodeOffsetPointLL(
        node_lat_lon=NodeLLmD64b(
            lon=40,
            lat=10
        )
    )
)
```

