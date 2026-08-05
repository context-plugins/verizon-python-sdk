
# Device Firmware List

Device Firmware Information.

## Structure

`DeviceFirmwareList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `device_firmwar_version_list` | [`List[DeviceFirmwareVersion]`](../../doc/models/device-firmware-version.md) | Optional | List of device & firmware. |

## Example

```python
import dateutil.parser

from verizon.models.device_firmware_list import DeviceFirmwareList
from verizon.models.device_firmware_version import DeviceFirmwareVersion

device_firmware_list = DeviceFirmwareList(
    account_name='0000123456-00001',
    device_firmwar_version_list=[
        DeviceFirmwareVersion(
            device_id='15-digit IMEI',
            firmware_version='SR1.2.0.0-10657',
            status='FirmwareVersionUpdateSuccess',
            reason='reason8',
            firmware_version_update_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

