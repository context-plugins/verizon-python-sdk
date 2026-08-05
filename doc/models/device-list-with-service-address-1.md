
# Device List with Service Address 1

## Structure

`DeviceListWithServiceAddress1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | List[[5gbideviceId1](../../doc/models/m5-g-bidevice-id-1.md)] \| None | Optional | This is List of a container for any-of cases. |
| `primary_placeofuse` | [`M5gBiprimaryPlaceofuse`](../../doc/models/m5-g-biprimary-placeofuse.md) | Optional | - |

## Example

```python
from verizon.models.device_list_with_service_address_1 import DeviceListWithServiceAddress1
from verizon.models.m_5g_bi_address import M5gBiAddress
from verizon.models.m_5g_bi_customer_name import M5gBiCustomerName
from verizon.models.m_5g_bidevice_id_1 import M5gBideviceId1
from verizon.models.m_5g_biprimary_placeofuse import M5gBiprimaryPlaceofuse

device_list_with_service_address_1 = DeviceListWithServiceAddress1(
    device_id=[
        M5gBideviceId1(
            id='id0',
            kind='kind8'
        ),
        M5gBideviceId1(
            id='id0',
            kind='kind8'
        ),
        M5gBideviceId1(
            id='id0',
            kind='kind8'
        )
    ],
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
```

