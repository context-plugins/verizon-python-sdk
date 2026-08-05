
# V2 Account Device List

List of device information for an account.

## Structure

`V2AccountDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `has_more_data` | `bool` | Required | Has more device flag? |
| `last_seen_device_id` | `str` | Optional | Last seen device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V2AccountDevice]`](../../doc/models/v2-account-device.md) | Required | Account device list. |

## Example

```python
from verizon.models.v2_account_device import V2AccountDevice
from verizon.models.v2_account_device_list import V2AccountDeviceList
from verizon.models.v2_software_info import V2SoftwareInfo

v2_account_device_list = V2AccountDeviceList(
    account_name='0000123456-00001',
    has_more_data=True,
    max_page_size=1000,
    device_list=[
        V2AccountDevice(
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
        ),
        V2AccountDevice(
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
        ),
        V2AccountDevice(
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
    ],
    last_seen_device_id='15-digit IMEI'
)
```

