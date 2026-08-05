
# M5 G Biaccount Nameobject

## Structure

`M5gBiaccountNameobject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `billing_cycle_end_date` | `str` | Optional | - |
| `carrier_information` | [`List[M5gBiCarrierInformation]`](../../doc/models/m5-g-bi-carrier-information.md) | Optional | - |
| `connected` | `bool` | Optional | - |
| `created_at` | `str` | Optional | - |
| `custom_fields` | List[[5gbikeyValue1](../../doc/models/m5-g-bikey-value-1.md)] \| None | Optional | This is List of a container for any-of cases. |
| `device_ids` | List[[5gbideviceId1](../../doc/models/m5-g-bidevice-id-1.md)] \| None | Optional | This is List of a container for any-of cases. |
| `extended_attributes` | List[[5gbiattribute1](../../doc/models/m5-g-biattribute-1.md) \| [5gbiattribute2](../../doc/models/m5-g-biattribute-2.md)] \| None | Optional | This is List of a container for any-of cases. |
| `group_names` | [`List[GroupName]`](../../doc/models/group-name.md) | Optional | - |
| `ipaddress` | `str` | Optional | - |
| `last_activation_by` | `str` | Optional | - |
| `last_activation_date` | `str` | Optional | - |

## Example

```python
from verizon.models.m_5g_bi_carrier_information import M5gBiCarrierInformation
from verizon.models.m_5g_biaccount_nameobject import M5gBiaccountNameobject

m_5g_biaccount_nameobject = M5gBiaccountNameobject(
    account_name='0000123456-00001',
    billing_cycle_end_date='2022-11-10T00:00:00.000Z',
    carrier_information=[
        M5gBiCarrierInformation(
            carrier_name='carrierName4'
        ),
        M5gBiCarrierInformation(
            carrier_name='carrierName4'
        ),
        M5gBiCarrierInformation(
            carrier_name='carrierName4'
        )
    ],
    connected=False,
    created_at='2022-10-20T18:23:41.000Z',
    ipaddress='0.0.0.0',
    last_activation_by='User Name',
    last_activation_date='2022-11-02 T21:36:18Z'
)
```

