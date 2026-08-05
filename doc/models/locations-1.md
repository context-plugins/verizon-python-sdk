
# Locations 1

## Structure

`Locations1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coordinates_list` | [`List[Coordinates]`](../../doc/models/coordinates.md) | Optional | - |
| `address_list` | [`List[AddressItem]`](../../doc/models/address-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.address_item import AddressItem
from verizon.models.coordinates import Coordinates
from verizon.models.locations_1 import Locations1

locations_1 = Locations1(
    coordinates_list=[
        Coordinates(
            latitude='latitude6',
            longitude='longitude4'
        ),
        Coordinates(
            latitude='latitude6',
            longitude='longitude4'
        )
    ],
    address_list=[
        AddressItem(
            address_line_1='addressLine10',
            address_line_2='addressLine28',
            city='city8',
            state='state4',
            country='country2'
        )
    ]
)
```

