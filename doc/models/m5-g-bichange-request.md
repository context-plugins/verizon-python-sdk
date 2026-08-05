
# M5 G Bichange Request

## Structure

`M5gBichangeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `device_list_with_service_address` | List[[5gbideviceIdarray2](../../doc/models/m5-g-bidevice-idarray-2.md) \| [5gbiaddressAndcustomerinfo2](../../doc/models/m5-g-biaddress-andcustomerinfo-2.md)] \| None | Optional | This is List of a container for any-of cases. |
| `current_service_plan` | `str` | Optional | - |

## Example

```python
from verizon.models.m_5g_bichange_request import M5gBichangeRequest
from verizon.models.m_5g_bidevice_id_1 import M5gBideviceId1
from verizon.models.m_5g_bidevice_idarray_2 import M5gBideviceIdarray2

m_5g_bichange_request = M5gBichangeRequest(
    account_name='0000123456-00001',
    service_plan='5G BI service plan name being changed to',
    device_list_with_service_address=[
        M5gBideviceIdarray2(
            device_id=[
                M5gBideviceId1(
                    id='id0',
                    kind='kind8'
                ),
                M5gBideviceId1(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    current_service_plan='Optional name of the plan being changed from'
)
```

