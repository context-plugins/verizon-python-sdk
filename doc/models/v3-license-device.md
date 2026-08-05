
# V3 License Device

Device IMEI.

## Structure

`V3LicenseDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `assignment_time` | `str` | Optional | License assignment time. |

## Example

```python
from verizon.models.v3_license_device import V3LicenseDevice

v3_license_device = V3LicenseDevice(
    device_id='15-digit IMEI',
    assignment_time='2017-11-29 20:15:42.738 +0000 UTC'
)
```

