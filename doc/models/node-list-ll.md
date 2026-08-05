
# Node List LL

The NodeListLL data structure provides the sequence of signed offset node point values for determining the latitude and longitude. Each LL point is referred to as a node point.

## Structure

`NodeListLL`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `nodes` | [`List[NodeLL]`](../../doc/models/node-ll.md) | Required | The NodeSetLL data frame consists of a list of NodeLL entries using LL offsets.<br><br>**Constraints**: *Minimum Items*: `2`, *Maximum Items*: `63` |

## Example

```python
from verizon.models.node_l_lm_d_64_b import NodeLLmD64b
from verizon.models.node_list_ll import NodeListLL
from verizon.models.node_ll import NodeLL
from verizon.models.node_offset_point_ll import NodeOffsetPointLL

node_list_ll = NodeListLL(
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
```

