
# Device List with Service Address

## Structure

`DeviceListWithServiceAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`List[M5gBideviceId1]`](../../doc/models/m5-g-bidevice-id-1.md) | Optional | - |
| `primary_placeofuse` | [`M5gBiaddressAndcustomerinfo`](../../doc/models/m5-g-biaddress-andcustomerinfo.md) | Optional | - |

## Example

```python
from verizon.models.device_list_with_service_address import DeviceListWithServiceAddress
from verizon.models.m_5g_bi_address import M5gBiAddress
from verizon.models.m_5g_bi_customer_name import M5gBiCustomerName
from verizon.models.m_5g_biaddress_andcustomerinfo import M5gBiaddressAndcustomerinfo
from verizon.models.m_5g_bidevice_id_1 import M5gBideviceId1
from verizon.models.m_5g_biprimary_placeofuse import M5gBiprimaryPlaceofuse

device_list_with_service_address = DeviceListWithServiceAddress(
    device_id=[
        M5gBideviceId1(
            id='id0',
            kind='kind8'
        )
    ],
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

