
# Region Intersection Pair

Specific region and intersection identification pair

## Structure

`RegionIntersectionPair`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region_id` | `int` | Optional | The region identifier code (0-65535)<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 65535` |
| `intersection_id` | `int` | Required | The intersection identifier code (0-65535)<br><br>**Constraints**: `>= 0`, `<= 65535` |

## Example

```python
from verizon.models.region_intersection_pair import RegionIntersectionPair

region_intersection_pair = RegionIntersectionPair(
    intersection_id=5233,
    region_id=100
)
```

