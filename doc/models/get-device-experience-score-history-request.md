
# Get Device Experience Score History Request

Get device experience score history.

## Structure

`GetDeviceExperienceScoreHistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `device_id` | [`DeviceIdentifier`](../../doc/models/device-identifier.md) | Required | Device Id details. |

## Example

```python
from verizon.models.device_identifier import DeviceIdentifier
from verizon.models.get_device_experience_score_history_request import GetDeviceExperienceScoreHistoryRequest

get_device_experience_score_history_request = GetDeviceExperienceScoreHistoryRequest(
    account_name='0000123456-00001',
    device_id=DeviceIdentifier(
        kind='iccid',
        id='01234567899876543210',
        mdn='0123456789'
    )
)
```

