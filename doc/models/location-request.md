
# Location Request

The body contains the the account name and list of devices that you want to locate, plus other options.

## Structure

`LocationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier in "##########-#####". |
| `device_list` | [`List[DeviceInfo]`](../../doc/models/device-info.md) | Required | Device list. |
| `accuracy_mode` | [`AccuracyModeEnum`](../../doc/models/accuracy-mode-enum.md) | Optional | Accurary, currently only 0-coarse supported. |
| `cache_mode` | [`CacheModeEnum`](../../doc/models/cache-mode-enum.md) | Optional | Location cache mode. |

## Example

```python
from verizon.models.accuracy_mode_enum import AccuracyModeEnum
from verizon.models.cache_mode_enum import CacheModeEnum
from verizon.models.device_info import DeviceInfo
from verizon.models.location_request import LocationRequest

location_request = LocationRequest(
    account_name='1234567890-00001',
    device_list=[
        DeviceInfo(
            id='980003420535573',
            kind='imei',
            mdn='7892345678'
        ),
        DeviceInfo(
            id='375535024300089',
            kind='imei',
            mdn='7897654321'
        ),
        DeviceInfo(
            id='A100003861E585',
            kind='meid',
            mdn='7897650914'
        )
    ],
    accuracy_mode=AccuracyModeEnum.ENUM_0,
    cache_mode=CacheModeEnum.ENUM_1
)
```

