
# V3 Account Device

Device information.

## Structure

`V3AccountDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device identifier. |
| `mdn` | `str` | Required | MDN. |
| `model` | `str` | Required | Device model. |
| `make` | `str` | Required | Device make. |
| `firmware` | `str` | Required | Device firmware version. |
| `fota_eligible` | `bool` | Required | Value=true if the device software can be upgraded over the air using the Software Management Services API. |
| `status` | `str` | Required | Device status. |
| `license_assigned` | `bool` | Required | License assigned device. |
| `protocol` | `str` | Required | Firmware protocol. Valid values include: LWM2M, OMADM, HTTP or NONE. |
| `software_list` | [`List[V3SoftwareInfo]`](../../doc/models/v3-software-info.md) | Required | List of sofware. |
| `file_list` | [`List[V3SoftwareInfo]`](../../doc/models/v3-software-info.md) | Optional | List of files. |
| `create_time` | `str` | Optional | The date and time of when the device is created. |
| `upgrade_time` | `str` | Optional | The date and time of when the device firmware or software is updated. |
| `update_time` | `str` | Optional | The date and time of when the device is updated. |
| `refresh_time` | `str` | Optional | The date and time of when the device is refreshed. |

## Example

```python
from verizon.models.v3_account_device import V3AccountDevice
from verizon.models.v3_software_info import V3SoftwareInfo

v3_account_device = V3AccountDevice(
    device_id='15-digit device ID',
    mdn='10-digit MDN',
    model='BG96',
    make='QUECTEL',
    firmware='BG96MAR04A04M1G',
    fota_eligible=False,
    status='Active',
    license_assigned=True,
    protocol='LWM2M',
    software_list=[
        V3SoftwareInfo(
            name='VZ_MDM_IOT',
            version='0.14',
            upgrade_time='2012-04-23T18:25:43.511Z'
        )
    ],
    file_list=[
        V3SoftwareInfo(
            name='VZ_MDM_IOT',
            version='0.14',
            upgrade_time='2012-04-23T18:25:43.511Z'
        )
    ],
    create_time='2021-06-03 00:03:56.079 +0000 UTC',
    upgrade_time='2021-06-03 00:03:56.079 +0000 UTC',
    update_time='2021-06-03 00:03:56.079 +0000 UTC',
    refresh_time='2021-06-03 00:03:56.079 +0000 UTC'
)
```

