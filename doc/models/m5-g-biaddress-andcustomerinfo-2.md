
# M5 G Biaddress Andcustomerinfo 2

## Structure

`M5gBiaddressAndcustomerinfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `primary_placeofuse` | [`M5gBiaddressAndcustomerinfo`](../../doc/models/m5-g-biaddress-andcustomerinfo.md) | Optional | - |

## Example

```python
from verizon.models.m_5g_bi_address import M5gBiAddress
from verizon.models.m_5g_bi_customer_name import M5gBiCustomerName
from verizon.models.m_5g_biaddress_andcustomerinfo import M5gBiaddressAndcustomerinfo
from verizon.models.m_5g_biaddress_andcustomerinfo_2 import M5gBiaddressAndcustomerinfo2
from verizon.models.m_5g_biprimary_placeofuse import M5gBiprimaryPlaceofuse

m_5g_biaddress_andcustomerinfo_2 = M5gBiaddressAndcustomerinfo2(
    primary_placeofuse=M5gBiaddressAndcustomerinfo(
        primary_placeofuse=M5gBiprimaryPlaceofuse(
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
    )
)
```

