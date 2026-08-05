
# Account License Info

Account license information.

## Structure

`AccountLicenseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `total_licenses` | `int` | Optional | Number of monthly licenses in an MRC subscription. |
| `assigned_licenses` | `int` | Optional | Number of licenses currently assigned to devices. |
| `has_more_data` | `bool` | Optional | True if there are more devices to retrieve. |
| `last_seen_device_id` | `int` | Optional | If hasMoreData=true, the startIndex to use for the next request. 0 if hasMoreData=false. |
| `device_list` | [`List[AccountLicenseDeviceListItem]`](../../doc/models/account-license-device-list-item.md) | Optional | The list of devices that have licenses assigned, including the date and time of when each license was assigned. |

## Example

```python
import dateutil.parser

from verizon.models.account_license_device_list_item import AccountLicenseDeviceListItem
from verizon.models.account_license_info import AccountLicenseInfo

account_license_info = AccountLicenseInfo(
    account_name='0402196254-00001',
    total_licenses=5000,
    assigned_licenses=4319,
    has_more_data=True,
    last_seen_device_id=1000,
    device_list=[
        AccountLicenseDeviceListItem(
            device_id='990003425730535',
            assignment_time=dateutil.parser.parse('2017-11-29T16:03:42.000Z')
        ),
        AccountLicenseDeviceListItem(
            device_id='990000473475989',
            assignment_time=dateutil.parser.parse('2017-11-29T16:03:42.000Z')
        ),
        AccountLicenseDeviceListItem(
            device_id='990000347475989',
            assignment_time=dateutil.parser.parse('2017-11-29T16:03:42.000Z')
        ),
        AccountLicenseDeviceListItem(
            device_id='990007303425535',
            assignment_time=dateutil.parser.parse('2016-11-29T16:03:42.000Z')
        )
    ]
)
```

