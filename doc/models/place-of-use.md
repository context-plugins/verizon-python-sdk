
# Place of Use

The customer name and the address of the device's primary place of use. Leave these fields empty to use the account profile address as the primary place of use. These values will be applied to all devices in the request.If the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also be used to derive the MDN for the device.

## Structure

`PlaceOfUse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address`](../../doc/models/address.md) | Required | The customer address for the line's primary place of use, for line usage taxation. |
| `customer_name` | [`CustomerName`](../../doc/models/customer-name.md) | Required | The customer name to be used for line usage taxation. |

## Example

```python
from verizon.models.address import Address
from verizon.models.customer_name import CustomerName
from verizon.models.place_of_use import PlaceOfUse

place_of_use = PlaceOfUse(
    address=Address(
        address_line_1='1600 Pennsylvania Ave NW',
        city='Washington',
        state='DC',
        zip='20500',
        country='USA',
        address_line_2='addressLine26',
        zip_4='zip40',
        phone='phone4',
        phone_type='phoneType0',
        email_address='emailAddress6'
    ),
    customer_name=CustomerName(
        first_name='Zaffod',
        last_name='Beeblebrox',
        title='President',
        middle_name='middleName8',
        suffix='suffix0'
    )
)
```

