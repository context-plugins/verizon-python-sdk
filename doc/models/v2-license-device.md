
# V2 License Device

Device IMEI list.

## Structure

`V2LicenseDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `assignment_time` | `str` | Optional | License assignment time. |

## Example

```python
from verizon.models.v2_license_device import V2LicenseDevice

v2_license_device = V2LicenseDevice(
    device_id='990003425730535',
    assignment_time='2017-11-29T16:03:42.000Z'
)
```

