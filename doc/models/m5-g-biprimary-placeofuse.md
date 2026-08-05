
# M5 G Biprimary Placeofuse

## Structure

`M5gBiprimaryPlaceofuse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`M5gBiAddress`](../../doc/models/m5-g-bi-address.md) | Optional | - |
| `customer_name` | [`M5gBiCustomerName`](../../doc/models/m5-g-bi-customer-name.md) | Optional | - |

## Example

```python
from verizon.models.m_5g_bi_address import M5gBiAddress
from verizon.models.m_5g_bi_customer_name import M5gBiCustomerName
from verizon.models.m_5g_biprimary_placeofuse import M5gBiprimaryPlaceofuse

m_5g_biprimary_placeofuse = M5gBiprimaryPlaceofuse(
    address=M5gBiAddress(
        address_line_1='addressLine18',
        city='city6',
        state='state2',
        zip='zip0',
        zip_4='zip+48'
    ),
    customer_name=M5gBiCustomerName(
        first_name='firstName4',
        last_name='lastName4',
        middle_name='middleName8',
        title='title4',
        suffex='suffex4'
    )
)
```

