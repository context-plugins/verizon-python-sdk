
# V3 Account Device List

Array of devices.

## Structure

`V3AccountDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `has_more_data` | `bool` | Required | Has more device flag? |
| `last_seen_device_id` | `str` | Optional | Last seen device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V3AccountDevice]`](../../doc/models/v3-account-device.md) | Required | Account device list. |

## Example

```python
from verizon.models.v3_account_device import V3AccountDevice
from verizon.models.v3_account_device_list import V3AccountDeviceList
from verizon.models.v3_software_info import V3SoftwareInfo

v3_account_device_list = V3AccountDeviceList(
    account_name='0000123456-00001',
    has_more_data=True,
    max_page_size=1000,
    device_list=[
        V3AccountDevice(
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
    ],
    last_seen_device_id='15-digit IMEI'
)
```

