
# Device Firmware Version Update Result

Device firmware version update response.

## Structure

`DeviceFirmwareVersionUpdateResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `request_id` | `str` | Required | Request identifier. |

## Example

```python
from verizon.models.device_firmware_version_update_result import DeviceFirmwareVersionUpdateResult

device_firmware_version_update_result = DeviceFirmwareVersionUpdateResult(
    account_name='accountName4',
    request_id='requestId2'
)
```

