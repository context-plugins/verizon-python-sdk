
# ESIM Profile Request

## Structure

`ESIMProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[ESIMDeviceList]`](../../doc/models/esim-device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `carrier_name` | `str` | Optional | - |
| `account_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `mdn_zip_code` | `str` | Optional | - |

## Example

```python
from verizon.models.esim_device_id import ESIMDeviceId
from verizon.models.esim_device_list import ESIMDeviceList
from verizon.models.esim_profile_request import ESIMProfileRequest

e_sim_profile_request = ESIMProfileRequest(
    devices=[
        ESIMDeviceList(
            device_ids=[
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                )
            ]
        ),
        ESIMDeviceList(
            device_ids=[
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                )
            ]
        )
    ],
    carrier_name='name of the mobile service provider',
    account_name='0000123456-00001',
    service_plan='The service plan name (The value used for Consumer eSIM for Enterprise will be HybridESim)',
    mdn_zip_code='five digit zip code'
)
```

