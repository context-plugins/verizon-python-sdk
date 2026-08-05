
# V2 Account Device

Account device information.

## Structure

`V2AccountDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device identifier. |
| `mdn` | `str` | Required | MDN. |
| `model` | `str` | Required | Device model. |
| `make` | `str` | Required | Device make. |
| `fota_eligible` | `bool` | Required | Device FOTA capable. |
| `app_fota_eligible` | `bool` | Required | Device application FOTA capable. |
| `license_assigned` | `bool` | Required | License assigned device. |
| `distribution_type` | `str` | Required | LWM2M, OMD-DM or HTTP. |
| `software_list` | [`List[V2SoftwareInfo]`](../../doc/models/v2-software-info.md) | Required | List of sofware. |
| `create_time` | `str` | Optional | The date and time of when the device is created. |
| `upgrade_time` | `str` | Optional | The date and time of when the device firmware or software is upgraded. |
| `update_time` | `str` | Optional | The date and time of when the device is updated. |
| `refresh_time` | `str` | Optional | The date and time of when the device is refreshed. |

## Example

```python
from verizon.models.v2_account_device import V2AccountDevice
from verizon.models.v2_software_info import V2SoftwareInfo

v2_account_device = V2AccountDevice(
    device_id='15-digit IMEI',
    mdn='10-digit MDN',
    model='Model-A',
    make='Verizon',
    fota_eligible=True,
    app_fota_eligible=True,
    license_assigned=True,
    distribution_type='HTTP',
    software_list=[
        V2SoftwareInfo(
            name='FOTA_Verizon_Model-A_02To03_HF',
            version='3',
            upgrade_time='2020-09-08T19:00:51.541Z'
        )
    ],
    create_time='2021-06-03 00:03:56.079 +0000 UTC',
    upgrade_time='2021-06-03 00:03:56.079 +0000 UTC',
    update_time='2021-06-03 00:03:56.079 +0000 UTC',
    refresh_time='2021-06-03 00:03:56.079 +0000 UTC'
)
```

