
# Primary Place of Use

## Structure

`PrimaryPlaceOfUse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_name` | [`List[CustomerName]`](../../doc/models/customer-name.md) | Optional | **Constraints**: *Maximum Items*: `5` |
| `address` | [`List[Address]`](../../doc/models/address.md) | Optional | **Constraints**: *Maximum Items*: `5` |

## Example

```python
from verizon.models.address import Address
from verizon.models.customer_name import CustomerName
from verizon.models.primary_place_of_use import PrimaryPlaceOfUse

primary_place_of_use = PrimaryPlaceOfUse(
    customer_name=[
        CustomerName(
            first_name='firstName4',
            last_name='lastName4',
            title='title4',
            middle_name='middleName8',
            suffix='suffix0'
        )
    ],
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
        )
    ]
)
```

