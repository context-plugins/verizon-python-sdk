
# Deactivate Device Profile Request

## Structure

`DeactivateDeviceProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `reason_code` | `str` | Required | - |
| `devices` | [`List[DeactivateDeviceList]`](../../doc/models/deactivate-device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `carrier_name` | `str` | Optional | - |
| `etf_waiver` | `bool` | Optional | **Default**: `True` |
| `check_fallback_profile` | `bool` | Optional | **Default**: `False` |

## Example

```python
from verizon.models.deactivate_device_list import DeactivateDeviceList
from verizon.models.deactivate_device_profile_request import DeactivateDeviceProfileRequest
from verizon.models.device_id import DeviceId

deactivate_device_profile_request = DeactivateDeviceProfileRequest(
    account_name='0000123456-00001',
    reason_code='a short code for the reason action was taken',
    devices=[
        DeactivateDeviceList(
            ids=[
                DeviceId(
                    id='id2',
                    kind='kind0'
                ),
                DeviceId(
                    id='id2',
                    kind='kind0'
                ),
                DeviceId(
                    id='id2',
                    kind='kind0'
                )
            ]
        )
    ],
    carrier_name='the name of the mobile service provider',
    etf_waiver=True,
    check_fallback_profile=False
)
```

