
# Fota V3 Callback Registration Request

Callback URL where the listening service is running.

## Structure

`FotaV3CallbackRegistrationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Callback URL for an subscribed service. |

## Example

```python
from verizon.models.fota_v3_callback_registration_request import FotaV3CallbackRegistrationRequest

fota_v3_callback_registration_request = FotaV3CallbackRegistrationRequest(
    url='https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'
)
```

