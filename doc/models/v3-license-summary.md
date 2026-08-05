
# V3 License Summary

Information for FOTA licenses assigned to devices.

## Structure

`V3LicenseSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `total_licenses` | `int` | Optional | Total FOTA license count. |
| `assigned_licenses` | `int` | Required | Assigned FOTA license count. |
| `has_more_data` | `bool` | Required | True if there are more devices to retrieve. |
| `last_seen_device_id` | `str` | Optional | Last seen device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V3LicenseDevice]`](../../doc/models/v3-license-device.md) | Optional | Device IMEI list. |

## Example

```python
from verizon.models.v3_license_device import V3LicenseDevice
from verizon.models.v3_license_summary import V3LicenseSummary

v3_license_summary = V3LicenseSummary(
    account_name='0000123456-00001',
    assigned_licenses=4319,
    has_more_data=True,
    max_page_size=1000,
    total_licenses=5000,
    last_seen_device_id='1000',
    device_list=[
        V3LicenseDevice(
            device_id='15-digit IMEI',
            assignment_time='2017-11-29 20:15:42.738 +0000 UTC'
        ),
        V3LicenseDevice(
            device_id='15-digit IMEI',
            assignment_time='2017-11-29 20:15:42.738 +0000 UTC'
        )
    ]
)
```

