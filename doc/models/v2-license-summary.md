
# V2 License Summary

Summary of license assignment.

## Structure

`V2LicenseSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `total_license` | `int` | Optional | Total FOTA license count. |
| `assigned_licenses` | `int` | Required | Assigned FOTA license count. |
| `has_more_data` | `bool` | Required | True if there are more devices to retrieve. |
| `last_seen_device_id` | `str` | Optional | Last seen device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V2LicenseDevice]`](../../doc/models/v2-license-device.md) | Optional | Device IMEI list. |

## Example

```python
from verizon.models.v2_license_device import V2LicenseDevice
from verizon.models.v2_license_summary import V2LicenseSummary

v2_license_summary = V2LicenseSummary(
    account_name='0402196254-00001',
    assigned_licenses=4319,
    has_more_data=True,
    max_page_size=10,
    total_license=5000,
    last_seen_device_id='1000',
    device_list=[
        V2LicenseDevice(
            device_id='990003425730535',
            assignment_time='2017-11-29T16:03:42.000Z'
        ),
        V2LicenseDevice(
            device_id='990000473475989',
            assignment_time='2017-11-29T16:03:42.000Z'
        ),
        V2LicenseDevice(
            device_id='990000347475989',
            assignment_time='2017-11-29T16:03:42.000Z'
        ),
        V2LicenseDevice(
            device_id='990007303425535',
            assignment_time='2017-11-29T16:03:42.000Z'
        )
    ]
)
```

