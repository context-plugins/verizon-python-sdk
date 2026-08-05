
# ESIM Profile Request 2

## Structure

`ESIMProfileRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[ESIMDeviceList]`](../../doc/models/esim-device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `mdn_zip_code` | `str` | Optional | - |

## Example

```python
from verizon.models.esim_device_id import ESIMDeviceId
from verizon.models.esim_device_list import ESIMDeviceList
from verizon.models.esim_profile_request_2 import ESIMProfileRequest2

e_sim_profile_request_2 = ESIMProfileRequest2(
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
    account_name='0000123456-00001',
    service_plan='The service plan name',
    mdn_zip_code='five digit zip code'
)
```

