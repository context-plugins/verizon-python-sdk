
# Locations

Location details.

## Structure

`Locations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_list` | [`List[AddressItem]`](../../doc/models/address-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.address_item import AddressItem
from verizon.models.locations import Locations

locations = Locations(
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

