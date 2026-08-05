
# Fota V2 Callback Registration Result

Callback listener URL.

## Structure

`FotaV2CallbackRegistrationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Callback URL. |

## Example

```python
from verizon.models.fota_v2_callback_registration_result import FotaV2CallbackRegistrationResult

fota_v2_callback_registration_result = FotaV2CallbackRegistrationResult(
    url='https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'
)
```

