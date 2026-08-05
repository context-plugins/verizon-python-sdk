
# M5 G Biactivate Request

## Structure

`M5gBiactivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `device_list_with_service_address` | List[[5gbideviceIdarray](../../doc/models/m5-g-bidevice-idarray.md) \| [5gbiaddressAndcustomerinfo](../../doc/models/m5-g-biaddress-andcustomerinfo.md)] \| None | Optional | This is List of a container for any-of cases. |
| `sku_number` | `str` | Optional | - |
| `public_ip_restriction` | `str` | Optional | - |
| `carrier_name` | `str` | Optional | - |
| `mdn_zip_code` | `str` | Optional | - |

## Example

```python
from verizon.models.m_5g_biactivate_request import M5gBiactivateRequest
from verizon.models.m_5g_bidevice_id_1 import M5gBideviceId1
from verizon.models.m_5g_bidevice_idarray import M5gBideviceIdarray

m_5g_biactivate_request = M5gBiactivateRequest(
    account_name='0000123456-00001',
    service_plan='service plan name',
    device_list_with_service_address=[
        M5gBideviceIdarray(
            device_id=[
                M5gBideviceId1(
                    id='id0',
                    kind='kind8'
                )
            ]
        ),
        M5gBideviceIdarray(
            device_id=[
                M5gBideviceId1(
                    id='id0',
                    kind='kind8'
                )
            ]
        ),
        M5gBideviceIdarray(
            device_id=[
                M5gBideviceId1(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    sku_number='VZW Stock Keeping Unit number',
    public_ip_restriction='Unrestricted',
    carrier_name='Verizon Wireless',
    mdn_zip_code='5-digit zip code'
)
```

