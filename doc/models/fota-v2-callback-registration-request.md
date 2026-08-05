
# Fota V2 Callback Registration Request

Callback URL registration.

## Structure

`FotaV2CallbackRegistrationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Callback URL for an subscribed service. |

## Example

```python
from verizon.models.fota_v2_callback_registration_request import FotaV2CallbackRegistrationRequest

fota_v2_callback_registration_request = FotaV2CallbackRegistrationRequest(
    url='https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'
)
```

