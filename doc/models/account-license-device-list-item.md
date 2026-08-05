
# Account License Device List Item

The list of devices that have licenses assigned, including the date and time of when each license was assigned.

## Structure

`AccountLicenseDeviceListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | Device IMEI. |
| `assignment_time` | `datetime` | Optional | Timestamp of when a license was assigned to the device. |

## Example

```python
import dateutil.parser

from verizon.models.account_license_device_list_item import AccountLicenseDeviceListItem

account_license_device_list_item = AccountLicenseDeviceListItem(
    device_id='990003425730535',
    assignment_time=dateutil.parser.parse('2017-11-29T16:03:42.000Z')
)
```

