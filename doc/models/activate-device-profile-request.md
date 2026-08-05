
# Activate Device Profile Request

## Structure

`ActivateDeviceProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Required | - |
| `service_plan` | `str` | Optional | - |
| `mdn_zip_code` | `str` | Optional | - |

## Example

```python
from verizon.models.activate_device_profile_request import ActivateDeviceProfileRequest
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList

activate_device_profile_request = ActivateDeviceProfileRequest(
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    account_name='0000123456-00001',
    service_plan='The service plan name',
    mdn_zip_code='five digit zip code'
)
```

