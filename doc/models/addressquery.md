
# Addressquery

## Structure

`Addressquery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`List[Address]`](../../doc/models/address.md) | Optional | **Constraints**: *Maximum Items*: `5` |

## Example

```python
from verizon.models.address import Address
from verizon.models.addressquery import Addressquery

addressquery = Addressquery(
    address=[
        Address(
            address_line_1='addressLine18',
            city='city6',
            state='state2',
            zip='zip0',
            country='country0',
            address_line_2='addressLine26',
            zip_4='zip40',
            phone='phone4',
            phone_type='phoneType0',
            email_address='emailAddress6'
        ),
        Address(
            address_line_1='addressLine18',
            city='city6',
            state='state2',
            zip='zip0',
            country='country0',
            address_line_2='addressLine26',
            zip_4='zip40',
            phone='phone4',
            phone_type='phoneType0',
            email_address='emailAddress6'
        ),
        Address(
            address_line_1='addressLine18',
            city='city6',
            state='state2',
            zip='zip0',
            country='country0',
            address_line_2='addressLine26',
            zip_4='zip40',
            phone='phone4',
            phone_type='phoneType0',
            email_address='emailAddress6'
        )
    ]
)
```

