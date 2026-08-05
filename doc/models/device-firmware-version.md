
# Device Firmware Version

Device and firmware information.

## Structure

`DeviceFirmwareVersion`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | - |
| `reason` | `str` | Optional | - |
| `device_id` | `str` | Required | Device IMEI. |
| `firmware_version` | `str` | Required | Device Firmware Version. |
| `firmware_version_update_time` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.device_firmware_version import DeviceFirmwareVersion

device_firmware_version = DeviceFirmwareVersion(
    device_id='15-digit IMEI',
    firmware_version='SR1.2.0.0-10657',
    status='FirmwareVersionUpdateSuccess',
    reason='reason2',
    firmware_version_update_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

