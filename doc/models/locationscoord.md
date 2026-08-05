
# Locationscoord

Location coordinates.

## Structure

`Locationscoord`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coordinates_list` | [`List[Coordinates]`](../../doc/models/coordinates.md) | Optional | - |

## Example

```python
from verizon.models.coordinates import Coordinates
from verizon.models.locationscoord import Locationscoord

locationscoord = Locationscoord(
    coordinates_list=[
        Coordinates(
            latitude='latitude6',
            longitude='longitude4'
        )
    ]
)
```

