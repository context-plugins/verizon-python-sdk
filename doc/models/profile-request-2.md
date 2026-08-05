
# Profile Request 2

## Structure

`ProfileRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[DeviceList2]`](../../doc/models/device-list-2.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Optional | - |
| `carrier_name` | `str` | Optional | - |
| `reason_code` | `str` | Optional | - |
| `etf_waiver` | `bool` | Optional | **Default**: `True` |
| `check_fallback_profile` | `bool` | Optional | **Default**: `False` |

## Example

```python
from verizon.models.device_list_2 import DeviceList2
from verizon.models.esim_device_id import ESIMDeviceId
from verizon.models.profile_request_2 import ProfileRequest2

profile_request_2 = ProfileRequest2(
    devices=[
        DeviceList2(
            ids=[
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                ),
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                ),
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                )
            ]
        ),
        DeviceList2(
            ids=[
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                ),
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                ),
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                )
            ]
        ),
        DeviceList2(
            ids=[
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                ),
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                ),
                ESIMDeviceId(
                    id='id4',
                    kind='kind2'
                )
            ]
        )
    ],
    account_name='0000123456-00001',
    carrier_name='Verizon Wireless',
    reason_code='FF',
    etf_waiver=True,
    check_fallback_profile=False
)
```

