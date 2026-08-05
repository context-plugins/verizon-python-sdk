
# M5 G Bidevice Detailsresponse

## Structure

`M5gBideviceDetailsresponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | - |
| `devices` | List[[5gbiaccountNameobject](../../doc/models/m5-g-biaccount-nameobject.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example

```python
from verizon.models.m_5g_bi_carrier_information import M5gBiCarrierInformation
from verizon.models.m_5g_biaccount_nameobject import M5gBiaccountNameobject
from verizon.models.m_5g_bidevice_detailsresponse import M5gBideviceDetailsresponse

m_5g_bidevice_detailsresponse = M5gBideviceDetailsresponse(
    has_more_data=False,
    devices=[
        M5gBiaccountNameobject(
            account_name='accountName0',
            billing_cycle_end_date='billingCycleEndDate6',
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
            created_at='createdAt0'
        )
    ]
)
```

